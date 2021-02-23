import pandas as pd
import csv
from tkinter import *

# window = Tk()
# window.title("Where would yo go?")
# window.geometry("640x640+0+0")

# heading = Label(window, text="Finding The Best Route", font=("arial",30,"italic"), fg="steelblue").pack()
# label1 = Label(window, text="Enter source: ", font=("arial",20,"bold"), fg="black").place(x=10,y=100)
# label2 = Label(window, text="Enter destination: ", font=("arial",20,"bold"), fg="black").place(x=10,y=150)

# source =  StringVar(value=''); destination = StringVar(value='');
# large_font= ('Verdana',20)
# entry1 = Entry(window, textvariable=source, font=large_font, width=20, bg="lightgreen").place(x=250, y=100)
# entry2 = Entry(window, textvariable=destination, font=large_font, width=20, bg="lightgreen").place(x=250, y=150)

# def search():
#     print ( str(source.get()), destination.get() )
# work = Button(window, text="Search", width=20, height=2, bg="lightblue", command=search).place(x=250, y=200)


# window.mainloop()

df = pd.read_csv('../sule_shwedagon.csv')
edges = []
# edges = [('A', 'B',3),('A','C',1)]
# for i in range(3):
#     x = input("Type source:")
#     y = input("Type destination:")
#     dist = float( input("Type distance: ") )

#     string =  x , y , dist 
#     print (string)
#     arr.append(string)
# print(arr)
# for x,lat, lon, in zip(df.Name,df.Latitude,df.Longitude):
name= "Sule"; lat = 16.7741; lon = 96.1588
infLat = 5000; infLon = 5000;
aboveLat = ''; aboveLon = None; 
maxminLat = ''; maxminLon = None;
minmaxLat =''; minmaxLon= None;
belowLat=''; belowLon = None;

for y,lat2, lon2, in zip(df.Name,df.Latitude,df.Longitude):
    if (lat2 == lat) & (lon2 == lon): continue;

    if (lat2 > lat) & (lon2 >= lon):       

        if (lat2 < infLat) & (lon2 < infLon):
            aboveLat = lat2; aboveLon = lon2;
            infLat = lat2; infLon = lon2;
            name = y;


if (aboveLat != '') & (aboveLon is not None): 
        print(name,aboveLat, aboveLon)



        # string =  x , y , dist    
        # arr.append(string)
        # elif lat2 > lat & lon2 < lon:
        #     if lat2 < infLat & lon2 < infLon:
        #         mLat = lat2; aboveLon = lon2;
        #         infLat = lat2; infLon = lon2;
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")
# for i in df_filter:
#     lat2 = i['Latitude']; lon2= i['Longitude']
#     if(aboveLat > lat2): aboveLat = lat2
#     if(aboveLon > lon2): aboveLon = lon2
# print(aboveLat, aboveLon)

    # print("lat" , aboveLat , 'Lon',aboveLon)

# df_filter = df[(df['Latitude']>16.7741) & (df['Longitude']<96.1588)]
# df_filter = df[(df['Latitude']<16.7741) & (df['Longitude']>96.1588)]
# df_filter = df[(df['Latitude']<16.7741) & (df['Longitude']<96.1588)]



    # with open('distance_csv/distance.csv', 'a') as csvFile:
    #     writer = csv.writer(csvFile)
    #     writer.writerow(sub_row)
    # csvFile.close()

# print(sub_row)
# print(row)

