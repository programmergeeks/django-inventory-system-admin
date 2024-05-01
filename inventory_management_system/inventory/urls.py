from django.urls import path # type: ignore
from .views import Index # type: ignore

urlpatterns = [
    path('', Index.as_view(), name="index"),
]
