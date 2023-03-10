"""
 _*_ coding: utf-8 _*_

 Copyright (C) 2023 - 2023 Tony Huang All Rights Reserved 

 @Time    : 2023/3/10 14:36
 @Author  : Tony Huang
 @File    : main.py
 @IDE     : PyCharm
 @Contact : hhh_htz@outlook.com
 """
from utils.handler import HandleData
from utils.backup import store_df
from utils.check import CheckData
from utils.read_data import read_data
from utils.Exceptions import *
from tkinter import filedialog
import tkinter as tk
import pandas as pd

root = tk.Tk()
root.withdraw()

# 获取文件路径
file_path = filedialog.askopenfilename()

# 读取数据
dataframe = read_data(file_path)
print(dataframe)

# 检查+处理数据
if not CheckData.check_null(dataframe):
    """
    如果数据存在空值
    """
    dataframe = HandleData.handle_null(dataframe)
if not CheckData.check_duplicate(dataframe):
    """
    如果数据存在重复值
    """
    dataframe = HandleData.handle_duplicate(dataframe)
if CheckData.check_data_type(dataframe):
    """
    如果数据类型错误
    """
    raise DataError('数据类型错误')
if not CheckData.check_int(dataframe):
    """
    如果数据存在非整数
    """
    dataframe = HandleData.handle_int(dataframe)

# 保存数据
with pd.ExcelWriter(file_path) as writer:
    dataframe.to_excel(writer, index=False)

# 备份数据
store_df(dataframe, '处理后备份')



