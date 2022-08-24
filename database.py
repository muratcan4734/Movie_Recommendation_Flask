import sqlite3
from flask import jsonify


def setupDatabase():

    connection = sqlite3.connect('Movies.db')
    cursor = connection.cursor()

    # Create Movies table with columns: genre,image,imdb,timestamp,title,year

    cursor.execute('''CREATE TABLE IF NOT EXISTS Movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        genre TEXT,
        image TEXT,
        imdb TEXT,
        title TEXT,
        year TEXT
        )''')

    cursor.execute(
        ''' CREATE TABLE IF NOT EXISTS Users (Id INTEGER PRIMARY KEY AUTOINCREMENT,Email TEXT, Password TEXT,IsAdmin INT)''')

    # create a table for session
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS Ratings (UserId TEXT, MovieId TEXT, Rating INT)''')

    connection.commit()
    connection.close()

    fillIfEmpty()


def fillIfEmpty():
    connection = sqlite3.connect('Movies.db')
    cursor = connection.cursor()

    # check if admin exists
    cursor.execute('''SELECT COUNT(*) FROM Users WHERE IsAdmin = 1''')
    if cursor.fetchone()[0] == 0:
        createAdmin()

    connection.commit()
    connection.close()


def createAdmin():
    connection = sqlite3.connect('Movies.db')
    cursor = connection.cursor()

    cursor.execute(
        '''INSERT INTO Users VALUES (NULL,'admin@admin.com', 'adminadmin', 1)''')
    connection.commit()
    connection.close()

def storeUser(email, password,isAdmin):
    # create user in database
    connection = sqlite3.connect('Movies.db')
    cursor = connection.cursor()

    cursor.execute('''INSERT INTO Users (Email, Password,isAdmin) VALUES (?, ?,?)''', (email, password,isAdmin))

    connection.commit()
    connection.close()


def storeMovie(title, year, genre, image, imdb):
    # store movie in database
    connection = sqlite3.connect('Movies.db')
    cursor = connection.cursor()

    cursor.execute('''INSERT INTO Movies (id,year,genre,imdb,title,image) VALUES (NULL, ?, ?, ?, ?, ?)''',
                   (year,genre, imdb, title, image ))

    #insert movie with column names specified   
    

    
    id = cursor.lastrowid

    connection.commit()
    connection.close()
    return id

def updateMovie(id,title,genre,year,imdb,image=None):
    #get the movie with the given id
    connection = sqlite3.connect('Movies.db')
    cursor = connection.cursor()

    cursor.execute('''SELECT * FROM Movies WHERE id = ?''', (id,))
    movie = cursor.fetchone()
    data = {"title": movie[4], "genre": movie[1], "image": movie[2], "year": movie[5], "imdb": movie[3]}
    
    
    data['title'] = title or data['title']
    data['genre'] = genre or data['genre']
    data['year'] = year or data['year']
    data['imdb'] = imdb or data['imdb']
    data['image'] = image or data['image']
    cursor.execute('''UPDATE Movies SET genre = ?, image = ?, imdb = ?, title = ?, year = ? WHERE id = ?''', (data['genre'], data['image'], data['imdb'], data['title'], data['year'], id))

    connection.commit()
    connection.close()
    return jsonify(data)
def deleteMovie(id):
    # delete movie from database
    connection = sqlite3.connect('Movies.db')
    cursor = connection.cursor()

    cursor.execute('''DELETE FROM Movies WHERE id = ?''', (id,))

    connection.commit()
    connection.close()

    return jsonify({"message": "success"})

def getAllMovies():
    # get all movies from database with column names
    connection = sqlite3.connect('Movies.db')

    cursor = connection.cursor()

    cursor.execute('''SELECT * FROM Movies''')
    movies = cursor.fetchall()

    connection.close()
    
    data = []
    for movie in movies:
        data.append({"id":movie[0],"title": movie[4], "genre": movie[1], "image": movie[2], "year": movie[5], "imdb": movie[3]})

    return jsonify({"movies": data})
def getLikedMovies(simUser,acUser):
     # get all movies that user has rated
    connection = sqlite3.connect('Movies.db')
    cursor = connection.cursor()
    #select movies which simUser rated 1 and acUser rated 0
    cursor.execute('''SELECT MovieId FROM Ratings WHERE UserId = ? AND Rating = 1''', (simUser,))
    simUserLiked = cursor.fetchall()
    cursor.execute('''SELECT MovieId FROM Ratings WHERE UserId = ? AND Rating = 0''', (acUser,))
    acUserLiked = cursor.fetchall()
    # simUserLiked = [movie[0] for movie in simUserLiked]
    # acUserLiked = [movie[0] for movie in acUserLiked]
    connection.close()
    
    #get all movies that simUser and acUser have in common
    commonMovies = list(set(simUserLiked).intersection(acUserLiked))

    
    data = []

    for movie in commonMovies:
        data.append({"movieId":movie[0]})
    return {"movies": data}        

def rateMovie(userId, movieId, rating):
    # insert into ratings
    # if user has already rated movie, update rating
    # if user has not rated movie, insert rating

    connection = sqlite3.connect('Movies.db')
    cursor = connection.cursor()

    cursor.execute('''SELECT COUNT(*) FROM Ratings WHERE UserId = ? AND MovieId = ?''', (userId, movieId))
    if cursor.fetchone()[0] == 0:
        cursor.execute('''INSERT INTO Ratings VALUES (?, ?, ?)''', (userId, movieId, rating))
    else:
        cursor.execute('''UPDATE Ratings SET Rating = ? WHERE UserId = ? AND MovieId = ?''', (rating, userId, movieId))

    connection.commit()
    connection.close()

    return jsonify({"message": "success"})


def getRatings(userId):
    # get ratings movie id and rating with column names
    connection = sqlite3.connect('Movies.db')

    cursor = connection.cursor()

    cursor.execute(
        '''SELECT MovieId, Rating FROM Ratings WHERE UserId = ?''', (userId,))
    ratings = cursor.fetchall()
    
    connection.close()
    
    # if ratings.count != 10:
    #     return "Not enough ratings"

    connection.close()

    data = []
    for rating in ratings:
        data.append({"movieId":rating[0],"rating": rating[1]})

        
    return data

def getAllUsers():
    # get all users with column names
    connection = sqlite3.connect('Movies.db')

    cursor = connection.cursor()

    cursor.execute('''SELECT * FROM Users''')
    users = cursor.fetchall()

    connection.close()

    data = []
    for user in users:
        data.append({"id":user[0],"email": user[1]})
        
    return data

def getMovie(id):
    # get movie from database
    connection = sqlite3.connect('Movies.db')
    cursor = connection.cursor()

    cursor.execute('''SELECT * FROM Movies WHERE id = ?''', (id,))
    movie = cursor.fetchone()

    connection.close()

    # don't mess the order of the returned values,they get complicated very quickly,don't know why
    return {"title": movie[4], "genre": movie[5], "image": movie[1], "year": movie[2], "imdb": movie[3]}
    return jsonify({"title": movie[4], "genre": movie[5], "image": movie[1], "year": movie[2], "imdb": movie[3]})