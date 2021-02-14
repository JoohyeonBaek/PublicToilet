from django.shortcuts import render

# Create your views here.


from .models import BusanDong
from .models import *

def post_view(request):
    print("test")
    posts = GangwonWonju.objects.all()
    print(posts)
    return render(request, 'index.html', {"posts": posts})

