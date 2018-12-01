import os
import numpy as np
import pandas as pd
import random
import csv
import pickle
from sklearn import preprocessing

# feature：12*9个rssi统计值 12*9个phase统计值
# 用来存储所有的数据集
data_dic = {}
sample_number = 0
false_sample_number = 0
data_dic["data"] = []
data_dic["target"] = []

# 遍历目录的函数


def gci(filepath, filenamelist):
    # 遍历filepath下所有文件，包括子目录
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            gci(fi_d)
        else:
            var = os.path.join(filepath, fi_d)
            if "csv" in var:
                filenamelist.append(os.path.join(filepath, fi_d))
                print(var)


# 递归遍历/root目录下所有文件
filenamelist = []
# "/Users/qianz/大三上/实验室/AutoID/AutoID/debug/每5s采集数据/slide/output_11_05_12_9_17.csv"]
gci('/Users/qianz/大三上/实验室/AutoID/AutoID/debug/每5s采集数据/slide/', filenamelist)
filenamelist1 = []
# "/Users/qianz/大三上/实验室/AutoID/AutoID/still/still1.csv"]
filenamelist2 = []
# "/Users/qianz/大三上/实验室/AutoID/AutoID/debug/每5s采集数据/slide/output_11_05_12_9_17.csv"]
gci('/Users/qianz/大三上/实验室/AutoID/AutoID/still/', filenamelist1)
gci('/Users/qianz/大三上/实验室/AutoID/AutoID/debug/每5s采集数据/thumb/', filenamelist2)
# # print(filenamelist)
antlist = ["1", "2", "3"]
epclist = ["E2801160600002073A4A0519",
           "E2801160600002073A4A0529", "E2801160600002073A4A0539"]

# 提取features


def status(x):
    return pd.Series([x.max() - x.min(), x.max(), x.min(),
                      x.sum(), x.mean(), x.std(), x.mad(), x.skew(), x.kurt(),
                      x.describe()["25%"], x.describe()["50%"], x.describe()["75%"]], index=['峰峰值',
                                                                                             '最大值', '最小值', '和', '平均值', '标准差', '平均绝对偏差', '偏度', '峰度', '25分位数',
                                                                                             '50分位数', '75分位数'])


# filenamelist = [
#     "/Users/qianz/大三上/实验室/AutoID/AutoID/debug/每5s采集数据/slide/output_11_05_12_9_2.csv"]
# header = []
for file in filenamelist:
    # 用来存储一次读取的所有数据
    rssi_00 = []
    phase_00 = []
    rssi_01 = []
    phase_01 = []
    rssi_02 = []
    phase_02 = []
    rssi_10 = []
    phase_10 = []
    rssi_11 = []
    phase_11 = []
    rssi_12 = []
    phase_12 = []
    rssi_20 = []
    phase_20 = []
    rssi_21 = []
    phase_21 = []
    rssi_22 = []
    phase_22 = []
    features_single = []
    print("now we read the filename:" + file)
    with open(file) as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        headers = next(csv_reader)  # 读取标题
        for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
            if row[0] == epclist[0]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[0]:  # 天线1
                    rssi_00.append(int(row[4]))
                    phase_00.append(int(row[5]))
                    continue
            if row[0] == epclist[0]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[1]:  # 天线1
                    rssi_01.append(int(row[4]))
                    phase_01.append(int(row[5]))
                    continue
            if row[0] == epclist[0]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[2]:  # 天线1
                    rssi_02.append(int(row[4]))
                    phase_02.append(int(row[5]))
                    continue
            if row[0] == epclist[1]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[0]:  # 天线1
                    rssi_10.append(int(row[4]))
                    phase_10.append(int(row[5]))
                    continue
            if row[0] == epclist[1]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[1]:  # 天线1
                    rssi_11.append(int(row[4]))
                    phase_11.append(int(row[5]))
                    continue
            if row[0] == epclist[1]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[2]:  # 天线1
                    rssi_12.append(int(row[4]))
                    phase_12.append(int(row[5]))
                    continue
            if row[0] == epclist[2]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[0]:  # 天线1
                    rssi_20.append(int(row[4]))
                    phase_20.append(int(row[5]))
                    continue
            if row[0] == epclist[2]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[1]:  # 天线1
                    rssi_21.append(int(row[4]))
                    phase_21.append(int(row[5]))
                    continue
            if row[0] == epclist[2]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[2]:  # 天线1
                    rssi_22.append(int(row[4]))
                    phase_22.append(int(row[5]))
        dict_all = []
        dict_all.append(rssi_00)
        dict_all.append(rssi_01)
        dict_all.append(rssi_02)
        dict_all.append(rssi_10)
        dict_all.append(rssi_11)
        dict_all.append(rssi_12)
        dict_all.append(rssi_20)
        dict_all.append(rssi_21)
        dict_all.append(rssi_22)
        dict_all.append(phase_00)
        dict_all.append(phase_01)
        dict_all.append(phase_02)
        dict_all.append(phase_10)
        dict_all.append(phase_11)
        dict_all.append(phase_12)
        dict_all.append(phase_20)
        dict_all.append(phase_21)
        dict_all.append(phase_22)
        for item in dict_all:
            tmpseries = pd.Series(item)
            tmpdf = pd.DataFrame(status(tmpseries))
            tmpdf = tmpdf.fillna(0)
            for item in tmpdf.values:
                features_single.append(item[0])
            # series_list_all.append(pd.Series(item))
        # rssi_series = pd.Series(rssi)
        # phase_seried = pd.Series(phase)
        # 第i个标签的rssi 特征
        # df_rssi = pd.DataFrame(status(rssi_series))
        # for item in df_rssi.values:
        #     features_single.append(item[0])
        # # print(features_single)
        # # 第i个标签的phase特征
        # df_phase = pd.DataFrame(status(phase_seried))
        # for item in df_phase.values:
        #     features_single.append(item[0])
        data_dic["data"].append(features_single)
        data_dic["target"].append("0")  # 类别0代表是滑动
        # print(type(df_rssi))
        # print(df_phase)

for file in filenamelist1:
    # 用来存储一次读取的所有数据
    rssi_00 = []
    phase_00 = []
    rssi_01 = []
    phase_01 = []
    rssi_02 = []
    phase_02 = []
    rssi_10 = []
    phase_10 = []
    rssi_11 = []
    phase_11 = []
    rssi_12 = []
    phase_12 = []
    rssi_20 = []
    phase_20 = []
    rssi_21 = []
    phase_21 = []
    rssi_22 = []
    phase_22 = []
    features_single = []
    print("now we read the filename:" + file)
    with open(file) as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        headers = next(csv_reader)  # 读取标题
        for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
            if row[0] == epclist[0]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[0]:  # 天线1
                    rssi_00.append(int(row[4]))
                    phase_00.append(int(row[5]))
                    continue
            if row[0] == epclist[0]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[1]:  # 天线1
                    rssi_01.append(int(row[4]))
                    phase_01.append(int(row[5]))
                    continue
            if row[0] == epclist[0]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[2]:  # 天线1
                    rssi_02.append(int(row[4]))
                    phase_02.append(int(row[5]))
                    continue
            if row[0] == epclist[1]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[0]:  # 天线1
                    rssi_10.append(int(row[4]))
                    phase_10.append(int(row[5]))
                    continue
            if row[0] == epclist[1]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[1]:  # 天线1
                    rssi_11.append(int(row[4]))
                    phase_11.append(int(row[5]))
                    continue
            if row[0] == epclist[1]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[2]:  # 天线1
                    rssi_12.append(int(row[4]))
                    phase_12.append(int(row[5]))
                    continue
            if row[0] == epclist[2]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[0]:  # 天线1
                    rssi_20.append(int(row[4]))
                    phase_20.append(int(row[5]))
                    continue
            if row[0] == epclist[2]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[1]:  # 天线1
                    rssi_21.append(int(row[4]))
                    phase_21.append(int(row[5]))
                    continue
            if row[0] == epclist[2]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[2]:  # 天线1
                    rssi_22.append(int(row[4]))
                    phase_22.append(int(row[5]))
        dict_all = []
        dict_all.append(rssi_00)
        dict_all.append(rssi_01)
        dict_all.append(rssi_02)
        dict_all.append(rssi_10)
        dict_all.append(rssi_11)
        dict_all.append(rssi_12)
        dict_all.append(rssi_20)
        dict_all.append(rssi_21)
        dict_all.append(rssi_22)
        dict_all.append(phase_00)
        dict_all.append(phase_01)
        dict_all.append(phase_02)
        dict_all.append(phase_10)
        dict_all.append(phase_11)
        dict_all.append(phase_12)
        dict_all.append(phase_20)
        dict_all.append(phase_21)
        dict_all.append(phase_22)
        for item in dict_all:
            tmpseries = pd.Series(item)
            tmpdf = pd.DataFrame(status(tmpseries))
            tmpdf = tmpdf.fillna(0)
            for item in tmpdf.values:
                features_single.append(item[0])
            # series_list_all.append(pd.Series(item))
        # rssi_series = pd.Series(rssi)
        # phase_seried = pd.Series(phase)
        # 第i个标签的rssi 特征
        # df_rssi = pd.DataFrame(status(rssi_series))
        # for item in df_rssi.values:
        #     features_single.append(item[0])
        # # print(features_single)
        # # 第i个标签的phase特征
        # df_phase = pd.DataFrame(status(phase_seried))
        # for item in df_phase.values:
        #     features_single.append(item[0])
        data_dic["data"].append(features_single)
        data_dic["target"].append("1")  # 类别0代表是滑动


for file in filenamelist2:
    # 用来存储一次读取的所有数据
    rssi_00 = []
    phase_00 = []
    rssi_01 = []
    phase_01 = []
    rssi_02 = []
    phase_02 = []
    rssi_10 = []
    phase_10 = []
    rssi_11 = []
    phase_11 = []
    rssi_12 = []
    phase_12 = []
    rssi_20 = []
    phase_20 = []
    rssi_21 = []
    phase_21 = []
    rssi_22 = []
    phase_22 = []
    features_single = []
    print("now we read the filename:" + file)
    with open(file) as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        headers = next(csv_reader)  # 读取标题
        for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
            if row[0] == epclist[0]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[0]:  # 天线1
                    rssi_00.append(int(row[4]))
                    phase_00.append(int(row[5]))
                    continue
            if row[0] == epclist[0]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[1]:  # 天线1
                    rssi_01.append(int(row[4]))
                    phase_01.append(int(row[5]))
                    continue
            if row[0] == epclist[0]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[2]:  # 天线1
                    rssi_02.append(int(row[4]))
                    phase_02.append(int(row[5]))
                    continue
            if row[0] == epclist[1]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[0]:  # 天线1
                    rssi_10.append(int(row[4]))
                    phase_10.append(int(row[5]))
                    continue
            if row[0] == epclist[1]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[1]:  # 天线1
                    rssi_11.append(int(row[4]))
                    phase_11.append(int(row[5]))
                    continue
            if row[0] == epclist[1]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[2]:  # 天线1
                    rssi_12.append(int(row[4]))
                    phase_12.append(int(row[5]))
                    continue
            if row[0] == epclist[2]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[0]:  # 天线1
                    rssi_20.append(int(row[4]))
                    phase_20.append(int(row[5]))
                    continue
            if row[0] == epclist[2]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[1]:  # 天线1
                    rssi_21.append(int(row[4]))
                    phase_21.append(int(row[5]))
                    continue
            if row[0] == epclist[2]:  # 读取不同的标签 目前只有三个519、529、539
                if row[1] == antlist[2]:  # 天线1
                    rssi_22.append(int(row[4]))
                    phase_22.append(int(row[5]))
        dict_all = []
        dict_all.append(rssi_00)
        dict_all.append(rssi_01)
        dict_all.append(rssi_02)
        dict_all.append(rssi_10)
        dict_all.append(rssi_11)
        dict_all.append(rssi_12)
        dict_all.append(rssi_20)
        dict_all.append(rssi_21)
        dict_all.append(rssi_22)
        dict_all.append(phase_00)
        dict_all.append(phase_01)
        dict_all.append(phase_02)
        dict_all.append(phase_10)
        dict_all.append(phase_11)
        dict_all.append(phase_12)
        dict_all.append(phase_20)
        dict_all.append(phase_21)
        dict_all.append(phase_22)
        for item in dict_all:
            tmpseries = pd.Series(item)
            tmpdf = pd.DataFrame(status(tmpseries))
            tmpdf = tmpdf.fillna(0)
            for item in tmpdf.values:
                features_single.append(item[0])
            # series_list_all.append(pd.Series(item))
        # rssi_series = pd.Series(rssi)
        # phase_seried = pd.Series(phase)
        # 第i个标签的rssi 特征
        # df_rssi = pd.DataFrame(status(rssi_series))
        # for item in df_rssi.values:
        #     features_single.append(item[0])
        # # print(features_single)
        # # 第i个标签的phase特征
        # df_phase = pd.DataFrame(status(phase_seried))
        # for item in df_phase.values:
        #     features_single.append(item[0])
        data_dic["data"].append(features_single)
        data_dic["target"].append("2")  # 类别2代表是大拇指点击
# 绘制图片时代码
# vardata = data_dic["data"]
# # print(vardata)
# var1 = np.array(vardata[0]).reshape(-1, 1)
# var2 = np.array(vardata[1]).reshape(-1, 1)
# # print(var1)
# # print(var2)
# normalizer = preprocessing.Normalizer(norm="l2", copy=True).fit(var1)
# var11 = normalizer.transform(var1)
# var11 = np.array(var11).reshape(1, -1)
# # var11 = np.array(var1).reshape(1, -1)
# # vardata_normalized2 = preprocessing.normalize(var2, norm="l2")
# normalizer = preprocessing.Normalizer(norm="l2", copy=True).fit(var2)
# var22 = normalizer.transform(var2)
# var22 = np.array(var22).reshape(1, -1)
# varlist1 = []
# varlist2 = []
# for item in var11[0]:
#     varlist1.append(item)
# # print(varlist1)
# for item in var22[0]:
#     varlist2.append(item)
# # print(varlist2)
# out = open('normalize_slide1.csv', 'a', newline='')
# csv_write = csv.writer(out, dialect='excel')
# # titlelist = ['峰峰值', '最大值', '最小值', '和', '平均值', '标准差',
# #              '平均绝对偏差', '偏度', '峰度', '25分位数', '50分位数', '75分位数']
# # csv_write.writerow(titlelist)
# csv_write.writerow(varlist1)
# csv_write.writerow(varlist2)
# out.close()
vardata = data_dic["data"]
varatarget = data_dic["target"]
print(varatarget)
output = open('data_3class.pkl', 'wb')
pickle.dump(data_dic, output)
output.close()

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
