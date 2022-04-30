from lib.scraper.news import News
import requests
from bs4 import BeautifulSoup

# ヤフーニュースから何かしらのニュースを取得してくる
class ScraperFromYahoo:
    SRC_URL = 'https://news.yahoo.co.jp/search'
    def search(self, keyword, newsNum=5):
        """
            指定したワードで検索を行い、指定された件数のニュースを返す
            Args:
                keyword: str : 検索に使用するキーワード
                newsNum:  int : 数値
            Returns:
                newsのリスト
        """
        res = requests.get(ScraperFromYahoo.SRC_URL + "?p=" + keyword + '&ei=utf-8')
        soup = BeautifulSoup(res.text, 'html.parser')
        newsFeed_item_elms = soup.find_all('li', {'class': 'newsFeed_item-normal'})
        
        news_list = []
        for elem in newsFeed_item_elms[0:newsNum]:
            title = elem.find('div', {'class': 'newsFeed_item_title'}).get_text()
            url = elem.find('a').get('href')
            # ToDo: 本文の取得
            body = ""
            news = News(title, url, body)
            news_list.append(news)
        
        return news_list