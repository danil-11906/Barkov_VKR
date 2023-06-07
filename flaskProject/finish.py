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


    # fig, ax = plt.subplots(figsize=(16,9))
    # a = dd.loc[dd.anomaly == -1, ['res']]
    # ax.plot(dd.index, dd.res)
    # ax.scatter(a.index, a, color='red')
    # return dd, result
    return dd, final_result




































    # plt.plot(list_res_x, list_res_y)
    # plt.show()
    # print(result)



    # len_min = [len(list_x), len(list_y), len(list_z)]
    # len_min = min(len_min)
    #
    # len2_min = [len(list1_x), len(list1_y), len(list1_z)]
    # len2_min = min(len2_min)

    # print(len_min, len2_min)

    # list_float_1_x = torch.FloatTensor(list_x)
    # list_float_1_y = torch.FloatTensor(list_y)
    # list_float_1_z = torch.FloatTensor(list_z)
    # list_float_2_x = torch.FloatTensor(list1_x)
    # list_float_2_y = torch.FloatTensor(list1_y)
    # list_float_2_z = torch.FloatTensor(list1_z)
    #
    # print(len(list_float_1_x))
    # print(len(list_float_1_y))
    # print(len(list_float_1_z))
    # print(len(list_float_2_x))
    # print(len(list_float_2_y))
    # print(len(list_float_2_z))
    #
    #
    # result = F.cosine_similarity(list_float_1_x, list_float_2_x, dim=0)
    # result1 = F.cosine_similarity(list_float_1_y, list_float_2_y, dim=0)
    # result2 = F.cosine_similarity(list_float_1_z, list_float_2_z, dim=0)
    #
    # result = round(float(result)*100, 2)
    # result1 = round(float(result1)*100, 2)
    # result2 = round(float(result2)*100, 2)
    # #
    # print((result + result1 + result2)/3)



    # for i in range(len_min):
    #     result.append((list_x[i] * list_x[i] * list_x[i] +
    #               list_x[i] * list_x[i] * list_x[i] +
    #                    list_x[i] * list_x[i] * list_x[i])/(
    #             math.sqrt(list_x[i] ** 2 + list_x[i] ** 2 + list_x[i] ** 2) *
    #             math.sqrt(list_x[i] ** 2 + list_x[i] ** 2 + list_x[i] ** 2)))
    # z = 0
    # for i in result:
    #     z = z + i
    # z = z / len(result)
    # print(z)