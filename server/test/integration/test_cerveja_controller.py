import json

from server.test.integration import BaseIntegrationTest


class TestCervejaApi(BaseIntegrationTest):

    def test_criar_cerveja(self):
        response = self.client.open(
            "/cervejas",
            method="POST",
            headers=self.headers_default,
            data=json.dumps({
                "nome": "Brooklyn East IPA",
                "estilo": "IPA",
                "teor_alcoolico": 6.8
            })
        )
        self.assertStatus(response, 201)

        response = self.client.open(
            "/cervejas",
            method="GET",
            headers=self.headers_default,
        )

        self.assert200(response)

        cervejas = response.json
        self.assertTrue(len(cervejas) == 1)

        cerveja1 = cervejas[0]

        self.assertTrue(cerveja1['estilo'] == 'IPA')
        self.assertTrue(cerveja1['teor_alcoolico'] == 6.8)

    def test_criar_cerveja_bad_request(self):
        response = self.client.open(
            "/cervejas",
            method="POST",
            headers=self.headers_default,
            data=json.dumps({
                "nome": "Brooklyn East IPA",
                "estilo": "IPA",
                "teor_alcoolico": "6.8"
            })
        )
        self.assertStatus(response, 400)
