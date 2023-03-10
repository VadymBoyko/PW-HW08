from mongoengine import *

connect(host="mongodb+srv://test_HW08:<password>@cluster0.yfciewx.mongodb.net/HW08", ssl=True)


class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quote(Document):
    quote = StringField(required=True)
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    tags = ListField(StringField())
    meta = {'allow_inheritance': True}



