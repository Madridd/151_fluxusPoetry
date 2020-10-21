from flask import Flask, render_template

app = Flask(__name__)

#Dependencies
from bs4 import BeautifulSoup
import requests
import re


@app.route('/')


def index():
    return render_template("index.html")


    ##look at proffessors example on git https://github.com/gramlivingston/derieve

@app.route('/pageTwo')
def edm():
    headers = {'user-agent': 'Mozilla/5.0'}
    page = requests.get("https://en.wikipedia.org/wiki/Electronic_dance_music", headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    whitelist = [
    'p'
    ]

    text = [t for t in soup.find_all(text=True) if t.parent.name in whitelist]
    print (text)
    return render_template("pageTwo.html", text = text )

@app.route('/pageThree')
def hiphop():
    headers = {'user-agent': 'Mozilla/5.0'}
    page3 = requests.get("https://en.wikipedia.org/wiki/Hip_hop_music", headers=headers)
    soup3 = BeautifulSoup(page3.content, 'html.parser')

    whitelist3 = [
    'p'
    ]

    text = [t for t in soup3.find_all(text=True) if t.parent.name in whitelist3]
    print (text)
    return render_template("pageThree.html", text = text )