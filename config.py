import os

class Config:
    '''
    parent class configuration
    '''
    NEWS_API_SOURCE_URL='https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
    CATEGORY_API_URL='https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'
