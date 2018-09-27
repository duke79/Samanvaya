from flask import request, jsonify
from app import app



@app.route('/')
def home():
    return "Seriously! What are you looking for? ;)"
