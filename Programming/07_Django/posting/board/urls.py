from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.posting_list, name='posting_list'),
    path('<int:id>/', views.posting_detail, name='posting_detail'),

]