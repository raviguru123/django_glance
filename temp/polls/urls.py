from django.urls import path


from . import views
app_name = 'polls'
urlpatterns =[
    path('', views.indexView.as_view(), name='index'),
    path('<int:pk>/', views.detailView.as_view(), name='detail'),
    path('<int:pk>/result/', views.resultView.as_view(), name='results'),
    path('<int:question_id>/votes/', views.vote, name='vote')
]



