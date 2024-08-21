from django.shortcuts import render,redirect
from django.views import View
from custom_auth. models import User
from . models import FriendRequest
from django.contrib import messages
from django.db.models import Q
# Create your views here.

class FriendView(View):
    
    def get(self, request):
        current_user = request.user
    
        print(current_user)
        # Get all users except the current user
        available_users = User.objects.exclude(id=current_user.id)
        pid =  FriendRequest.objects.filter(
            Q(from_user=current_user, status='accepted')|
            Q(to_user=current_user, status='accepted')
            ).values_list('from_user_id', 'to_user_id')
        
        accepted_request_ids = set(id for sublist in pid for id in sublist)
        users_to_display = available_users.exclude(id__in=accepted_request_ids)
        print(f'users to display{users_to_display}')

        friend_requests_sent = FriendRequest.objects.filter(Q(from_user=current_user,status='pending')|Q(to_user=current_user,status='pending'))
       
        print(f'friend request sent are{friend_requests_sent}')

        pending_requests = FriendRequest.objects.filter(Q(from_user=current_user,status='pending')|Q(to_user=current_user,status='pending')).values_list('from_user_id', 'to_user_id')
        pending_requests_ids = set(id for sublist in pending_requests for id in sublist)
        new_users= users_to_display.exclude(id__in=pending_requests_ids)
        print(f'new user{new_users}')

        return render(request, 'friends.html', { 'users': users_to_display,'pending_request': friend_requests_sent,'new_users':new_users})


    def post(self,request,id):
        data = request.POST
        receiver = User.objects.get(id = id)
        print(receiver.id)
        ftable = FriendRequest()
        ftable.from_user = request.user
        ftable.to_user = receiver
        ftable.save()
        messages.error(request,"Sent sucessfully ")
        return redirect("friend")

