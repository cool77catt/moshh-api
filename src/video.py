from flask_restful import Resource
from flask import request
import os
from utils.video_processor import VideoProcessor


class Video(Resource):

    def get(self):
        return {
            'users': [],
            'tags': [],
        }

    def post(self):
        body = request.json
        video_path = body.get('videoPath')

        hls_path = os.path.join(os.path.dirname(video_path), 'hls')
        video_output_dir_name = os.path.splitext(os.path.basename(video_path))[0]
        video_output_path = os.path.join(hls_path, video_output_dir_name)

        proc = VideoProcessor()
        status = proc.convert_mp4_to_hls(video_path, video_output_path)

        return {
            'outputPath': video_output_path,
            'status': status,
        }
