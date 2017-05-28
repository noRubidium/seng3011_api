import json

csvfile = open('pe.csv', 'r')
jsonfile = open('pe.json', 'w')

result = dict()

for l in csvfile:
