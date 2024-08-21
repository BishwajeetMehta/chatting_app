from django.urls import path
from .views import FriendView 
urlpatterns = [
    path('friends/',FriendView.as_view(),name="friend"),
    path("friends/<int:id>",FriendView.as_view(), name="friend_request")
]
