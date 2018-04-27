DEV_SERVER_ADDR = '0.0.0.0'
DEV_SERVER_PORT = 8000  # must be an integer
DEV_USE_DEBUGGER = True
DEV_USE_RELOADER = True

MONGO_CONNECTION_NAME = 'myconnection'
MONGO_CONNECTION_HOST = 'mongodb://db1.example.net:27017,db2.example.net:2500/\
                        ?replicaSet=test'
MONGO_MOCKED_CONNECTION_HOST = 'mongomock://db1.example.net:27017,db2.example.net:2500/\
                        ?replicaSet=test'

# Read more about Mongo Connection
# https://docs.mongodb.com/manual/reference/connection-string/
