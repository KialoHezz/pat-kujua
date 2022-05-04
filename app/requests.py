from app import create_app
import urllib.request,json
from .models import Articles,Sources

api_key = None
base_url = None
base_url_top_headlines = None


def configure_request(app):

    global api_key,base_url,base_url_top_headlines

    api_key = app.config['NEWS_API_KEY'] 
    base_url = app.config['NEW_BASE_URL_SOURCES']
    base_url_top_headlines = app.config['NEWS_BASE_HEADLINES_URL']
    

def get_sources():
    sources_url = base_url.format(api_key)
    # use with for context manager to send a requestusingurllib function with argument and send a request as url
    with urllib.request.urlopen(sources_url) as url:
        # use read function to read the response and store it in source_url_data
        sources_url_data = url.read()
        # convert JSON response to python dictionary
        sources_url_response = json.loads(sources_url_data)


        source_results = None

        if sources_url_response['sources']:
            source_results_list = sources_url_response['sources']
            source_results = process_results(source_results_list)

    return source_results  


def process_results(sources_list):
    '''
    sources_list is a list of dictionaries that contain  sources detaills
    '''
    source_result = []

    for source in sources_list:
        id = source.get("id")
        name = source.get("name")
        description = source.get("description")
       

        if name != ('ANSA.it') : 

            source_object = Sources(id, name, description)
            source_result.append(source_object)


    return source_result


def get_articles():
    articles_url = base_url.format(api_key)

    with urllib.request.urlopen(articles_url) as url:
        articles_url_data = url.read()
        articles_url_response = json.loads(articles_url_data)

        articles_result = None

        if articles_url_response['articles']:
            print('available')
            articles_results_list = articles_url_response['articles']
            articles_results=process_article_results(articles_results_list)


    return articles_results



def process_article_results(article_result_list):
    article_results=[]
    if article_result_list:
        for article in article_result_list:
            title=article.get('title')
            description=article.get('description')
            url=article.get('url')
            urlToImage=article.get('urlToImage')
            publishedAt=article.get('publishedAt')




