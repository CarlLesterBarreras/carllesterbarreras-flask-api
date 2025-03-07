from flask import Flask, jsonify, request, render_template, redirect, url_for, session
import json
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"  # For flash messages

DATA_FILE = "movies.json"

# Function to load movies from file
def load_movies():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# Function to save movies to file
def save_movies(movies):
    with open(DATA_FILE, "w") as f:
        json.dump(movies, f, indent=4)

movies = load_movies()  # Load movies initially

# Welcome message endpoint
@app.route('/api/welcome', methods=['GET'])
def welcome():
    return jsonify({"message": "Welcome to the Movie Collection API!"})

# Get all movies (API)
@app.route('/api/movies', methods=['GET'])
def get_movies():
    return jsonify(movies)

# Get a specific movie by ID (API)
@app.route('/api/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = next((movie for movie in movies if movie["id"] == movie_id), None)
    if movie:
        return jsonify(movie)
    return jsonify({"error": "Movie not found"}), 404

# Add a new movie (API)
@app.route('/api/movies', methods=['POST'])
def add_movie():
    global movies
    data = request.json
    if not data or "title" not in data or "director" not in data:
        return jsonify({"error": "Invalid data"}), 400

    new_movie = {
        "id": len(movies) + 1,
        "title": data["title"],
        "director": data["director"],
    }
    movies.append(new_movie)
    save_movies(movies)
    return jsonify(new_movie), 201

# Show movies page
@app.route('/movies', methods=['GET'])
def show_movies():
    message = session.pop('message', '')  # Get message and remove it after showing
    return render_template('movies.html', movies=movies, message=message)

# Add movie (Form)
@app.route('/submit-movie', methods=['POST'])
def submit_movie():
    global movies
    title = request.form.get('title')
    director = request.form.get('director')

    if not title or not director:
        session['message'] = "Please enter both title and director!"
        return redirect(url_for('show_movies'))

    new_movie = {
        "id": len(movies) + 1,
        "title": title,
        "director": director
    }

    movies.append(new_movie)
    save_movies(movies)

    session['message'] = "Movie added successfully!"
    return redirect(url_for('show_movies'))

# Delete movie (Form)
@app.route('/delete-movie', methods=['POST'])
def delete_movie():
    global movies
    movie_id = int(request.form['movie_id'])
    movies = [movie for movie in movies if movie["id"] != movie_id]
    save_movies(movies)

    session['message'] = "Movie deleted successfully!"
    return redirect(url_for('show_movies'))

if __name__ == '__main__':
    app.run(debug=True)
