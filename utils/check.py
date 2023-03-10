"""
 _*_ coding: utf-8 _*_

 Copyright (C) 2023 - 2023 Tony Huang All Rights Reserved 

 @Time    : 2023/3/10 10:07
 @Author  : Tony Huang
 @File    : check.py
 @IDE     : PyCharm
 @Contact : hhh_htz@outlook.com
 """
import pandas as pd
from utils.Exceptions import *

logging.basicConfig(level=logging.INFO, filename='pre-handle.log', filemode='w', format='%(asctime)s - %(name)s - %('
                                                                                        'levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class CheckData(object):
    """
    检查数据
    :param object: pandas.DataFrame
    """

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def check_null(self):
        """
        检查数据是否有空值
        :return: bool
        """
        if self.dataframe.isnull().values.any():
            logger.error('数据存在空值', exc_info=True)
            raise DataNullError('数据存在空值')
        else:
            logger.info('数据不存在空值')
            return True

    def check_duplicate(self):
        """
        检查数据是否有重复值
        :return: bool
        """
        if self.dataframe.duplicated().any():
            logger.error('数据存在重复值', exc_info=True)
            raise DataError('数据存在重复值')
        else:
            logger.info('数据不存在重复值')
            return True

    def check_data_type(self):
        """
        检查数据类型
        :return: bool
        """
        if self.dataframe.dtypes == 'object':
            logger.error('数据类型错误', exc_info=True)
            raise DataError('数据类型错误')
        else:
            logger.info('数据类型正确')
            return True
