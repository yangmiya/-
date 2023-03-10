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
        if self.dataframe.isnull().values.any():
            logger.warning('数据存在空值')
            # 用均值填充
            self.dataframe = self.dataframe.fillna(self.dataframe.mean())
            return self.dataframe
        else:
            logger.info('数据不存在空值')
            return self.dataframe

    def handle_duplicate(self):
        """
        处理数据中的重复值
        :return: pandas.DataFrame
        """
        if self.dataframe.duplicated().values.any():
            logger.warning('数据存在重复值')
            self.dataframe = self.dataframe.drop_duplicates()
            logger.info('已删除重复值')
            return self.dataframe
        else:
            logger.info('数据不存在重复值')
            return self.dataframe

    def handle_outlier(self):
        """
        处理数据中的异常值
        :return: pandas.DataFrame
        """
        if self.dataframe.isnull().values.any():
            logger.warning('数据存在异常值')
            self.dataframe = self.dataframe.dropna()
            logger.info('已删除异常值')
            return self.dataframe
        else:
            logger.info('数据不存在异常值')
            return self.dataframe

    def handle_all(self):
        """
        处理数据中的所有异常
        :return: pandas.DataFrame
        """
        self.dataframe = self.handle_null()
        self.dataframe = self.handle_duplicate()
        self.dataframe = self.handle_outlier()
        return self.dataframe
