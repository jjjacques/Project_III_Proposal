import csv
import json

csvfile = open('HQ1-company_location.csv', 'r')
jsonfile = open('HQ1-company_location1.json', 'w')

fieldnames = ("Company","Exchange","Symbol","Industry","Address","Lat","Long")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write(',\n')