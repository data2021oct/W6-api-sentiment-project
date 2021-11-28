from config.configuration import engine
import random
import sqltools as sqt

def personajes():
    query = list(engine.execute("SELECT distinct(nombre) FROM friends.characters;"))
    return [q[0] for q in query]


def random_quote(character):
    # try
    idchar = list(engine.execute(f"SELECT idcharacters FROM characters WHERE nombre ='{character}';"))[0][0]
    que = list(engine.execute(f"SELECT texto FROM quotes WHERE idcharacters ='{idchar}';"))
    return random.choice(que)

def random_season(season):
    idepisodes = list(engine.execute(f"SELECT idEpisodio FROM episodios where idTemporadas = {season};"))
    idep = random.choice(idepisodes)[0]
    epi = list(engine.execute(f"SELECT tituloEp FROM episodios where idEpisodio = {idep};"))[0][0]
    que = list(engine.execute(f"SELECT texto, idcharacters FROM quotes WHERE idEpisodio ={idep};"))
    line_ch = random.choice(que)
    char = list(engine.execute(f"SELECT nombre FROM characters WHERE idcharacters = {line_ch[1]};"))[0][0]
    line = line_ch[0]
    
    return f"in episdode '{epi}', from season {season} {char} says '{line}'"


def newline(temp, epi, charac, line):
    sqt.insertTemp("season",temp)
    sqt.insertCar("character",charac)
    sqt.insertEp("episode_title",epi)
    sqt.insertquote("quote",line,epi,charac)
    return "inserted"

def insertusuario(nombre):
    if sqt.check("usuario", nombre):
        return "choose another user name, this one is taken"
    else:
        engine.execute(f"INSERT INTO usuario (nombre) VALUES ('{nombre}');")
        return f"your username is {nombre}"
    
    
    

    
