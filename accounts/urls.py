from django.urls import path
from . import views
from .views import CustomConfirmEmailView

urlpatterns = [
    path('', views.profile, name='customer_profile'),
    path('accounts/confirm-email/<str:key>/', CustomConfirmEmailView.as_view(), name='account_confirm_email'),
    path('booking_history/<booking_number>',
         views.booking_history, name='booking_history'),
    path('delete_profile/', views.delete_profile, name='delete_profile'),
]