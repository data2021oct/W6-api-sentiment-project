from config.configuration import engine
import random

def personajes():
    query = list(engine.execute("SELECT distinct(nombre) FROM friends.characters;"))
    lista =  [{"nombre": elemento[0]} for elemento in query]
    return [q[0] for q in query]
    #return lista


def random_quote(character):
    idchar = list(engine.execute(f"SELECT idcharacters FROM characters WHERE nombre ='{character}';"))[0][0]
    que = list(engine.execute(f"SELECT texto FROM quotes WHERE idcharacters ='{idchar}';"))
    return random.choice(que)

def random_season(season):
    idepisode = list(engine.execute(f"SELECT idEpisodio FROM episodios where idTemporadas = {season};"))[0]
    randep = random.choice(idepisode)
    que = list(engine.execute(f"SELECT texto FROM quotes WHERE idEpisodio ={randep};"))
    
    return random.choice(que)
    
