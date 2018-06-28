# GEO1000 - Assignment 1
# Authors: Leonardo Melo
# Studentnumbers: 4690923

def mi_km(value, nautical):
    #1 mile = 1609.344 meter
	#1 nautical mile = 1852 meter
	if type(nautical)!=bool:
		print "Nautical should be of type boolean"
		return
	if nautical==True:
		conversion=value*1.852
		print conversion,'kilometers'
	elif nautical==False:
		conversion=value*1.609344
		print conversion,'kilometers'
	else: 
		print "Nautical should be true or false"
	

def km_mi(value, nautical):
    #1 mile = 1609.344 meter
	#1 nautical mile = 1852 meter
	if type(nautical)!=bool:
		print "Nautical should be of type boolean"
		return
	if nautical==True:
		conversion=value/1.852
		print conversion,'nautical miles'
	elif nautical==False:
		conversion=value/1.609344
		print conversion,'miles'
	

def kmh_ms(value):
    conversion=value*1000.0/3600.0
    print conversion, 'm.s'
	
def ms_kmh(value):
	conversion=value/1000.0*3600.0
	print conversion,'km/h'
	
mi_km(7, False)

#km_mi(5, False)

#kmh_ms(10)

#ms_kmh(1)
