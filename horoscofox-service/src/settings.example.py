DEV_SERVER_ADDR = '0.0.0.0'
DEV_SERVER_PORT = 8000  # must be an integer
DEV_USE_DEBUGGER = True
DEV_USE_RELOADER = True


# If you use AWS DynamoDB
# AWS DynamoDB information
# arn:aws:dynamodb:<region>:<identifier>:table/Horoscofox
# <Region>
# Primary partition key : sign (String)
# Primary sort key: date_start (String)
DYNAMODB_TABLE_NAME = 'Horoscofox'  # use an existing table or create it
