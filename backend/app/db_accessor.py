import pymongo
from django.conf import settings

client = pymongo.MongoClient(
    host=settings.MONGO_HOST,
    port=settings.MONGO_PORT,
    username=settings.MONGO_USERNAME,
    password=settings.MONGO_PASSWORD,
)

db = client[settings.MONGO_DATABASE_NAME]
quizzes_collection = db["quizzes"]

'''
This class lists down database accessor methods
to interact with mongo db using pymongo.
We are not using django's ORM model here.
'''

'''
 Get all quizzes from db
'''
def get_all_quizzes():
    pass


'''
Get a quiz by its id
'''
def get_quiz_by_id(quiz_id):
    pass


'''
Create a quiz in db
'''
def create_quiz(quiz_data):
    pass


'''
Delete a quiz
'''
def delete_quiz(quiz_id):
    pass
