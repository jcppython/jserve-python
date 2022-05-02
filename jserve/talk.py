# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: talk.py
Author: jcppython(jcppython@outlook.com)
Date: 2022/04/30 16:50:18
"""

from abc import abstractmethod
from http.cookies import SimpleCookie


class Talk(object):
    r"""
    - 功能

    1. 管理一次 “对话” 过程中与 “单次请求逻辑” 无关的数据（类比 session）。业务请求数据由 request 管理
    2. 同一会话的不同请求之间会共享一份 talk 数据

    - 实现

    1. 为支持序列化存储，以 json 存放在 self._info 字段（注意：不是 dict 数据）
    2. 在请求处理入口，会调用对应类型的 parser 解析数据。在组件初始化时需要 register 注册
    3. 不保证是采用 session 来实现
    """

    __talks = {}

    ''' 记录各类解析器 '''
    __parser = {
        'sioenv': None,
        'webenv': None,
        'curlenv': None
    }

    @classmethod
    def register(cls, talk_type, parser):
        r""" 注册解析器，同一类型只允许注册一个

        Args:

        talk_type: string 类型，已内置常用: 'sioenv', 'webenv', 'curlenv'

        Returns:

        Raises:
            Exception: 同一类型重复注册
        """
        if talk_type in cls.__parser:
            raise Exception("register parser twice for the same type")

        cls.__parser[talk_type] = parser

    def __init__(self, talk_type, talk_id, data):
        r"""
        Args:

        talk_type: 参考 register 接口
        talk_id: string 类型，一个会话的唯一标识

        sioenv: object 来自 socket io 的环境数据，参考 connect 接口
        webenv: object 来自浏览器 http 请求的环境数据
        curlenv: object 来自机器人 http 请求的环境数据
        """

        parser = Talk.__parser[talk_type]
        if parser is None:
            raise Exception("can't find parser for type")

        parser.parse(self, data)

    def set(self, name, value):
        r""" 设置字段
        """
        self._info[name] = value

    def get(self, name):
        r""" 获取字段
        """
        return self._info[name]


class BasicParser(object):
    """
    解析器接口类，需要业务实现
    """

    @classmethod
    @abstractmethod
    def parse(cls, **kwargs):
        """
        """
        pass

    @property
    @abstractmethod
    def talk_type(cls):
        pass
