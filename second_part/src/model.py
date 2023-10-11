from mongoengine import Document
from mongoengine.fields import StringField, BooleanField


class Contact(Document):
    fullname = StringField(max_length=150)
    email = StringField(max_length=200)
    send = BooleanField(default=False)
    phone = StringField(max_length=200)
    address = StringField(max_length=300)
