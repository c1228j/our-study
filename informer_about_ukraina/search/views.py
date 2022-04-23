from django.shortcuts import render
from django.views import generic

# sample.htmlを表示するためのビュー
class SampleView(generic.TemplateView):
    template_name = 'search/sample.html'

    # テンプレートに表示したいことがある時
    """
        スクレイピングした結果を表示する場合
        context['テンプレートで使用する変数名'] = スクレイピングの結果

    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'サンプル用のコードを作成しました。'

        return context