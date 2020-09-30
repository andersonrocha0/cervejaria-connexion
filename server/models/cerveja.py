from dataclasses import dataclass
from typing import List

from sqlalchemy import Column, Integer, String, Numeric

from server import db


@dataclass
class Cerveja:
    id: int = None
    estilo: str = None
    nome: str = None
    teor_alcoolico: float = None


class CervejaEntity(db.Model):
    __tablename__ = 'tb_cerveja'

    id = Column(Integer, primary_key=True)
    estilo = Column(String)
    nome = Column(String)
    teor_alcoolico = Column(Numeric)


def converte_cerveja_entity_para_cerveja(cerveja_entity: CervejaEntity) -> Cerveja:
    cerveja = Cerveja(
        id=cerveja_entity.id,
        estilo=cerveja_entity.estilo,
        nome=cerveja_entity.nome,
        teor_alcoolico=cerveja_entity.teor_alcoolico
    )

    return cerveja


def converte_cervejas_entity_para_cervejas(cervejas_entities: List[CervejaEntity]) -> List[Cerveja]:
    return [converte_cerveja_entity_para_cerveja(c) for c in cervejas_entities]
