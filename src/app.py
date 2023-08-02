import os
from flask import Flask
from flask_restful import Resource, Api
from views import UserView, EventView, SearchView, VideoView, ArtistView
import settings


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')
api.add_resource(UserView, '/user', '/user/<string:user_id>')
api.add_resource(EventView, '/event')
api.add_resource(SearchView, '/search')
api.add_resource(VideoView, '/video')
api.add_resource(ArtistView, '/artist', '/artist/<string:artist_id>')


if __name__ == '__main__':
    app.run(debug=True)
