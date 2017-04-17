# Helpers from tutorial:
# http://github.com/spchuang/DoubleDibz-tutorial/blob/master/flask_simple_authentication/app/common/helpers.py

from datetime import datetime, timedelta
from flask.json import JSONEncoder as BaseJSONEncoder
import os

def get_current_time():
    return datetime.utcnow()

def get_current_time_plus(days = 0, hours = 0, minutes = 0, seconds = 0):
    return get_current_time() + timedelta(days = days, hours = hours, minutes = minutes, seconds = seconds)

def make_dir(dir_path):
    try:
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
    except Exception, e:
        raise e

class JSONEncoder(BaseJSONEncoder):
    """Custom class which represents objects that include the JsonSerializer mixin."""
    
    def default(self, obj):
        if isinstance(obj, JsonSerializer):
            return obj.to_json()
        return super(JSONEncoder, self).default(obj)

class JsonSerializer(object):
    """Mixin that marks a SQLAlchemy model class that implements a to_json method."""
    
    __json_public__ = None
    __json_hidden__ = None
    __json_modifiers__ = None

    def get_field_names(self):
        for p in self.__mapper__.iterate_properties:
            yield p.key

    def to_json(self):
        field_names = self.get_field_names()

        public = self.__json_public__ or field_names
        hidden = self.__json_hidden__ or []
        modifiers = self.__json_modifiers__ or dict()

        rv = dict()
        for key in public:
            rv[key] = getattr(self,key)

        for key, modifier in modifiers.items():
            value = getattr(self,key)
            if isinstance(modifier, list):
                rv[modifier[0]] = modifier[1](value)
            else:
                rv[key] = modifier(value)

        for key in hidden:
            rv.pop(key, None)
        return rv
