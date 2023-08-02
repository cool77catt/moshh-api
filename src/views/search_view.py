from flask_restful import Resource

class SearchView(Resource):
    def get(self):
        return {
            'users': [],
            'tags': [],
        }