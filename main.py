import webapp2
import jinja2
import os
import json

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class SeedPage(webapp2.RequestHandler):
    def get(self):
        animalsEasyEndPoint = "https://opentdb.com/api.php?amount=10&category=27&difficulty=easy"
        animalsMediumEndPoint = "https://opentdb.com/api.php?amount=10&category=27&difficulty=medium"
        animalsHardEndPoint = "https://opentdb.com/api.php?amount=10&category=27&difficulty=hard"
        geoEasyEndpoint = "https://opentdb.com/api.php?amount=10&category=21&difficulty=easy"
        geoMediumEndPoint = "https://opentdb.com/api.php?amount=10&category=22&difficulty=medium"
        geoHardEndPoint = "https://opentdb.com/api.php?amount=10&category=22&difficulty=hard"

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
    ('/seed-page', SeedPage)
], debug=True)
