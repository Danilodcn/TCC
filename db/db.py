from tinymongo import TinyMongoClient

def configure_db():
    conn = TinyMongoClient("teste")
    db = conn.db
    return db

def configure_app(app):
    app.db = configure_db()
