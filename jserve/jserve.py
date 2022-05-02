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
import tornado
import tornado.web
import tornado.options
import tornado.platform.asyncio

import log
import configure
import ssocketio

class Server(object):
    r""" App 服务
    """

    @classmethod
    def run(cls, port, routes):
        r""" 需要捕获异常
        """
        tornado.platform.asyncio.AsyncIOMainLoop().install()

        cls.__enable_log()
        app = cls.__create_app(routes)
        app.listen(port)

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

    @classmethod
    def __enable_log(cls):
        """
        启用日志
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

    @classmethod
    def __create_app(cls, routes):
        ssocketio.init(True, async_mode='tornado', cors_allowed_origins="*")
        ssocketio.load_event("./event/")

        routes.append(
            (r"/socket.io/.*/", socketio.get_tornado_handler(ssocketio.sio))
        )

        return tornado.web.Application(
            routes,
            settings = dict(
                debug=True,
                autoescape=None
            )
        )
