#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: http.py
Author: jcppython(jcppython@outlook.com)
Date: 2022/05/02 17:50:18
"""

from abc import abstractmethod

class Http(object):
    r""" http 服务
    """

    def __init__(self):
        r""" 初始化服务
        """
        self._routes = ()

    @abstractmethod
    def add_route(self, route, handler):
        r""" 添加请求处理路由
        """
        pass

    @abstractmethod
    def run(self):
        r""" 运行服务
        """
        pass

