from typing import List

from server import cervejas
from server.models.cerveja import Cerveja


def find_all_cervejas() -> List[Cerveja]:
    return cervejas
