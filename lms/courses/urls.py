from . import views

from django.urls import path

urlpatterns = [
    
    
    path('course-detail/<str:uuid>/',views.CoursesDetailView.as_view(), name ='course-detail'),

    path('home/',views.HomeView.as_view(), name ='home'),

    path('instructor-courses-list/', views.InstructorCourseListView.as_view(), name = 'instructor-courses-list'),

    path('create-course/', views.CourseCreateView.as_view(), name= 'create-course'),

    path('instructor-course-detail/<str:uuid>/', views.InstructorCoursesDetailView.as_view(), name='instructor-course-detail'),
    
    path('instructor-course-delete/<str:uuid>/', views.CourseDeleteView.as_view(), name='instructor-course-delete'),
    
    path('instructor-course-update/<str:uuid>/', views.InatructorCourseUpdateView.as_view(), name='instructor-course-update'),

    
]