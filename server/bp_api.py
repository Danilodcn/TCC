from flask import Blueprint
from .api import API

def create_bp(root="/api"):
    bp = Blueprint("api", __name__)
    api = API(bp, root)

    @api.get("/")
    def home():
        return "Nao sei"

    return bp