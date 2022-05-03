import os

class Config:
    NEW_BASE_URL_SOURCES = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={}" 
    NEWS_BASE_HEADLINES_URL = "https://newsapi.org/v2/top-headlines?country=us&apiKey={}"
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')



class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    pass

config_options = {
    'development': DevConfig,
    'production': ProdConfig 
}