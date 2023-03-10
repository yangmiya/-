"""
 _*_ coding: utf-8 _*_

 Copyright (C) 2023 - 2023 Tony Huang All Rights Reserved 

 @Time    : 2023/3/10 10:07
 @Author  : Tony Huang
 @File    : check.py
 @IDE     : PyCharm
 @Contact : hhh_htz@outlook.com
 """
from conf.config import *
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
        # 从StrCol中获取应为字符串类型的列
        str_col = StrCol
        if self[str_col].applymap(lambda x: isinstance(x, str)).all().all():
            logger.info('应为字符串的列校验通过')
        else:
            # 报错精确到哪一列第几行
            logger.error('应为字符串的列校验未通过', exc_info=True)
        # 检查ScoreCol中的列是否为整数类型
        score_col = ScoreCol
        if self[score_col].applymap(lambda x: isinstance(x, int)).all().all():
            logger.info('应为整数的列校验通过')
            return True
        else:
            logger.error('应为整数的列校验未通过', exc_info=True)
            return False

    def check_int(self):
        """
        检查数据是否为整数类型
        :return: bool
        """
        # 检查是否有非整数的值
        for col in ScoreCol:
            if self[col].apply(lambda x: isinstance(x, int)).all():
                logger.info('数据类型正确')
                return True
            else:
                logger.error('数据类型错误', exc_info=True)
                return False
