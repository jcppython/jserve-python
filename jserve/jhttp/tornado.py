#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: jserve.py
Author: jcppython(jcppython@outlook.com)
Date: 2022/05/02 01:50:18
"""

import os
import asyncio
import tornado
import tornado.log
import tornado.platform.asyncio

from .. import log
from .. import configure
from .http import Http

class Tornado(Http):
    r""" 基于 tornado 的 http 服务
    """

    def __init__(self):
        r"""
        """
        super(Tornado, self).__init__()
        self.__enable_log()
        self._routes = []

    def run(self):
        r""" 需要捕获异常
        """

        tornado.platform.asyncio.AsyncIOMainLoop().install()

        self._app = tornado.web.Application(
            self._routes,
            settings = dict(
                debug=True,
                autoescape=None
            )
        )
        self._app.listen(configure.options['app']['port']['http'])

        loop = asyncio.get_event_loop()
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            for task in asyncio.Task.all_tasks():
                task.cancel()
            loop.stop()
            loop.run_forever()
        finally:
            loop.close()

    def add_route(self, route, handler):
        r""" 添加路由
        """
        self._routes.append((route, handler))

    def __enable_log(self):
        r""" 设置日志
        """

        config = [
            {
                'logger': tornado.log.access_log,
                'file': 'tornado_access.log'
            },
            {
                'logger': tornado.log.gen_log,
                'file': 'tornado_other.log'
            },
            {
                'logger': tornado.log.app_log,
                'file': 'tornado_other.log'
            }
        ]

        for d in config:
            h = log.createFileHandler(os.path.join(configure.options['log']['path'], d['file']))
            d['logger'].addHandler(h)
            d['logger'].setLevel(configure.options['log']['level'])

