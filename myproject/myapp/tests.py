from django.test import TestCase
from .models import Article

class ArticleTests(TestCase):
    def test_article_creation(self):
        article = Article.objects.create(title='Test Title', content='Test Content')
        self.assertEqual(article.title, 'Test Title')
        self.assertEqual(article.content, 'Test Content')

    # Add more test methods as needed
