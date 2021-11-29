from flask import Flask, request
from flask import jsonify
import tools.sql_api as tsa
import tools.emotions as tem




app = Flask(__name__)




@app.route("/")
def inicial():
    return jsonify("I'll be there for you")


@app.route("/personajes")
def per():
    return jsonify(f"choose one of these characters: {', '.join(tsa.personajes())}")


@app.route("/frases/<name>")
def frasename(name):
    # frase = f"{name} says: {tsa.random_quote(name)[0]}"
    # return frase
    return tsa.random_quote(name)



@app.route("/frasestemp/<temp>")
def frasetempo(temp):
    frase = f"{tsa.random_season(temp)}"
    return frase



@app.route("/usuario", methods=["POST"])
def usuario():
    names = request.form.get("nombre")
    
    return tsa.insertusuario(names)


@app.route("/newline", methods=["POST"])
def insertamensaje():
    temp = request.form.get("temporada")
    epi = request.form.get("episodio")
    charac = request.form.get("personaje")
    line = request.form.get("frase")
    
    return tsa.newline(temp, epi, charac, line)



@app.route("/sentiment/<character>")

def sentimientos(character):
    """
    listado = [neg,neu,pos,compound]
    """
    frase = f"{character} says: {tsa.random_quote(character)[0]}"
    listado = tem.sentimientos_fr(frase)
    return listado
    
















app.run(debug=True)

