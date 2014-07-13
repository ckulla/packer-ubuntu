#!/usr/bin/python

import json

def readBaseTemplate():
	with open('base-template.json', 'r') as infile:
		data = json.load(infile)
		return data

def writeTemplate (data, filename):
	with open(filename, 'w') as outfile:
  		json.dump(data, outfile, indent=2)

data = readBaseTemplate()
writeTemplate (data, "mybox.json")
