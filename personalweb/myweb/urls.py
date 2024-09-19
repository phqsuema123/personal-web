from django.urls import path
from myweb import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns =[
    path('',views.index),
    path('homepage', views.homepage, name='homepage')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
