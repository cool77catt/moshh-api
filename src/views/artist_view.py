from flask_restful import Resource
from flask import request
from models.artist_model import ArtistModel
from fireo.utils import utils as fireo_utils
from utils.fireo import fireo_model_to_response
from utils import view_helpers


class ArtistView(Resource):

    def _get_artist_by_id(self, artist_id):
        key = fireo_utils.generateKeyFromId(ArtistModel, artist_id)
        return ArtistModel.collection.get(key)

    def _get_artist_by_name(self, artist_name):
        lower_name = artist_name.lower()
        return ArtistModel.collection.filter('name_lowercase', '==', lower_name).get()

    def get(self, artist_id=None):
        results = []
        if not artist_id:
            results = [
                fireo_model_to_response(a)
                for a in ArtistModel.collection.fetch()
            ]
        else:
            artist = self._get_artist_by_id(artist_id)
            if not artist:
                return view_helpers.return_error('artist not found')
            results = [fireo_model_to_response(artist)]

        return (results, 200)

    def post(self):
        status = True
        req_body = request.json
        artist_name = req_body['name']

        existing_artist = self._get_artist_by_name(artist_name)
        if existing_artist:
            return view_helpers.return_success_with_message('artist already exists')

        # Create the artist
        artist = ArtistModel()
        artist.name = artist_name
        artist.name_lowercase = artist_name.lower()
        artist.save()

        return {
            'status': status,
        }
