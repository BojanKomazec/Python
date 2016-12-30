'''
Web page scraping example.
Original code: http://docs.python-guide.org/en/latest/scenarios/scrape/
'''
from lxml import html
import requests

def example1():
    response = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
    TREE = html.fromstring(response.content)
    #This will create a list of buyers:
    BUYERS = TREE.xpath('//div[@title="buyer-name"]/text()')
    #This will create a list of prices
    PRICES = TREE.xpath('//span[@class="item-price"]/text()')
    print('Buyers: ', BUYERS)
    print('Prices: ', PRICES)

def main():
    example1()

main()