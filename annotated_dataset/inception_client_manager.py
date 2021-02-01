from pycaprio import Pycaprio


class InceptionClientManager:
    def __init__(self):
        # Todo load config from file
        self.config = {
            'mapa': {
                'inception_host': 'https://mapa.pangeamt.com/',
                'username': 'API',
                'password': 'api314'}
        }

    def create_client(self, name):
        return Pycaprio(
            inception_host=self.config[name]['inception_host'],
            authentication=(
                self.config[name]['username'],
                self.config[name]['password'])
        )
