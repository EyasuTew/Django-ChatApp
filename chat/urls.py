from django.urls import path
from . import views
from .views import ChatroomListCreate, ChatroomLeave, ChatroomEnter, CreateMessage, MessageList, MessageDetail, \
    UserListCreate, UserDetail

urlpatterns = [

    #apis
    path('chatrooms/', ChatroomListCreate.as_view(), name='chatroom-list-create'),
    path('chatroom/<int:pk>/leave/', ChatroomLeave.as_view(), name='chatroom-leave'),
    path('chatroom/<int:pk>/enter/', ChatroomEnter.as_view(), name='chatroom-enter'),
    path('send-message/', CreateMessage.as_view(), name='message-create'),
    path('messages/', MessageList.as_view(), name='message-list'),
    path('message/<int:pk>/', MessageDetail.as_view(), name='message-detail'),
    path('users/', UserListCreate.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),

    #ui
    path('', views.index, name='home'),
    path('<str:room_name>/', views.room, name='room'),
]