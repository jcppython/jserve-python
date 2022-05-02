# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: record.py
Author: jcppython(jcppython@outlook.com)
Date: 2022/04/30 16:15:12
Ref: 追踪一个处理逻辑，记录其中的关键字段 {k: v}，提供 str() 接口供日志打印
"""

import os
import time


class Record(object):
    r""" record 实例负责全流程追踪一个记录
    """

    def __init__(self, name):
        self.__items = {}
        self.__times = {}
        self.record_name = name

    def __del__(self):
        r"""

        Todo:
        检查是否 name 都 start ~ end 闭环等
        """
        pass

    def string():
        r""" 生成当前 recorder 数据的字符串 \t 分割
        """
        l0 = [f'{key}={value}' for key, value in self.__items.items()]
        l1 = [f'{key}={value}' for key, value in self.__items.times()]
        l = [l0, l1]
        s = '\t'.join([l0, l1])
        return s

    def add(self, desc, name, value):
        r""" 增加 name=value 日志字段，会覆盖已存在字段

        Args:
        name: 字段名
        value: 字段值
        desc: 是 name 的含义解释，代码要解释自己。todo：生成日志文档

        Returns:
        """
        self.__items[name] = value

    def start(self, name, desc):
        r""" 开始 name 字段的计时（ms）

        Args:
        name: 字段名
        desc: 是 name 的含义解释，代码要解释自己。todo：生成日志文档

        Returns:
        """
        self.__times[name] = int(round(time.time() * 1000))

    def end(self, name):
        r""" 结束 name 字段的计时（ms）

        Args:
        name: 字段名

        Returns:
        """
        self.__times[name] = int(round(time.time() * 1000)) - self.__times[name]

    def increase(self, name, time, desc=None):
        r""" 为 name 增加指定耗时(ms)

        Args:
        name: 字段名
        time: 增加的耗时
        desc: 是 name 的含义解释，name 字段已存在时不需要提供描述，代码要解释自己。todo：生成日志文档

        Returns:
        """
        if name not in self.__times and desc is None:
            raise Exception("desc can't be none first")

        self.__times[name] = self.__times[name] + time
