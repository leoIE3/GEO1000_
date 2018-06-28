# GEO1000 - Assignment 2
# Authors: Leonardo Melo	
# Studentnumbers: 4690923

import math

def haversin(latlon1, latlon2):
  
  delta_lat=latlon1[0]-latlon2[0]
  delta_lon=latlon1[1]-latlon2[1]
  
  #Conversion from degrees to radians
  lat1_rad=math.radians(latlon1[0])
  lat2_rad=math.radians(latlon2[0])
  lon1_rad=math.radians(latlon1[1])
  lon2_rad=math.radians(latlon2[1])
  delta_lat_rad=math.radians(delta_lat)
  delta_lon_rad=math.radians(delta_lon)

	#lat is phi
	#lon is lambda
	#distance is Delta delta
    
  A=math.sin(delta_lat_rad/2.0)
  B=math.sin(delta_lon_rad/2.0)
  C=math.cos(lat1_rad)
  D=math.cos(lat2_rad)
  distance=6371.0*2.0*math.asin(math.sqrt((A*A)+(C*D*B*B)))
  
  return distance
	



def _test():
    print 'The distance between the 2 points is: %0.4f kms' %(haversin((51.99945997222222,4.36272452777778),(-48.1359085,17.15974405555556)))	
   


if __name__ == "__main__":
    _test()
