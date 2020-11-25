class User:
    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented

        return self.__dict__ == other.__dict__

    def get_value(self, key):
        return self.__getattribute__(key)

    @staticmethod
    def get_user_from_list(users_list, user_id):
        user = list(filter(lambda i: i.get_value('id') == user_id,
                           users_list))[0]
        return user
