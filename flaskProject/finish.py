import math

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler


def finish (file_1):
    myfile = open(file_1, "r", encoding="utf-8")
    list_x = []
    list_y = []
    list_z = []
    lines = myfile.readlines()

    myfile2 = open("list2.txt", "r", encoding="utf-8")
    list1_x = []
    list1_y = []
    list1_z = []
    lines1 = myfile2.readlines()

    for i in range(min(len(lines), len(lines1))):
        if (len(lines[i]) < 30 and len(lines[i]) > 20):
            if lines[i][2] == "x":
                lines[i] = lines[i][:-1]
                lines[i] = lines[i][1:]
                lines[i] = lines[i][1:]
                lines[i] = lines[i][1:]
                lines[i] = lines[i][1:]
                lines[i] = lines[i][1:]
                list_x.append(float(lines[i]))
            if lines[i][2] == "y":
                lines[i] = lines[i][:-1]
                lines[i] = lines[i][1:]
                lines[i] = lines[i][1:]
                lines[i] = lines[i][1:]
                lines[i] = lines[i][1:]
                lines[i] = lines[i][1:]
                list_y.append(float(lines[i]))
            if lines[i][2] == "z":
                lines[i] = lines[i][:-1]
                lines[i] = lines[i][1:]
                lines[i] = lines[i][1:]
                lines[i] = lines[i][1:]
                lines[i] = lines[i][1:]
                lines[i] = lines[i][1:]
                list_z.append(float(lines[i]))

    for i in range(min(len(lines), len(lines1))):
        if (len(lines1[i]) < 30 and len(lines1[i]) > 20):
            if lines1[i][2] == "x":
                lines1[i] = lines1[i][:-1]
                lines1[i] = lines1[i][1:]
                lines1[i] = lines1[i][1:]
                lines1[i] = lines1[i][1:]
                lines1[i] = lines1[i][1:]
                lines1[i] = lines1[i][1:]
                list1_x.append(float(lines1[i]))
            if lines1[i][2] == "y":
                lines1[i] = lines1[i][:-1]
                lines1[i] = lines1[i][1:]
                lines1[i] = lines1[i][1:]
                lines1[i] = lines1[i][1:]
                lines1[i] = lines1[i][1:]
                lines1[i] = lines1[i][1:]
                list1_y.append(float(lines1[i]))
            if lines1[i][2] == "z":
                lines1[i] = lines1[i][:-1]
                lines1[i] = lines1[i][1:]
                lines1[i] = lines1[i][1:]
                lines1[i] = lines1[i][1:]
                lines1[i] = lines1[i][1:]
                lines1[i] = lines1[i][1:]
                list1_z.append(float(lines1[i]))

    result = 0
    list_res_y = []
    list_res_x = []
    s = 0
    f = min(len(list_x),len(list_y),len(list_z),len(list1_x),len(list1_y),len(list1_z))
    f_1 = f // 3
    final_result = []
    ret = 0
    for i in range(0, f):
        obj = []
        obj.append(list_x[i])
        obj.append(list_y[i])
        obj.append(list_z[i])
        obj1 = []
        obj1.append(list1_x[i])
        obj1.append(list1_y[i])
        obj1.append(list1_z[i])
        z = (obj[0] * obj1[0] +
                       obj[1] * obj1[1] +
                       obj[2] * obj1[2])/(math.sqrt(obj[0] ** 2 + obj[1] ** 2 + obj[2] ** 2) *
                                          math.sqrt(obj1[0] ** 2 + obj1[1] ** 2 + obj1[2] ** 2)) * 100
        result = result + (z / 100)
        ret = ret + (z / 100)
        if (i == f_1) | (i == f_1 * 2) | (i == f_1 * 3):
            final_result.append(round(float(ret / f_1) * 100, 2))
            ret = 0
        s += 1
        list_res_x.append(s)
        if i % 8 == 0:
            list_res_y.append(z)

    result = result / f
    result = round(float(result) * 100, 2)
    final_result.append(result)

    dd = pd.DataFrame({"res": list_res_y})
    scaler = StandardScaler()
    np_scaled = scaler.fit_transform(dd.values.reshape(-1,1))

    data = pd.DataFrame(np_scaled)
    print(data)
    model = IsolationForest(contamination=0.05)
    model.fit(data)

    dd['anomaly'] = model.predict(data)

    return dd, final_result

