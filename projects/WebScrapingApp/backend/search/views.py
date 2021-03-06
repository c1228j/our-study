from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from lib.scraper import scraper
from .forms import KeywordForm

class ScrapingUkraineView(generic.TemplateView):
    template_name = 'search/index.html'
    NEWS_KEYWORD = "ウクライナ"
    NEWS_NUMBER = 5

    def __init__(self):
        self.scraper = scraper.ScraperFromYahoo()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        news_list = self.scraper.search(self.NEWS_KEYWORD, self.NEWS_NUMBER)
        data_list = []
        for news in news_list:
            data = {"title":news.title, "url":news.url, "body": news.body}
            data_list.append(data)

        context['data_list'] = data_list
        context['keyword'] = self.NEWS_KEYWORD

        return context

class ScrapingView(generic.FormView):
    template_name = 'search/index.html'
    form_class = KeywordForm
    success_url = reverse_lazy('search:index')

    # form_validにあるコメントにした場合、次のNEWS_KEYWORDを削除する
    NEWS_KEYWORD = "ウクライナ"
    NEWS_NUMBER = 5

    def __init__(self):
        self.scraper = scraper.ScraperFromYahoo()

    def form_valid(self, form):

        # この2行を削除する
        keyword = form.cleaned_data['keyword']
        ScrapingUkraineView.NEWS_KEYWORD = keyword

        news_list = self.scraper.search(ScrapingUkraineView.NEWS_KEYWORD, self.NEWS_NUMBER)
        # new_list = self.scraper.search(form.cleaned_data['keyword'], self.NEWS_NUMBER) に修正する

        data_list = []
        for news in news_list:
            data = {'title': news.title, 'url': news.url}
            data_list.append(data)

        context = self.get_context_data(data_list=data_list, keyword=ScrapingUkraineView.NEWS_KEYWORD)
        # context = self.get_context_data(data_list=data_list, keyword=form.cleaned_data['keyword'])に修正する

        return self.render_to_response(context)
        

