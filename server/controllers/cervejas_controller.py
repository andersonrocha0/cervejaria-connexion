from server.services import cerveja_service


def get_cervejas(teor_alcoolico_min=None, teor_alcoolico_max=None):
    return cerveja_service.get_cervejas(teor_alcoolico_min, teor_alcoolico_max), 200


def post_cerveja(cerveja_input):
    return cerveja_service.post_cerveja(cerveja_input), 201


def get_cerveja(id_cerveja):
    cerveja = cerveja_service.get_cerveja(id_cerveja)
    return handle_cerveja(cerveja)


def handle_cerveja(cerveja):
    if cerveja is not None:
        return cerveja, 200
    else:
        return None, 404


def delete_cerveja(id_cerveja):
    return cerveja_service.delete_cerveja(id_cerveja), 204


def put_cerveja(id_cerveja, cerveja_input):
    cerveja = cerveja_service.put_cerveja(id_cerveja, cerveja_input)
    return handle_cerveja(cerveja)
