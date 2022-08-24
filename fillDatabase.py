import database,sqlite3,json

database.setupDatabase()

def fill():
    jsonF = json.load(open("data.json")).get('Ratings')

    connection = sqlite3.connect('Movies.db')
    cursor = connection.cursor()

    userCounter = 2
    for record in jsonF:
        name = record.get('Name').replace(" ","")
        email = name + "@user.com"
        cursor.execute('''INSERT INTO Users (Email, Password,isAdmin) VALUES (?, ?,?)''', (email, "password",0))

        count = 0
        movieCount = 1
        for attr in record:
            if count > 1:
                cursor.execute('''INSERT INTO Ratings (userId,movieId,rating) VALUES (?, ?, ?)''', (userCounter,movieCount,record.get(attr)))
                movieCount += 1              
            count += 1
        userCounter += 1  
    connection.commit()
    connection.close()

fill()