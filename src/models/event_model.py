from fireo.models import Model
from fireo.fields import TextField, GeoPoint, DateTime


class EventModel(Model):
    name = TextField(required=True)
    location = TextField(required=True)
    datetime = DateTime(required=True)
    geo_point = GeoPoint()
