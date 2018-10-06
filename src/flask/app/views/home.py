import json
import os

from flask import request, jsonify
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from app import app
from app.data.tables.user import User
from app.utils.scrape import Scrape
from app.utils.spider import Spider
from app.utils.traces import print_exception_traces


@app.route("/")
def home():
    import app.scraper.crawler
    return "!"


@app.route('/result/<string:board>/<string:year>/<string:standard>/<string:roll_number>')
def result(board, year, standard, roll_number):
    if board == "cbse":
        ret = Scrape().cbse(roll_number, year=year, standard=standard)
        try:
            json_data = json.dumps(ret)
            # json_data = ret
            user = User(marksheet_10=json_data)
            user = user.save()
        except TypeError as e:
            print_exception_traces(e)
        return jsonify(ret)
    return "!"


@app.route('/scholarship/up')
def scholarship():
    return jsonify(Scrape().up_scholarship())

@app.route('/captcha')
def captcha():
    return jsonify(Scrape().captcha())