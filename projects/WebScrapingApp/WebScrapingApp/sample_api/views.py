from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
import jsonschema

from lib.scraper import scraper

class NewsView(APIView):
    # ToDo: getも実装したら消す
    DEFAULT_KEY_WORD = "経済"

    # 参考 https://qiita.com/mink0212/items/8564d2ed5cf778d539c5
    SCHEMA = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties" :{
            "search_word": {
                "type": "string"
            },
            "search_num": {
                "type": "integer"
            }
        },
        "required": [
            "search_word",
            "search_num",
        ],
    }

    def __init__(self):
        self.scraper = scraper.ScraperFromYahoo()

    def get(self, request):
        # ToDo: 作る
        news_list = self.scraper.search(NewsView.DEFAULT_KEY_WORD, 5)
        data_list = []
        for news in news_list:
            data = {"title":news.title, "url":news.url, "body": news.body}
            data_list.append(data)

        return Response(data_list)

    def post(self, request):
        try:
            jsonschema.validate(request.data, NewsView.SCHEMA)
            news_list = self.scraper.search(request.data["search_word"], request.data["search_num"])
            data_list = []
            for news in news_list:
                data = {"title":news.title, "url":news.url, "body": news.body}
                data_list.append(data)

            return Response(data_list)

        except jsonschema.ValidationError as e:
            return Response(data={'error': e.message}, status=404)

        except Exception as e:
            return Response(data={'error': "予期せぬエラー"}, status=404)
            