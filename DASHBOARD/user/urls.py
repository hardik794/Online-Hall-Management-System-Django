from django.urls import path
from . import views
# from django.contrib.auth.views import LoginView

urlpatterns=[
    path('dashboard',views.dashboard,name="dashboard"),
    path('login', views.login,name='login'),
    path('register',views.register,name="register"),
    path('logout',views.logout,name="logout"),
    path('book',views.book,name="book"),
    path('cancel',views.cancel,name="cancel"),
]