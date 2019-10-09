
from django.urls import path,include
from . import views

urlpatterns = [
    path("add/",views.add,name="add"),
    path("guideA/",views.guideA,name="guideA"),
    path("guideB/",views.guideB,name="guideB"),
]