from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    Index page Function that returns root page views
    '''
    return render_template('index.html')

# Render template Searches for template file in app/template directory.

