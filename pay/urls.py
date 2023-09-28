from django.urls import path
from .views import *




urlpatterns = [
    # Payment
    path('payment/alerts/', payment_alerts, name='payment_alerts'),
    path('payment/success/', payment_success, name='payment_success'),
    path('payment/error/', payment_error, name='payment_error')
]