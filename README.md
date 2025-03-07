# Flask Movie API Mini-Project

## Features:
- Flask API with JSON responses
- HTML page rendered with Jinja2
- Add new movies via API and form

## Setup Instructions:

How to run and check if its working:

Method 1: Using cURL (Command Line)

1. look for the project folder

2. go to folder search bar and type cmd then enter

3. type python app.py to run the file 

4. open a new command prompt then enter the following curl commands then check if the project is working :

* Get all movies:
curl http://127.0.0.1:5000/api/movies

* Get a movie by ID:
curl http://127.0.0.1:5000/api/movies/1

* Add a movie via API:
curl -X POST http://127.0.0.1:5000/api/movies -H "Content-Type: application/json" -d "{\"title\": \"Dune: Part Two\", \"director\": \"Denis Villeneuve\"}"




API Endpoints:

Method	Endpoint	Description

GET	/api/welcome	Returns a welcome message

GET	/api/movies	Returns all movies in JSON

GET	/api/movies/<id>	Returns details of a specific movie

POST	/api/movies	Adds a new movie via API

GET	/movies	Displays movies in an HTML page

POST	/submit-movie	Adds a movie via form submission



Method 2: Using jinja templates 

1. run app.py on command prompt (python app.py)

2. check if the jinja templates is working using this url
http://127.0.0.1:5000/movies
