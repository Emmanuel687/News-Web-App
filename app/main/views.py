from flask import render_template,request
from . import main
from flask import render_template,request
from ..request import get_source,get_headlines

#our views
@main.route('/')
def index():
    '''
    Root function returning index/home page with data
    '''
    source= get_source()
    headlines = get_headlines()
    return render_template('index.html',sources=source, headlines = headlines)
