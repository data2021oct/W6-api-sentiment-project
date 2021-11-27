from flask import Flask, request
from flask import jsonify
import tools.sql_api as tsa




app = Flask(__name__)




@app.route("/")
def inicial():
    return jsonify("I'll be there for you")


@app.route("/personajes")
def per():
    return jsonify(f"choose one of these characters: {', '.join(tsa.personajes())}")


@app.route("/fraseper")
def fraseper():
    character = request.args.get("character")
    frase = f"{character} says: {tsa.random_quote(character)[0]}"
    return frase













app.run(debug=True)

