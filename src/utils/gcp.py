from google.cloud import storage


class GCPManager():

    APP_BUCKET = 'moshh-338102.appspot.com'

    _instance = None

    @staticmethod
    def instance():
        if not GCPManager._instance:
            GCPManager._instance = GCPManager()
        return GCPManager._instance

    def __init__(self):
        # Instantiates a client
        self._storage_client = storage.Client()

    def create_bucket(self, bucket_name):
        return self._storage_client.create_bucket(bucket_name)

    def get_bucket(self, bucket_name):
        return self._storage_client.get_bucket(bucket_name)
