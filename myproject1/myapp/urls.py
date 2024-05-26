from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_page, name='input'),
    #path('output/', views.output_page, name='output'),
    path('output/<int:number>/<str:text>/<int:square>/', views.output_page, name='output'),
]
