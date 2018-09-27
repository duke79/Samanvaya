import os

from flask import request, jsonify
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from app import app
from app.utils.scrape import Scrape
from app.utils.spider import Spider


@app.route('/<string:board>/<string:year>/<string:standard>/<string:roll_number>')
def home(board, year, standard, roll_number):
    if board == "cbse":
        return jsonify(Scrape().cbse(roll_number, year=year, standard=standard))
    return "!"
