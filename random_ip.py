#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: jye
@email: jj.wu@idiaoyan.com
@time: 2019/8/10 0:03
"""
from flask import Flask, render_template, request
import os, socket, struct,random

ip_to_int = lambda x: sum([256 ** j * int(i) for j, i in enumerate(x.split('.')[::-1])])
int_to_ip = lambda x: '.'.join([str(x/(256**i)%256) for i in range(3,-1,-1)])




def gen_ip_list(ip_settings):
    ip_list = []
    ran_ip_list = []
    for settings in ip_settings:
        min_ip = settings['min']
        max_ip = settings['max']
        count_ip = settings['count']
        for i in range(1,int(count_ip)+1):
            int_ip = random.randint(ip_to_int(min_ip), ip_to_int(max_ip) + 1)
            ip_list.append(int_ip)
    for j in ip_list:
        ran_ip_list.append(int_to_ip(j))
    return ran_ip_list



