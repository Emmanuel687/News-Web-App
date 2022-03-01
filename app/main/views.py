from flask import render_template
from app import app

@app.route('/')
def index():

    '''
    Function that returns root page views
    '''
    return render_template('index.html')



