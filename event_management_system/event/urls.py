# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.event_list, name='event_list'),
#     path('event/<int:event_id>/', views.event_detail, name='event_detail'),
#     path('create_event/', views.create_event, name='create_event'),
#     path('register_event/<int:event_id>/', views.register_event, name='register_event'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.eventList, name="events"),
    path('detail/<str:pk>/', views.eventDetail, name="detail"),
    path('create', views.eventCreate, name="create"),
    path('update/<str:pk>/', views.eventUpdate, name="update"),
    path('delete/<str:pk>/', views.eventDelete, name="delete"),
]
