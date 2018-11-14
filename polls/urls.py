from django.urls import path, re_path

from polls import views


app_name = 'polls'
urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    re_path(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    re_path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    path('list/', views.list_polls),
    path('add/', views.add_polls),
    path('get/<int:polls_id>/', views.get_polls),
    path('update/<int:polls_id>/', views.update_polls),
    path('delete/<int:polls_id>/', views.delete_polls),
]
