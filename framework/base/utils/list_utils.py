import random


class ListUtils:
    @staticmethod
    def get_attr_list_from_elements(elements_list: list, attr: str):
        attr_list = [i.get_attribute(attr) for i in elements_list]
        return attr_list

    @staticmethod
    def get_random_elements(elements_list, number:int):
        random_list = random.choices(elements_list, k=number)
        return random_list
