from django.urls import path
from .views import Validate_csv
urlpatterns = [
    path('validate_csv/', Validate_csv.as_view())
]