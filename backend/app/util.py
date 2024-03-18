from flask import Flask
from werkzeug.routing import BaseConverter, ValidationError
import base64

class Base32Converter(BaseConverter):
    def to_python(self, value):
        try:
            return base64.b32decode(value.upper()).decode()
        except Exception:
            raise ValidationError()

    def to_url(self, value):
        return base64.b32encode(value.encode()).decode()