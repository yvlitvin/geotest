import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


connection = sqlite3.connect("atm_numbers.sqlite")
connection.row_factory = dict_factory

cursor = connection.cursor()

location_lat = 50.461502
location_lng = 30.406538

cursor.execute('SELECT * FROM Ukraine ORDER BY ((?-lat)*(?-lat)) + ((? - long)*(? - long)) ASC limit 3',(location_lat,location_lat,location_lng,location_lng))

# fetch all or one we'll go for all.

results = cursor.fetchall()

print(results)

connection.close()