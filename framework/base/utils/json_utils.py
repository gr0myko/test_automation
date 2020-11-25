import json


class JSONutils:
    @staticmethod
    def sort_by_key(elements_list: list, key: str, reverse_order=None):
        sorted_result = sorted(elements_list, key=lambda i: i[key],
                               reverse=reverse_order)
        return sorted_result

    @staticmethod
    def string_output(elements_list: list, spaces_num=4):
        json_string = json.dumps(elements_list, indent=spaces_num)
        return json_string

    @staticmethod
    def json_to_list(json_text: str):
        result_list = json.loads(json_text)
        return result_list
