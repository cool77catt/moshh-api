from flask_restful import Resource
from flask import request
from models.user_model import UserModel
from fireo.utils import utils as fireo_utils
from utils.fireo import fireo_model_to_response
import constants


class UserView(Resource):

    def _get_user(self, user_id):
        key = fireo_utils.generateKeyFromId(UserModel, user_id)
        return UserModel.collection.get(key)

    def get(self, user_id):
        user = self._get_user(user_id)
        if user:
            return fireo_model_to_response(user), 200
        return ({constants.RESPONSE_MSG_KEY: 'user doesnt exist.'}, 400)

    def post(self, user_id):
        user = self._get_user(user_id)
        if not user:
            req_body = request.json
            handle = req_body['handle']
            handle_lowercase = handle.lower()

            # Make sure handle doesn't exist
            existing_user = UserModel.collection.filter(
                'handle_lowercase', '==', handle_lowercase
                ).get()
            if existing_user:
                return (
                    {constants.RESPONSE_MSG_KEY: 'handle already exists.'},
                    400
                    )

            # Handle is available, create the user
            user = UserModel()
            user.id = user_id
            user.handle = handle
            user.handle_lowercase = handle_lowercase
            user.save()

        return fireo_model_to_response(user), 200
