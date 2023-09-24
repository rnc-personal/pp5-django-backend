from django.urls import path
from comments import views

urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>', views.CommentDetail.as_view()),
    path('ratings/', views.RatingsList.as_view()),
    path('ratings/<int:pk>', views.RatingDetail.as_view()),
]