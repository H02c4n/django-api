from django.urls import path
from . import views

urlpatterns=[
    path('student-list/', views.students_list, name='list'),
    path('add/', views.add_student, name='add_new'),
    path('student-detail/<int:id>/', views.student_detail, name='detail'),
    path('student-update/<int:id>/', views.student_update, name='update'),
    path('student-delete/<int:id>/', views.student_delete, name='delete'),
]