from simplemooc.core.views import home, contact
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    ]
