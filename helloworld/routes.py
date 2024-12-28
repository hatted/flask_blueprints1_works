from flask import Blueprint
helloworld = Blueprint('helloworld', __name__)


@helloworld.route('/')
def index():
    return 'helloworld'
