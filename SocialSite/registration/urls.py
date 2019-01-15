from django.urls import path
from . import views
urlpatterns = [

    path('signup/',views.showSignUp),
    path('login/', views.showLogin),
    path('',views.showSignUp),
]