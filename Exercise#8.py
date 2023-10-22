#Connection to DataBase
import mysql.connector
from geopy.distance import geodesic as GD

connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='Allahtallah1'
)
cus = connection.cursor()

#Task 1
print("Task#1")
print()
Icao = input("Enter ICAO Code: ")

sql = "select name, municipality from airport where ident = '"+Icao+"'"
cus.execute(sql)
Info = cus.fetchall()
for i,j in Info:
    Name = i
    if j != "":
            Town = j
    else:
            Town = "[Not Available]"

print(f"The name of Airport with ICAO Code \'{Icao}\' is {Name} and it is located in {Town}")
print()

#Task 2

from tabulate import tabulate

print("Task#2")
print()
Area = input("Enter Area Code: ")

sql = "select name, type from airport where iso_country = '"+Area+"' order by type desc;"
cus.execute(sql)
Info_Area = cus.fetchall()

print(tabulate((Info_Area), headers = ["Name","Type"]))
print("-------------------------------------------------")
print()
print("End of Table")
print()

#Task 3
print("Task#3")
print()
def distanceairport(currentID, destinationID):
    sql = "SELECT latitude_deg, longitude_deg FROM airport"
    sql += " WHERE ident = '" + currentID + "' OR ident = '" + destinationID + "'"
    cus.execute(sql)
    row = cus.fetchall()
    if row == 0:
        print("No result")
    else:
        location = []
        for lat, long in row:
            location.append(lat)
            location.append(long)
        dist = GD((location[0], location[1]), (location[2], location[3]))
        disArr = (str(dist)).split()
        dis = float(disArr[0])
        distance = int(dis)
        return distance
F_ICAO = input("Enter First ICAO Code: ")
S_ICAO = input ("Enter Second ICAO Code: ")
print(f"The Distance Between The Two Airports is {distanceairport(F_ICAO,S_ICAO)}Km")

