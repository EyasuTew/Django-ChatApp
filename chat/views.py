from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ChatRoom, Message
from rest_framework import generics, status
from .models import ChatRoom, Message
from .serializers import ChatroomSerializer, MessageSerializer, UserSerializer, CreateMessageSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .websocket_client import sendMessageWS
def get_chatrooms_with_last_message():
    chat_rooms = ChatRoom.objects.all()
    chat_rooms_with_last_message = []
    
    for room in chat_rooms:
        last_message = Message.objects.filter(chatroom=room).order_by('-timestamp').first()
        
        chat_rooms_with_last_message.append({
            'id': room.id,
            'room_name': room.name,
            'last_message': {
                'message': last_message.message if last_message else None,
                'timestamp': last_message.timestamp if last_message else None,
                'sender': last_message.sender.username if last_message and last_message.sender else None
            }
        })
    
    return chat_rooms_with_last_message

# Create your views here.
def index(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    chat_rooms = get_chatrooms_with_last_message()
    
    return render(request, 'index.html', context={'chat_rooms': chat_rooms})

def room(request, room_name):
    chatroom, created = ChatRoom.objects.get_or_create(name=room_name)
    chat_messages = Message.objects.filter(chatroom=chatroom)

    context = {
        'room_name': room_name,
        'chat_messages': chat_messages,
        'current_user': request.user.username
    }

    return render(request, 'chat_room.html', context)


class ChatroomListCreate(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = ChatRoom.objects.all()
    serializer_class = ChatroomSerializer

class ChatroomLeave(generics.DestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = ChatRoom.objects.all()
    serializer_class = ChatroomSerializer

class ChatroomEnter(generics.UpdateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = ChatRoom.objects.all()
    serializer_class = ChatroomSerializer

class CreateMessage(generics.CreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer
    def create(self, request, *args, **kwargs): # don't need to `self.request` since `request` is available as a parameter.

        chatroom = ChatRoom.objects.get(pk=self.request.data['chatroom'])
        message = self.request.data['message'],
        user =self.request.user
        # newmessage = Message(
        #     # content=self.request.data['content'],
        #     sender=self.request.user,
        #     chatroom=chatroom
        # )
        # newmessage.save()

        sendMessageWS(message=self.request.data['message'], chatroom=chatroom.name, username=str(user))
        return Response(status=status.HTTP_201_CREATED, data={"message" : "message has been sent"})


class MessageList(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
