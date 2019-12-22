import bs4
import requests

##trade-info > div.coin-price.border-right-gray > p.coin-price-current > span

html=requests.get('https://coinmarketcap.com/ko/currencies/hdac/')
soup=bs4.BeautifulSoup(html.text,'html.parser')

hdac=soup.select_one('#__next > div > div.container.cmc-main-section > div.cmc-main-section__content > div.cmc-currencies.aiq2zi-0.eXmmQp > div.cmc-currencies__details-panel > div > div.cmc-details-panel-price.jta9t4-0.fcilTk > span:nth-child(1) > span.cmc-details-panel-price__price')

print(hdac.text)