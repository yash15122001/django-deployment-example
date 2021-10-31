from django.conf.urls import url
from basicapp import views
from django.urls import path

# Template tagging
app_name = 'basicapp'

urlpatterns = [
    path('other/', views.other,name='other'),
    path('relative/', views.relative,name='index'),
]
