import os
import subprocess
import time
from pathlib import Path

import connexion
import psycopg2
from flask_testing import TestCase

from server import db
from server.test import integration

APP_RUNNING = None


def remove_docker_db():
    cmd_command = "docker kill db_cervejas_testes"
    process = subprocess.Popen(cmd_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output)
    print(error)


def run_docker_db():
    remove_docker_db()
    cmd_command = "docker run --rm --name db_cervejas_testes -p 5432:5432 -e POSTGRES_PASSWORD=1234 -d postgres"
    process = subprocess.Popen(cmd_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output)
    print(error)


def aguardar_postgres(tentativa=1):
    if tentativa > 10:
        raise Exception('Numero de tentativas ao conectar com o banco excedidas')

    print(f'Aguardando o banco de dados com a tentativa de número: {tentativa}')

    conn = None
    cur = None
    try:
        conn = psycopg2.connect('postgresql://postgres:1234@localhost:5432/postgres')
        cur = conn.cursor()

        cur.execute("select 1")
        resultado = cur.fetchone()
        if resultado[0] != 1:
            raise Exception('Resultado do select incorreto')
    except Exception:
        time.sleep(1)
        aguardar_postgres(tentativa + 1)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


def aplicar_migrations():
    full_path = os.path.abspath(__file__)
    cwd = Path(full_path).parents[3]
    cmd_command = "alembic upgrade head"
    process = subprocess.Popen(cmd_command.split(), stdout=subprocess.PIPE, cwd=cwd)
    output, error = process.communicate()
    print(output)
    print(error)


class BaseIntegrationTest(TestCase):
    headers_default = {
        'content-type': 'application/json'
    }

    def create_app(self):
        if integration.APP_RUNNING:
            print('Usou o app já criado')
            return integration.APP_RUNNING

        app = connexion.App(__name__, specification_dir='../../swagger/')
        app.add_api('swagger.yaml')
        app.app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:1234@localhost:5432/postgres'
        app.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.app.config["SQLALCHEMY_ECHO"] = True

        db.init_app(app.app)

        integration.APP_RUNNING = app.app
        print('Criou o app uma única vez')
        return app.app

    @classmethod
    def setUpClass(cls) -> None:
        run_docker_db()
        aguardar_postgres()
        aplicar_migrations()

    @classmethod
    def tearDownClass(cls) -> None:
        remove_docker_db()
