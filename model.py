from google.appengine.ext import ndb

class easyAnimals(ndb.Model):
    animal_e_question = ndb.StringProperty(required=True)
    animal_e_correct = ndb.StringProperty(required=True)
    animal_e_wrong = ndb.StringProperty(repeated=True)

class mediumAnimals(ndb.Model):
    animal_m_question = ndb.StringProperty(required=True)
    animal_m_correct = ndb.StringProperty(required=True)
    animal_m_wrong = ndb.StringProperty(repeated=True)

class hardAnimals(ndb.Model):
    animal_h_question = ndb.StringProperty(required=True)
    animal_h_correct = ndb.StringProperty(required=True)
    animal_h_wrong = ndb.StringProperty(repeated=True)


class easyGeography(ndb.Model):
    geo_e_question = ndb.StringProperty(required=True)
    geo_e_correct = ndb.StringProperty(required=True)
    geo_e_wrong = ndb.StringProperty(repeated=True)

class mediumGeography(ndb.Model):
    geo_m_question = ndb.StringProperty(required=True)
    geo_m_correct = ndb.StringProperty(required=True)
    geo_m_wrong = ndb.StringProperty(repeated=True)

class hardGeography(ndb.Model):
    geo_h_question = ndb.StringProperty(required=True)
    geo_h_correct = ndb.StringProperty(required=True)
    geo_h_wrong = ndb.StringProperty(repeated=True)

class timeData(ndb.Model):
   time = ndb.StringProperty(required=True)

class pointsData(ndb.Model):
    points = ndb.StringProperty(required=True)

# questions_stuff = ndb.Query(questionData)
