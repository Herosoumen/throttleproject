from django.urls import path
from . import views

urlpatterns = [

    path('api/userdetails/', views.UserDataAPIView.as_view(), name='user_details')
]
