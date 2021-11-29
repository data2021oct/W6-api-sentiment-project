
# Api Friends' Lines
This Api conects to a Mysql database that stores lines of the six main characters of the famous TV show.
<iframe width="560" height="315" src="https://www.youtube.com/embed/q-9kPks0IfE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# ¿Cómo Funciona?

# @POST
Endpoint
- /nueva/frase

De esta manera insertamos una frase en la base de datos.


# @GET
Endpoint
- /frases/<name>

Extraemos todas las frases que tenemos de un usuario en la base de datos

```
url_frases = "http://localhost:5000/frases/"
person = "Albus Dumbledore"
```


## ¿Qué personajes hay?
Para saber los usuarios que hay en la base de datos tienes que hacer una query del tipo get al endpoint /personajes