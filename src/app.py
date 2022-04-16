import os
from flask import Flask
from flask_restful import Resource, Api
import settings
from search import Search
from video import Video

# Set the GCP Environment Variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = \
    settings.GCP_CREDENTIALS_PATH


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')
api.add_resource(Search, '/search')
api.add_resource(Video, '/video')


# if __name__ == '__main__':
#     app.run(debug=True)
