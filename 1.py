import psycopg2
import csv

# Connect to the PostgreSQL database
conn= psycopg2.connect(host="localhost", dbname="postgres", user="postgres",
                       password="dilnaz", port="5433")
cur = conn.cursor()

# Design tables for PhoneBook
cur.execute("""
CREATE TABLE IF NOT EXISTS PhoneBook (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20) NOT NULL
);
""")
conn.commit()

# Implement two ways of inserting data into the PhoneBook

# 1. Upload data from CSV file
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header
    for row in reader:
        cur.execute(
            "INSERT INTO PhoneBook (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
            (row[0], row[1], row[2])
        )

# 2. Entering user name and phone from console
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
phone_number = input("Enter phone number: ")

cur.execute(
    "INSERT INTO PhoneBook (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
    (first_name, last_name, phone_number)
)

# Implement updating data in the table (change user first name or phone)
first_name = input("Enter first name of the user you want to update: ")
new_phone_number = input("Enter the new phone number: ")

cur.execute(
    "UPDATE PhoneBook SET phone_number = %s WHERE first_name = %s",
    (new_phone_number, first_name)
)

# Querying data from the tables (with different filters)
pattern = input("Enter a pattern to search for: ")

cur.execute(
    "SELECT * FROM PhoneBook WHERE first_name LIKE %s",
    ('%' + pattern + '%',)
)

# Implement deleting data from tables by username or phone
first_name = input("Enter first name of the user you want to delete: ")

cur.execute(
    "DELETE FROM PhoneBook WHERE first_name = %s",
    (first_name,)
)

# Close the cursor and commit the transaction
conn.commit()
cur.close()
conn.close()
