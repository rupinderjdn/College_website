from django.urls import path
from main import views
urlpatterns=[
    path('',views.index),
    path('college/<int:pk>',views.CollegeDetail.as_view(),name='college'),
    path('colleges',views.CollegeList.as_view(),name='colleges'),
    path('create_student',views.StudentCreate.as_view()),
    path('create_college',views.CollegeCreate.as_view()),
    path('update_college/<int:pk>',views.CollegeUpdate.as_view()),
    path('update_student/<int:pk>',views.StudentUpdate.as_view()),
    path('college_delete/<int:pk>',views.DeleteCollege.as_view())
]
