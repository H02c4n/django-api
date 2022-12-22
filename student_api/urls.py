from django.urls import path
from . import views


urlpatterns =[
    path('', views.home),
    path('student/',views.student_api),
    path('student/<int:pk>',views.student_api_get_update_delete, name='detail'),
    path('path/', views.path_api)
]
