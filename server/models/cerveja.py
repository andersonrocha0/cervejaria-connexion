from dataclasses import dataclass


@dataclass
class Cerveja:
    id: int = None
    estilo: str = None
    nome: str = None
    teor_alcoolico: float = None
