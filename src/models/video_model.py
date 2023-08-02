from fireo.models import Model
from fireo.fields import TextField, IDField


class VideoModel(Model):
    artist_id = TextField(required=True)
    event_id = TextField(required=True)
    track = TextField(required=True)
    description = TextField(required=True)
    storage_id = TextField(required=True)
