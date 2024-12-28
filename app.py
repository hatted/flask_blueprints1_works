from flask import Flask
from goodbyeworld.routes import goodbyeworld
from helloworld.routes import helloworld

app = Flask(__name__)

# register apps
app.register_blueprint(goodbyeworld, url_prefix='/goodbyeworld')
app.register_blueprint(helloworld, url_prefix='/helloworld')


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)
