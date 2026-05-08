from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tests/', views.test_results, name='test_results'),
    path('api/availability', views.check_availability, name='availability'),
    path('api/book', views.book_room, name='book'),
    path('api/cancel', views.cancel_booking, name='cancel'),
    path('api/pricing', views.get_pricing, name='pricing'),
    path('api/contact', views.contact_hotel, name='contact'),
]
