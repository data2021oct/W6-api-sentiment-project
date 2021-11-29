from config.configuration import engine
import random
import sqltools as sqt
from flask import redirect

def personajes():
    """
    hace una selección los nombres de personajes en la tabla characters de mysql
    """
    query = list(engine.execute("SELECT distinct(nombre) FROM friends.characters;"))
    return [q[0] for q in query]

def random_season(season):
    """
    recibe un numero de temporada de friends (Entre el 1 y el 10)
    devuelve una frase random de esa temporada indicando qué personaje la dice y el título del episodio.
    """
    try:
        idepisodes = list(engine.execute(f"SELECT idEpisodio FROM episodios where idTemporadas = {season};"))
        idep = random.choice(idepisodes)[0]
        epi = list(engine.execute(f"SELECT tituloEp FROM episodios where idEpisodio = {idep};"))[0][0]
        que = list(engine.execute(f"SELECT texto, idcharacters FROM quotes WHERE idEpisodio ={idep};"))
        line_ch = random.choice(que)
        char = list(engine.execute(f"SELECT nombre FROM characters WHERE idcharacters = {line_ch[1]};"))[0][0]
        line = line_ch[0]
        
        return f"in episdode '{epi}', from season {season} {char} says '{line}'"
    except:
        return "Friends tiene 10 temporadas, elige un número del 1 al 10"
    
def insertusuario(nombre):
    """º
    recibe el nombre de un nuevo usuario 
    inserta el usuario en su tabla correspondiente.
    """
    try:
        if sqt.check("usuario", nombre):
            return "choose another user name, this one is taken"
        else:
            engine.execute(f"INSERT INTO usuario (nombre) VALUES ('{nombre}');")
            return f"your username is {nombre}"
    except:
        return "fallo garrafal"


# def newline(temp, epi, charac, line):
#     """
#     recibe temporada, episodio, nombre de presonaje y frase qué ha dicho
#     la inserta en las tablas de mysql.

#     """
#     try:
#         sqt.insertTemp("season",temp)
#         sqt.insertCar("character",charac)
#         sqt.insertEp("episode_title",epi)
#         sqt.insertquote("quote",line,epi,charac)
#         return "inserted"
#     except:
#         return "fallo garrafal"

# def newline(temp, epi, charac, line):
#     try:
    
#         sqt.insertTemp("season",temp)
#         sqt.insertCar("character",charac)
#         sqt.insertEp("episode_title",epi)
#         sqt.insertquote("quote",line,epi,charac)
#         return "inserted"
    
#     except:
#         return "fallo garrafal"
        
        

def random_quote(character):
    """
    hace una seleccion del id de un personaje que se pide
    te devuelve una frase random de ese personaje
    también devuelve el nombre del episodio y la temporada en la que sale
    """
    try: 
        idchar = list(engine.execute(f"SELECT idcharacters FROM characters WHERE nombre ='{character}';"))[0][0]
        que = list(engine.execute(f"SELECT texto,idEpisodio FROM quotes WHERE idcharacters ='{idchar}';"))
        frase = random.choice(que)[0]
        idep = random.choice(que)[1]
        episode = list(engine.execute(f"SELECT tituloEp FROM episodios WHERE idEpisodio ={idep};"))
        temp = list(engine.execute(f"SELECT idTemporadas FROM episodios WHERE idEpisodio ={idep};"))
        tot = f"{character} says: '{frase}' in episode '{episode[0][0]}' from season {temp[0][0]}"
        dic = {"character": character, "line": frase, "episode": episode[0][0], "season" : temp[0][0]}
        return dic
    except:
        return redirect("http://127.0.0.1:5000/personajes")
        
        
    

    
