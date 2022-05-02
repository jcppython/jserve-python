# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: jsocketio.py
Author: jcppython(jcppython@outlook.com)
Date: 2022/05/01 20:50:18
Ref: https://python-socketio.readthedocs.io/en/latest/api.html#server-class
"""

import os
import sys
import re
import eventlet
import socketio
import importlib
import logging


logger = logging.getLogger()
sio = None


def init(is_async=True, **kwargs):
    r""" 初始化 socketio 服务，赋值 sio 对象
    """
    global sio

    if sio is not None:
        raise Exception("you can't init jsocketio twice")

    sio = __create_async_server(**kwargs) if is_async else __create_sync_server(**kwargs)


def load_event(path):
    r""" 遍历 path 目录 .py 模块，完成 @sio 事件的加载
    """

    def help_load(file):
        r""" 辅助加载函数
        """

        if re.match("^_", file):
            return "none", "ignore"

        mod_name = file[:-3]   # strip .py at the end
        importlib.import_module(mod_name, package=__name__)
        return mod_name, "success"

    sys.path.append(path)
    for file in os.listdir(path):
        mod_name, state = help_load(file)
        logger.warning("state[{}] importlib [{}] from path[{}] file[{}]".format(
            state, mod_name, path, file
        ))


def __config_server(kwargs, is_async=True):
    r""" 完成 server 创建的配置构建

    https://python-socketio.readthedocs.io/en/latest/server.html#emitting-from-external-processes
    connect to the redis queue as an external process
    external_sio = socketio.RedisManager('redis://', write_only=True)
    """

    # kwargs['client_manager'] = socketio.RedisManager('redis://')
    kwargs['logger'] = logger
    kwargs['engineio_logger'] = logger
    return kwargs


def __create_sync_server(**kwargs):
    r""" 创建同步 sio 服务
    todo: 这是一个未经测试的服务
    """

    return socketio.Server(**__config_server(kwargs, True))


def __create_async_server(**kwargs):
    r""" 创建异步 sio 服务
    """

    return socketio.AsyncServer(**__config_server(kwargs, True))

