from django.urls import path
from cms import views

urlpatterns = [
    path('cms/', views.CmsDetailView.as_view()),
]