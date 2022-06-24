# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 00:19:13 2022

@author: Satya
"""

pip3 install dash


from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello():
    return '<h1> Hello World <h1>'

if __name__=='__main__':
    app.run()