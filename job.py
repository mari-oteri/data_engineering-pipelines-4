# imports
import csv
import sqlite3

# create connection & database
conn = sqlite3.connect('dsadb.db')

# create table into db for data storage
conn.execute('''
            CREATE TABLE production (
            product TEXT,
            amount INTEGER,
            average_price REAL,
            total_revenue REAL
            )
            ''')
# recording commands
conn.commit()

# closing connection
conn.close()

# read date file
with open('food_production.csv','r') as file: 

    # create file reader
    reader = csv.reader(file)

    # skip columns header
    next(reader)

    # connect to db
    conn = sqlite3.connect('dsadb.db')

    # insert into db loop
    for row in reader: 
        conn.execute('INSERT INTO production (product,amount,average_price,total_revenue) VALUES (?,?,?,?)', row)

    conn.commit()
    conn.close()

print("Job Successful")