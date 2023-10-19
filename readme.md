## Modelling:
*myapp/models.py*:
1. Define the Article model:
fields:
titel
content
python
   from django.db import models
   from django.urls import reverse

   class Article():

       def __str__(self):

       def get_absolute_url(self):
   
2. *Apply Migrations*:
   This will set up your database with the new model:
bash
   python manage.py makemigrations
   python manage.py migrate
   
---
## Using Django's CreateView, ListView, DetailView:
*myapp/views.py*:
1. Implement the CreateView:
python
   from django.views.generic import CreateView
   from .models import Article

   
   
---
## URL Configuration:
*myapp/urls.py*:
1. Define URLs for the views:
python
   from django.urls import path
   from .views import ArticleCreateView

   urlpatterns = [
       ????
   ]
   
2. *Include the App URLs* in the main project's urls.py:
python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('articles/', include('myapp.urls')),
   ]
   
---
## Templates:
1. *Set up Template Directories*:
   ---> settings.py
2. *Implement the CreateView Template*:
   Inside myapp/templates, create a file article_form.html:
html
   <h2>Create Article</h2>
   <form method="post">
      ????
       <input type="submit" value="Submit">
   </form>
   
---
### Testing
   - Check the creation of the Article model
   - check status code
   - content
   - templateimport Article
   class ArticleTests(TestCase):
python
   from django.test import TestCase
   from .models import Article

   class ArticleTests(TestCase):

   
   Execute the tests with:
bash
   python manage.py test myapp
   

Bonus: Add css style to your form
### Create CSS:
*static/styles.css*:
css
body {
    font-family: Arial, sans-serif;
    padding: 20px;
    background-color: #f5f5f5;
}

.styled-article-form {
    width: 80%;
    margin: 20px auto;
    padding: 20px;
    border: 1px solid #ccc;
    background-color: #ffffff;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

.styled-form-group {
    margin-bottom: 15px;
}

.styled-form-group label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

.styled-form-group input[type="text"],
.styled-form-group textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
}

.styled-submit-btn {
    padding: 10px 15px;
    background-color: #007BFF;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.styled-submit-btn:hover {
    background-color: #0056b3;
}
### Configure Django to serve static files:
Ensure you've set up Django to serve static files correctly during development. In your myproject/settings.py, ensure you have:
python


STATIC_URL = '/static/'
?????????