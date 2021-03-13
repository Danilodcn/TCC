from unittest import TestCase
from flask import Flask, url_for
try:
    from server.bp_api import create_bp
except:
    None


class TesteBlueprint(TestCase):
    def setUp(self) -> None:
        self.rota = "/"
        self.app = Flask(__name__)
        self.app.register_blueprint(create_bp(self.rota))

        self.app.context = self.app.test_request_context()
        self.app.context.push()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_root_return_200(self):
        rotas = list(self.app.url_map.iter_rules())
        retornos = []
        for endpoint in [rotas[i].endpoint for i in range(len(rotas)-1)]:
            print(endpoint)
            result = self.client.get(url_for(endpoint))
            self.assertEqual(200, result.status_code, f"A rota {endpoint} deveria retornar 200 mas retorna {result.status_code}")





