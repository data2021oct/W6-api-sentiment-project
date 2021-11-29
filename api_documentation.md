
# Api Friends' Lines
This Api conects to a Mysql database that stores lines of the six main characters of the famous TV show.

[![](https://imagenes.elpais.com/resizer/5YAXQY0dKqqqil7bzunHHyL8rCg=/980x735/filters:focal(888x367:898x377)/cloudfront-eu-central-1.images.arcpublishing.com/prisa/4HSTSOKON5H7BDAHRT5DG24O7E.jpeg)](https://www.youtube.com/embed/q-9kPks0IfE)

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