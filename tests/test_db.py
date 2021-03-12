import sys, os
sys.path.append(os.getcwd())
from unittest import TestCase
from Trafo import tabelas


class TesteTabelas(TestCase):
    def test_se_existe_json_dentro_da_pasta(self):
        self.assertIsInstance(tabelas.file, dict, "O arquivo não é um json válido")
