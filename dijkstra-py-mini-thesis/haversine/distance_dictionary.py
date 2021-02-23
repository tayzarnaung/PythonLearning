import pandas as pd
import csv

dictionary= {}; 
distance = []; header=[]
# header=['a','b','c']
# header = ['Sule', 'Sule Myodaw Hall', 'Yoke Shin Yone']

df = pd.read_csv('sule_shwedagon.csv')
for name in (df.Name):
    header.append(name); 
# print(header)

with open('haversine/distance_csv/distance_run.csv', 'r') as readFile:
	reader = csv.reader(readFile)	
	
	for row in reader:
		sub_dist_row = []
		for column in row:
			# if column == '0': continue;	
			if column == '':	continue;		
			sub_dist_row.append(column)
		# if sub_dist_row != []:
		distance.append(sub_dist_row)
		# print (distance)
	distance = list(filter(None, distance)) #remove empty string([]) arr from string list
	# print(distance)
readFile.close()
# print(header[1])	# print(distance[1][0])


# print(len(header), header)  #length = 3 .i.e index 0,1,2
# for n in range(1,len(header)): #1,2
for n in range(len(header)): #0,1,2	 #row
	sub_dict ={}
	prefix = header[n];	dist = distance[n]
	dist.pop(0) #remove an element from a list by index
	# print('d',dist)

	# sub_dict.update({'a':0,'b':1})
	# dictionary.update({'a':sub_dict})  #{'a': {'a': 0, 'b': 1}}

	for i in range(len(header)):	#0,1,2	#column
		# sub_dict.update({header[i]:1})
		sub_dict.update({header[i]:float(dist[i])})
	# print('s_d',sub_dict)
	dictionary.update({prefix:sub_dict})
# print('final',dictionary)