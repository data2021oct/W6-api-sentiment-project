from flask import Flask, request
from flask import jsonify
import tools.sql_api as tsa
import tools.emotions as tem
import tools.sqltools as sqt




app = Flask(__name__)




@app.route("/")
def inicial():
    return jsonify("I'll be there for you")


@app.route("/personajes")
def per():
    return jsonify(f"choose one of these characters: {', '.join(tsa.personajes())}")


@app.route("/frases/<name>")
def frasename(name):
    return tsa.random_quote(name)



@app.route("/frasestemp/<temp>")
def frasetempo(temp):
    frase = f"{tsa.random_season(temp)}"
    return frase



@app.route("/sentiment/<character>")

def sentimientos(character):
    """
    listado = {neg,neu,pos,compound}
    """
    frase = tsa.random_quote(character)
    listado = tem.sentimientos_fr(frase["line"])
    dic = {"datos": frase, "sentimient":listado}
    #return f"{frase} and the sentiment analisis is: {listado}"
    return dic


@app.route("/usuario", methods=["POST"])
def usuario():
    names = request.form.get("nombre")
    
    return tsa.insertusuario(names)


@app.route("/newperson", methods=["POST"])
def insertcharacter():
    charac = request.form.get("personaje")
    return sqt.insertCar("character",charac)

@app.route("/newepisode", methods=["POST"])
def insertepisode():
    epis = request.form.get("episodio")
    tempo = request.form.get("temporada")
    num = request.form.get("numero")
    return sqt.insertEp("episode_title",epis,num,tempo)


@app.route("/newline", methods=["POST"])
def insertline():
    
    episode = request.form.get("episodio")
    charac = request.form.get("personaje")
    line = request.form.get("frase")
    return sqt.insertquote("quote",line,episode,charac)
    
    
















app.run(debug=True)

