from django.urls import path
from user_save import views

urlpatterns = [
    path('saved/', views.SaveList.as_view()),
    path('saved/<int:pk>/', views.SaveDetail.as_view()),
]