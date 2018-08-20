from flask import Flask, render_template
import json
import urllib3
import requests
import pipeline
import random

app = Flask(__name__)

stocks = pipeline.stock_object_list()
top_gainers_list = pipeline.get_top_gainsers()
top_losers_list = pipeline.get_top_losers()
most_active_list = pipeline.get_most_active()

@app.route("/home")
def home():
    return render_template('home.html', items=stocks)

@app.route("/top_gainers")
def top_gainers():
    return render_template('top_lists.html', items=top_gainers_list)

@app.route("/top_losers")
def top_losers():
    return render_template('top_lists.html', items=top_losers_list)

@app.route("/most_active")
def most_active():
    return render_template('top_lists.html', items=most_active_list)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/")
def index():
    return render_template('index.html')

#to run app with python
if __name__ == '__main__':
    app.run(debug=True)