import bs4
import requests

def DolarHoje():
    url = 'https://dolarhoje.com/'
    html = requests.get(url)

    # print(html.content)

    masoquista = bs4.BeautifulSoup(
        html.content, 'html.parser'
    )

    return masoquista.find(id='nacional').get('value')

