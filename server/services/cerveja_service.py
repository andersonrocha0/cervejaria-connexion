from server import Cerveja, cervejas
from server.repositories import cerveja_repository


def get_cervejas():
    return cerveja_repository.find_all_cervejas()


def post_cerveja(cerveja_input):
    cerveja = Cerveja(
        estilo=cerveja_input['estilo'],
        nome=cerveja_input['nome'],
        teor_alcoolico=cerveja_input['teor_alcoolico'],
        id=get_max_id_mais_um()
    )
    cervejas.append(cerveja)
    return cerveja


def get_max_id_mais_um() -> int:
    return max([c.id for c in cervejas]) + 1
