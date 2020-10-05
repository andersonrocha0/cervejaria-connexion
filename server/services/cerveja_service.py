from server.models.cerveja import Cerveja, CervejaEntity
from server.repositories import cerveja_repository


def get_cerveja_entre_min_max(cerveja: Cerveja, teor_min, teor_max):
    if teor_min <= cerveja.teor_alcoolico <= teor_max:
        return True


def get_cervejas(teor_alcoolico_min=None, teor_alcoolico_max=None):
    cervejas_para_retornar = cerveja_repository.find_all_cervejas(teor_alcoolico_min, teor_alcoolico_max)
    return cervejas_para_retornar


def post_cerveja(cerveja_input):
    cerveja_entity = CervejaEntity()
    cerveja_entity.estilo = cerveja_input['estilo']
    cerveja_entity.nome = cerveja_input['nome']
    cerveja_entity.teor_alcoolico = cerveja_input['teor_alcoolico']

    return cerveja_repository.save_obj(cerveja_entity)


def get_cerveja(id_cerveja):
    cerveja = cerveja_repository.get_obj_by_id(CervejaEntity, id_cerveja)
    return cerveja


def delete_cerveja(id_cerveja):
    cerveja_repository.remove_obj_by_id(CervejaEntity, id_cerveja)


def put_cerveja(id_cerveja, cerveja_input):
    cerveja_entity = cerveja_repository.get_entity_by_id(CervejaEntity, id_cerveja)
    if cerveja_entity is None:
        return None

    cerveja_entity.estilo = cerveja_input['estilo']
    cerveja_entity.nome = cerveja_input['nome']
    cerveja_entity.teor_alcoolico = cerveja_input['teor_alcoolico']

    cerveja = cerveja_repository.save_obj(cerveja_entity)

    return cerveja
