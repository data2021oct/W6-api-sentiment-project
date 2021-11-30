
# Api Friends' Lines
This Api conects to a Mysql database that stores lines of the six main characters of the famous TV show.

[![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThB-Oyt9ZEJjBjvc0Byo2xgCWx68vYs5gWe0ZDJ4jxRjqYEyALT2DqF8e1tZDSNHmC7ko&usqp=CAU)](https://www.youtube.com/embed/q-9kPks0IfE)


# @GET

- inicial: [http://127.0.0.1:5000/](http://127.0.0.1:5000")

Endpoint
- /personajes

A list of the characters to choose from

Endpoint
- /frases/name 
```
http://127.0.0.1:5000/frases/Chandler
```
```
{
  "character": "Phoebe", 
  "episode": "The one with The Stripper Cries", 
  "line": "(disgusted) Uh.", 
  "season": 10
}

```

Giving a name of one of our main characters, it returns a random line of the chosen characer and tells you in which episode it's said

Endpoint
- /frasestemp/temporada

```
http://127.0.0.1:5000/frasestemp/10
```
```
in episdode 'The one with The Videotape', from season 8, Joey says 'Hey, hang up! You get food poisoning just talkin` to that place.'
```

Giving the number of one of the ten seasons of our beloved TV show, it returns a ramndom line of given season and tells you who says it and in which episode it's said.

Endpoint
- sentiment/character
```
http://127.0.0.1:5000/sentiment/Chandler
```

```
{
  "datos": {
    "character": "Chandler", 
    "episode": "The one with Mac And C.H.E.E.S.E.", 
    "line": "Yeah, and then I fell asleep on the subway and went all the way to Brooklyn. Brooklyn is f-far!!", 
    "season": 6
  }, 
  "sentimient": {
    "compound": 0.296, 
    "neg": 0.0, 
    "neu": 0.784, 
    "pos": 0.216
  }
}
```
like frases/name endpoint it returns a random line of the chosen characters and not only tells you in which episode and season it's said, it also [analyzes it's sentiment](https://en.wikipedia.org/wiki/Natural_Language_Toolkit). values = Negative, neutra, positvie and a media of each values.
    


# @POST

Endpoint
- /usuario
```
url = "http://127.0.0.1:5000/usuario
nombre = username
```
Your registration in our database. Your useranme is unique!!

Endpoint
- /newperson
```
url = "http://127.0.0.1:5000/newperson
nombre = personaje
```
Inserts a new character in our database

Endpoint
- /newepisode
```
url = "http://127.0.0.1:5000/newepisode
episodio = "the one with the new episode"
temporada = 10
numero = 3 #number of the episode in the season
```
Inserts a new episode in our database

Endpoint
- /newline
```
url = "http://127.0.0.1:5000/newline
episodio = "the one with the new episode"
personaje = "Chandler"
line = "Could i have more lines?"
```
Inserts a new line in our database

