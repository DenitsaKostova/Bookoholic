import urllib.request
from goodread.goodreads_parser import GoodReadsParser


class GoodReadsClient():

    BASE_URL = "http://www.goodreads.com/"
    DEFAULT_PAGE_SIZE = 20

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        self.parser = GoodReadsParser()

    def get_resource(self, base_url, query_params):
        if "key" not in query_params:
            query_params["key"] = self.key
        if "per_page" not in query_params:
            query_params["per_page"] = self.DEFAULT_PAGE_SIZE

        params = []

        for key, value in query_params.items():
            if value is not None:
                params.append("{}={}".format(key, value))
        url = "{}?{}".format(base_url, "&".join(params))

        url_handler = urllib.request.urlopen(url)
        return url_handler

    def parse_result(self, url_handler):
        return self.parser.parse_result(url_handler)

    def get_shelf(self, user_id, shelf_name):
        url = "{}review/list.xml".format(self.BASE_URL)
        query_params = {
            "id": user_id,
            "shelf": shelf_name,
            "v": 2,
        }

        url_handler = self.get_resource(url, query_params)

        return self.parser.parse_books(url_handler)
