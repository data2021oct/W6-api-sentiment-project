import pandas as pd
import sqlalchemy as alch
from getpass import getpass



import sqlalchemy as alch
import os
import dotenv


dotenv.load_dotenv()

passw = os.getenv("pass_sql")
dbName = "friends"
connectionData = f"mysql+pymysql://root:{passw}@localhost/{dbName}"
engine = alch.create_engine(connectionData)



def check(col,value):
    """
    recibe un nombre de columna y el contenido de una celda
    comprueba en las tablas correspondientes existe el valor que le pasamos
    """
    if col == "season":
        query = list(engine.execute(f"SELECT idTemporadas FROM temporadas WHERE idTemporadas = {value};"))
        if len(query) > 0:
            return True
        else:
            return False
        
    elif col == "character":
        query = list(engine.execute(f"SELECT nombre FROM characters WHERE nombre = '{value}';"))
        if len(query) > 0:
            return True
        else:
            return False
        
    elif col == "episode_title":
        query = list(engine.execute(f"SELECT tituloEp FROM episodios WHERE tituloEp = '{value}';"))
        if len(query) > 0:
            return True
        else:
            return False
    
    # elif col == "cancion":
    #     query = list(engine.execute(f"SELECT nombre FROM canciones WHERE nombre = '{value}'"))
    #     if len(query) > 0:
    #         return True
    #     else:
    #         return False
        
        
        
        
def insertTemp(col,value):
    """
    Llama a la función check para comprobar si existe el ironhacker
    Inserta ironhacker si no existe
    """
    if check(col, value):
        return "season exists"
    else:
        engine.execute(f"INSERT INTO temporadas (idTemporadas) VALUES ({value});")
        

def insertCar(col,value):
    """
    Llama a la función check para comprobar si existe el ironhacker
    Inserta ironhacker si no existe
    """
    if check(col, value):
        return "character exists"
    else:
        engine.execute(f"INSERT INTO characters (nombre) VALUES ('{value}');")
        

def insertEp(col,value,num,tempo):
    """
    Llama a la función check para comprobar si existe el ironhacker
    Inserta ironhacker si no existe
    """
    if check(col, value):
        return "epiosde exists"
    else:
        engine.execute(f"INSERT INTO episodios (numero,tituloEP,idTemporadas) VALUES ({num},'{value}',{tempo});")
        
def dameId(col,value):
    """
    Devuelve el ID de lo que le pidamos sabiendo que ese elemento EXISTE
    """
    if col == "character":
        return list(engine.execute(f"SELECT idcharacters FROM characters WHERE nombre ='{value}';"))[0][0]
    elif col == "episode_title":
        return list(engine.execute(f"SELECT idironhacker FROM ironhackers WHERE username ='{value}';"))[0][0]
    
    
def insertEp(col,value,num,tempo):
    """
    Llama a la función check para comprobar si existe el ironhacker
    Inserta ironhacker si no existe
    """
    if check(col, value):
        return "epiosde exists"
    else:
        engine.execute(f"INSERT INTO episodios (texto,idEpisodio,idcharacters) VALUES ({num},'{value}',{tempo});")
    
    
#texto,idEpisodio,idcharacters