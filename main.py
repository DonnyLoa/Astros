import webapp2
import jinja2
import os
from google.appengine.api import urlfetch
import json
import random
from random import shuffle
from model import easyAnimals
from model import mediumAnimals
from model import hardAnimals
from model import easyGeography
from model import mediumGeography
from model import hardGeography

#from model import Settings #Name of this class comes from Dee
roundNumber = 0
i = 0

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class SeedPage(webapp2.RequestHandler):
    def get(self):
         animalsEasyEndPoint = "https://opentdb.com/api.php?amount=10&category=27&difficulty=easy"
         animalsMediumEndPoint = "https://opentdb.com/api.php?amount=10&category=27&difficulty=medium"
         animalsHardEndPoint = "https://opentdb.com/api.php?amount=10&category=27&difficulty=hard"
         geoEasyEndPoint = "https://opentdb.com/api.php?amount=10&category=22&difficulty=easy"
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
         son_a_m_response = json.loads(a_m_response)
         a_m_results = json_a_m_response["results"]
         for b in a_m_results:
             a_m_question = mediumAnimals(
                animal_m_question= b["question"],
                animal_m_correct= b["correct_answer"],
                animal_m_wrong = b["incorrect_answers"])
             a_m_question.put()

         a_h_response = urlfetch.fetch(animalsHardEndPoint).content
         json_a_h_response = json.loads(a_h_response)
         a_h_results = json_a_h_response["results"]
         for c in a_h_results:
             a_h_question = hardAnimals(
                animal_h_question = c["question"],
                animal_h_correct = c["correct_answer"],
                animal_h_wrong = c["incorrect_answers"])
             a_h_question.put()

         g_e_response = urlfetch.fetch(geoEasyEndPoint).content
         json_g_e_response = json.loads(g_e_response)
         g_e_results = json_g_e_response["results"]
         for d in g_e_results:
             g_e_question = easyGeography(
                geo_e_question = d["question"],
                geo_e_correct = d["correct_answer"],
                geo_e_wrong = d["incorrect_answers"])
             g_e_question.put()

         g_m_response = urlfetch.fetch(geoMediumEndPoint).content
         json_g_m_response = json.loads(g_m_response)
         g_m_results = json_g_m_response["results"]
         for e in g_m_results:
             g_m_question = mediumGeography(
                geo_m_question = e["question"],
                geo_m_correct = e["correct_answer"],
                geo_m_wrong = e["incorrect_answers"])
             g_m_question.put()

         g_h_response = urlfetch.fetch(geoHardEndPoint).content
         json_g_h_response = json.loads(g_h_response)
         g_h_results = json_g_h_response["results"]
         for f in g_h_results:
             g_h_question = hardGeography(
                geo_h_question = f["question"],
                geo_h_correct = f["correct_answer"],
                geo_h_wrong = f["incorrect_answers"])
             g_h_question.put()

class TitleScreen(webapp2.RequestHandler):
    def get(self):
        start_template = JINJA_ENVIRONMENT.get_template('templates/astros.html') #Html pages comes from Dee M
        self.response.write(start_template.render())

    def post(self):
        name_template = JINJA_ENVIRONMENT.get_template('templates/astros.html')

    def post(self):
        name_template = JINJA_ENVIRONMENT.get_template('templates/astros.html')
        difficulty = self.request.get("difficulty") #Dee's Data variables
        category = self.request.get("category")  #Dee's Data variables
        numRounds = self.request.get("numRounds")  #Dee's Data variables

        #game_settings = Settings(difficulty=difficulty,    #class with data from ^ comes from Dee H
        #                         category=category,
        #                         numRounds=numRounds)

        #game_settings.put()

        settings_data = {'line1': difficulty,
                         'line2': category,
                         'line3': numRounds}

        self.response.write(name_template.render(settings_data))
        #self.response.write(name_template.render())

    def get(self):
        name_template = JINJA_ENVIRONMENT.get_template('templates/astros.html')
        self.response.write(name_template.render())

class MagicDecision(webapp2.RequestHandler):
    def post(self):
        magic_template = JINJA_ENVIRONMENT.get_template('templates/magic_decision.html')
        name1 = self.request.get("name1")
        name2 = self.request.get("name2")

        #player_names = Names(name1=name1,    #class with data from ^ comes from Dee H
        #                     name2=name2)

        #player_names.put()

        #all_players = player_names.query().fetch()

        #names_data = {'line1': name1,
        #              'line2': name2}

        #self.response.write(magic_template.render(names_data))
        self.response.write(magic_template.render())

    def get(self):
        magic_template = JINJA_ENVIRONMENT.get_template('templates/magic_decision.html')
        self.response.write(magic_template.render())

class Trivia(webapp2.RequestHandler):
    def post(self):
        # = self.request.get("difficulty") #Dee's Data variables
        trivia_template = JINJA_ENVIRONMENT.get_template('templates/trivia.html')
        player = self.request.get("player")  #Dee's Data variables
        points = self.request.get("points")  #Dee's Data variables

        #generated_trivia = SeedPage(difficulty=difficulty,    #class with data from ^ comes from Dee H
        #                         player=player,
        #                         points=points)

        #generated_trivia.put()

        #all_trivia = trivia_questions.query().fetch()

        trivia_data = {'line1': player,
                       'line2': points}
                       #'all_trivia': all_trivia}

        self.response.write("<h1> Answer the question! </h1>")
# CATEGORY: ANIMALS DIFFCULTY: EASY
        j = [""]
        all_answers = []

        for i in range(1,10):
             j = random.randint(1,10)

        in_quiry = easyAnimals.query().fetch()[j].animal_e_question
        correct_answer = easyAnimals.query().fetch()[j].animal_e_correct
        incorrect_answers = easyAnimals.query().fetch()[j].animal_e_wrong
        self.response.write(in_quiry)

        all_answers = [correct_answer]
        for v in incorrect_answers:
            all_answers.append(v)
        shuffle(all_answers)

        for answer in all_answers:
            self.response.write("<p>" + answer + "</p>")

# CATEGORY: ANIMALS DIFFICULTY: MEDIUM
<<<<<<< HEAD
#         def get(self):
#             for i in range(1,10):
#                 j= random.randint(1,10)
#                 in_quiry = mediumAnimals.query().fetch()[j].animal_m_question
#                 answers = mediumAnimals.query().fetch()[j].animal_m_correct
#                 incorrect_answers = mediumAnimals.query().fetch()[j].animal_m_wrong
#             self.response.write("<br>" + in_quiry )
#
#             all_answers = [correct_answer]
#             for v in incorrect_answers:
#                 all_answers.append(v)
#             shuffle(all_answers)
#
#             for answer in all_answers:
#                 self.response.write("<p>" + answer + "</p>")
#         # CATEGORY: ANIMALS DIFFICULTY: HARD
#         def get(self):
#             for i in range(1,10):
#                 j= random.randint(1,10)
#                 in_quiry = hardAnimals.query().fetch()[j].animal_h_question
#                 answers = hardAnimals.query().fetch()[j].animal_h_correct
#                 incorrect_answers = hardAnimals.query().fetch()[j].animal_h_wrong
#             self.response.write("<br>" + in_quiry )
#
#             all_answers = [correct_answer]
#             for v in incorrect_answers:
#                 all_answers.append(v)
#             shuffle(all_answers)
#
#             for answer in all_answers:
#                 self.response.write("<p>" + answer + "</p>")
#
#         # CATEGORY: GEOGRAPHY DIFFICULTY: EASY
#         def get(self):
#             for i in range(1,10):
#                 j= random.randint(1,10)
#                 in_quiry = easyGeography.query().fetch()[j].geo_e_question
#                 answers = easyGeography.query().fetch()[j].geo_e_correct
#                 incorrect_answers = easyGeography.query().fetch()[j].geo_e_wrong
#             self.response.write("<br>" + in_quiry )
#
#             all_answers = [correct_answer]
#             for v in incorrect_answers:
#                 all_answers.append(v)
#             shuffle(all_answers)
#
#             for answer in all_answers:
#                 self.response.write("<p>" + answer + "</p>")
#
#         # CATEGORY: GEOGRAPHY DIFFICULTY: MEDIUM
#         def get(self):
#             for i in range(1,10):
#                 j= random.randint(1,10)
#                 in_quiry = mediumGeography.query().fetch()[j].geo_m_question
#                 answers = mediumGeography.query().fetch()[j].geo_m_correct
#                 incorrect_answers = mediumGeography.query().fetch()[j].geo_m_wrong
#             self.response.write("<br>" + in_quiry )
#
#             all_answers = [correct_answer]
#             for v in incorrect_answers:
#                 all_answers.append(v)
#             shuffle(all_answers)
#
#             for answer in all_answers:
#                 self.response.write("<p>" + answer + "</p>")
#         # CATEGORY GEOGRAPHY DIFFICULTY: HARD
#         def get(self):
#             for i in range(1,10):
#                 j= random.randint(1,10)
#                 in_quiry = hardGeography.query().fetch()[j].geo_h_question
#                 answers = hardGeography.query().fetch()[j].geo_h_correct
#                 incorrect_answers = hardGeography.query().fetch()[j].geo_h_wrong
#             self.response.write("<br>" + in_quiry )
#
# <<<<<<< HEAD
#             all_answers = [correct_answer]
#             for v in incorrect_answers:
#                 all_answers.append(v)
#             shuffle(all_answers)
#
#             for answer in all_answers:
#                 self.response.write("<p>" + answer + "</p>"
#
#             trivia_template = JINJA_ENVIRONMENT.get_template('templates/trivia.html')
#             self.response.write(trivia_template.render(trivia_data))
# =======
#     def get(self):
#         trivia_template = JINJA_ENVIRONMENT.get_template('templates/trivia.html')
#         self.response.write(trivia_template.render(trivia_data))
# >>>>>>> 08bc5f9174c2bf8b666a0497b8d57b6b4fb9974a
=======
        def get(self):
            for i in range(1,10):
                j= random.randint(1,10)
                in_quiry = mediumAnimals.query().fetch()[j].animal_m_question
                answers = mediumAnimals.query().fetch()[j].animal_m_correct
                incorrect_answers = mediumAnimals.query().fetch()[j].animal_m_wrong
            self.response.write("<br>" + in_quiry )

            all_answers = [correct_answer]
            for v in incorrect_answers:
                all_answers.append(v)
            shuffle(all_answers)

            for answer in all_answers:
                self.response.write("<p>" + answer + "</p>")
        # CATEGORY: ANIMALS DIFFICULTY: HARD
        def get(self):
            for i in range(1,10):
                j= random.randint(1,10)
                in_quiry = hardAnimals.query().fetch()[j].animal_h_question
                answers = hardAnimals.query().fetch()[j].animal_h_correct
                incorrect_answers = hardAnimals.query().fetch()[j].animal_h_wrong
            self.response.write("<br>" + in_quiry )

            all_answers = [correct_answer]
            for v in incorrect_answers:
                all_answers.append(v)
            shuffle(all_answers)

            for answer in all_answers:
                self.response.write("<p>" + answer + "</p>")

        # CATEGORY: GEOGRAPHY DIFFICULTY: EASY
        def get(self):
            for i in range(1,10):
                j= random.randint(1,10)
                in_quiry = easyGeography.query().fetch()[j].geo_e_question
                answers = easyGeography.query().fetch()[j].geo_e_correct
                incorrect_answers = easyGeography.query().fetch()[j].geo_e_wrong
            self.response.write("<br>" + in_quiry )

            all_answers = [correct_answer]
            for v in incorrect_answers:
                all_answers.append(v)
            shuffle(all_answers)

            for answer in all_answers:
                self.response.write("<p>" + answer + "</p>")

        # CATEGORY: GEOGRAPHY DIFFICULTY: MEDIUM
        def get(self):
            for i in range(1,10):
                j= random.randint(1,10)
                in_quiry = mediumGeography.query().fetch()[j].geo_m_question
                answers = mediumGeography.query().fetch()[j].geo_m_correct
                incorrect_answers = mediumGeography.query().fetch()[j].geo_m_wrong
            self.response.write("<br>" + in_quiry )

            all_answers = [correct_answer]
            for v in incorrect_answers:
                all_answers.append(v)
            shuffle(all_answers)

            for answer in all_answers:
                self.response.write("<p>" + answer + "</p>")
        # CATEGORY GEOGRAPHY DIFFICULTY: HARD
        def get(self):
            for i in range(1,10):
                j= random.randint(1,10)
                in_quiry = hardGeography.query().fetch()[j].geo_h_question
                answers = hardGeography.query().fetch()[j].geo_h_correct
                incorrect_answers = hardGeography.query().fetch()[j].geo_h_wrong
            self.response.write("<br>" + in_quiry )


            all_answers = [correct_answer]
            for v in incorrect_answers:
                all_answers.append(v)
            shuffle(all_answers)

            for answer in all_answers:
                self.response.write("<p>" + answer + "</p>"

            trivia_template = JINJA_ENVIRONMENT.get_template('templates/trivia.html')
            self.response.write(trivia_template.render(trivia_data))

    def get(self):
        trivia_template = JINJA_ENVIRONMENT.get_template('templates/trivia.html')
        self.response.write(trivia_template.render(trivia_data))
>>>>>>> a8fa544857c8ba8a5893d5291c68428d5ef09cc3

class Results(webapp2.RequestHandler):
    def post(self):
        results_template = JINJA_ENVIRONMENT.get_template('templates/results.html')
        self.response.write(results_template.render())

    def get(self):
        results_template = JINJA_ENVIRONMENT.get_template('templates/results.html')
        self.response.write(results_template.render())

class EndGame(webapp2.RequestHandler):
    def post(self):
        end_template = JINJA_ENVIRONMENT.get_template('endgame.html')
        self.response.write(end_template.render())

    def get(self):
        end_template = JINJA_ENVIRONMENT.get_template('endgame.html')
        self.response.write(end_template.render())

app = webapp2.WSGIApplication([
    ('/', TitleScreen),
    ('/eightBall', MagicDecision),
    ('/trivia', Trivia),
    ('/results', Results),
    ('/endGame', EndGame),
    ('/seed-page', SeedPage),
], debug=True)
