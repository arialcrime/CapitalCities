#########################################################
#
# A simple script to create a random string of city names
# from A to Z and copy that to Robofont’s Space Center. 
# The content in the file cities.txt is based on data 
# from http://www.geonames.org/
#
# 2018 Benedikt Bramböck
# @arialcrime
#
#########################################################

from mojo.UI import OpenSpaceCenter

import collections, random, string, os

letters = string.ascii_uppercase

azcities = ''

alphabetdict = collections.defaultdict(list)
with open('cities.txt', 'r') as cities:
	for city in cities:
		city = city[:-1]
		alphabetdict[city[0].upper()].append(city)

for l in letters: 
	add = random.choice(alphabetdict[l]) + ' '
	azcities += add

# Alternatively copy list of cities to clipboard
# os.system("echo '%s' | pbcopy" % azcities)

sp = OpenSpaceCenter(CurrentFont())
sp.setRaw(azcities)