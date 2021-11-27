from flask import Flask, request
from flask import jsonify
import tools.sql_api as tsa




app = Flask(__name__)




@app.route("/")
def inicial():
    return jsonify("I'll be there for you")


@app.route("/personajes")
def per():
    return jsonify(tsa.personajes())















app.run(debug=True)

