from django.urls import path
from .views import signup, login_view, logout_view, home

urlpatterns = [
    path('', home, name='home'),  # Home page view
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
