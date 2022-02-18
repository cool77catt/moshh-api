from flask_restful import Resource

class Search(Resource):
    def get(self):
        return {
            'users': [],
            'tags': [],
        }