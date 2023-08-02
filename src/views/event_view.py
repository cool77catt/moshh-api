from flask_restful import Resource
from flask import request
import datetime as dt
from models.event_model import EventModel
from utils.fireo import fireo_model_to_response


class EventView(Resource):

    def get(self):
        results = []
        for e in EventModel.collection.fetch():
            e_dict = fireo_model_to_response(e)
            e_dict['datetime'] = str(e_dict['datetime'].date())
            results.append(e_dict)
        return (results, 200)

    def post(self):
        status = True
        req_body = request.json

        event_date = req_body.get('datetime', None)
        if event_date:
            event_date = dt.datetime.strptime(event_date, '%Y-%m-%d')
        else:
            event_date = dt.datetime.now()

        event = EventModel()
        event.name = req_body['name']
        event.location = req_body['location']
        event.datetime = event_date
        event.save()

        return {
            'status': status,
        }
