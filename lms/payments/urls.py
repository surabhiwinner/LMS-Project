from django.urls import path

from . import views


urlpatterns = [
    path('entrol-confirmation/<str:uuid>', views.EnrollConfirmationView.as_view(),name= 'enroll-confirmation')
]