import ffmpeg_streaming
from ffmpeg_streaming import GCS, CloudManager, Formats, Bitrate, Representation, Size
import os
from .gcp import GCPManager


class VideoProcessor():

    _360p = Representation(Size(640, 360), Bitrate(276 * 1024, 128 * 1024))
    _480p = Representation(Size(854, 480), Bitrate(750 * 1024, 192 * 1024))
    _720p = Representation(Size(1280, 720), Bitrate(2048 * 1024, 320 * 1024))

    _representations = [_360p, _480p]

    @staticmethod
    def get_tmp_path(user_id, video_name):
        return f'videos/tmp/{user_id}/{video_name}'

    @staticmethod
    def get_library_path(user_id, video_name):
        return f'videos/library/{user_id}/{video_name.strip(".mp4")}'

    @staticmethod
    def get_hls_path(user_id, video_name):
        return f'{VideoProcessor.get_library_path(user_id, video_name)}/hls'

    def __init__(self):
        self._gcs = GCS()

    def convert_mp4_to_hls(self, input_path, output_dir_path):
        video = ffmpeg_streaming.input(input_path)
        output_path = os.path.join(output_dir_path, 'hls.m3u8')
        hls = video.hls(Formats.h264())
        hls.representations(*self._representations)
        hls.output(output_path)
        return True

    def convert_mp4_to_hls_gcp(self, user_id, video_name):
        # Setup save location
        save_to_gcs = CloudManager().add(
            self._gcs,
            bucket_name=GCPManager.APP_BUCKET,
            folder=self.get_hls_path(user_id, video_name)
        )

        # Get the input
        video = ffmpeg_streaming.input(
            self._gcs,
            bucket_name=GCPManager.APP_BUCKET,
            object_name=self.get_tmp_path(user_id, video_name)
        )

        # Generate the representations
        hls = video.hls(Formats.h264())
        hls.representations(self._360p, self._480p, self._720p)
        hls.output(clouds=save_to_gcs)
