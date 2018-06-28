# GEO1000 - Assignment 2
# Authors: Leonardo Melo	
# Studentnumbers: 4690923

import string
from nominatim import nominatim
from dms import format_dd_as_dms
from distance import haversin

def query():
    
	print "I will find the distance for you between 2 places"
	
	Iloop=True
	while Iloop:
		place1=raw_input("Enter place 1 ")
		coord1=nominatim(place1)
		if place1.lower()=='quit':
			return 
		elif coord1==():
			print place1+" was not found, try again"
		else:
			Iloop=False
	
	Iloop=True
	while Iloop:
		place2=raw_input("Enter place 2 ")
		coord2=nominatim(place2)
		if place2.lower()=='quit':
			return 
		elif coord2==():
			print place2+" was not found, try again"
		else:
			Iloop=False
	
	DMS1=format_dd_as_dms(coord1)
	DMS2=format_dd_as_dms(coord2)
	print "Coordinates for "+place1+": "+DMS1
	print "Coordinates for "+place2+": "+DMS2
	distance=haversin(coord1,coord2)
	print "The distance between "+place1+" and "+place2+" is %0.1f kms"%(distance)
	print "\n=====New run!\n"
	
	print "I will find the distance for you between 2 places"
	
	Iloop=True
	while Iloop:
		place1=raw_input("Enter place 1 ")
		coord1=nominatim(place1)
		if place1.lower()=='quit':
			return 
		elif coord1==():
			print place1+" was not found, try again"
		else:
			Iloop=False
	
	Iloop=True
	while Iloop:
		place2=raw_input("Enter place 2 ")
		coord2=nominatim(place2)
		if place2.lower()=='quit':
			return 
		elif coord2==():
			print place2+" was not found, try again"
		else:
			Iloop=False
			
if __name__ == "__main__":
	query()
	