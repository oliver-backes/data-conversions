import csv

#Read veggies.cvs into var = vegetables
with open('veggies.csv') as f:
	reader = csv.DictReader(f)
	vegetables = list(reader)

#Write vegetables as a JSON
import json

with open('vegetables.json', 'w') as f:
	json.dump(vegetables, f, indent=2)