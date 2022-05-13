from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from lib.scraper import scraper
from .forms import SearchForm

class ScrapingUkraineView(generic.TemplateView):
    template_name = 'search/index.html'
    NEWS_KEYWORD = "ウクライナ"
    NEWS_NUMBER = 5

    def __init__(self):
        self.scraper = scraper.ScraperFromYahoo()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        news_list = self.scraper.search(self.KEYWORD, self.number)
        data_list = []
        for news in news_list:
            data = {"title":news.title, "url":news.url, "body": news.body}
            data_list.append(data)

        context['data_list'] = data_list
        context['keyword'] = self.KEYWORD

        return context

class ScrapingView(generic.FormView):
    template_name = 'search/index.html'
    form_class = SearchForm
    success_url = reverse_lazy('search:index')

    def __init__(self):
        self.scraper = scraper.ScraperFromYahoo()
        self.number = 5
        self.KEYWORD = ''

    def form_valid(self, form):
        keyword = form.cleaned_data['keyword']
        ScrapingUkraineView.KEYWORD = keyword

        news_list = self.scraper.search(ScrapingUkraineView.KEYWORD, self.number)
        data_list = []
        for news in news_list:
            data = {'title': news.title, 'url': news.url}
            data_list.append(data)

        context = self.get_context_data(data_list=data_list, keyword=ScrapingUkraineView.KEYWORD)
        return self.render_to_response(context)
        

