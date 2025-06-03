from django.urls import path

from . import views


urlpatterns = [
    path('entrol-confirmation/<str:uuid>', views.EnrollConfirmationView.as_view(),name= 'enroll-confirmation'),
    path('razorpay-view/<str:uuid>', views.RazorpayView.as_view(),name= 'razorpay-view'),
    path('verify-payment/',views.PaymentVerifyView.as_view(),name='verify-payment')
]