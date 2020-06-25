from django.urls import path
from . import views

urlpatterns = [

    path('', views.UserDataAPIView.as_view(), name='user_details')
]
