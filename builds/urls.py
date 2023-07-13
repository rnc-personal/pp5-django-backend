from django.urls import path
from builds import views

urlpatterns = [
    path('builds/', views.BuildList.as_view()),
    path('builds/<int:pk>', views.BuildDetail.as_view()),
]