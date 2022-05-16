#!/usr/bin/env python3
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


__event_paths = []

def init(is_async=True, **kwargs):
    r""" 初始化 socketio 服务，赋值 sio 对象
    """
    global sio
    global __event_dirs

    if sio is not None:
        raise Exception("you can't init jsocketio twice")

    sio = __create_async_server(**kwargs) if is_async else __create_sync_server(**kwargs)
    add_event(os.path.join(os.path.dirname(__file__), 'basic_event.py'))

    for event_path in __event_paths:
        __load_event(event_path)


def http_handler(**kwargs):
    r""" 返回 http 处理器
    """
    global sio
    return socketio.get_tornado_handler(sio)


def add_event(event_path):
    r""" 添加事件

    Args:
    event_path: 加载 module 完成事件注册 (1) 如果指定文件，加载对应 module, (1) 如果指定目录，将遍历并 import 所有 module
    """
    global __event_paths
    __event_paths.append(event_path)


def __load_event(path):
    r""" 遍历 path 目录 .py 模块，完成 @sio 事件的加载
    """

    def help_load(file):
        r""" 辅助加载函数
        """

        if re.match("^_", file):
            return "none", "ignore"

        mod_name = file[:-3]   # strip .py at the end
        importlib.import_module(mod_name)
        return mod_name, "success"

    module_files = []

    module_dir = path
    if os.path.isfile(path):
        module_dir = os.path.dirname(path)
        module_files.append(os.path.basename(path))
    elif os.path.isdir(path):
        for file in os.listdir(path):
            module_files.append(file)

    """ todo: 是否有不污染 sys.path 的优雅方式, remove path from sys.path """
    sys.path.append(module_dir)
    for file in module_files:
        mod_name, state = help_load(file)
        logger.warning("state[{}] importlib [{}] from path[{}] file[{}]".format(
            state, mod_name, path, file
        ))


def __config_server(kwargs, is_async=True):
    r""" 完成 server 创建的配置构建

    https://python-socketio.readthedocs.io/en/latest/api.html#server-class
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

