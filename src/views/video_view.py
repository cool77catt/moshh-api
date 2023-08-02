from flask_restful import Resource
from flask import request
from models.video_model import VideoModel
from utils.fireo import fireo_model_to_response
from utils import view_helpers


class VideoView(Resource):

    def get(self):
        return {
            'users': [],
            'tags': [],
        }

    def post(self):
        req_body = request.json

        # Check if video exists
        storage_id = req_body['storage_id']
        video = VideoModel.collection.filter(
            'storage_id', '==', storage_id
        ).get()
        if video:
            return view_helpers.return_success_with_message('artist already exists')

        # Save the video
        video = VideoModel()
        video.artist_id = req_body['artist_id']
        video.event_id = req_body['event_id']
        video.track = req_body['track']
        video.description = req_body['description']
        video.storage_id = req_body['storage_id']
        video.save()

        return (fireo_model_to_response(video), 200)
