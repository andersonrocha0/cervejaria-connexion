from flask_sqlalchemy import SQLAlchemy

# from server.models.cerveja import Cerveja

db = SQLAlchemy()

cervejas = []

# cervejas = [
#     Cerveja(estilo="IPA", nome="Brooklyn East IPA", teor_alcoolico=6.8, id=1),
#     Cerveja(estilo="Brown Ale", nome="Brooklyn Brown Ale", teor_alcoolico=5.6, id=2),
#     Cerveja(estilo="Belgian Dubbel", nome="Chimay Roug", teor_alcoolico=7, id=3),
#     Cerveja(estilo="German Weizene", nome="Paulaner Hefe Weiss", teor_alcoolico=5.5, id=4),
#     Cerveja(estilo="Belgian Blond Ale", nome="La Trappe Blon", teor_alcoolico=6.5, id=5),
#     Cerveja(estilo="Imperial India Pale Lager", nome="Bastards Piná a Vivá", teor_alcoolico=8.5, id=6),
#     Cerveja(estilo="Witibier", nome="La Trappe Witbier", teor_alcoolico=5.5, id=7),
#     Cerveja(estilo="Stout", nome="Guinness Special Export", teor_alcoolico=8, id=8),
#     Cerveja(estilo="Imperial Red Ale", nome="Dado Bier Imperial Red Ale", teor_alcoolico=9.5, id=9),
#     Cerveja(estilo="Vienna Lager", nome="Samuel Adams Boston Lager", teor_alcoolico=5.7, id=10),
#     Cerveja(estilo="Fruit Lambic", nome="Boon Framboise", teor_alcoolico=5, id=11),
# ]
