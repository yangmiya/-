"""
 _*_ coding: utf-8 _*_

 Copyright (C) 2023 - 2023 Tony Huang All Rights Reserved 

 @Time    : 2023/3/10 21:10
 @Author  : Tony Huang
 @File    : judge.py
 @IDE     : PyCharm
 @Contact : hhh_htz@outlook.com
 """
import logging
import os
from pandas import DataFrame as dataframe
import pandas as pd
from conf.config import *


class GradeJudge(object):
    """
    评分判断
    总分 = 除 学号 班级 姓名 性别 外的所有分数之和
    排名 = 总分从高到低排序 从1开始
    评价 = 根据排名判断 前25%优秀 50%良好 30%中等 40%及格
    """

    def __init__(self, dataframe: dataframe):
        """
        初始化
        :param dataframe:
        """
        self.dataframe = dataframe
        self.ScoreCol = ScoreCol

    def handle_data(self):
        """
        处理数据
        :return:
        """
        # 计算总分, 把总分列放在最后一列
        self.dataframe['总分'] = self.dataframe[ScoreCol].sum(axis=1)
        # 新增一列排名，把排名列放在最后一列，以总分从高到低排序 从1开始
        self.dataframe['排名'] = self.dataframe['总分'].rank(ascending=False, method='first')

        # 评价
        self.dataframe['评价'] = self.dataframe['排名'].apply(
            lambda x: '优秀' if x <= 0.25 * len(self.dataframe) else '良好' if x <= 0.5 * len(
                self.dataframe) else '中等' if x <= 0.8 * len(self.dataframe) else '及格')

        # 保存数据
        self.dataframe.to_excel(SaveName, index=False)
        logging.info('保存成功！')

        return self.dataframe


if __name__ == '__main__':
    # 读取数据.
    # 文件'C:\Users\Administrator\Desktop\cansai\stu_score.xlsx'
    file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'stu_score.xlsx')
    dataframe = pd.read_excel(file)

    # 处理数据
    grade_judge = GradeJudge(dataframe)
    dataframe = grade_judge.handle_data()
    print(dataframe)
