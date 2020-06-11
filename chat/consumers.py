# import json
# from channels.generic.websocket import WebsocketConsumer

# class ChatConsumer(WebsocketConsumer):
    
#     def connect(self):
#         self.accept()
        
        

#     def disconnect(self, close_code):
#         pass

#     def receive(self, text_data):
#         print(text_data)
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         self.send(text_data=json.dumps({
#             'message': message
#         }))

from datetime import datetime
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Message , roomName
from django.contrib.auth import get_user_model

User = get_user_model()

from .models import person , Message
class ChatConsumer(WebsocketConsumer):
    
    
    def fetch_messages(self , data):
       
        messages = Message.last_30_messages()
        content = {
            "command" : "messages",
            'messages': self.messages_to_json(messages)
        }
        self.send_chat_message(content)
        
    def messages_to_json(self , messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result
            
    def message_to_json(self , message):
        return {
            'user':message.author.username,
            'content':message.content,
            'timestamp': str(message.timestamp)
        }
    def new_message(self, data):
        
        author = data['from']
        
        user = person.objects.filter(username=author)[0]
        room = roomName.objects.get(name = data['room_name'])
        message = Message.objects.create(author = user , content=data['message'] , timestamp = datetime.now() , roomName = room)
        print(message)
        content = {
            'command' : 'new_message',
            'message' : self.message_to_json(message)
        }
        self.send_chat_message(content)

    commands = {
        'fetch_messages':  fetch_messages,
        'new_message' : new_message,
    }
    def connect(self):
        
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
    

        self.accept()
        

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        print(data)
        self.commands[data['command']](self, data)
        # self.commands[data['commands']](self,data)

    
    def send_chat_message(self , message):
        
        # Send message to room group // actually when a message came ,, this part send this one to all persons in group_room
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        ) 
    def send_message(self , message):
        self.send(text_data=json.dumps(message))

    # send message for every person in room_group
    def chat_message(self, event):
        message = event['message']
        # Send message to WebSocket
        self.send(json.dumps(message))


# import json
# from channels.generic.websocket import AsyncWebsocketConsumer

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name

#         # Join room group
#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )

#         await self.accept()

#     async def disconnect(self, close_code):
#         # Leave room group
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )

#     # Receive message from WebSocket
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         # Send message to room group
#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )

#     # Receive message from room group
#     async def chat_message(self, event):
#         message = event['message']

#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({
#             'message': message
#         }))
