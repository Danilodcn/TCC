from tinymongo import TinyMongoClient

def configure_db():
    conn = TinyMongoClient()
    db = conn.my_database
    return db

def configure(app):
    app.db = configure_db()

def api(app_or_blueprint, name=None):

    def decorator(func):

        nonlocal name

        if name is None:
            name = func.__name__

        parser = Parser(func)

        @app_or_blueprint.route('/{}'.format(name), methods=['POST'], endpoint=name)
        @functools.wraps(func)
        def new_func():
            kwargs = parser.parse_kwargs()
            returned = func(**kwargs)
            return jsonify({'result': returned})
        return new_func
    return decorator
