from mongoengine import *

connect(host="mongodb+srv://test_HW08:<password>@cluster0.yfciewx.mongodb.net/HW08", ssl=True)


class Contact(Document):
    fullname = StringField(required=True)
    email = StringField(required=True)
    was_send = BooleanField(required=True, default=False)
    msg_text = StringField()

