from django.urls import path
from .views import homepage, custom_logout

urlpatterns = [
    path('', homepage, name="homepage"),
    path('logout/', custom_logout, name="logout"),
]
