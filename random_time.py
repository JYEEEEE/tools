# -*- coding:utf-8 -*-
import datetime
import random
import time

tm = time.mktime
tsp = time.strptime
tsf = time.strftime


def format_str_timestamp(start_time: str, format='%Y/%m/%d %H:%M:%S'):
    """
    将字符串转为时间戳(单位: s)
    :param start_time: str
    :param format: str
    :return: float
    """
    return int(tm(tsp(start_time, format)))


def convert_str_seconds(last_time):
    """
    转换答题时间字符串为秒数
    :param last_time:
    :return:
    """
    hour, minute, second = last_time.split(':')
    return int(hour) * 60 * 60 + int(minute) * 60 + int(second)


def convert_seconds_str(seconds):
    """
    将秒数转为时间字符串
    :param seconds:
    :return:
    """

    mins, secs = divmod(seconds, 60)

    hour = 0
    if mins >= 60:
        hour, mins = divmod(mins, 60)

    return '%s:%s:%s' % (hour, mins, secs)


def format_timestamp_to_str(timestamp):
    """

    :param timestamp:
    :return:
    """
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y/%m/%d %H:%M:%S')


def do_gene_random_time(start_time_min, start_time_max, last_time_min, last_time_max):
    """

    :param start_time_min: 最早的答题开始时间
    :param start_time_max: 最晚的答题开始时间
    :param last_time_min: 最少的答题时长
    :param last_time_max: 最多的答题时长
    :return:
    """
    start_time_min = format_str_timestamp(start_time_min)
    start_time_max = format_str_timestamp(start_time_max)
    last_time_min = convert_str_seconds(last_time_min)
    last_time_max = convert_str_seconds(last_time_max)

    _start_ts = random.randint(start_time_min, start_time_max)
    _answer_seconds = random.randint(last_time_min, last_time_max)
    _end_ts = _start_ts + _answer_seconds

    return format_timestamp_to_str(_start_ts), convert_seconds_str(_answer_seconds), format_timestamp_to_str(_end_ts)


if __name__ == '__main__':
    pass
    # while True:
    #     try:
    #         # 输入（开始时间范围、答题时间范围）
    #         start_time_min = format_str_timestamp(input('请输入最早的答题开始时间：(年/月/日 时:分:秒)'))
    #         start_time_max = format_str_timestamp(input('请输入最晚的答题开始时间：(年/月/日 时:分:秒)'))
    #         last_time_min = convert_str_seconds(input('请输入最少的答题时长：(时:分:秒)'))
    #         last_time_max = convert_str_seconds(input('请输入最多的答题时长：(时:分:秒)'))
    #         n = int(input('请输入需要的条数：'))
    #     except ValueError as e:
    #         print('输入格式有误，请检查。')
    #         continue
    #
    #     print('开始时间', '答题时长', '结束时间')
    #     for i in range(n):
    #         # 随机生成范围内开始时间和答题时间
    #         random_start_ts = random.randint(start_time_min, start_time_max)
    #         random_answer_seconds = random.randint(last_time_min, last_time_max)
    #         random_end_ts = random_start_ts + random_answer_seconds
    #
    #         print(format_timestamp_to_str(random_start_ts),
    #               convert_seconds_str(random_answer_seconds),
    #               format_timestamp_to_str(random_end_ts))
    #
    #     if input('是否继续：(Y/N)').upper() == 'N':
    #         exit(1)
