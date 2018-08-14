import json


class Field:

    def __init__(self, initial_value=None):
        self.initial_value = initial_value

    def validate(self, value):
        return True


class StringField(Field):

    def __init__(self, initial_value=None, maximum_length=None):
        super().__init__(initial_value)

        self.maximum_length = maximum_length

    def validate(self, value):
        """ Check if this is a valid value for this field """
        if super().validate(value):
            return (value is None) or (isinstance(value, str) and self._validate_length(value))
        else:
            return False

    def _validate_length(self, value):
        """ Check if string has correct length """
        return (self.maximum_length is None) or (len(value) <= self.maximum_length)


class IntegerField(Field):
    def __init__(self, initial_value=None, maximum_value=None):
        super().__init__(initial_value)

        self.maximum_value = maximum_value

    def validate(self, value):
        """ Check if this is a valid value for this field """
        if super().validate(value):
            return (value is None) or (isinstance(value, int) and self._validate_value(value))
        else:
            return False

    def _validate_value(self, value):
        """ Check if integer falls in desired range """
        return (self.maximum_value is None) or (value <= self.maximum_value)


class AstrologerField(StringField):
    def __init__(self, initial_value=None, maximum_length=None, choices=None):
        super().__init__(initial_value, maximum_length)
        self.choices = choices

    def validate(self, value):
        """ Check if this is a valid value for this field """
        if super().validate(value):
            return self._validate_choices(value)
        else:
            return False

    def _validate_choices(self, code):
        """ Check if code is in choices """
        return (self.choices is None) or any([True if code in astrologer else False for astrologer in self.choices])


class ModelMeta(type):
    """ Metaclass of our own ORM """

    def __new__(self, name, bases, namespace):
        fields = {
            name: field
            for name, field in namespace.items()
            if isinstance(field, Field)
        }

        new_namespace = namespace.copy()

        # Remove fields from class variables
        for name in fields.keys():
            del new_namespace[name]

        new_namespace['_fields'] = fields

        return super().__new__(self, name, bases, new_namespace)


class Model(metaclass=ModelMeta):
    """ User interface for the base class """

    def __init__(self, json_input=None):
        for name, field in self._fields.items():
            setattr(self, name, field.initial_value)

        # If there is a JSON supplied, we'll parse it
        if json_input is not None:
            json_value = json.loads(json_input)

            if not isinstance(json_value, dict):
                raise RuntimeError("Supplied JSON must be a dictionary")

            for key, value in json_value.items():
                setattr(self, key, value)

    def __setattr__(self, key, value):
        """ Magic method setter """
        if key in self._fields:
            if self._fields[key].validate(value):
                super().__setattr__(key, value)
            else:
                raise AttributeError(
                    'Invalid value "{}" for field "{}"'.format(value, key))
        else:
            raise AttributeError('Unknown field "{}"'.format(key))

    def to_json(self):
        """ Convert given object to JSON """
        new_dictionary = {}

        for name in self._fields.keys():
            new_dictionary[name] = getattr(self, name)

        return json.dumps(new_dictionary)



# Read more about metaclasses on http://millionintegrals.com/post/metaclasses-in-python/
