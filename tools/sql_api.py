from config.configuration import engine

def personajes():
    query = list(engine.execute("SELECT distinct(nombre) FROM friends.characters;"))
    lista =  [{"nombre": elemento[0]} for elemento in query]
    # return [q[0] for q in query]
    return lista