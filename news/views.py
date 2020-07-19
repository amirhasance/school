from django.shortcuts import render
from django.http import HttpResponse
from .models import News , Comments
from school_home.serializers import serialize_comments
from django.utils.safestring import mark_safe
import json

# Create your views here.

def site_news(request , template_name = 'news/news.html'):

    data = {}
    
    return render(request , template_name , data)

def comments_of_this_new(new):
    return Comments.objects.filter(news = new)

def this_new(request  , pk = None , template_name = 'news/this_new.html'):
    new = News.objects.get(id = pk)
    data_to_send = {}
    data_to_send['new'] = new
    news = News.objects.exclude(id = new.id)[:20]
    data_to_send['news'] = news
    # data_to_send['comments'] = mark_safe(json.dumps(serialized_comment_of_this_news.data))
    # data_to_send['comments'] = comments_of_this_new(new)

    
    return render(request , template_name , data_to_send )
  