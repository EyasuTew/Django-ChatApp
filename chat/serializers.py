from rest_framework import serializers
from .models import ChatRoom, Message
from django.contrib.auth.models import User

class ChatroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ('id', 'name') #, 'participants')

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('id', 'sender', 'timestamp', 'message', 'chatroom') #, 'attachment', '')

class CreateMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('message', #'attachment',
         'chatroom')

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    # # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    #
    # class Meta:
    #     model = User
    #     fields = ['id', 'username']#, 'snippets']