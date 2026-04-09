import json 
from channels.generic.websocket import WebsocketConsumer
from main_app.models import ActiveApplicants , User
class ApplicantNotifier(WebsocketConsumer):
    def connect(self):
        user_id = self.scope['url_route']['kwargs']['user_id']
        print(user_id)
        self.accept()
        user = User.objects.get(pk=user_id)
        ActiveApplicants.objects.create(channel_name=self.channel_name,user=user)
        print(self.channel_name)
        print(type(self.channel_name))

    def disconnect(self, code):
        print(code)
        print("will be deleted : ",ActiveApplicants.objects.filter(channel_name=self.channel_name).delete())

    def notification_send(self,event):
        message = event['message']
        print("Sending notification : ",message)
        data = {
            "action":"notification",
            "message":message
        }
        self.send(text_data=json.dumps(data))
    

        

        