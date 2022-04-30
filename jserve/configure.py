#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: configure.py
Author: jcppython(jcppython@outlook.com)
Date: 2022/04/30 16:05:33
"""

import os
import logging
import json

options = None

__fixed_sserver_conf = "conf/sserver.conf"
__fixed_sserver_logname = "app"

def add_option(path, value):
    """
    添加指定配置

    Args:

    path: 形如 "a.b.c.d" 指定配置项路径位置

    value: 具体值 object 类型（内部维护的 dict）
    """
    global options
    p = options

    path = path.split(".")
    length = len(path)
    for index, key in enumerate(path):
        if index == length - 1:
            p[key] = value
        elif key not in p:
            p[key] = {}
            p = p[key]
        else:
            p = p[key]


def __buildin_option(workdir, category):
    """
    填充内置配置项
    """
    global options

    options['app']['name'] = category
    add_option('env.workdir', workdir)
    options['log']['name'] = __fixed_sserver_logname
    options['log']['path'] = os.path.join(options['env']['workdir'], options['log']['path'])
    options['log']['level'] = getattr(logging, options['log']['level'].upper())


def init(workdir, category):
    """
    创建配置
    """
    global options

    if options is not None:
        raise Exception("you can't init configure twice")

    with open("{}/{}/{}".format(workdir, category, __fixed_sserver_conf)) as f:
        options = json.load(f)

    __buildin_option(workdir, category)

