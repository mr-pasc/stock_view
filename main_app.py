from flask import Flask, render_template
import json
import urllib3
import requests
import pipeline
import random

app = Flask(__name__)
symbol = 'AAPL'

company_info_list = pipeline.get_company_info()
top_gainers_list = pipeline.get_top_gainsers()
top_losers_list = pipeline.get_top_losers()
most_active_list = pipeline.get_most_active()
#news_articles_list = pipeline.get_news()

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', items=company_info_list)

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

#to run app with python
if __name__ == '__main__':
    app.run(debug=True)