#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: jye
@email: jj.wu@idiaoyan.com
@time: 2019/8/10 0:03
"""
from random import randint


def ip_to_int(ip: str):
    ip_list = ip.split('.')  # ['192',]
    bin_ip = []
    for i in ip_list:
        ip = bin(int(i))[2:]
        ip = ip.zfill(8)
        bin_ip.append(ip)

    _b = '0b' + ''.join(bin_ip)
    return int(_b, 2)


def int_to_ip(num):
    bin_ip = bin(num)[2:].zfill(32)

    ip_list = []
    for i in range(0, 32, 8):
        # 0-8, 9-16, 17, 24, 25
        ip = '0b' + bin_ip[i: i + 8]
        ip = int(ip, 2)
        ip_list.append(str(ip))

    return '.'.join(ip_list)


def gen_ip_list(ip_settings: list):
    """

    :param ip_settings:
    :return:
    """

    ran_ip_list = []
    for st in ip_settings:
        min = st.get('min')
        max = st.get('max')
        count = st.get('count')
        for i in range(count):
            num_min = ip_to_int(min)
            num_max = ip_to_int(max)
            ran_int = randint(num_min, num_max)
            ip = int_to_ip(ran_int)
            ran_ip_list.append(ip)
    return ran_ip_list


if __name__ == "__main__":
    num = ip_to_int('255.255.255.1')
    ip = int_to_ip(num)

    print(ip, num)
