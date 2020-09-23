import requests


class ApiWrapper(requests.Session):
    def __init__(self, baseurl, verify, token):
        super().__init__()

        self.headers.update({
            'Authorization': f'bearer {token}',
            'Content-type': 'application/json',
            'Accept': 'application/json'
        })

        self.baseurl = baseurl
        self.verify = verify

    def request(self, method, url, **kwargs):
        if '://' not in url:
            url = f'{self.baseurl}{url}'

        return super().request(method, url, **kwargs)
