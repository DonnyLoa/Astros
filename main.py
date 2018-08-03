import webapp2
import jinja2
import os
from google.appengine.api import urlfetch
import json
import random
#import PyV8
from random import shuffle
from model import easyAnimals
from model import mediumAnimals
from model import hardAnimals
from model import easyGeography
from model import mediumGeography
from model import hardGeography
from model import pointsData
from model import timeData
import urlparse
#from model import questionData
from webapp2_extras import sessions

class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)

        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

#from model import Settings #Name of this class comes from Dee
roundNumber = 0
i = 0
p1score = 0
p2score = 0

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class SeedPage(BaseHandler):
    def get(self):
         animalsEasyEndPoint = "https://opentdb.com/api.php?amount=30&category=17&difficulty=easy&encode=url3986"
         animalsMediumEndPoint = "https://opentdb.com/api.php?amount=30&category=17&difficulty=medium&encode=url3986"
         animalsHardEndPoint = "https://opentdb.com/api.php?amount=30&category=17&difficulty=hard&encode=url3986"
         geoEasyEndPoint = "https://opentdb.com/api.php?amount=30&category=22&difficulty=easy&encode=url3986"
         geoMediumEndPoint = "https://opentdb.com/api.php?amount=30&category=22&difficulty=medium&encode=url3986"
         geoHardEndPoint = "https://opentdb.com/api.php?amount=30&category=22&difficulty=hard&encode=url3986"

         a_e_response = urlfetch.fetch(animalsEasyEndPoint).content
         print a_e_response
         json_a_e_response = json.loads(a_e_response)
         a_e_results = json_a_e_response["results"]
         for a in a_e_results:
            aeqp = urlparse.unquote(a["question"])
            aecp = urlparse.unquote(a["correct_answer"])
            aewplist = []
            for x in a["incorrect_answers"]:
               aewp = urlparse.unquote(x)
               aewplist.append(aewp)
            a_e_question = easyAnimals(
               animal_e_question = aeqp,
               animal_e_correct = aecp,
               animal_e_wrong = aewplist)
            a_e_question.put()

         a_m_response = urlfetch.fetch(animalsMediumEndPoint).content
         json_a_m_response = json.loads(a_m_response)
         a_m_results = json_a_m_response["results"]
         for b in a_m_results:
             amqp = urlparse.unquote(b["question"])
             amcp = urlparse.unquote(b["correct_answer"])
             amwplist = []
             for x in b["incorrect_answers"]:
                amwp = urlparse.unquote(x)
                amwplist.append(amwp)
             a_m_question = mediumAnimals(
                animal_m_question = amqp,
                animal_m_correct = amcp,
                animal_m_wrong = amwplist)
             a_m_question.put()

         a_h_response = urlfetch.fetch(animalsHardEndPoint).content
         json_a_h_response = json.loads(a_h_response)
         a_h_results = json_a_h_response["results"]
         for c in a_h_results:
             ahqp = urlparse.unquote(c["question"])
             ahcp = urlparse.unquote(c["correct_answer"])
             ahwplist = []
             for x in c["incorrect_answers"]:
                ahwp = urlparse.unquote(x)
                ahwplist.append(ahwp)
             a_h_question = hardAnimals(
                animal_h_question = ahqp,
                animal_h_correct = ahcp,
                animal_h_wrong = ahwplist)
             a_h_question.put()


         g_e_response = urlfetch.fetch(geoEasyEndPoint).content
         json_g_e_response = json.loads(g_e_response)
         g_e_results = json_g_e_response["results"]
         for d in g_e_results:
             geqp = urlparse.unquote(d["question"])
             gecp = urlparse.unquote(d["correct_answer"])
             gewplist = []
             for x in d["incorrect_answers"]:
                gewp = urlparse.unquote(x)
                gewplist.append(gewp)
             g_e_question = easyGeography(
                geo_e_question = geqp,
                geo_e_correct = gecp,
                geo_e_wrong = gewplist)
             g_e_question.put()

         g_m_response = urlfetch.fetch(geoMediumEndPoint).content
         json_g_m_response = json.loads(g_m_response)
         g_m_results = json_g_m_response["results"]
         for e in g_m_results:
             gmqp = urlparse.unquote(e["question"])
             gmcp = urlparse.unquote(e["correct_answer"])
             gmwplist = []
             for x in e["incorrect_answers"]:
                gmwp = urlparse.unquote(x)
                gmwplist.append(gmwp)
             g_m_question = mediumGeography(
                geo_m_question = gmqp,
                geo_m_correct = gmcp,
                geo_m_wrong = gmwplist)
             g_m_question.put()

         g_h_response = urlfetch.fetch(geoHardEndPoint).content
         json_g_h_response = json.loads(g_h_response)
         g_h_results = json_g_h_response["results"]
         for f in g_h_results:
             ghqp = urlparse.unquote(f["question"])
             ghcp = urlparse.unquote(f["correct_answer"])
             ghwplist = []
             for x in f["incorrect_answers"]:
                ghwp = urlparse.unquote(x)
                ghwplist.append(ghwp)
             g_h_question = hardGeography(
                geo_h_question = ghqp,
                geo_h_correct = ghcp,
                geo_h_wrong = ghwplist)
             g_h_question.put()

         # ourTimes = {
         # "15000": "15000",
         # "30000": "30000",
         # }
         # ourPoints = {
         # "5": "5",
         # "10": "10",
         # }
         # for x in ourTimes:
         #     randomizedData = timeData(
         #        time = x["ourTimes"]
         #        )
         # for x in ourPoints:
         #     dominzedData = pointsData(
         #     points = x["ourPoints"]
         #     )
         #
         # randomizedData.put()
         # dominzedData.put()

        #player_1_data = questionData(player=1,points=0).put()
        #player_2_data = questionData(player=1,points=0).put()

         # for g in range(10):
         #    triviaData = questionData(
         #        player = g["player"],
         #        points = g["points"])
         #    triviaData.put()

class TitleScreen(BaseHandler):
    def get(self):
        start_template = jinja_env.get_template('templates/astros.html') #Html pages comes from Dee M

        category = self.request.get("category")    # Category
        self.session['category'] = category

        difficulty = self.request.get("difficulty")     # Difficulty
        self.session['difficulty'] = difficulty

        player_1 = self.request.get("player_1")     # First Player
        self.session['player_1'] = player_1

        player_2 = self.request.get("player_2")     # Second Player
        self.session['player_2'] = player_2

        text_box = self.request.get("Click to see the outcome")   # Page 2 Textbox
        self.session['text_box'] = text_box

        # numRounds = self.request.get("1")
        # self.session['numRounds'] = numRounds

        #Num rounds dictionary-----------------------

        # convertNum = self.session.ToInt32();

        self.response.write(start_template.render(difficulty=difficulty,category=category,player_1=player_1,player_2=player_2,text_box=text_box))

    #def post(self):
    #    name_template = jinja_env.get_template('templates/first_page.html')

    def post(self):
        start_template = jinja_env.get_template('templates/astros.html') #Html pages comes from Dee M

        category = self.request.get("category")    # Category
        self.session['category'] = category

        difficulty = self.request.get("difficulty")     # Difficulty
        self.session['difficulty'] = difficulty

        player_1 = self.request.get("player_1")     # First Player
        self.session['player_1'] = player_1

        player_2 = self.request.get("player_2")     # Second Player
        self.session['player_2'] = player_2

        text_box = self.request.get("Click to see the outcome")
        self.session['text_box'] = text_box

        # numRounds = self.request.get("1")
        # self.session['numRounds'] = numRounds
        # convertNum = Convert.ToInt32(self.session["numRounds"]);
        # text_box = "Click to see the outcome"    # Page 2 Textbox
        # self.session['player_2'] = text_box

        self.response.write(start_template.render(difficulty=difficulty,category=category,player_1=player_1,player_2=player_2,text_box=text_box))

        # name_template = jinja_env.get_template('templates/astros.html')
        # difficulty = self.request.get("difficulty") #Dee's Data variables
        # category = self.request.get("category")  #Dee's Data variables
        # numRounds = self.request.get("numRounds")  #Dee's Data variables

        #game_settings = Settings(difficulty=difficulty,    #class with data from ^ comes from Dee H
        #                         category=category,
        #                         numRounds=numRounds)

        #game_settings.put()

        # settings_data = {'line1': difficulty,
        #                  'line2': category,
        #                  'line3': numRounds}
        #
        # self.response.write(name_template.render(settings_data))
        #self.response.write(name_template.render())
class MagicDecision(BaseHandler):
    def post(self):
        magic_template = jinja_env.get_template('templates/Page2.html')

        difficulty = self.request.get("difficulty")
        self.session['difficulty'] = difficulty
        difficulty = self.session.get('difficulty')
        self.response.write("Difficulty: " + difficulty + "<br>")

        category = self.request.get("category")
        self.session['category'] = category
        category = self.session.get('category')
        self.response.write("Category: " + category + "<br>")

        player_1 = self.request.get("player_1")
        self.session['player_1'] = player_1
        player_1 = self.session.get('player_1')
        self.response.write("player_1: " + player_1 + "<br>")

        player_2 = self.request.get("player_2")
        self.session['player_2'] = player_2
        player_2 = self.session.get('player_2')
        self.response.write("player_2: " + player_2 + "<br>")

# Page 2 Textbox
        self.session['text_box'] = "Click to see the outcome"
        text_box = self.session.get('text_box')
        self.response.write(" text: " + text_box)

        self.response.write(magic_template.render(difficulty=difficulty,category=category,player_1=player_1,player_2=player_2,text_box=text_box))

    def get(self):
        magic_template = jinja_env.get_template('templates/Page2.html')

        self.response.write(magic_template.render())

        self.session['text_box'] = "Click to see the outcome"
        text_box = self.session.get('text_box')
        self.response.write(" text: " + text_box)

        self.response.write(magic_template.render(difficulty=difficulty,category=category,player_1=player_1,player_2=player_2,text_box=text_box))

class MagicDecision2(BaseHandler):
    def post(self):
        magic_template = jinja_env.get_template('templates/Page2-2.html')

        # difficulty = self.request.get("difficulty")
        # self.session['difficulty'] = difficulty
        difficulty = self.session.get('difficulty')
        self.response.write("Difficulty: " + difficulty + "<br>")

        # category = self.request.get("category")
        # self.session['category'] = category
        category = self.session.get('category')
        self.response.write("Category: " + category + "<br>")

        # player_1 = self.request.get("player_1")
        # self.session['player_1'] = player_1
        player_1 = self.session.get('player_1')
        # self.response.write("player_1: " + player_1 + "<br>")

        # player_2 = self.request.get("player_2")
        # self.session['player_2'] = player_2
        player_2 = self.session.get('player_2')
        # self.response.write("player_2: " + player_2 + "<br>")

        self.session['text_box'] = "Continue"
        text_box = self.session.get('text_box')
        # self.response.write(" text: " + text_box)

        self.response.write(magic_template.render(difficulty=difficulty,category=category,player_1=player_1,player_2=player_2,text_box=text_box))

    def get(self):
        magic_template = jinja_env.get_template('templates/Page2-2.html')

        difficulty = self.session.get('difficulty')
        self.response.write(" Difficulty: " + difficulty)

        category = self.session.get('category')
        self.response.write(" Category: " + category)

        player_1 = self.session.get('player_1')
        # self.response.write(" player_1: " + player_1)

        player_2 = self.session.get('player_2')
        # self.response.write(" player_2: " + player_2)

        self.session['text_box'] = "Continue"
        text_box = self.session.get('text_box')
        # self.response.write(" text: " + text_box)

        self.response.write(magic_template.render(difficulty=difficulty,category=category,player_1=player_1,player_2=player_2,text_box=text_box))
#------------------------------------------------------------------Personal Trivia Page that loads different data depending on difficulty and category
class Trivia(BaseHandler):
    def post(self):
        # difficulty = self.request.get("difficulty")
        # self.session['difficulty'] = difficulty
        difficulty = self.session.get('difficulty')
        self.response.write(" Difficulty: " + difficulty)

        category = self.session.get('category')
        self.response.write(" Category: " + category)

        player_1 = self.session.get('player_1')
        self.response.write(" player_1: " + player_1)

        player_2 = self.session.get('player_2')
        self.response.write(" player_2: " + player_2)

        j = [""]
        all_answers = []

        for i in range(0,10):
            j = random.randint(0,10)

        if (category == "Animals"):             # Determines category and difficulty for question
            if (difficulty == "Easy"):
                trivia_template = jinja_env.get_template('templates/trivia.html')

                in_quiry = easyAnimals.query().fetch()[j].animal_e_question
                correct_answer = easyAnimals.query().fetch()[j].animal_e_correct
                incorrect_answers = easyAnimals.query().fetch()[j].animal_e_wrong

                self.response.write(in_quiry)
                all_answers = [correct_answer]
                for h in incorrect_answers:
                    all_answers.append(h)
                    shuffle(all_answers)

                self.response.write(trivia_template.render(difficulty=difficulty,category=category,player_1=player_1,player_2=player_2,in_quiry=in_quiry,all_answers=all_answers))

                for answer in all_answers:
                    self.response.write("<p>" + answer + "</p>")

            elif (difficulty == "Less Easy"):
                trivia_template = jinja_env.get_template('templates/trivia.html')

                in_quiry = mediumAnimals.query().fetch()[j].animal_m_question
                correct_answer = mediumAnimals.query().fetch()[j].animal_m_correct
                incorrect_answers = mediumAnimals.query().fetch()[j].animal_m_wrong

                self.response.write(in_quiry)
                all_answers = [correct_answer]
                for h in incorrect_answers:
                    all_answers.append(h)
                    shuffle(all_answers)

                self.response.write(trivia_template.render(difficulty=difficulty,category=category,player_1=player_1,player_2=player_2,in_quiry=in_quiry,all_answers=all_answers))

                for answer in all_answers:
                    self.response.write("<p>" + answer + "</p>")

            elif (difficulty == "Waaaayyy Less Easy"):
                trivia_template = jinja_env.get_template('templates/trivia.html')

                in_quiry = hardAnimals.query().fetch()[j].animal_h_question
                correct_answer = hardAnimals.query().fetch()[j].animal_h_correct
                incorrect_answers = hardAnimals.query().fetch()[j].animal_h_wrong

                self.response.write(in_quiry)
                all_answers = [correct_answer]
                for h in incorrect_answers:
                    all_answers.append(h)
                    shuffle(all_answers)

                self.response.write(trivia_template.render(difficulty=difficulty,category=category,player_1=player_1,player_2=player_2,in_quiry=in_quiry,all_answers=all_answers))

                for answer in all_answers:
                    self.response.write("<p>" + answer + "</p>")
        elif (category == "Geography"):
            if (difficulty == "Easy"):
                trivia_template = jinja_env.get_template('templates/trivia.html')

                in_quiry = easyGeography.query().fetch()[j].geo_e_question
                correct_answer = easyGeography.query().fetch()[j].geo_e_correct
                incorrect_answers = easyGeography.query().fetch()[j].geo_e_wrong

                self.response.write(in_quiry)
                all_answers = [correct_answer]
                for h in incorrect_answers:
                    all_answers.append(h)
                    shuffle(all_answers)

                self.response.write(trivia_template.render(difficulty=difficulty,category=category,player_1=player_1,player_2=player_2,in_quiry=in_quiry,all_answers=all_answers))

                for answer in all_answers:
                    self.response.write("<p>" + answer + "</p>")

            elif (difficulty == "Less Easy"):
                trivia_template = jinja_env.get_template('templates/trivia.html')

                in_quiry = mediumGeography.query().fetch()[j].geo_m_question
                correct_answer = mediumGeography.query().fetch()[j].geo_m_correct
                incorrect_answers = mediumGeography.query().fetch()[j].geo_m_wrong

                self.response.write(in_quiry)
                all_answers = [correct_answer]
                for h in incorrect_answers:
                    all_answers.append(h)
                    shuffle(all_answers)

                self.response.write(trivia_template.render(difficulty=difficulty,category=category,player_1=player_1,player_2=player_2,in_quiry=in_quiry,all_answers=all_answers))

                for answer in all_answers:
                    self.response.write("<p>" + answer + "</p>")

            elif (difficulty == "Waaaayyy Less Easy"):
                trivia_template = jinja_env.get_template('templates/trivia.html')

                in_quiry = hardGeography.query().fetch()[j].geo_h_question
                correct_answer = hardGeography.query().fetch()[j].geo_h_correct
                incorrect_answers = hardGeography.query().fetch()[j].geo_h_wrong

                self.response.write(in_quiry)
                all_answers = [correct_answer]
                for h in incorrect_answers:
                    all_answers.append(h)
                    shuffle(all_answers)

                self.response.write(trivia_template.render(difficulty=difficulty,category=category,player_1=player_1,player_2=player_2,in_quiry=in_quiry,all_answers=all_answers))

                for answer in all_answers:
                    self.response.write("<p>" + answer + "</p>")


        # trivia_template = jinja_env.get_template('templates/trivia.html')


# CATEGORY: ANIMALS DIFFCULTY: EASY
#----------------------------------------------------------------------------------------
class Results1(BaseHandler):
    def post(self):
        results_template = jinja_env.get_template('templates/results1.html')

        difficulty = self.session.get('difficulty')
        self.response.write(" Difficulty: " + difficulty)

        category = self.session.get('category')
        self.response.write(" Category: " + category)

        player_1 = self.session.get('player_1')
        # self.response.write(" player_1: " + player_1)

        player_2 = self.session.get('player_2')
        # self.response.write(" player_2: " + player_2)

        self.response.write(results_template.render(difficulty=difficulty,category=category,player_1=player_1,player_2=player_2))

    def get(self):
        results_template = jinja_env.get_template('templates/results1.html')

        difficulty = self.session.get('difficulty')
        self.response.write(" Difficulty: " + difficulty)

        category = self.session.get('category')
        self.response.write(" Category: " + category)

        player_1 = self.session.get('player_1')
        # self.response.write(" player_1: " + player_1)

        player_2 = self.session.get('player_2')
        # self.response.write(" player_2: " + player_2)

        self.response.write(results_template.render(difficulty=difficulty,category=category,player_1=player_1,player_2=player_2))

class Results2(BaseHandler):
    def post(self):
        results_template = jinja_env.get_template('templates/results2.html')

        difficulty = self.session.get('difficulty')
        self.response.write(" Difficulty: " + difficulty)

        category = self.session.get('category')
        self.response.write(" Category: " + category)

        player_1 = self.session.get('player_1')
        # self.response.write(" player_1: " + player_1)

        player_2 = self.session.get('player_2')
        # self.response.write(" player_2: " + player_2)

        self.response.write(results_template.render(difficulty=difficulty,category=category,player_1=player_1,player_2=player_2))

    def get(self):
        results_template = jinja_env.get_template('templates/results2.html')

        difficulty = self.session.get('difficulty')
        self.response.write(" Difficulty: " + difficulty)

        category = self.session.get('category')
        self.response.write(" Category: " + category)

        player_1 = self.session.get('player_1')
        # self.response.write(" player_1: " + player_1)

        player_2 = self.session.get('player_2')
        # self.response.write(" player_2: " + player_2)

        self.response.write(results_template.render(difficulty=difficulty,category=category,player_1=player_1,player_2=player_2))

class Results3(BaseHandler):
    def post(self):
        results_template = jinja_env.get_template('templates/results3.html')

        difficulty = self.session.get('difficulty')
        self.response.write(" Difficulty: " + difficulty)

        category = self.session.get('category')
        self.response.write(" Category: " + category)

        player_1 = self.session.get('player_1')
        # self.response.write(" player_1: " + player_1)

        player_2 = self.session.get('player_2')
        # self.response.write(" player_2: " + player_2)

        self.response.write(results_template.render(difficulty=difficulty,category=category,player_1=player_1,player_2=player_2))

    def get(self):
        results_template = jinja_env.get_template('templates/results3.html')

        difficulty = self.session.get('difficulty')
        self.response.write(" Difficulty: " + difficulty)

        category = self.session.get('category')
        self.response.write(" Category: " + category)

        player_1 = self.session.get('player_1')
        # self.response.write(" player_1: " + player_1)

        player_2 = self.session.get('player_2')
        # self.response.write(" player_2: " + player_2)

        self.response.write(results_template.render(difficulty=difficulty,category=category,player_1=player_1,player_2=player_2))

class EndGame(BaseHandler):
    def post(self):
        end_template = jinja_env.get_template('templates/endgame.html')

        difficulty = self.session.get('difficulty')
        self.response.write(" Difficulty: " + difficulty)

        category = self.session.get('category')
        self.response.write(" Category: " + category)

        player_1 = self.session.get('player_1')
        # self.response.write(" player_1: " + player_1)

        player_2 = self.session.get('player_2')
        # self.response.write(" player_2: " + player_2)

        self.response.write(end_template.render(difficulty=difficulty,category=category,player_1=player_1,player_2=player_2))

    def get(self):
        end_template = jinja_env.get_template('templates/endgame.html')

        difficulty = self.session.get('difficulty')
        self.response.write(" Difficulty: " + difficulty)

        category = self.session.get('category')
        self.response.write(" Category: " + category)

        player_1 = self.session.get('player_1')
        # self.response.write(" player_1: " + player_1)

        player_2 = self.session.get('player_2')
        # self.response.write(" player_2: " + player_2)

        self.response.write(end_template.render(difficulty=difficulty,category=category,player_1=player_1,player_2=player_2))

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}

app = webapp2.WSGIApplication([
    ('/', TitleScreen),
    ('/trivia', Trivia),
    ('/seed-page', SeedPage),
    ('/eightBall', MagicDecision),
    ('/eightBall2', MagicDecision2),
    ('/results1', Results1),
    ('/results2', Results2),
    ('/results3', Results3),
    ('/endGame', EndGame),
], config=config,
   debug=True)
