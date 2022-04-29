from rest_framework.response import Response
from rest_framework.views import APIView
from lib.scraper import scraper

class NewsView(APIView):
    DEFAULT_KEY_WORD = "ウクライナ"
    def __init__(self):
        self.scraper = scraper.ScraperFromYahoo()

    def post(self, request):
        # ToDo: 作る
        news_list = self.scraper.search(NewsView.DEFAULT_KEY_WORD, 5)
        data_list = []
        for news in news_list:
            data = {"title":news.title, "url":news.url, "body": news.body}
            data_list.append(data)

        return Response(data_list)