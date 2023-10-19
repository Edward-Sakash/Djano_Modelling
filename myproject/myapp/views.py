from django.views.generic.edit import CreateView
from .models import Article

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'myapp/article_form.html'
    fields = ['title', 'content']
