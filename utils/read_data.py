"""
 _*_ coding: utf-8 _*_

 Copyright (C) 2023 - 2023 Tony Huang All Rights Reserved 

 @Time    : 2023/3/10 12:32
 @Author  : Tony Huang
 @File    : read_data.py
 @IDE     : PyCharm
 @Contact : hhh_htz@outlook.com
 """
import logging
import utils.backup as bk
import pandas as pd

from utils.Exceptions import FileTypeUnsupportError
from utils.backup import backup

logging.getLogger(__name__)


def read_data(path):
    """
    读取数据
    :param path: 数据路径
    :return: 数据
    """
    # 读取文件后缀
    file_type = path.split('.')[-1]
    if file_type == 'csv':
        data = pd.read_csv(path)
        df = pd.DataFrame(data)
        df1 = df.copy()
        bk.store_df(df1, '原始文件备份')
    elif file_type == 'xlsx' or file_type == 'xls':
        data = pd.read_excel(path)
        df = pd.DataFrame(data)
        df1 = df.copy()
        bk.store_df(df1, '原始文件备份')
    else:
        print('path:', path)
        raise FileTypeUnsupportError('文件类型不支持')
    return df
