import pandas as pd
import sqlalchemy as alch
from getpass import getpass
#from config.configuration import engine



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
    
    elif col == "quote":
        query = list(engine.execute(f"SELECT texto FROM quotes WHERE texto = '{value}'"))
        if len(query) > 0:
            return True
        else:
            return False
    
    elif col == "usuario":
        query = list(engine.execute(f"SELECT nombre FROM usuario WHERE nombre = '{value}'"))
        if len(query) > 0:
            return True
        else:
            return False
        
        
        
        
        
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
        return list(engine.execute(f"SELECT idEpisodio FROM episodios WHERE tituloEp ='{value}';"))[0][0]
    
    
def insertquote(col,value,col2,col3):
    """
    col2 = episode_title
    col3 = character
    """
    if check(col, value):
        return "quote exists"
    else:
        
        idEpisodio = dameId("episode_title",col2)
        idcharacters = dameId("character",col3)
         
        engine.execute(f"INSERT INTO quotes (texto,idEpisodio,idcharacters) VALUES ('{value}',{idEpisodio},{idcharacters});")
        
        
def insertaciones(df,col1,col2,col3,col4,col5):
    """
    col1 = season
    col2 = character
    col3 = episode_title
    col4 = quote
    col5 = episode_number
    """

    for i,r in df.iterrows():
        try:
            insertTemp(col1,r[col1])
            
            insertCar(col2,r[col2])

            insertEp(col3,r[col3],r[col5],r[col1])

            insertquote(col4,r[col4],r[col3],r[col2])
        except:
  
            return f"{i},{Exception}"
            
        
        
#texto,idEpisodio,idcharacters