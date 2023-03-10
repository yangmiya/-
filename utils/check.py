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
        :param dataframe: pandas.DataFrame
        :return: bool
        """
        # 报错 AttributeError: 'DataFrame' object has no attribute 'dataframe'
        if self.isnull().values.any():
            logger.error('数据存在空值', exc_info=True)
            return False
        else:
            logger.info('数据不存在空值')
            return True

    def check_duplicate(self):
        """
        检查数据是否有重复值
        :return: bool
        """
        if self.duplicated().any():
            logger.error('数据存在重复值', exc_info=True)
            return False
        else:
            logger.info('数据不存在重复值')
            return True

    # def check_data_type(self):
    #     """
    #     检查数据类型
    #     :return: bool
    #     """
    #     if self.dtypes == 'object':
    #         logger.error('数据类型错误', exc_info=True)
    #         raise DataError('数据类型错误')
    #     else:
    #         logger.info('数据类型正确')
    #         return True

    def check_data_type(self):
        """
        检查数据类型
        :return: bool
        """
        # 检查姓名和性别列是否为字符串类型
        if isinstance(self['姓名'].dtype, object) and isinstance(self['性别'].dtype, object):
            logger.info('姓名和性别列为字符串类型')
        else:
            logger.error('姓名或性别列不是字符串类型', exc_info=True)
            raise DataError('姓名或性别列不是字符串类型')

        # 检查其他列是否为整数类型
        for col in self.columns:
            if col not in ['姓名', '性别']:
                if isinstance(self[col].dtype, int):
                    logger.info(f'{col}列为整数类型')
            else:
                logger.error(f'{col}列不是整数类型', exc_info=True)
                return False

    def check_int(self):
        """
        检查数据是否为整数类型
        :return: bool
        """
        # 检查是否有非整数的值
        for col in self.columns:
            if col not in ['姓名', '性别']:
                if self[col].apply(lambda x: not isinstance(x, int)).any():
                    logger.info(f'{col}列有非整数的值')
                    return False
                else:
                    logger.info(f'{col}列没有非整数的值')
                    return True
