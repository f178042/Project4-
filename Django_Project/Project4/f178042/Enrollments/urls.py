from django.urls import path
from .import views

urlpatterns = [
    path('enrollments/create', views.create.as_view(), name='create'),
    path('enrollments/', views.listView.as_view(), name='listView'),
    path('enrollments/<pk>', views.detailView.as_view(), name='detailView'),
    path('enrollments/update/<pk>', views.update.as_view(), name='update'),
    path('enrollments/delete/<pk>', views.delete.as_view(), name='delete'),
]

