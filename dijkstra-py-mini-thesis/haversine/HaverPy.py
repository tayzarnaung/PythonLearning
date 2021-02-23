from math import radians, cos, sin, asin, sqrt
import pandas as pd
import csv

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians (mile unit)
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

def add_row():
    sub_row= []; 
    sub_row.append(name)

    for lat2, lon2, in zip(df.Latitude,df.Longitude):
        distance = haversine(lat,lon,lat2,lon2)
        sub_row.append( distance)
    # row.append(sub_row)

    for lat2, lon2, in zip(df2.Latitude,df2.Longitude):
        distance = haversine(lat,lon,lat2,lon2)
        sub_row.append( distance)
    # row.append(sub_row)

    with open('distance_csv/distance.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(sub_row)
    csvFile.close()
#end function -   -   -   -   -   -


csvData = [ ['Name', 'Latitude', 'Longitude', 'Distance'] ]
header= []; sub_header = ['Name']; 
row = [];   sub_row= []


df = pd.read_csv('../sule_shwedagon.csv')
df2 = pd.read_csv('../test_cor.csv')

for name in (df.Name):
    sub_header.append(name); 
for name in (df2.Name):
    sub_header.append(name)
header.append(sub_header)
# print(header)

with open('distance_csv/distance.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(header)
csvFile.close()



for name,lat, lon, in zip(df.Name,df.Latitude,df.Longitude):
    add_row()

for name,lat, lon, in zip(df2.Name,df2.Latitude,df2.Longitude):
    add_row()
# print(sub_row)
# print(row)

