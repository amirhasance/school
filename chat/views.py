from django.shortcuts import render , redirect , get_object_or_404
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
import json
from django import forms
from django.forms import Form , ModelForm
from django.http import HttpResponse
from .models import person , roomName
from django.views.decorators.csrf import csrf_exempt
from .serializer import Message_serializer , person_serializer , Room_serializer
from rest_framework.request import Request

def index(request):
  return render (request , 'chat/index.html' , {})


@csrf_exempt
def room(request  ,room_name):
  
   username = request.session['username']
   import pdb
   
   user  = person.objects.get(username = username)
   user_serializer= person_serializer(user)
   users = person.objects.filter(rooms__name = str(room_name))
   users_serializer = person_serializer(users , many=True)
   room_name = str(room_name)
   room = roomName.objects.filter(name = room_name)
   serializer_context = {
    'request': Request(request),}
   room_serialize = Room_serializer(instance=room , many = True ,  context = serializer_context)
   
   return render (request , 'chat/room.html' , {  'room': mark_safe(json.dumps(room_serialize.data))  \
     , 'users': mark_safe( json.dumps(users_serializer.data) ) , \
       'room_name' : mark_safe(json.dumps(room_name)),
       'user':mark_safe(json.dumps(user_serializer.data)) })
  #  else :
  #        return HttpResponse("at first you must log in !!")
  # except :
  #   return redirect('chat:signin')

 
def test(request, template_name = 'chat/test.html'):
  import pdb
  user = None
  
  try:
  
   print(request.session['username'])
   print(request.session['password'])
   
   user = {request.session['username']  ,  request.session['password'] } 
    
  except:
    pass
    
        
  
  return render (request , template_name , {"user": json.dumps(user)})

class User_Form(ModelForm):
      class Meta:
        model = person
        fields = ['image' , 'username' , 'password']
class user_form_login(forms.Form):
      username = forms.CharField()
      password = forms.CharField()
      roomName = forms.CharField()
      
      
@csrf_exempt

def login(request , template_name='chat/login.html'):
      form = user_form_login(request.POST or None )
      
      if request.method == "POST":
            if form.is_valid():
                  import pdb ; pdb.set_trace()
                  user = get_object_or_404(person , username=form.cleaned_data.get('username') , password = form.cleaned_data.get('password'))
                  request.session['username'] = form.cleaned_data.get('username')
                  request.session['password'] = form.cleaned_data.get('password')
                  room = get_object_or_404(roomName , name = form.cleaned_data.get('roomName'))
                  return redirect('../{}'.format(room))
      else :
            return render(request , template_name , {'form':form})
                  
      
   


def signin(request , template_name = 'chat/signin.html'):
  import pdb
  form = User_Form(request.POST or None  , request.FILES or None )
  path= str(request.path).split("/")[-2]
 
  if request.method == "POST":
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      image = form.cleaned_data.get('image')
      person.objects.create_user(username=username , password=password , image = image)
      request.session['username'] = str(username)
      request.session['password'] = str(password)
      pdb.set_trace()
      return redirect('../')
    else :
          print("Form is not valid ")
  try:
    pass
    #TODO we must redirect to group
      # username = request.session['username']
      # user = person.objects.filter(username=username )
      # print(user)
      
      
      # if not user is None:
      #   print(person.objects.filter(username=username))
      #   return redirect(f'chat/{path}')
  except:
      pass
          

    
  return render(request, template_name, {'form':form}) 