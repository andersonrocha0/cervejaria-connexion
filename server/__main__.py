import connexion

from server import db


def start_server():
    app = connexion.App(__name__, specification_dir='swagger/')
    app.add_api('swagger.yaml')

    app.app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:1234@localhost:5432/postgres'
    app.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.app.config["SQLALCHEMY_ECHO"] = True
    app.app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {'pool_pre_ping': True}

    db.init_app(app.app)

    app.run(port=8080)


if __name__ == '__main__':
    start_server()
