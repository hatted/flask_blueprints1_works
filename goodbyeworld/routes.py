from flask import Blueprint
goodbyeworld = Blueprint('goodbyeworld', __name__)


@goodbyeworld.route('/')
def index():
    return 'goodbyeworld'
