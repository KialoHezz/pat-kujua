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

def get_sources(category):
    sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(sources_url) as url:
        sources_url_data = url.read()
        sources_url_response = json.loads(sources_url_data)


        source_results = None

        if sources_url_response['articles']:
            source_results_list = sources_url_response['articles']
            source_results = process_results(source_results_list)

    return source_results  


def process_results(sources_list):
    source_result = []

    for source in sources_list:
        id = source.get("id")
        name = source.get("name")
        urlToImage = source.get("urlToImage,")
        description = source.get("description")
        publishedAt = source.get("publishedAt")


        if urlToImage:
            source_object = Sources(id, name, urlToImage, description, publishedAt)
            source_result.append(source_object)


    return source_result
