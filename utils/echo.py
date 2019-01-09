#!/usr/bin/env python  
#-*- coding:utf-8 _*-  
"""
@author: HJK 
@file: echo.py 
@time: 2019-01-09

控制台输出内容控制

"""

colors = {
    'blue': '\033[94m',
    'pink': '\033[95m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'qq': '\033[92m',
    'kugou': '\033[95m',
}


def colorize(string, color):
    if not color in colors: return string
    return colors[color] + string + '\033[0m'


def info(music):
    ''' 打印歌曲信息 '''
    s = ' ------------ \n -> 歌曲：%s\n -> 歌手：%s\n -> 时长: %s\n -> 大小: %s\n -> 比率: %s\n -> URL: %s\n' % \
        (music['title'], music['singer'], music['length'], music['size'], music['rate'], music['url'])
    print(s)


def menu(music_list):
    ''' 打印歌曲列表信息 '''
    for music in music_list:
        idx = colorize(' [ %s ] ' % music_list.index(music), 'blue')
        source = colorize('%6s | ' % music['source'].upper(), music['source'])
        size = colorize('%5sMB' % music['size'], 'yellow')
        info = '%s - %s - %s - %s - %s' % \
               (music['length'], size, music['title'], music['singer'], music['album'])

        print(idx + source + info)
