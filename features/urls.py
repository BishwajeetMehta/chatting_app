from django.urls import path
from .views import FriendView,Accept_requestView
urlpatterns = [
    path('friends/',FriendView.as_view(),name="friend"),
    path("friends/<int:id>",FriendView.as_view(), name="friend_request"),
    path("accept_friends",Accept_requestView.as_view(), name="pending_requests"),
    path("accept_friends/<int:id>/",Accept_requestView .as_view(), name="accept_requests"),
    
]
