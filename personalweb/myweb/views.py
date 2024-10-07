from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import HomepageContent , Activity
# Create your views here.

from django.shortcuts import render
from .models import Activity  # Import the Activity model

from django.shortcuts import render
from .models import Activity, AcademicProject

def index(request):
    activities = Activity.objects.all().order_by('-date_posted')
    academic_projects = AcademicProject.objects.all().order_by('-date_posted')
    return render(request, "index.html", {'activities': activities, 'academic_projects': academic_projects})



def image_activity(request):
    return render(request,"image_activity.html")

def homepage(request):
    content = HomepageContent.objects.first()  # ดึงข้อมูลหน้าแรกจากโมเดล
    return render(request, 'homepage.html', {'content': content})

def activity_view(request):
    activities = Activity.objects.all().order_by('-date_posted')
    return render(request, 'activity.html', {'activities': activities})