#! /usr/bin/python

"""
@author: jye
@email: jj.wu@idiaoyan.com
@time: 2019/6/5 18:42
"""
import json

from flask import Flask, render_template, request
from random_time import do_gene_random_time
from random_ip import gen_ip_list

app = Flask(__name__)


@app.route('/')
def index():
    return 'test'


@app.route('/random/time', methods=['GET', 'POST'])
def page_random_time():
    if request.method == 'GET':
        return render_template('random_time.html')

    if request.method == 'POST':
        res = {'status': 1}
        max_bg_time = request.form["max_begin_time"]
        min_bg_time = request.form["min_begin_time"]
        min_last_time = request.form["min_last_time"]
        max_last_time = request.form["max_last_time"]
        gene_count = request.form["gene_count"]

        advenable_bg_time = request.form["advenable_bg_time"]  # 开始时间高级设置bool
        advenable_last_time = request.form["advenable_last_time"]  # 时长高级设置bool

        if advenable_bg_time:
            # if bg
            advenable_bg_time_settings = request.form["advenable_bg_time_settings"]  # 开始时间字典集
            time_list = list()
            for bgsettings in advenable_bg_time_settings:  # 开始时间字典
                adv_min_bg_time = bgsettings['min']
                adv_max_bg_time = bgsettings['max']
                adv_rate_bg_time = bgsettings['rate']
                if advenable_last_time:
                    # if bg and last
                    advenable_last_time_settings = request.form["advenable_last_time_settings"]  # 时长字典集
                    for lsettings in advenable_last_time_settings:  # 时长字典
                        adv_min_last_time = lsettings['min']
                        adv_max_last_time = lsettings['max']
                        adv_rate_last_time = lsettings['rate']
                        for i in range(int(gene_count) * float(adv_rate_bg_time)):
                            for j in range(int(gene_count) * float(adv_rate_last_time)):
                                time_list.append(
                                    do_gene_random_time(adv_min_bg_time, adv_max_bg_time, adv_min_last_time,
                                                        adv_max_last_time))
                else:
                    # if bg but last
                    for i in range(int(gene_count) * float(adv_rate_bg_time)):
                        time_list.append(
                            do_gene_random_time(adv_min_bg_time, adv_max_bg_time, min_last_time, max_last_time))
            res['time_list'] = time_list

        elif advenable_last_time:
            # if last but bg
            advenable_last_time_settings = request.form["advenable_last_time_settings"]  # 时长字典集
            time_list = list()
            for lsettings in advenable_last_time_settings:  # 时长字典
                adv_min_last_time = lsettings['min']
                adv_max_last_time = lsettings['max']
                adv_rate_last_time = lsettings['rate']
                for i in range(int(gene_count) * float(adv_rate_last_time)):
                    time_list.append(
                        do_gene_random_time(min_bg_time, max_bg_time, adv_min_last_time, adv_max_last_time))
            res['time_list'] = time_list

        else:
            # not bg or last
            try:
                time_list = list()
                for i in range(int(gene_count)):
                    time_list.append(do_gene_random_time(min_bg_time, max_bg_time, min_last_time, max_last_time))

                res['time_list'] = time_list
                res['status'] = 0

            except ValueError as e:
                res['status'] = -1

        return json.dumps(res)


@app.route('/random/ip', methods=['GET', 'POST'])
def page_random_ip():
    if request.method == 'GET':
        return render_template('random_ip.html')

    if request.method == 'POST':
        res = {'status': 1}
        ip_settings = request.form["ip_settings"]
        ip_settings = json.loads(ip_settings)  # [{"min':192.1.1.1, 'max':193.1.1.1, 'count':5},{},{}]
        res['ran_ip_list'] = gen_ip_list(ip_settings)
        return json.dumps(res)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
