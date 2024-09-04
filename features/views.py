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

        return render(request, 'send_friends.html', { 'users': users_to_display,'pending_request': friend_requests_sent,'new_users':new_users})


    def post(self,request,id):
        action = request.POST.get('action')
        if action == 'delete':
            request_to_delete = FriendRequest.objects.get(id=id)
            request_to_delete.delete()
            print("deleted sucessfully")
            return redirect("friend")
        
        receiver = User.objects.get(id = id)
        print(receiver.id)
        ftable = FriendRequest()
        ftable.from_user = request.user
        ftable.to_user = receiver
        ftable.save()
        messages.error(request,"Sent sucessfully ")
        print("request send sucessfully")
        return redirect("friend")
    
    

class Accept_requestView(View):
    def get(self,request):
        current_user = request.user
        pendings= FriendRequest.objects.filter(to_user=current_user,status='pending').all()
        print(pendings)
        return render(request,'accept_friends.html',{'pendings':pendings})
    
    def post(self,request,id):
        action = request.POST.get('action')
        pending_requests = FriendRequest.objects.get(id=id)
        print(pending_requests)

        if action == 'accept':
            if pending_requests.to_user == request.user:
                pending_requests.status = 'accepted'
                pending_requests.save()
                return redirect('pending_requests')
        elif action == 'delete':
            pending_requests.delete()
            print('deleted sucessfully')
            return redirect('pending_requests')
        
        print('something went wrong')
        return redirect('pending_requests')
        
class MessangerView(View):
    def get(self,request):
        user = request.user 
        friends = User.objects.filter(
        Q(sent_requests__to_user=user, sent_requests__status="accepted") |
        Q(received_requests__from_user=user, received_requests__status="accepted")
    ).distinct()
        
#         for f in friends:
#             if f.to_user == request.user:
#                 frie = f.from_user
#                 print('fi')
#             if f.from_user == request.user:
#                 frie = f.to_user
#                 print("sec")

            



        print(friends)
        return render(request,'messanger.html',{'friends':friends})



