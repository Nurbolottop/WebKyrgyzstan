from django.urls import path

from . import views

app_name = 'learn'

urlpatterns = [
    path('', views.index, name='index'),
    path('quizzes/', views.quiz_list, name='quizzes'),
    path('quizzes/<slug:slug>/', views.quiz_detail, name='quiz'),
    path('riddles/', views.puzzle_list, {'kind': 'riddle'}, name='riddles'),
    path('rebuses/', views.puzzle_list, {'kind': 'rebus'}, name='rebuses'),
    path('kyrgyz/', views.word_topic_list, name='word_topics'),
    path('kyrgyz/<slug:slug>/', views.word_topic_detail, name='words'),
    path('play/', views.game_list, name='games'),
    path('play/<slug:slug>/', views.game_detail, name='game'),
]
