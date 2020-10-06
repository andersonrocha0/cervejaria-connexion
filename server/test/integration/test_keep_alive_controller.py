from server.test.integration import BaseIntegrationTest


class TestKeepAliveApi(BaseIntegrationTest):

    def test_api_keep_alive(self):
        response = self.client.open(
            "/ping",
            method="GET",
        )
        self.assert200(response)

        retorno_da_request = response.json
        self.assertEqual("pong", retorno_da_request)
