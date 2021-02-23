import csv
import pandas as pd
	
# SN, Name, City			<--people.csv
# 1, John, Washington
# 2, Eric, Los Angeles
# 3, Brad, Texas

# Example 1: Modifying existing rows of people.csv
row = ['2', ' Marie', ' California']
with open('distance_csv/people.csv', 'r') as readFile:
	reader = csv.reader(readFile)
	lines = list(reader)
	lines[2] = row
with open('distance_csv/people.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)
readFile.close()
writeFile.close()

# Example 2: Appending new rows to people.csv file
row = ['4', ' Danny', ' New York']
with open('distance_csv/people.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)
csvFile.close()

#Example 3: Write a python list into person.csv file
csvData = [['Person', 'Age'], ['Peter', '22'], ['Jasmine', '21'], ['Sam', '24']]
# csvData = ['Person', 'Age', 'Aung Aung', '22']
with open('distance_csv/person.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)
    # writer.writerow(csvData)
    # writer.writerow(['Person', 'Age', 'Aung Aung', '23'])
csvFile.close()

raw_data = pd.read_excel('distance_csv/people.xlsx')
print(raw_data)