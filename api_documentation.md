
# Api Friends' Lines
This Api conects to a Mysql database that stores lines of the six main characters of the famous TV show.

[![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThB-Oyt9ZEJjBjvc0Byo2xgCWx68vYs5gWe0ZDJ4jxRjqYEyALT2DqF8e1tZDSNHmC7ko&usqp=CAU)](https://www.youtube.com/embed/q-9kPks0IfE)

# ¿Cómo Funciona?


# @GET

- inicial: "http://127.0.0.1:5000/" 

Endpoint
- /personajes

A list of the characters to choose from so you have in the database

Endpoint
- /frases/name 

Giving a name of one of our main characters, it returns a random line of the chosen characer and tells you in which episode it's said

Endpoint
- /frasestemp/temporada

Giving the number of one of the ten seasons of our beloved TV show, it returns a ramndom line of given season and tells you who says it and in which episode it's said.

Endpoint
- sentiment/character

like frases/name endpoint it returns a random line of the chosen characters and not only tells you in which episode and season it's said, it also [analyzes it's sentiment](https://en.wikipedia.org/wiki/Natural_Language_Toolkit). values = Negative, neutra, positvie and a media of each values.
    





# @POST
Endpoint
- /nueva/frase

De esta manera insertamos una frase en la base de datos.


Endpoint
- /frases/<name>

Extraemos todas las frases que tenemos de un usuario en la base de datos

```
url_frases = "http://localhost:5000/frases/"
person = "Albus Dumbledore"
```


## ¿Qué personajes hay?
Para saber los usuarios que hay en la base de datos tienes que hacer una query del tipo get al endpoint /personajes
    
    
 

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