#Ryan Barber assignment 6.2 2/15/26

import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ns17goat!",
        database="movies"
    )

    cursor = db.cursor()

    #query 1
    print ("\n-- DISPLAYING Studio RECORDS --")
    cursor.execute("SELECT * FROM studio")
    studios = cursor.fetchall()

    for studio in studios:
        print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

    #query 2
    print("\n-- DISPLAYING Genre RECORDS --")
    cursor.execute("SELECT * FROM genre")
    genres = cursor.fetchall()

    for genre in genres:
        print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

    #query 3
    print ("\n-- DISPLAYING Short Film RECORDS (Under 2 hours) --")
    cursor.execute("SELECT film_name, film_runtime FROM film where film_runtime < 120")
    films = cursor.fetchall()
    for film in films:
        print("Film Name: {}\nRuntime: {}\n".format(film[0], film[1]))

    #query 4
    print("\n-- DISPLAYING Director RECORDS in ORDER --")
    cursor.execute("""
        SELECT film_name, film_director
        FROM film
        ORDER BY film_director
    """)

    films = cursor.fetchall()
    for film in films:
        print("Film Name: {}\nDirector: {}\n".format(film[0], film[1]))

    cursor.close()
    db.close()

except mysql.connector.Error as error:
    print("Database error:", error)