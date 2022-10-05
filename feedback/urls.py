from django.contrib import admin
from django.urls import path
from .views import done, FeedBackView, UpdateFeedback

urlpatterns = [
    path('done', done),
    path('', FeedBackView.as_view()),
    path('<int:id_feedback>', UpdateFeedback.as_view()),
]
