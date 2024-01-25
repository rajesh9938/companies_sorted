from django.urls import path
from . import views
urlpatterns=[
    path('',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('uploaddata/',views.upload_csv,name="uploaddata"),
    path('logout/',views.logout,name="logout"),
    path('users/',views.users,name="users"),
    path('querrybuilder/',views.querrybuilder,name="querrybuilder"),





]