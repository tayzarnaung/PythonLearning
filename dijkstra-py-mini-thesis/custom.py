import csv
import pandas as pd
	
bus_stop2 = pd.read_csv('bus_stop.csv')

header = []; row = []

sub_header= ['Name', 'Latitude', 'Longitude']
header.append(sub_header)

for name,lat, lng, in zip(bus_stop2.Name,bus_stop2.Latitude,bus_stop2.Longitude):
    if ( 16.7616 <= lat <= 16.8265) & (96.1301 <= lng <= 96.1834):
    	sub_row = []
    	sub_row.append(name)
    	sub_row.append(lat)
    	sub_row.append(lng)
    	row.append(sub_row)

# print(row)
with open('custom.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(header)
    writer.writerows(row)
writeFile.close()

