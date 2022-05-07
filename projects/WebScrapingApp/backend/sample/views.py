from django.shortcuts import render
from django.views import generic

from lib.scraper import scraper

# sample.htmlを表示するためのビュー
class SampleView(generic.TemplateView):
    template_name = 'sample/sample.html'

    DEFAULT_KEY_WORD = "ウクライナ"

    # テンプレートに表示したいことがある時
    """
        スクレイピングした結果を表示する場合
        context['テンプレートで使用する変数名'] = スクレイピングの結果
    """

    def __init__(self):
        self.scraper = scraper.ScraperFromYahoo()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        news_list = self.scraper.search(SampleView.DEFAULT_KEY_WORD, 5)
        data_list = []
        for news in news_list:
            data = {"title":news.title, "url":news.url, "body": news.body}
            data_list.append(data)


        context['message'] = 'サンプル用のコードを作成しました。'
        context['news_list'] = data_list

        return context