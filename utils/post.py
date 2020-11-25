class Post(object):
    def __init__(self, *initial_data):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])

    def get_value(self, key):
        return self.__getattribute__(key)

    def is_value_empty(self, value):
        if self.get_value(value) == '':
            return True
        else:
            return False

    def add_attribute(self, key, value):
        setattr(self, key, value)
