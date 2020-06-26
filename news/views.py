from django.shortcuts import render

# Create your views here.

def site_news(request , template_name = 'news/news.html'):

    data = {}
    
    return render(request , template_name , data)