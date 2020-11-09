from django.urls import path
from . import views

urlpatterns = [

    path('ussd-done/', views.Welcome, name='user-done'),
    path('ussd-list/', views.listView, name='user-list'),
    path('ussd-detail/<str:pk>', views.listView, name='user-detail'),
    path('ussd-create/', views.createView, name='user-create'),
    path('users/', views.UserList.as_view(), name='users'),
]
