# GEO1000 - Assignment 2
# Authors: Leonardo Melo	
# Studentnumbers: 4690923 


import math
def dd_dms(decdegrees):
  d=int(decdegrees)
  m=int((decdegrees-d)*60)
  s=(decdegrees-d-(m/60.0))*3600.0
  d=float(d)
  m=float(m)
  s=float(s)
  return (d,m,s)
    
def format_ordinate(ordinate, latitude):
  if latitude==True:
  
    if ordinate[0]>=0:
      return 'N'+'{:>4}'.format("%d"%(ordinate[0]))+'{:>3}'.format("%d"%(ordinate[1]))+"'"+'{:>8}\"'.format('%.4f'%(ordinate[2]))
    else:
      A=math.fabs(ordinate[0])
      B=math.fabs(ordinate[1])
      C=math.fabs(ordinate[2])
      return 'S'+'{:>4}'.format("%d"%(A))+'{:>3}'.format("%d"%(B))+"'"+'{:>8}\"'.format('%.4f'%(C))
  else:
    if ordinate[0]>=0: 
      return 'E'+'{:>4}'.format("%d"%(ordinate[0]))+'{:>3}'.format("%d"%(ordinate[1]))+"'"+'{:>8}\"'.format('%.4f'%(ordinate[2]))
    else:
      A=math.fabs(ordinate[0])
      B=math.fabs(ordinate[1])
      C=math.fabs(ordinate[2])
      return 'W'+'{:>4}'.format("%d"%(A))+'{:>3}'.format("%d"%(B))+"'"+'{:>8}\"'.format('%.4f'%(C))
    
def format_dd_as_dms(coordinate):
    #dd to dms conversion
    lat=dd_dms(coordinate[0])
    lon=dd_dms(coordinate[1])
    #dms to string
    lat1=format_ordinate(lat,1)
    lon1=format_ordinate(lon,0)
    return lat1+','+' '+lon1
 
def _test():
    
    # Expected output:
    #N   0  0'  0.0000", E   0  0'  0.0000"
    #N  52  0'  0.0000", E   4 19' 43.3200"
    #S  52  0'  0.0000", E   4 19' 43.3200"
    #N  52  0'  0.0000", W   4 19' 43.3200"
    #S  52  0'  0.0000", W   4 19' 43.3200"
    #N  45  0'  0.0000", E 180  0'  0.0000"
    #S  45  0'  0.0000", W 180  0'  0.0000"
    #S  50 27' 24.1200", E   4 19' 43.3200"
    coordinates = [(0.0, 0.0),
        (52, 4.3287),
        (-52, 4.3287),
        (52, -4.3287),
        (-52, -4.3287),
        (45.0, 180.0),
        (-45.0, -180.0),
        (-50.4567, 4.3287)]
    for coordinate in coordinates:
        print format_dd_as_dms(coordinate)

if __name__ == "__main__":
    _test()
    


