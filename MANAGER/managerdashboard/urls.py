from django.urls import path
from . import views

urlpatterns=[
    path('managerlogin',views.managerlogin,name="managerlogin"),
    path('managerpanel', views.managerpanel,name='managerpanel'),
    path('logoutpanel', views.logoutpanel,name='logoutpanel'),
    path('approve', views.approve,name='approve'),
    path('reject', views.reject,name='reject'),
]