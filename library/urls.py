from django.urls import path,include
from .views import ListBook


urlpatterns=[

    path("",ListBook.as_view()),
    

]