class Post(object):
    def __init__(self, *initial_data):
        for dictionary in initial_data:
            for key in dictionary:
                if key == 'userId':
                    setattr(self, key, int(dictionary[key]))
                else:
                    setattr(self, key, dictionary[key])

    def __eq__(self, other):
        if not isinstance(other, Post):
            return NotImplemented

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)

    def get_value(self, key):
        return self.__getattribute__(key)

    def is_empty(self):
        if self.__dict__ == {}:
            return True
        else:
            return False
