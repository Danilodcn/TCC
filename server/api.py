from flask import current_app, jsonify, Response, request
from functools import wraps

class API(object):
    def __init__(self, app=None, root="/", api_json=True):
        self.api_json = api_json
        self.root = root
        self.app = app
        if self.app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app


    def __getattr__(self, item: str):
        if item.lower() in ["get", "post"]:
            # TODO: criar uma maneira de retornar apenas json
            #       nos retornos dos métodos

            return self.metodo(item)

        else:
            raise NotImplementedError("Esse método nao foi criado '{}'".format(item))


    def __trata_rotas(self, rota: str):
        rota = self.root + rota
        rota.replace("//", "/")
        return rota

    def jsonify(self, func):
        def wraper(*args, **kwargs):
            resposta = func(*args, *kwargs)
            if isinstance(resposta, dict):
                return jsonify(resposta)

            else:
                return jsonify({"result": resposta})
        #import ipdb; ipdb.set_trace()
        wraper.__name__ = func.__name__
        return wraper


    def metodo(self, tipo_requisicao:str):

        def requisicao(rota, *args, **kwargs):
            def clouse(func, rule=rota):

                def _new_func():
                    print
                    return "TEste bem sucedido"
                name = func.__name__
                #func = _new_func
                func.__name__ = name


                rule = self.__trata_rotas(rule)
                self.app.add_url_rule(
                    rule=rule,
                    view_func=func,
                    methods=[tipo_requisicao.upper()],
                    *args,
                    **kwargs
                )
                return func

            return clouse
        return requisicao

