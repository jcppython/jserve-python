# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: log.py
Author: jcppython(jcppython@outlook.com)
Date: 2022/04/30 16:17:12
Ref: 我们讲日志分为两类：一次处理过程集中打印一条记录-INFO、其它各类错误统一打分-WARN
"""

import os
import logging

class InfoFilter(logging.Filter):
    r""" 仅打印 INFO 级别日志过滤器 xx.log
    """
    def filter(self, record):
        """
        过滤规则
        """
        return record.levelno == logging.INFO


class WarnFilter(logging.Filter):
    r""" 打印除 INFO 外的日志过滤器: xx.log.wf
    """
    def filter(self, record):
        """
        过滤规则
        """
        return record.levelno != logging.INFO


def logDecorateStandard(logger, logpath, name):
    r"""
    创建 xx.log 和 xx.log.wf 标准日志
    """

    hnotice = createFileHandler("{}/{}.log".format(logpath, name), InfoFilter())
    hwarn = createFileHandler("{}/{}.log.wf".format(logpath, name), WarnFilter())
    logger.addHandler(hnotice)
    logger.addHandler(hwarn)


def createFileHandler(fullfile, logfilter=None,
        formatter='%(asctime)-15s %(message)s', datefmt='%Y-%m-%d %H:%M:%S'):
    r""" 创建日志打印的文件 handler

    Args:

    fullname: 包含全路径的文件名

    filter: 应用的过滤器, None

    formatter: 日志格式, None 则采用标准格式（组内工程, 你通常应该用 None)
    """

    log_path = os.path.dirname(fullfile)
    try:
        os.makedirs(log_path)
    except OSError:
        pass

    handler = logging.handlers.TimedRotatingFileHandler(fullfile)
    handler.setFormatter(logging.Formatter(formatter, datefmt))
    handler.setLevel(logging.DEBUG)
    if logfilter is not None:
        handler.addFilter(logfilter)

    return handler
