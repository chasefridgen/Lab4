#!/usr/bin/env python3
import sqlite3
#some initial data
id = 4;
temperature = 0.0;
date = '2014-01-05';
#connect to database file
dbconnect = sqlite3.connect("my.db");
#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();
for i in range(10):
    #execute insert statement
    id += 1;
    temperature += 1.1;
    cursor.execute('''insert into temperature values (?, ?, ?)''',
    (id, temperature, date));
dbconnect.commit();
#execute simple select statement
cursor.execute('SELECT * FROM temperature');
#print data
for row in cursor:
    print(row['id'],row['temp'],row['date'] );


#EXERCISE 4
#list of types
typesList = ["door", "temperature", "door", "motion", "temperature"]
#list of zones
zonesList = ["kitchen", "kitchen", "garage", "garage", "garage"]
cursor.execute('''CREATE TABLE IF NOT EXISTS sensors (sensorID integer PRIMARY KEY,type text NOT NULL,zone text)'''); #Create new table
for i in range(0,5):
    cursor.execute('''INSERT INTO sensors(sensorID, type, zone) VALUES(?,?,?)''', (i+1,typesList[i], zonesList[i])); #Fill table with data

cursor.execute("SELECT * FROM sensors WHERE zone=?", ("kitchen",)); #get all the sensors in the kitchen
rows1 = cursor.fetchall();
print("Sensors in the Kitchen: ");
for row in rows1: #print the sensors
    print(row['sensorID'], row['type'], row['zone']);


cursor.execute("SELECT * FROM sensors WHERE type=?", ("door",)); #get all the door sensors
rows2 = cursor.fetchall();
print("Door Sensors: ");
for row in rows2: #print the sensors
    print(row['sensorID'], row['type'], row['zone']);


#close the connection
dbconnect.close();