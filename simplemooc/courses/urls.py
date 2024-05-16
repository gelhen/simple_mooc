from simplemooc.courses.views import index, details
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', details, name='datails'),
    ]
