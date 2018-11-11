from django.urls import path

from polls import views

urlpatterns = [
    path('list/', views.list_polls),
    path('add/', views.add_polls),
    path('get/<int:polls_id>/', views.get_polls),
    path('update/<int:polls_id>/', views.update_polls),
    path('delete/<int:polls_id>/', views.delete_polls),
]