from django.urls import path
from myweb import views
urlpatterns =[
    path('',views.index),
    path('image_activity',views.image_activity)
]