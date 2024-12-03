from django.urls import path
from .views import helloworldview, covidview

urlpatterns = [
    path('helloworld/', helloworldview),
    path('', covidview)
]
