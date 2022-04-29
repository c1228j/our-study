from lib.scraper.news import News

# ヤフーニュースから何かしらのニュースを取得してくる
class ScraperFromYahoo:
    SRC_URL = ''
    def __init__(self):
        pass

    def search(self, keywords, newsNum=5):
        """
            指定したワードで検索を行い、指定された件数のニュースを返す
            Args:
                keywords: str : 検索に使用するキーワード
                newsNum:  int : 数値
            Returns:
                newsのリスト
        """
        # ToDo: スクレイピングする
        
        news_list = []
        for i in range(newsNum):
            # ToDo: スクレイピングした結果を詰め込む
            news = News("title" + str(i), "url" + str(i), "body" + str(i))
            news_list.append(news)

        return news_list

# 動作確認用
if __name__ == '__main__':
    scraper = ScraperFromYahoo()
    news_list = scraper.search("3", 5)
    for news in news_list:
        print(f'title: {news.title}')
        print(f'url: {news.url}')
        print(f'body: {news.body}')