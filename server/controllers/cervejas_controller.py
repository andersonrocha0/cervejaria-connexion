from server.services import cerveja_service


def get_cervejas():
    return cerveja_service.get_cervejas(), 200


def post_cerveja(cerveja_input):
    return cerveja_service.post_cerveja(cerveja_input), 201
