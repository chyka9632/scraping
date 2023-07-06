import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query all data
cursor.execute("select * from events where band_name='Feng Suave' ")
rows = cursor.fetchall()
print(rows)

# Query certain columns
cursor.execute("select band_name, date from events where band_name='Feng Suave' ")
rows = cursor.fetchall()
print(rows)

# Insert new rows
new_rows = [('Linh Hu', 'Beijin City', '5.8.2089'),
            ('Tigress Rock', 'Miami City', '10.5.2089')]
cursor.executemany("insert into events values(?,?,?)", new_rows)
connection.commit()

# Query all data
cursor.execute("select * from events")
rows = cursor.fetchall()
print(rows)
