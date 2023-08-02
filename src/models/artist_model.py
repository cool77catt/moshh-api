from fireo.models import Model
from fireo.fields import TextField, IDField


class ArtistModel(Model):
    name = TextField(required=True)
    name_lowercase = TextField(required=True)
