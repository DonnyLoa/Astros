import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class TitleScreen(webapp2.RequestHandler):
    def get(self):
        start_template = JINJA_ENVIRONMENT.get_template('(title_screen.html)')
        self.response.write(start_template.render())

class Name(webapp2.RequestHandler):
    def get(self):
        start_template = JINJA_ENVIRONMENT.get_template('')
        self.response.write(start_template.render())

app = webapp2.WSGIApplication([
    ('/mainPage', TitleScreen),
    ('/name', Name),
], debug=True)
