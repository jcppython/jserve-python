# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: jserve.py
Author: jcppython(jcppython@outlook.com)
Date: 2022/05/02 01:50:18
"""

import os
import logging
import asyncio

import logging
import traceback
import importlib

from . import configure
from . import log
from . import jsocketio
from .jhttp import tornado as jtornado
import jserve.jsocketio.socketio as socketio

__http_server = None


def create_http_server():
    r""" 创建 http 服务

    todo:
    需要改成动态 import 对应的 http 框架
    """
    if configure.options['http']['type'] == 'tornado':
        return jtornado.Tornado()

    return None

def run(workdir, confFile):
    r""" 创建 server 服务
    """
    global __http_server

    configure.init(workdir, confFile)

    logger = logging.getLogger()
    logger.setLevel(configure.options['log']['level'])
    log.logDecorateStandard(logger, configure.options['log']['path'], configure.options['log']['name'])

    __http_server = create_http_server()

    if 'socketio' in configure.options:
        socketio.init(True, async_mode='tornado', cors_allowed_origins="*")
        socketio_route = configure.options['socketio']['route']
        __http_server.add_route(
            f"/{socketio_route}/.*/", socketio.http_handler()
        )

    try:
        __http_server.run()
    except Exception as e:
        logger.error("{}\n{}".format("app exit by some fatal error", traceback.format_exc()))
    finally:
        logger.warning("app exit")
