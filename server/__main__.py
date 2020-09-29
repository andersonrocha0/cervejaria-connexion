import connexion


def start_server():
    app = connexion.App(__name__, specification_dir='swagger/')
    app.add_api('swagger.yaml')
    app.run(port=8080)


if __name__ == '__main__':
    start_server()
