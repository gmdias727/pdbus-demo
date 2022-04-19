from bs4 import *
from requests import *

def DolarHoje():
    url = 'https://dolarhoje.com/'
    html = get(url)
    
    element = BeautifulSoup(
        html.content, 'html.parser'
    )

    return element.find(id='nacional').get('value')