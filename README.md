# The one with the apis

![](https://i.pinimg.com/originals/67/5f/5e/675f5ea011e851aa8e4f45f554b92966.gif)

# Objetive:

- Create my own API. This api recives, stores and serves lines from our beloved TV Show: **FRIENDS**
    - [API documentation](https://github.com/data2021oct/W6-api-sentiment-project/blob/main/api_documentation.md)
    

# Method:
- Find a dataset with the script of Friends and use pandas to clean it: 
    - [Kaggle friends-transcript](https://www.kaggle.com/ryanstonebraker/friends-transcript)
- Design the structure of the database in Mysql
- Conecting jupyther notebook with mysql, insert a sample of the lines of the six main characters.
- Write an API using flask to recive and store lines of the script.
- Use the API to extract emotional value of the lines througth and endpoint
![](https://y.yarn.co/e875bec8-ea3f-4409-9f98-2290dea6189b_text.gif)


# Structure:
#### Folders:
- config: configuration.py -> conects with mysql database
- data:
    - friends-transcipt csv
    - diferent csv that i have created during de cleansing of my data
    - friends.mwb (creates the diagram of our database)
    - databasefriends.sql: (the dump of the structure + data of our database)
- notebooks: (jupyther notebooks)
    - 01_dataset_insert (cleaning a first insert of our data in mysql)
    - 02_api_post (Use or my post apis)
    - 03_NLTK (emotional value of my database)
- tools: (stores the .py documents with the functions that i use to create my apis)
#### api_documentation.md
- the user manual of my api
- main.py -> runs my apis
    
# Libraries:

* [sys](https://docs.python.org/3/library/sys.html)
* [pandas](https://pandas.pydata.org/)
* [os](https://docs.python.org/3/library/os.html)
* [sqlalchemy](https://docs.sqlalchemy.org/en/14/)
* [dotenv](https://pypi.org/project/python-dotenv/)
* [requests](https://pypi.org/project/requests/2.7.0/)
* [nltk](https://www.nltk.org/)
* [string](https://docs.python.org/3/library/string.html)
* [spacy](https://spacy.io/api/doc)
* [en_core_web_sm](https://spacy.io/models/en)
* [getpass](https://docs.python.org/es/3/library/getpass.html)
* [random](https://docs.python.org/es/3/library/random.html)
* [flask](https://flask.palletsprojects.com/en/2.0.x/)
* [re](https://docs.python.org/3/library/re.html)
* [textblob](https://textblob.readthedocs.io/en/dev/)

![](https://media1.popsugar-assets.com/files/thumbor/CSTJRBzkQILxTqJfq761vtkDnnQ/fit-in/1024x1024/filters:format_auto-!!-:strip_icc-!!-/2014/07/28/928/n/1922283/6f2bf2d182bef221_orig-21241971/i/When-She-Harnesses-Her-Star-Power.gif)

