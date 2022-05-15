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

def init(workdir, conf):
    r""" 初始化配置
    """
    global options

    if options is not None:
        raise Exception("you can't init configure twice")

    with open(conf) as f:
        options = json.load(f)

    __buildin_option(workdir)


def add_option(path, value):
    r""" 添加配置

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


def __buildin_option(workdir):
    """
    填充内置配置项
    """
    global options

    add_option('env.workdir', workdir)
    options['log']['path'] = os.path.join(options['env']['workdir'], options['log']['path'])
    options['log']['level'] = getattr(logging, options['log']['level'].upper())
