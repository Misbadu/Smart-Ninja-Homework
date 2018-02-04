from google.appengine.ext import ndb

class Message(ndb.Model):
    text = ndb.StringProperty(required=True)
    name = ndb.StringProperty()
    email = ndb.StringProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)