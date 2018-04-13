from mongoengine import connect
from settings import MONGO_CONNECTION_HOST, MONGO_CONNECTION_NAME

connect(MONGO_CONNECTION_NAME, host=MONGO_CONNECTION_HOST)
