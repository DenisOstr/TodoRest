from flask import Flask
from app import apiBp
# from Model import db

def run(confFile):
    app = Flask(__name__)
    app.config.from_object(confFile)

    app.register_blueprint(apiBp, url_prefix = '/api')

    # db.init_app(app)

    return app


if __name__ == "__main__":
    app = run("config")
    app.run(debug = True)