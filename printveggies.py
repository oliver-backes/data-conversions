vegetables = [
	{"name": "carrot"},
	{"name": "tomato"},
	{"name": "basil"},
	{"name": "eggplant"},
	{"name": "potato"},
	{"name": "pea"},
]	

import csv

#Write header file to csv
with open('veggies.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['Name', "Length"])
#Loop through each vegetable
	for veggie in vegetables: 
		name = veggie["name"]
		length = len(name)
#For each vegetable, write a row to the csv
		writer.writerow([name, length])