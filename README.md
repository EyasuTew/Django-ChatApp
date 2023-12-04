# Chat App
Chat Room app using Django WebSockets and Bootstrap


## Project Setup

1. Create virtual env using `python3 -m venv venv`
2. After activating virtual env, install dependencies using `pip install -Ur requirements.txt`
3. Change directory to root folder and perform DB migrations
```
    python manage.py makemigrations
    python manage.py migrate
```
4. Start server using `python manage.py runserver`

## Functionality

# UI - For demonstration purpose
Use http://127.0.0.1:8000/chat/
- Sign Up
- Log in
    - via username & password
- Create an account
- Create new chat rooms
- Send new chat messages over web sockets
- Retrieve Chat Rooms and Message history from DB CRUD operations

# API
Use http://localhost:8000/swagger/
- Sign up POST /api/v1/chat-api/users/
- Sign in / generate Bearer token POST /api/v1/token/
  - Copy **access** from token respones 
  - {
      "refresh": "<Token>",
      "access": "<Token>"
   } 
  - Add **access** on Authorize section of swagger `Bearer **access**` then user will be authenticated

- Add chat room POST /api/v1/chat-api/chatrooms/
- User enter into chatroom
- User leave chat room
- Send message POST /api/v1/chat-api/send-message/




