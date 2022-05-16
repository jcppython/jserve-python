#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: basic_event.py
Author: jcppython(jcppython@outlook.com)
Date: 2022/05/02 00:50:18
"""

import logging

from jserve.jsocketio.socketio import sio
from jserve.talk import Talk

logger = logging.getLogger()
namespace = '/test'

class EventDefault(object):
    """
    默认事件
    """

    @sio.on('connect', namespace=namespace)
    async def connect(sid, sioenv):
        """
        建连事件
        """

        talk = Talk(talkid=sid, sioenv=sioenv)

        logger.warning('connect sid[{}] username [{}]'.format(sid, talk.username))
        sio.get_session()

        ''' reject request with return false or raise exception '''
        if False:
            raise socketio.exceptions.ConnectionRefusedError('authentication failed')

    @sio.on('disconnect', namespace=namespace)
    def disconnect(sid):
        r""" 断开连接事件
        """
        logger.warning('disconnect {}'.format(sid))

    @sio.on('*', namespace=namespace)
    async def catch_all(event, sid, data):
        r"""
        “catch-all” event handler is invoked for any events that do not have an event handler
        """
        logger.warning('message by catch-all event[{}] sid[{}] {}'.format(event, sid, data))

    @sio.on('my message', namespace=namespace)
    async def my_message1(sid, data):
        r""" 测试事件，只接收
        """
        logger.warning('message {}'.format(data))

    @sio.on('my message', namespace=namespace)
    async def my_message(sid, data):
        r""" 测试事件，接收和发送数据
        """
        logger.warning('message {}'.format(data))
        await sio.emit("client event", "hello {}".format(sid))
        async with sio.session(sid, namespace=namespace) as session:
            # session['username'] = username
            pass

        return "OK", 123

