# imports
import csv
import sqlite3

# remove dot from last column
def remove_dot(value):
    return int(value.replace('.',''))

# read data file
with open('food_production.csv','r') as file: 

    # create file reader
    reader = csv.reader(file)

    # skip columns header
    next(reader)

    # connect to db
    conn = sqlite3.connect('dsadb.db')

    # drop current table 
    conn.execute('DROP TABLE IF EXISTS production')

    # create table into db for data storage
    conn.execute('''
                CREATE TABLE production (
                product TEXT,
                amount INTEGER,
                average_price REAL,
                total_revenue INTEGER,
                profit_margin REAL
                )
                ''')

    # insert into db loop
    for row in reader: 
    
    # condition:  amount bigger than 10 
        if int(row[1]) > 10:

            # remove dot from the last column and convert into integer
            row[3]= remove_dot(row[3])

            # profit margin 
            profit_margin = round((row[3] / float(row[1])) - float(row[2]),2)

            # register data into db
            conn.execute('INSERT INTO production (product, amount, average_price, total_revenue, profit_margin) VALUES (?, ?, ?, ?, ?)', (row[0], row[1], row[2], row[3], profit_margin))
     


    conn.commit()
    conn.close()

print("Job Successful")