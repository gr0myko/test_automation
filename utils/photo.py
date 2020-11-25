class Photo(object):
    def __init__(self, *initial_data):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])

    def get_value(self, key):
        return self.__getattribute__(key)