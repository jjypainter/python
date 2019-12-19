import bs4
import requests
##exchangeList > li.on > a.head.usd > div > span.value
##content > div.spot > div.today > p.no_today

html=requests.get('https://finance.naver.com/marketindex/?tabSel=exchange#tab_section')
soup=bs4.BeautifulSoup(html.text,'html.parser')

dollor=soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')


print(dollor.text)