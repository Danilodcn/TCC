import sys, os
sys.path.append(os.getcwd())

import app
from unittest import TestCase


class TesteApp(TestCase):
    def test_se_create_app_existe(self):
        self.assertIn("create_app", dir(app), "A função 'create_app' não foi criada")

    def test_create_app_chamavel(self):
        self.assertIn("__call__", dir(app.create_app))
