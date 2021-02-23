import folium
import pandas as pd

import dijkstra_sp as dijk
import shortest_path 
import sp
from tkinter import *

import distance_fixed
# import distance_dictionary as dictionary
import webbrowser

# print(distance_fixed.graph)
# print(dictionary.dictionary)
m = folium.Map(location=[16.7982,96.1422],zoom_start=14)

test_cor= pd.read_csv('test_cor.csv')

bus_stop = pd.read_csv('sule_shwedagon.csv')
# print ( bus_stop.get('Name') )
# bus_stop2 = pd.read_csv('bus_stop.csv')

incidents = folium.map.FeatureGroup()

for lat, lng, in zip(test_cor.Latitude,test_cor.Longitude):
    incidents.add_child(
        folium.CircleMarker(
            [lat, lng],
            radius=5, # define how big you want the circle markers to be
            color='red',
            fill=True,
            fill_color='darkgreen',
            fill_opacity=0.6
        )
    )

names = []
for name,lat, lng, in zip(bus_stop.Name,bus_stop.Latitude,bus_stop.Longitude):
    names.append(name)
    marker = folium.Marker(location=[lat, lng], popup=name).add_to(m)    
print(names) 

m.add_child(incidents)        

window = Tk()
window.title("Where would yo go?")
window.geometry("640x440+0+0")

heading = Label(window, text="Finding The Best Route", font=("arial",30,"italic"), fg="steelblue").pack()
label1 = Label(window, text="Enter source: ", font=("arial",20,"bold"), fg="black").place(x=10,y=100)
label2 = Label(window, text="Enter destination: ", font=("arial",20,"bold"), fg="black").place(x=10,y=150)

source =  StringVar(value=''); destination = StringVar(value='');
large_font= ('Verdana',20)
entry1 = Entry(window, textvariable=source, font=large_font, width=20, bg="lightgreen").place(x=250, y=100)
entry2 = Entry(window, textvariable=destination, font=large_font, width=20, bg="lightgreen").place(x=250, y=150)

start = ''; end =''
def search():
    global start; global end;
    start = str(source.get()); end = destination.get()
    # print ( str(source.get()), destination.get() )
    window.destroy()
work = Button(window, text="Search", width=20, height=2, bg="lightblue", command=search).place(x=250, y=200)

window.mainloop()

# dijk.dijkstra(graph, 'Sule', 'Bar Lan')
# start = input("Type a new source: ")
# end = input("Type a new destination : ")

# shortest_path = shortest_path.dijkstra(distance_fixed.graph, start, end)
# shortest_path = shortest_path.dijkstra(distance_fixed.dictionary, start, end)

# path = dijk.dijkstra(distance_fixed.graph, start, end)
# path = dijk.dijkstra(distance_fixed.dictionary, start, end) 
# print(path)

shortest_path = sp.dijsktra(sp.graph, start, end)

# path = []
# path.append( dijk.dijkstra(dictionary.dictionary, start, end) )

# print("sp" , shortest_path)
print("dijkstra is" , shortest_path)

toDraw= []; poly =[];

for p in shortest_path:
    for name,lat,lng in zip(test_cor.Name,test_cor.Latitude,test_cor.Longitude):            
        if p == name:
            # print (name, lat , lng); # break;
            # toDraw.append(lat); toDraw.append(lng);            
        # else: print(p)
            # poly.append( [lat , lng] )
            # print("line will connect " , name)
            toDraw.append( { 'name': name,'lat': lat,"lng": lng } ) 


for idx, word in enumerate(shortest_path):
    # print (idx, word)
    for name,lat,lng in zip(bus_stop.Name,bus_stop.Latitude,bus_stop.Longitude): 
            if word == name:
                poly.append( [lat , lng] )

            

# print ("Polyline" , poly)

# print(toDraw); print (toDraw[0]['lat'])
# for i in toDraw:
#     print (i['lat'])

folium.PolyLine(poly, color="red", weight=3.5, opacity=1).add_to(m)
m.save("index1.html")

webbrowser.open_new_tab("index1.html")