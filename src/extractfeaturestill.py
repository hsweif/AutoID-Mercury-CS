import os
import numpy as np
import pandas as pd
import random
import csv
import pickle

filenamelist = [
    "/Users/qianz/大三上/实验室/AutoID/AutoID/debug/没有任何动作的场景一+收集5分钟，最后一分钟人坐在那里/output_11_05_10_45_8.csv"]
# 最终的rssi的dic 包含target和features
# dic_rssi = {}
# dic_phase = {}
# header = []
out = open('tmpfilename', 'a', newline='')
csv_write = csv.writer(out, dialect='excel')
for file in filenamelist:
    # 用来存储一次读取的所有数据
    print("now we read the filename:" + file)
    i = 800
    num = 0
    with open(file) as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        headers = next(csv_reader)  # 读取标题
        for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
            if i < 800:
                csv_write.writerow(row)
                i += 1
            else:
                tmpfilename = "/Users/qianz/大三上/实验室/AutoID/AutoID/still/still" + \
                    str(num) + ".csv"
                out = open(tmpfilename, 'a', newline='')
                csv_write = csv.writer(out, dialect='excel')
                csv_write.writerow(headers)
                i = 0
                num += 1
            # # 峰峰值
            # max_min = np.max(rssi) - np.min(rssi)
            # # 最小值的坐标
            # id_min = rssi_series.idxmin()
            # # 最大值的坐标
            # id_max = rssi_series.idxmax()
            # # 最大值
            # max_value = rssi_series.max()
            # # 最小值
            # min_value = rssi_series.min()
            # # 求和
            # sum = rssi_series.sum()
            # # 中位数
            # mean = rssi_series.mean()
            # # 众数
            # mode = rssi_series.mode()
            # # 标准差
            # std = rssi_series.std()
            # # 平均绝对偏差
            # mad = rssi_series.mad()
            # # 偏度
            # skew = rssi_series.skew()
            # # 峰度
            # kurt = rssi_series.kurt()
            # # 不同的分位数
            # describe25 = rssi_series.describe()["25%"]
            # describe50 = rssi_series.describe()["50%"]
            # describe75 = rssi_series.describe()["75%"]

            # def status_rssi(x):
            #     return pd.Series([x.max() - x.min(), x.max(), x.min(),
            #                       x.sum(), x.mean(), x.std(), x.mad(), x.skew(), x.kurt(),
            #                       x.describe()["25%"], x.describe()["50%"], x.describe()["75%"]], index=['峰峰值',
            #                                                                                              '最大值', '最小值', '和', '平均值', '标准差', '平均绝对偏差', '偏度', '峰度', '25分位数',
            #                                                                                              '50分位数', '75分位数'])

            # df = pd.DataFrame(status_rssi(rssi_series))
            # print(df)
            # print("max_min rssi:" + str(max_min))
            # # print("min id:" + str(id_min))
            # # print("max id:" + str(id_max))
            # print("max:" + str(max_value))
            # print("min:" + str(min_value))
            # print("sum:" + str(sum))
            # print("mean:" + str(mean))
            # # print("mode:" + str(mode))
            # print("std:" + str(std))
            # print("mad:" + str(mad))
            # print("skew:" + str(skew))
            # print("kurt:" + str(kurt))
            # print("describe25:" + str(describe25))
            # print("describe50:" + str(describe50))
            # print("describe75:" + str(describe75))
            # print("10% quantile:" + str(quantile))
            # print(data_dic)
            # out = open('Stu_csv4.csv', 'a', newline='')
            # csv_write = csv.writer(out, dialect='excel')
            # print("total_sample:" + str(sample_number))
            # keynumber = 0
            # for key in data_dic:
            #     titlelist = []
            #     mystr = str(key) + "number"
            #     if(mystr in data_dic):
            #         keynumber += 1
            #         titlelist.append(key)
            #         for item in data_dic[str(key) + "list"]:
            #             # print(item)
            #             titlelist.append(item)
            #         csv_write.writerow(titlelist)
            #         # print(str(key) + ":")
            #         # print(data_dic[key] / data_dic[mystr])
            # print("total_sample:" + str(keynumber))
            # # print(rowlist)
            # print("write over")
