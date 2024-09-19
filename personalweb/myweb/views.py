from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import HomepageContent
# Create your views here.

def index(request):
    return render(request,"index.html")

def image_activity(request):
    return render(request,"image_activity.html")

def homepage(request):
    content = HomepageContent.objects.first()  # ดึงข้อมูลหน้าแรกจากโมเดล
    return render(request, 'homepage.html', {'content': content})