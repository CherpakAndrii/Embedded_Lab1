from marshmallow import Schema, fields
from src.schema.accelerometer_schema import AccelerometerSchema
from src.schema.location_schema import GpsSchema
from src.domain.aggregated_data import AggregatedData


class AggregatedDataSchema(Schema):
    accelerometer = fields.Nested(AccelerometerSchema)
    gps = fields.Nested(GpsSchema)
    time = fields.DateTime('iso')
