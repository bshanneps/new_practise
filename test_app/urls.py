from django.urls import path
from . import views

urlpatterns = [
    path('', views.abc),
    path('message', views.msg),
    path('template/', views.temp_example),
    path('names', views.show_names),
    path('okay', views.ink)
]
