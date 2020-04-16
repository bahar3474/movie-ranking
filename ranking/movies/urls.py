from django.urls import path
from . import views

urlpatterns = [
    path('', views.top5),
    path('score', views.score),
    path('score/confirm', views.score_confirm, name='confirm_score')
]
