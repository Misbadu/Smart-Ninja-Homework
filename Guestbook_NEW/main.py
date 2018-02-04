#!/usr/bin/env python
import os
import jinja2
import webapp2
from models import Message


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("index.html")


class CreateHandler(BaseHandler):
    def get(self):
        messages = Message.query().fetch()
        params = {"messages": messages}
        return self.render_template("create.html", params=params)

    def post(self):
        user_name = self.request.get("name")
        user_email = self.request.get("email")
        user_text = self.request.get("text")
        if not user_name:
            user_name = "Anonymus"
        new_message = Message(name=user_name, email=user_email, text=user_text)
        new_message.put()

        return self.redirect_to("messagelist")

class MessageListHandler(BaseHandler):
    def get(self):
        messages = Message.query().fetch()
        params = {"messages": messages}
        return self.render_template("messagelist.html", params=params)

class MessageDetailsHandler(BaseHandler):
    def get(self, message_id):
        message = Message.get_by_id(int(message_id))
        params = {"message": message}
        return self.render_template("message_details.html", params=params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/create', CreateHandler, name="create_site"),
    webapp2.Route('/messagelist', MessageListHandler, name="messagelist"),
    webapp2.Route('/message/<message_id:\d+>', MessageDetailsHandler),
], debug=True)
