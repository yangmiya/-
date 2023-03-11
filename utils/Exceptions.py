"""
 _*_ coding: utf-8 _*_

 Copyright (C) 2023 - 2023 Tony Huang All Rights Reserved 

 @Time    : 2023/3/10 10:13
 @Author  : Tony Huang
 @File    : Exceptions.py
 @IDE     : PyCharm
 @Contact : hhh_htz@outlook.com
 @Desc    : 自定义异常
"""
import logging

logging.getLogger('pre-handle.log').setLevel(logging.INFO)


class FileTypeUnsupportError(Exception):
    """
    文件类型不支持异常
    """

    def __init__(self, message):
        super().__init__(message)


class DataError(Exception):
    """
    数据异常
    """

    def __init__(self, message):
        super().__init__(message)


class FileError(Exception):
    """
    文件异常
    """

    def __init__(self, message):
        super().__init__(message)


class PathError(Exception):
    """
    路径异常
    """

    def __init__(self, message):
        super().__init__(message)


class ModelError(Exception):
    """
    模型异常
    """

    def __init__(self, message):
        super().__init__(message)


class ArgsError(Exception):
    """
    参数异常
    """

    def __init__(self, message):
        super().__init__(message)


class UnexpectedError(Exception):
    """
    其他异常
    """

    def __init__(self, message):
        super().__init__(message)


class GetError(Exception):
    """
    获取异常
    """

    def __init__(self, message):
        logging.error(message)
        super().__init__(message)


class DataMissingError(DataError):
    """
    数据缺失异常
    """

    def __init__(self, message, miss_data):
        super().__init__(message)
        self.message = message
        self.miss_data = miss_data

    def __str__(self):
        logging.error(self.message + '缺失数据: ' + '\n' + str(self.miss_data))
        return self.message + '缺失数据: ' + '\n' + str(self.miss_data)


class DataDuplicateError(DataError):
    """
    数据重复异常
    """

    def __init__(self, message, error_data=None):
        super().__init__(message)
        self.message = message
        self.error = '数据中存在重复值'
        self.error_data = error_data

    def __str__(self):
        logging.error(self.message + '重复数据: ' + '\n' + str(self.error_data))
        return self.message + '重复数据: ' + '\n' + str(self.error_data)


class DataNullError(DataError):
    """
    数据空值异常
    """

    def __init__(self, message, error_data=None):
        super().__init__(message)
        self.message = message
        self.error = '数据中存在空值'
        self.error_data = error_data

    def __str__(self):
        logging.error(self.message + '空值数据: ' + '\n' + str(self.error_data))
        return self.message + '空值数据: ' + '\n' + str(self.error_data)
