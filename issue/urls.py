from django.urls import path

from issue import views

urlpatterns = [
    path('list/', views.list_issue),
    path('add/', views.add_issue),
    path('get/<str:issue_id>/', views.get_issue),
    path('update/<int:issue_id>/', views.update_issue),
    path('delete/<int:issue_id>/', views.delete_issue),
]
