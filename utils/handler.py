"""
 _*_ coding: utf-8 _*_

 Copyright (C) 2023 - 2023 Tony Huang All Rights Reserved 

 @Time    : 2023/3/10 22:08
 @Author  : Tony Huang
 @File    : handler.py
 @IDE     : PyCharm
 @Contact : hhh_htz@outlook.com
 """
# 导入pandas库
import pandas as pd
import logging
from conf.config import *

logging.getLogger().setLevel(logging.INFO)


# class DataHandler:
#     def __init__(self):
#         self.dataframe = dataframe
#         self.scorecol = ScoreCol
#         self.strcol = StrCol
#
#     def clean_data(self):
#         # 去除重复行
#         self.drop_duplicates(inplace=True)
#         # 在ScoreCol范围内去除空值，inplace=True表示在原数据上修改，用0填充
#         self.dropna(subset=self.scoreCol, how='all', inplace=True)
#         # 用0 替换ScoreCol范围内不为int类型的数据
#         self[self.ScoreCol] = self.dataframe[self.ScoreCol].fillna(0).astype(int)
#         # 把StrCol范围内的数据转换为str类型
#         self[self.StrCol] = self.dataframe[self.StrCol].astype(str)
class DataHandler:
    def __init__(self, dataframe, scorecol, strcol):
        self.dataframe = dataframe
        self.scorecol = scorecol
        self.strcol = strcol

    def clean_data(self):
        # 去除重复行
        self.dataframe.drop_duplicates(inplace=True)
        # 在ScoreCol范围内 把所有空值替换为0
        self.dataframe[self.scorecol] = self.dataframe[self.scorecol].fillna(0)

        # 用0 替换ScoreCol范围内不为int类型的数据
        def to_int(x):
            try:
                return int(x)
            except ValueError:
                return 0

        self.dataframe[self.scorecol] = self.dataframe[self.scorecol].applymap(to_int)
        # 把StrCol范围内的数据转换为str类型
        self.dataframe[self.strcol] = self.dataframe[self.strcol].astype(str)
        return self.dataframe
