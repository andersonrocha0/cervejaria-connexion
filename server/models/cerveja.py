from dataclasses import dataclass

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
