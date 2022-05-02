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
import socketio

import log
import configure
import sio
import logging
import traceback

import http

def create(workdir, conf):
    r""" 创建 server 服务
    """

    configure.init(workdir, conf)

    logger = logging.getLogger()
    logger.setLevel(configure.options['log']['level'])
    log.logDecorateStandard(logger, configure.options['log']['path'], configure.options['log']['name'])

    return Server()


class Server(object):
    r""" jserve 服务接口
    """

    def __init__(self):
        r""" 创建一个 server

        Args:

        workdir: string 服务运行目录，决定 log 等产出位置
        conf: 服务配置文件
        """

        self._http_server = http.Http(conf['http'])

        if 'sio' in kwargs:
            self._http_server.add_route(
                (r"/socket.io/.*/", sio.http_handler())
            )

    def run(self):
        try:
            self._http_server.run()
        except Exception as e:
            logger.error("{}\n{}".format("app exit by some fatal error", traceback.format_exc()))
        finally:
            logger.warning("app exit")

