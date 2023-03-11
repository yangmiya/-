"""
 _*_ coding: utf-8 _*_

 Copyright (C) 2023 - 2023 Tony Huang All Rights Reserved 

 @Time    : 2023/3/10 12:29
 @Author  : Tony Huang
 @File    : backup.py
 @IDE     : PyCharm
 @Contact : hhh_htz@outlook.com
 """
import datetime
import os
import logging

logging.basicConfig(level=logging.INFO, filename='backup.log', filemode='w', format='%(asctime)s - %(name)s - %('
                                                                                    'levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def backup(path, info):
    """
    备份文件
    :param path: 文件路径
    :type path: str
    :param info: 备份信息
    :type info: str
    :return: None
    """
    # 清空超过七天的备份文件
    for file in os.listdir(os.path.dirname(path)):
        if file.split('.')[-1] == 'csv':
            # 获取文件创建时间
            create_time = datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(os.path.dirname(path), file)))
            # 获取当前时间
            now = datetime.datetime.now()
            # 计算文件创建时间与当前时间的差值
            delta = now - create_time
            # 如果文件创建时间与当前时间的差值大于7天
            if delta.days > 7:
                # 删除文件
                os.remove(os.path.join(os.path.dirname(path), file))
                logger.info('删除文件成功，文件路径为：{}'.format(os.path.join(os.path.dirname(path), file)),
                            extra={'info': info})
    # 获取文件名
    file_name = path.split('\\')[-1]
    # 获取文件后缀
    file_type = file_name.split('.')[-1]
    # 获取当前时间
    now = datetime.datetime.now()
    # 生成备份文件名
    backup_file_name = file_name.split('.')[0] + '_' + str(now.year) + str(now.month) + str(now.day) + str(
        now.hour) + str(
        now.minute) + str(now.second) + '.' + file_type
    # 生成备份文件路径
    backup_path = os.path.join(os.path.dirname(path), backup_file_name)
    # 备份文件
    os.rename(path, backup_path)
    logger.info('备份文件成功，备份文件路径为：{}'.format(backup_path), extra={'info': info})


def store_df(df, info):
    """
    将DataFrame存储为csv文件
    :param df: DataFrame
    :type df: pandas.DataFrame
    :param info: 备份信息
    :type info: str
    :return: None
    """
    # 生成文件路径
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'backup', 'backup {}.csv'.format(info))
    # 如果文件存在
    if os.path.exists(path):
        # 删除文件
        os.remove(path)
    # 将DataFrame存储为xlsx文件
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'backup', 'backup {}.xlsx'.format(info))
    df.to_excel(path, index=False)
    logger.info('存储文件成功，文件路径为：{}'.format(path), extra={'info': info})
