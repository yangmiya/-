"""
 _*_ coding: utf-8 _*_

 Copyright (C) 2023 - 2023 Tony Huang All Rights Reserved 

 @Time    : 2023/3/10 12:45
 @Author  : Tony Huang
 @File    : handler.py
 @IDE     : PyCharm
 @Contact : hhh_htz@outlook.com
 """
# 处理数据中的空值 异常值 以及重复值
import pandas as pd
import numpy as np
import logging
from utils.Exceptions import *
from utils.backup import backup, store_df

logging.basicConfig(level=logging.INFO, filename='pre-handle.log', filemode='w', format='%(asctime)s - %(name)s - %('
                                                                                        'levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class HandleData(object):
    """
    处理数据中的空值 异常值 以及重复值
    :param object: pandas.DataFrame
    """

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def handle_null(self):
        """
        处理数据中的空值
        :return: pandas.DataFrame
        """
        if self.isnull().values.any():
            logger.warning('数据存在空值')
            store_df(self, '替换空值前备份')
            # 空值用0填充
            self = self.fillna(0)
            logger.info('已用0填充空值')
            return self
        else:
            logger.info('数据不存在空值')
            return self

    def handle_duplicate(self):
        """
        处理数据中的所有值重复的行
        :return: pandas.DataFrame
        """
        if self.duplicated().any():
            store_df(self, '删除重复值前备份')
            logger.warning('第{}行数据存在重复值'.format(self.duplicated().any()))
            # 删除重复的行
            self = self.drop_duplicates()
            logger.info('已删除第{}行数据'.format(self.duplicated().any()))
            return self
        else:
            logger.info('数据不存在重复值')
            return self

    def handle_format(self):
        """
        处理数据中的格式异常
        :return: pandas.DataFrame
        """
        store_df(self.dataframe, '格式化异常前备份')
        # 除['姓名', '性别']外的列应为int类型，查询格式异常的数据，使用0替换
        for col in self.dataframe.columns:
            if col not in ['姓名', '性别']:
                self.dataframe[col] = self.dataframe[col].apply(lambda x: 0 if type(x) != int else x)
        logger.info('已将格式异常的数据替换为0')
        return self.dataframe

    def handle_all(self):
        """
        处理数据中的所有异常
        :return: pandas.DataFrame
        """
        self.dataframe = self.handle_null()
        self.dataframe = self.handle_duplicate()
        self.dataframe = self.handle_format()
        return self.dataframe

    def handle_int(self):
        """
        处理非int类型的数据
        :return: pandas.DataFrame
        """
        # 把非整数的值转换为0
        for col in self.columns:
            if col not in ['姓名', '性别']:
                self[col] = pd.to_numeric(self[col], errors='coerce').fillna(0).astype(int)
        logger.info('已把非整数的值转换为0')
