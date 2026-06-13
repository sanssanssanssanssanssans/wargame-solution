import requests

class Client:
    def __init__(self, base_url):
        self.base = base_url
        self.s = requests.Session()

    def get(self, path):
        return self.s.get(self.base + path)

    def post(self, path, data=None):
        return self.s.post(self.base + path, data=data)

    def put(self, path, data=None, headers=None):
        return self.s.put(self.base + path, data=data, headers=headers)

    def request(self, method, path, **kwargs):
        return self.s.request(method, self.base + path, **kwargs)