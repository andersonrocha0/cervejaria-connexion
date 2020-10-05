import connexion
from flask_testing import TestCase


class TestKeepAliveApi(TestCase):

    def create_app(self):
        app = connexion.App(__name__, specification_dir='../../swagger/')
        app.add_api('swagger.yaml')
        return app.app

    def test_api_keep_alive(self):
        response = self.client.open(
            "/ping",
            method="GET",
        )
        self.assert200(response)

        retorno_da_request = response.json
        self.assertEqual("pong", retorno_da_request)
