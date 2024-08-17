from django.urls import path
from . views import demo,SignupView,LoginView,LogoutView,ProfileView

urlpatterns = [
    path('test',demo.as_view(), name="demo"),
    path('profile',ProfileView.as_view(), name="profile"),
    path('signup/',SignupView.as_view(),name="signupform"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
   
]
