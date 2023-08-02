from fireo.models import Model
from fireo.fields import TextField, IDField, BooleanField


class UserModel(Model):
    handle = TextField(required=True)
    handle_lowercase = TextField(required=True)
