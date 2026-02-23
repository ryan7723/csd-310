#Ryan Barber Module 7.2 2/22/25

import mysql.connector
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Ns17goat!",
  database="movies"
)

cursor = db.cursor()

def show_films(cursor, title):
    print("\n--{}--".format(title))

    query="""
    SELECT film.film_name AS Name,
           film.film_director AS Director,
           genre.genre_name AS Genre,
           studio.studio_name AS Studio
    FROM film
    INNER JOIN genre ON film.genre_id = genre.genre_id
    INNER JOIN studio ON film.studio_id = studio.studio_id
    """
    cursor.execute(query)
    films = cursor.fetchall()

    for film in films:
        print("Film NAME:", film[0])
        print("Director:", film[1])
        print("Genre Name ID:", film[2])
        print("Studio Name:", film[3])
        print()

show_films(cursor, "DISPLAYING FILMS")

insert_query = """
    INSERT INTO film(
    film_name, 
    film_releaseDate, film_runtime,
    film_director, 
    studio_id, 
    genre_id
    )
    VALUES (%s, %s, %s, %s, %s, %s)
    """
new_film = (
    "Inception",
    "2010",
    148,
    "Christopher Nolan",
    1,
    2
)
cursor.execute(insert_query, new_film)
db.commit()

print("\nInserted new film.\n")

show_films(cursor, "AFTER INSERT")

update_query = """
UPDATE film
set genre_id = (
    SELECT genre_id FROM genre WHERE genre_name = "Horror"
)
WHERE film_name = "Alien"
"""
cursor.execute(update_query)
db.commit()

print("\nUpdated Alien to Horror.\n")

show_films(cursor, "AFTER UPDATE")

delete_query = """
DELETE FROM film
WHERE film_name = 'Gladiator'
"""
cursor.execute(delete_query)
db.commit()

print("\nDeleted Gladiator.\n")

show_films(cursor, "AFTER DELETE")

cursor.close()
db.close()
