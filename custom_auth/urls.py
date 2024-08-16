from django.urls import path
from . views import SignupPageView,demo,UserView,LoginView

urlpatterns = [
    path('signup',SignupPageView.as_view(),name='signupform'),
    path('test',demo.as_view(), name="demo"),
    path('userCRUD/',UserView.as_view(),name="userCRUD"),
    path('login/', LoginView.as_view(), name='login'),
]
