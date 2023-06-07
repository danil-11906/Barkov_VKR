import os
import random
import io

import mediapipe as mp
import cv2
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import finish

from collections import namedtuple
from flask import Flask, render_template, redirect, url_for, request, send_file, Response

app = Flask(__name__)

Message = namedtuple('Message', 'text')
messages = []


@app.route('/', methods=['GET'])
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/main', methods=['GET'])
def main():
    return render_template('main.html', messages=messages)


@app.route('/add_message', methods=['POST'])
def add_message():
    if 'video' not in request.files:
        return redirect('/main')
    file = request.files['video']
    file.save(file.filename)
    if file.filename == "":
        return redirect('/')
    result, video_name = work_video(file.filename)
    for i in range(100):
        if os.path.isfile(file.filename):
            os.remove(file.filename)
    return render_template('images.html', string_variable=result, string_video=video_name)


@app.route('/display/<filename>')
def display_video(filename):
    print('display_video filename: ' + filename)
    return send_file('static\\' + filename, as_attachment=True)


def work_video(file):
    mp_pose = mp.solutions.pose
    mp_draw = mp.solutions.drawing_utils
    pose = mp_pose.Pose()
    cap = cv2.VideoCapture(file)
    finish_list = "list_gan.txt"
    myfile = open(finish_list, "w", encoding="utf-8")
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    finish_video = "video_model" + str(random.randint(1, 100)) + ".mp4"
    out = cv2.VideoWriter("D:\\flaskProject\\static\\" + finish_video, fourcc, 20.0, (800, 600))

    try:
        while True:
            ret, img = cap.read()
            img = cv2.resize(img, (800, 600))

            results = pose.process(img)
            mp_draw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                   mp_draw.DrawingSpec([255, 0, 0]))

            if results.pose_landmarks != None:
                myfile.write(str(results.pose_landmarks))
            out.write(img)
            cv2.imshow("Pose Estimation", img)
            cv2.waitKey(1)


    finally:
        dd, result = finish.finish(finish_list)
        return result, finish_video


@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def create_figure():
    finish_list = "list_gan.txt"
    dd, result = finish.finish(finish_list)
    fig = Figure()
    axis = fig.add_subplot(2, 1, 1)
    axis.plot([0, 1, 2, 3], [0, 0, 0, 0])
    axis.set_ylim(0, 0.1)
    axis.tick_params(labelleft=False, left=False)
    axis.text(1.25, 0.01, 'Подход, (№)')
    axis = fig.add_subplot(2, 1, 2)
    a = dd.loc[dd.anomaly == -1, ['res']]
    axis.plot(dd.index, dd.res)
    axis.scatter(a.index, a, color='red')
    axis.tick_params(labelbottom=False, bottom=False)
    axis.set_ylabel('Сходство, (%)')
    return fig


if __name__ == '__main__':
    app.run()
