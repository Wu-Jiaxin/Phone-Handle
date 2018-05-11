# -*- coding: utf-8 -*-
"""
Created on Thu May 03 09:37:50 2018

@author: 86546
"""

#Tips: It can work in python2 and python3

from bottle import run, route, static_file

@route('/')
def index():
    return static_file('index.html', 'C:/Users/86546/Desktop/work')

@route('/resource/<filename>')
def staticFile(filename):
    return static_file(filename, '.C:/Users/86546/Desktop/work/resource')

run(host='10.162.23.17', port='8080')