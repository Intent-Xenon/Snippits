import sqlite3
import os
import os.path

# Define the DDL SQL 
sql = """
CREATE TABLE "customer" (
	"Id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"Name"	TEXT,
	"Height"	REAL
);
"""
#
# global database name
#
database_file = 'customer.db'
# Delete the database
# in case it already exists
#
if os.path.exists(database_file):
  os.remove(database_file)
#
# Connect to the database
#
conn = sqlite3.connect(database_file)
# Get a cursor pointing to the database
cursor = conn.cursor()
# Create the tables
cursor.executescript(sql)
# Commit to save everything
conn.commit()
# Close the connection to the database
conn.close()