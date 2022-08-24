from fileinput import filename
from flask import Flask, json, jsonify, request, send_file, make_response
from flask_cors import CORS, cross_origin
import sqlite3,database,similarity

import os

database.setupDatabase()

UPLOAD_FOLDER = "./upload"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
CORS(app)


@app.route("/getSuggestion", methods=["GET"])
def getSuggestions():
    userId = request.args.get("id")
    
    top5 = similarity.getSuggestion(userId)
    
   
    mostSimUser = int(top5[0]['userId'])
    
    movies = database.getLikedMovies(mostSimUser,userId)
    print({"similarities":top5,"suggestions": movies})
    return jsonify({"similarities":top5,"suggestions": movies})


@app.route('/getRatings', methods=['GET'])
def getRatings():
    connection = sqlite3.connect('Movies.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM Ratings''')
    ratings = cursor.fetchall()
    connection.close()
    return jsonify(ratings)


@app.route('/rate', methods=['POST'])
def rateMovie():
    content_type = request.headers.get('Content-Type')
    if (content_type != 'application/json'):
        return jsonify('Content-Type not supported!')

    json = request.json

    userId = json['userId']
    movieId = json['movieId']
    rating = json['rating']
    rating = int(rating)
    if rating == 0:
        rating = -1
    return database.rateMovie(userId, movieId, rating)


@app.route('/get_image', methods=['GET'])
def get_image():
    fileName = request.args['fileName']

    if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], fileName)):
        return send_file(os.path.join(app.config['UPLOAD_FOLDER'], fileName))
    else:
        return "Image not found"

@app.route('/getAllMovies', methods=['GET'])
def getAllMovies():
    return database.getAllMovies()


@app.route('/movie', methods=['GET'])
def getMovie():
    id = request.args['id']
    movie = database.getMovie(id)
    return movie


@app.route('/movie', methods=['POST'])
def storeMovie():

    if request.files['image']:
        image = request.files['image']
        path = os.path.join(app.config["UPLOAD_FOLDER"], image.filename)
        image.save(path)

        title = request.args['title']
        genre = request.args['genre']
        image = image.filename
        year = request.args['year']
        imdb = request.args['imdb']

        id = database.storeMovie(title, genre, image, year, imdb)
        return jsonify({"id": id})


@app.route('/movie', methods=['PUT'])
def updateMovie():
    if request.files:
        if request.files['image']:
            image = request.files['image']
            path = os.path.join(app.config["UPLOAD_FOLDER"], image.filename)
            image.save(path)

            id = request.args['id']
            title = request.args['title']
            genre = request.args['genre']
            image = image.filename
            year = request.args['year']
            imdb = request.args['imdb']

            message = database.updateMovie(id, title, genre, year, imdb, image)
            return message

    id = request.args['id']
    title = request.args['title']
    genre = request.args['genre']
    year = request.args['year']
    imdb = request.args['imdb']

    message = database.updateMovie(id, title, genre, year, imdb)
    return  message

@app.route('/movie', methods=['DELETE'])
def deleteMovie():
    id = request.args['id']
    return database.deleteMovie(id)

@app.route('/admin/login', methods=['POST'])
def adminLogin():

    content_type = request.headers.get('Content-Type')
    if (content_type != 'application/json'):
        return jsonify('Content-Type not supported!')

    json = request.json

    connection = sqlite3.connect('Movies.db')
    cursor = connection.cursor()

    email = json['email']
    password = json['password']
    # check if the user is admin and get the id
    cursor.execute(
        '''SELECT * FROM Users WHERE Email = ? AND Password = ? AND IsAdmin = 1''', (email, password))
    result = cursor.fetchone()
    if result is not None:
        return jsonify({'success': True, 'id': result[0], 'email': result[1]})
    else:
        return jsonify({'success': False})


@app.route('/register', methods=['POST'])
def userRegister():
    content_type = request.headers.get('Content-Type')
    if (content_type != 'application/json'):
        return jsonify('Content-Type not supported!')

    json = request.json

    connection = sqlite3.connect('Movies.db')
    cursor = connection.cursor()

    email = json['email']
    password = json['password']

    cursor.execute('''SELECT * FROM Users WHERE Email = ?''', (email,))
    result = cursor.fetchone()
    if result is not None:
        return jsonify({'success': 'Email is taken'})
    else:
        cursor.execute(
            '''INSERT INTO Users (Email, Password,IsAdmin) VALUES (?, ?,0)''', (email, password))
        lastUser = cursor.lastrowid
        for i in range (100):
            cursor.execute('''INSERT INTO Ratings (UserId,MovieId,Rating) VALUES (?,?,?)''', (lastUser,i+1,0))
        connection.commit()
        return jsonify({'success': True})


@app.route('/login', methods=['POST'])
def userLogin():

    content_type = request.headers.get('Content-Type')

    if (content_type != 'application/json'):
        return jsonify('Content-Type not supported!')

    json = request.json

    connection = sqlite3.connect('Movies.db')
    cursor = connection.cursor()

    email = json['email']
    password = json['password']

    cursor.execute(
        '''SELECT * FROM Users WHERE Email = ? AND Password = ?''', (email, password))
    result = cursor.fetchone()
    if result is not None:
        return jsonify({'success': True, 'id': result[0], 'email': result[1], "isAdmin": result[3]})
    else:
        return jsonify({'success': False})


if __name__ == '__main__':
    app.run(debug=True)
