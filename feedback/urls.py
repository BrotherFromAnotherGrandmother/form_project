from django.contrib import admin
from django.urls import path
from .views import done, update_feedback, FeedBackView

urlpatterns = [
    path('done', done),
    path('', FeedBackView.as_view()),
    path('<int:id_feedback>', update_feedback),
]
