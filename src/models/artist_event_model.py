from fireo.models import Model
from fireo.fields import IDField


class ArtistEventModel(Model):
    artist_uid = IDField(required=True)
    event_uid = IDField(required=True)
