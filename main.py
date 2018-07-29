import webapp2
import jinja2
import os
from google.appengine.api import urlfetch
import json
from random import shuffle
from model import easyAnimals
from model import mediumAnimals
from model import hardAnimals
from model import easyGeography
from model import mediumGeography
from model import hardGeography

#from model import Settings #Name of this class comes from Dee
roundNumber = 0

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class SeedPage(webapp2.RequestHandler):
    def get(self):
        animalsEasyEndPoint = "https://opentdb.com/api.php?amount=10&category=27&difficulty=easy"
        animalsMediumEndPoint = "https://opentdb.com/api.php?amount=10&category=27&difficulty=medium"
        animalsHardEndPoint = "https://opentdb.com/api.php?amount=10&category=27&difficulty=hard"
        geoEasyEndPoint = "https://opentdb.com/api.php?amount=10&category=21&difficulty=easy"
        geoMediumEndPoint = "https://opentdb.com/api.php?amount=10&category=22&difficulty=medium"
        geoHardEndPoint = "https://opentdb.com/api.php?amount=10&category=22&difficulty=hard"

        a_e_response = urlfetch.fetch(animalsEasyEndPoint).content
        json_a_e_response = json.loads(a_e_response)
        a_e_results = json_a_e_response["results"]
        for a in a_e_results:
            a_e_question = easyAnimals(
                animal_e_question= a["question"],
                animal_e_correct= a["correct_answer"],
                animal_e_wrong = a["incorrect_answers"])
            a_e_question.put()

        a_m_response = urlfetch.fetch(animalsMediumEndPoint).content
        json_a_m_response = json.loads(a_m_response)
        a_m_results = json_a_m_response["results"]
        for b in a_m_results:
            a_m_question = mediumAnimals(
                animal_m_question= b["question"],
                animal_m_correct= b["correct_answer"],
                animal_m_wrong = b["incorrect_answers"])
            a_m_question.put()

        a_h_response = urlfetch.fetch(animalsHardEndPoint)
        json_a_h_response = json.loads(a_h_response)
        a_h_results = json_a_h_response["results"]
        for c in a_h_results:
            a_h_question = hardAnimals(
                animal_h_question = c["question"]
                animal_h_correct = c["correct_answer"]
                animal_h_wrong = c["incorrect_answers"])
            a_h_question.put()

        g_e_response = urlfetch.fetch(geoEasyEndPoint)
        json_g_e_response = json.loads(g_e_response)
        g_e_results = json_g_e_response["results"]
        for d in g_e_results:
            g_e_question = easyGeography(
                geo_e_question = d["question"]
                geo_e_correct = d["correct_answer"]
                geo_e_wrong = d["incorrect_answers"])
            g_e_question.put()

        g_m_response = urlfetch.fetch(geoMediumEndPoint)
        json_g_m_respone = json.loads(g_m_response)
        g_m_results = json_g_m_response["results"]
        for e in g_m_results:
            g_m_question = mediumGeography(
                geo_m_question = e["question"]
                geo_m_correct = e["correct_answer"]
                geo_m_wrong = e["incorrect_answers"])
            g_m_question.put()

        g_h_response = urlfetch.fetch(geoHardEndPoint)
        json_g_h_response = json.loads(g_h_response)
        g_h_results = json_g_h_results["results"]
        for f in g_h_results:
            g_h_question = hardGeography(
                geo_h_question = f["question"]
                geo_h_correct = f["correct_answer"]
                geo_h_wrong = f["incorrect_answers"])
        g_h_question.put()

class TitleScreen(webapp2.RequestHandler):
    def get(self):
        start_template = JINJA_ENVIRONMENT.get_template('templates/first_page.html') #Html pages comes from Dee M
        self.response.write(start_template.render())

    def post(self):
        name_template = JINJA_ENVIRONMENT.get_template('templates/first_page.html')

class Name(webapp2.RequestHandler):
    def get(self):
        name_template = JINJA_ENVIRONMENT.get_template('templates/name.html')
        self.response.write(name_template.render())

app = webapp2.WSGIApplication([
    ('/mainPage', TitleScreen),
    ('/name', Name),
    ('/seed-page', SeedPage)
], debug=True
