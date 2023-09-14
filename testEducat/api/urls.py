from django.urls import path

from .views import TaskItemViews

urlpatterns = [
    path('task', TaskItemViews.as_view()),
    path('task/<int:id>', TaskItemViews.as_view()),
]