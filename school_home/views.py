from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request , template_name = 'home.html'):
    return render(request , template_name )





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