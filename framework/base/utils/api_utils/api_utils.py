import requests
from framework.base.config_class import Config
from framework.base.utils.api_utils.request_type import RequestType
from framework.base.utils.json_utils import JSONutils
from framework.base.utils.api_utils.status_code import StatusCode


class APIutils:
    def __init__(self, url, request_type: RequestType, data=None, files=None):
        if files is not None:
            self.url = url
        else:
            self.url = Config().get_vk_api_url() + url
        self.response = self.send_request(request_type=request_type, data=data, files=files)

    def send_request(self, request_type: RequestType, data=None, files=None):
        if request_type == RequestType.GET:
            return requests.get(self.url)
        elif request_type == RequestType.POST:
            return requests.post(self.url, data=data, files=files)
        elif request_type == RequestType.PUT:
            return requests.put(self.url, data=data)
        elif request_type == RequestType.DELETE:
            return requests.delete(self.url)
        else:
            pass

    def check_status(self, status=StatusCode.SUCCESS):
        return self.response.status_code == status

    def get_request_text(self):
        return self.response.text

    def get_json_result(self):
        result_list = JSONutils.json_to_list(self.get_request_text())
        return result_list

    def sort_values(self, parameter: str, reverse_order=False):
        result_list = self.get_json_result()
        sorted_result = JSONutils.sort_by_key(result_list, parameter,
                                              reverse_order=reverse_order)
        return sorted_result

    def get_values(self):
        result_dict = self.get_json_result()
        return result_dict
