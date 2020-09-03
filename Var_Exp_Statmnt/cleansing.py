from pymongo import MongoClient, InsertOne, UpdateOne
import pprint
import dateparser
from bson.json_util import loads

# Replace XXXX with your connection URI from the Atlas UI
client = MongoClient('mongodb+srv://analytics:analytics-password@mflix.pccrc.mongodb.net/mflix?retryWrites=true&w=majority')
people_raw = client.cleansing['people-raw']

batch_size = 1000
inserts = []
count = 0

# There are over 50,000 lines, so this might take a while...
# Make sure to wait until the cell finishes executing before moving on (the * will turn into a number)
with open("people-raw.json") as dataset:
    for line in dataset:
        inserts.append(InsertOne(loads(line)))

        count += 1

        if count == batch_size:
            people_raw.bulk_write(inserts)
            inserts = []
            count = 0
if inserts:
    people_raw.bulk_write(inserts)
    count = 0

# Confirm that 50,474 documents are in your collection before moving on
people_raw.count()

# Replace YYYY with a query on the people-raw collection that will return a cursor with only
# documents where the birthday field is a string
people_with_string_birthdays = people_raw.find({"Birthday" : {"$type" : "string"}})

# This is the answer to verify you completed the lab
people_with_string_birthdays.count()