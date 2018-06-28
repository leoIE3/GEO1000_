# GEO1000 - Assignment 3
# Authors: Leonardo Melo & Arjang Tajbakhsh
# Studentnumbers: 4690923 & 4628853

def read_points(file_nm, max_points = 0):
    my_list = []
    with open('pointcloud.off') as fin:
        #Read the heading row
        fin.readline()
        #Counter
        n = 0
        for i in fin:
            line = i.strip().split()
            #Ensure all lines are in the correct format (7 values)
            if len(line) == 7:
                new_tuple = (float(line[0]),float(line[1]),float(line[2]),int(line[3]),int(line[4]),int(line[5]),int(line[6]))
                my_list.append(new_tuple)
                n+=1
            if max_points <> 0 and n == max_points:
                break
    return my_list


def bbox(pts):
    #Intitially store bounds as a list of list so you can change them. 
    #To start, set the first min/max as the value of the first row
    extents = [pts[0][0],pts[0][1],pts[0][2],pts[0][0],pts[0][1],pts[0][2]]
   
    for i in pts:
        for d in range (0,3):
            if i[d]<extents[d]:
                extents[d]=i[d]
        for d in range (0,3):
            if i[d]>extents[d+3]:
                extents[d+3]=i[d]
    
    #finally convert list of list to list of tuple
    extents_tup = [(extents[0],extents[1],extents[2]),(extents[3],extents[4],extents[5])]
    return extents_tup

def _test():
    pts = read_points('pointcloud.off', 150)
    print bbox(pts)


if __name__ == '__main__':
    _test()
