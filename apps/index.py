#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template, request, g, session, redirect, url_for
from apps import app


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='Home')
