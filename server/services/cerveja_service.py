from server import Cerveja, cervejas


def get_cerveja_entre_min_max(cerveja: Cerveja, teor_min, teor_max):
    if teor_min <= cerveja.teor_alcoolico <= teor_max:
        return True


def get_cervejas(teor_alcoolico_min=None, teor_alcoolico_max=None):
    cervejas_para_retornar = cervejas
    if teor_alcoolico_min is not None and teor_alcoolico_max is not None:
        cervejas_para_retornar = list(
            filter(lambda cerveja: get_cerveja_entre_min_max(cerveja, teor_alcoolico_min, teor_alcoolico_max),
                   cervejas))

    return cervejas_para_retornar


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
    return max([c.id for c in cervejas]) + 1 if len(cervejas) > 0 else 1


def get_cerveja(id_cerveja):
    cerveja = next(filter(lambda x: x.id == id_cerveja, cervejas), None)
    return cerveja


def delete_cerveja(id_cerveja):
    i = 0
    remover = False
    for cerveja in cervejas:
        if id_cerveja == cerveja.id:
            remover = True
            break
        i = i + 1

    if remover:
        del cervejas[i]


def put_cerveja(id_cerveja, cerveja_input):
    cerveja = get_cerveja(id_cerveja)
    if cerveja is None:
        return None

    cerveja.estilo = cerveja_input['estilo']
    cerveja.nome = cerveja_input['nome']
    cerveja.teor_alcoolico = cerveja_input['teor_alcoolico']

    return cerveja
