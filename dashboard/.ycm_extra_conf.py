#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# File   : .ycm_extra_conf.py
# Author : Yiqi Sun
# Email  : ysun697@gatech.com
# Date   : 05/07/2022
#
# This file is part of dashboard.
# Distributed under terms of the MIT license.

import os.path as osp

def PythonSysPath(**kwargs):
    sys_path = kwargs['sys_path']
    sys_path.insert(0,osp.dirname(__file__))
    return sys_path