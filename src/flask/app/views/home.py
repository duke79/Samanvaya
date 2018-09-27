import os

from flask import request, jsonify
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from app import app
from app.utils.spider import Spider


@app.route('/')
def home():
    with Spider() as spider:
        driver = spider.driver()
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        return "Seriously! What are you looking for? ;)"
