#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: jserver.py
Author: jcppython(jcppython@outlook.com)
Date: 2022/05/01 20:50:18
"""

import argparse

import jserve.server

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='the demo of jserve')
    parser.add_argument('--conf', type=str, required=True)
    parser.add_argument('--workdir', type=str, required=True)
    args = parser.parse_args()

    server = jserve.run(args.workdir, args.conf)


