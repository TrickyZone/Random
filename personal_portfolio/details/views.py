from django.shortcuts import render
from .models import *

# Create your views here.
def details(request):
   WhoAreYou=WhoAreYou.objects.all() 
   socialMedia=socialMedia.objects.all()
   AboutMe=AboutMe.objects.all()
   
   return render(request,'templates/home.html',{'socialMedia':socialMedia},{'WhoAreYou':WhoAreYou},{'AboutMe':AboutMe})