"""
 _*_ coding: utf-8 _*_

 Copyright (C) 2023 - 2023 Tony Huang All Rights Reserved 

 @Time    : 2023/3/10 14:36
 @Author  : Tony Huang
 @File    : main.py
 @IDE     : PyCharm
 @Contact : hhh_htz@outlook.com
 """
import os
from tools.judge import GradeJudge
from utils.handler import DataHandler
from utils.backup import store_df
from utils.read_data import read_data
from tkinter import filedialog
import tkinter as tk
from conf.config import *

# 初始化流程 备份上一次的数据
if os.path.exists('Proceed.xlsx'):
    store_df(read_data('Proceed.xlsx'), '上一次处理的数据')
    os.remove('Proceed.xlsx')

# TODO: 正式环境下使用tkinter获取文件路径 本地测试使用
# 正式环境下 使用tkinter获取文件路径
# root = tk.Tk()
# root.withdraw()
#
# # 获取文件路径
# file_path = filedialog.askopenfilename()
# 文件是本目录下的stu_score.csv
file_path = 'stu_score.xlsx'

# 读取数据
dataframe = read_data(file_path)

# 处理数据
data_handler = DataHandler(dataframe, ScoreCol, StrCol)
dataframe2 = data_handler.clean_data()
print(dataframe2)

# 备份数据
store_df(dataframe2, '处理后备份')

# 评分判断
grade_judge = GradeJudge(dataframe2)
dataframe = grade_judge.handle_data()
print(dataframe)

# 保存数据
dataframe.to_excel(SaveName, index=False)
print('保存成功！')
