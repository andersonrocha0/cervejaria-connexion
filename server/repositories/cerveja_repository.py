from typing import List

from server import db
from server.models.cerveja import Cerveja, CervejaEntity, converte_cervejas_entity_para_cervejas, \
    converte_cerveja_entity_para_cerveja


def find_all_cervejas(teor_alcoolico_min=None, teor_alcoolico_max=None) -> List[Cerveja]:
    query = CervejaEntity.query
    if teor_alcoolico_min is not None and teor_alcoolico_max is not None:
        query = CervejaEntity.query.filter(CervejaEntity.teor_alcoolico.between(teor_alcoolico_min, teor_alcoolico_max))

    cervejas_entities = query.all()
    return converte_cervejas_entity_para_cervejas(cervejas_entities)


def save_obj(cerveja_entity: CervejaEntity) -> Cerveja:
    db.session.add(cerveja_entity)
    db.session.commit()
    return converte_cerveja_entity_para_cerveja(cerveja_entity)


def remove_obj_by_id(clazz, id_objeto):
    objeto = get_entity_by_id(clazz, id_objeto)
    if objeto is not None:
        db.session.delete(objeto)
        db.session.commit()


def get_entity_by_id(clazz, id_objeto) -> CervejaEntity:
    entity = db.session.query(clazz).filter(clazz.id == id_objeto).first()
    return entity


def get_obj_by_id(clazz, id_objeto) -> Cerveja or None:
    entity = get_entity_by_id(clazz, id_objeto)
    if entity is None:
        return None
    objeto = converte_cerveja_entity_para_cerveja(entity)
    return objeto
