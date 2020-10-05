from unittest import TestCase

from server.utils import utils


class TestUtils(TestCase):

    def test_teor_alcoolico_valores_invalidos(self):
        retorno_0 = utils.valida_teor_alcoolico(0)
        self.assertFalse(retorno_0)

        retorno_100 = utils.valida_teor_alcoolico(100)
        self.assertFalse(retorno_100)

        retorno_menos_1 = utils.valida_teor_alcoolico(-1)
        self.assertFalse(retorno_menos_1)

        retorno_101 = utils.valida_teor_alcoolico(101)
        self.assertFalse(retorno_101)

    def test_teor_alcoolico_valores_validos(self):
        for i in range(1, 99):
            retorno = utils.valida_teor_alcoolico(i)
            self.assertTrue(retorno)

    def test_teor_alcoolico_valores_validos_com_casas_decimais(self):
        for i in range(0, 99):
            retorno = utils.valida_teor_alcoolico(i + 0.99)
            self.assertTrue(retorno)
