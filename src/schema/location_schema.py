from marshmallow import Schema, fields
from src.domain.gps import Gps


class GpsSchema(Schema):
    longitude = fields.Number()
    latitude = fields.Number()
