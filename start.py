#! /usr/bin/python

"""
@author: yan.zhao
@contact: zhaoyanz405@gmail.com
@time: 2019/6/4 18:20
"""
import json

from flask import Flask, render_template, request
from random_time import do_gene_random_time

app = Flask(__name__)


@app.route('/')
def index():
    return 'test'


@app.route('/random/time', methods=['GET', 'POST'])
def page_random_time():
    if request.method == 'GET':
        return render_template('random_time.html')

    if request.method == 'POST':
        max_bg_time = request.form["max_begin_time"]
        min_bg_time = request.form["min_begin_time"]
        min_last_time = request.form["min_last_time"]
        max_last_time = request.form["max_last_time"]
        gene_count = request.form["gene_count"]

        time_list = list()
        for i in range(int(gene_count)):
            time_list.append(do_gene_random_time(min_bg_time, max_bg_time, min_last_time, max_last_time))

        return json.dumps(time_list)


if __name__ == '__main__':
    # stetts
    app.run(host="0.0.0.0")
