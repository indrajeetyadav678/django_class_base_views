from django.urls import path
from .views import Studentviews

urlpatterns = [
 path('', Studentviews.as_view())
]