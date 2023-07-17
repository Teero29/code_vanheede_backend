# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 15:02:41 2022

@author: Younes
"""

import mysql.connector
import requests

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database ='vanheede_v5'
    )
mycursor = mydb.cursor();

#%% Maj matrices Quevy

mycursor.execute('select id_site,longitude,latitude from site where id_depot = 1')
result_quevy = mycursor.fetchall()


url = 'http://localhost:8080/ors/v2/matrix/driving-hgv' #ors-app

cords = [] 
for i in result_quevy:
    cord = [i[1],i[2]]
    cords.append(cord)

myobj = {"locations": cords, "metrics":["distance","duration"]}
x = requests.post(url, json = myobj)
x = x.json()
durees = x["durations"]
distances = x["distances"]
print(f'distance: {distances}')
print(f'duree: {durees}')

    
for i in range(len(durees)):
    
    mycursor.execute(f"UPDATE site SET time_vector = '{durees[i]}',distance_vector	= '{distances[i]}' WHERE id_site = {result_quevy[i][0]}")
    print(i)
    mydb.commit()
 
    
#%% Maj matrices Dottignies

mycursor.execute('select id_site,longitude,latitude from site where id_depot = 2')
result_dottignies = mycursor.fetchall()

url = 'http://localhost:8080/ors/v2/matrix/driving-hgv' #ors-app

cords = [] 
for i in result_dottignies:
    cord = [i[1],i[2]]
    cords.append(cord)

myobj = {"locations": cords, "metrics":["distance","duration"]}
x = requests.post(url, json = myobj)
x = x.json()
durees = x["durations"]
distances = x["distances"]
print(f'distance: {distances}')
print(f'duree: {durees}')

    
for i in range(len(durees)):
    
    mycursor.execute(f"UPDATE site SET time_vector = '{durees[i]}',distance_vector	= '{distances[i]}' WHERE id_site = {result_dottignies[i][0]}")
    print(i)
    mydb.commit()

#%% Maj Matrices Depots Quevy

mycursor.execute('select id_site,longitude,latitude from site where id_depot = 1')
result_quevy = mycursor.fetchall()
print(result_quevy)
print()
mycursor.execute('select longitude,latitude from depot where id_depot = 1')
depot_quevy = mycursor.fetchall()

cords_quevy = [depot_quevy[0][0],depot_quevy[0][1]]

cords = [] 
for i in result_quevy:
    cord = [i[1],i[2]]
    cords.append(cord)

cords.insert(0,cords_quevy)
print(cords)
print()
myobj = {"locations": cords, "metrics":["distance","duration"],"sources":[0]}
x = requests.post(url, json = myobj)
x = x.json()
durees = x["durations"]
distances = x["distances"]
print(f'distance: {distances}')
print()
print()
print()
print(f'duree: {durees}')

for i in range(len(durees)):
    
    mycursor.execute(f"UPDATE depot SET time_vector = '{durees[0]}',distance_vector	= '{distances[0]}' WHERE id_depot = 1")
    print(i)
    mydb.commit()
    
#%% Maj Matrices Depots Dottignies
mycursor.execute('select id_site,longitude,latitude from site where id_depot = 2')
result_dottignies = mycursor.fetchall()
print(result_dottignies)
print()
mycursor.execute('select longitude,latitude from depot where id_depot = 2')
depot_dottignies = mycursor.fetchall()

cords_dottignies = [depot_dottignies[0][0],depot_dottignies[0][1]]

cords = [] 
for i in result_dottignies:
    cord = [i[1],i[2]]
    cords.append(cord)

cords.insert(0,cords_dottignies)
print(cords)
print()
myobj = {"locations": cords, "metrics":["distance","duration"],"sources":[0]}
x = requests.post(url, json = myobj)
x = x.json()
durees = x["durations"]
distances = x["distances"]
print(f'distance: {distances}')
print()
print()
print()
print(f'duree: {durees}')

for i in range(len(durees)):
    
    mycursor.execute(f"UPDATE depot SET time_vector = '{durees[0]}',distance_vector	= '{distances[0]}' WHERE id_depot = 2")
    print(i)
    mydb.commit()
    

#%% Maj Matrices Depots Mineral
mycursor.execute('select id_site,longitude,latitude from site')
result_mineral = mycursor.fetchall()
print(result_mineral)
print()
mycursor.execute('select longitude,latitude from depot where id_depot = 3')
depot_mineral = mycursor.fetchall()

cords_mineral = [depot_mineral[0][0],depot_mineral[0][1]]

cords = [] 
for i in result_mineral:
    cord = [i[1],i[2]]
    cords.append(cord)

cords.insert(0,cords_mineral)
print(cords)
print()
myobj = {"locations": cords, "metrics":["distance","duration"],"sources":[0]}
x = requests.post(url, json = myobj)
x = x.json()
durees = x["durations"]
distances = x["distances"]
print(f'distance: {distances}')
print()
print()
print()
print(f'duree: {durees}')

for i in range(len(durees)):
    
    mycursor.execute(f"UPDATE depot SET time_vector = '{durees[0]}',distance_vector	= '{distances[0]}' WHERE id_depot = 3")
    print(i)
    mydb.commit()
  
#%% Maj Matrices Depots Renaix    
mycursor.execute('select id_site,longitude,latitude from site')
result_renaix = mycursor.fetchall()
print(result_renaix)
print()
mycursor.execute('select longitude,latitude from depot where id_depot = 4')
depot_renaix = mycursor.fetchall()

cords_renaix = [depot_renaix[0][0],depot_renaix[0][1]]

cords = [] 
for i in result_renaix:
    cord = [i[1],i[2]]
    cords.append(cord)

cords.insert(0,cords_renaix)
print(cords)
print()
myobj = {"locations": cords, "metrics":["distance","duration"],"sources":[0]}
x = requests.post(url, json = myobj)
x = x.json()
durees = x["durations"]
distances = x["distances"]
print(f'distance: {distances}')
print()
print()
print()
print(f'duree: {durees}')

for i in range(len(durees)):
    
    mycursor.execute(f"UPDATE depot SET time_vector = '{durees[0]}',distance_vector	= '{distances[0]}' WHERE id_depot = 4")
    print(i)
    mydb.commit()