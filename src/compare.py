import os
import numpy as np
import pandas as pd
import random
import csv

data_dic = {}
sample_number = 0
false_sample_number = 0
filenamelist = [
    "/Users/qianz/大三上/实验室/AutoID/AutoID/debug/没有任何动作的场景一+收集5分钟，最后一分钟人坐在那里/output_11_05_10_45_8.csv"]

for file in filenamelist:
    print(file)
    with open(file) as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        birth_header = next(csv_reader)  # 读取第一行每一列的标题
        print(birth_header)
        for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
            if row[0] == "E2801160600002073A4A0519":  # 错误的不要
                if row[1] == "1":
                    frequency = int(row[3])
                    sample_number += 1
                    if(frequency in data_dic):
                        data_dic[frequency] += int(row[4])
                        data_dic[str(frequency) + "number"] += 1
                        data_dic[str(frequency) + "list"].append(row[4])
                    else:
                        data_dic[frequency] = int(row[4])
                        data_dic[str(frequency) + "number"] = 1
                        data_dic[str(frequency) + "list"] = []
print(data_dic)
out = open('Stu_csv_rssi_all.csv', 'a', newline='')
csv_write = csv.writer(out, dialect='excel')
print("total_sample:" + str(sample_number))
keynumber = 0
for key in data_dic:
    titlelist = []
    mystr = str(key) + "number"
    if(mystr in data_dic):
        keynumber += 1
        titlelist.append(key)
        for item in data_dic[str(key) + "list"]:
            # print(item)
            titlelist.append(item)
        csv_write.writerow(titlelist)
        # print(str(key) + ":")
        # print(data_dic[key] / data_dic[mystr])
print("total_sample:" + str(keynumber))
# print(rowlist)
# print("write over")
# titlelist = []
# contentlist = []
# for key in data_dic:
#     mystr = str(key) + "number"
#     if(mystr in data_dic):
#         keynumber += 1
#         titlelist.append(key)
#         contentlist.append(data_dic[key] / data_dic[mystr])

#         # csv_write.writerow(titlelist)
#         # print(str(key) + ":")
#         # print(data_dic[key] / data_dic[mystr])
# csv_write.writerow(titlelist)
# csv_write.writerow(contentlist)
# # print(rowlist)
# print("write over")
