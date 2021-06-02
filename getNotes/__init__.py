import logging
import azure.functions as func
import pymongo
import json
import os
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = os.environ['luterimongodbconnectionstring']
        client = pymongo.MongoClient(url)
        database = client['lutericosmosdb']
        collection = database['notes']

        result = collection.find({})
        result = dumps(result)
        
        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad getNotes request.", status_code=400)
