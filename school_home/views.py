from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from news.models import last_3_news
from django.utils.safestring import mark_safe
import json
from django.core.exceptions import ValidationError
# Create your views here.

def home(request , template_name = 'home.html'):

    data_to_send = {}

    news = last_3_news()
    data_to_send['news'] = news
    data_to_send['school_name'] = school_data["school_name"]
    data_to_send['telephone'] = school_data['telephone']

    return render(request , template_name , data_to_send )



def ajax_comment(request):
    index = str(request.GET.get('index'))
    print(index)
    if len(index) > 25:
        data = {
            'is_ok' : True
        }
    else :
        data = {
            'is_ok' : False
        }
    return JsonResponse(data)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def grecaptcha_verify(request):
    pass
    # data = request.POST
    # captcha_rs = data.get('g-recaptcha-response')
    # url = "https://www.google.com/recaptcha/api/siteverify"
    # params = {
    #     'secret': settings.RECAPTCHA_SECRET_KEY,
    #     'response': captcha_rs,
    #     'remoteip': get_client_ip(request)
    # }
    # verify_rs = requests.get(url, params=params, verify=True)
    # verify_rs = verify_rs.json()
    # return verify_rs.get("success", False)



def file_size(value):
    limit = 1 * 1024 * 1024
    if value.size > limit :
        raise ValidationError ("File size is too much and must be less than 20MG")


school_data = {
    "school_name" : "  نخبگان آمل" ,
    "telephone" : "011 442 42 921",

}

from news.models import News
from .serializers import News_Serializers
def test(request , template_name = 'test.html'):
    data = {}
    news = News.objects.all()
    data['news'] = news
    return render(request , template_name , data)
