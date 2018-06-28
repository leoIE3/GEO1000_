# GEO1000 - Assignment 3
# Authors: Leonardo Melo & Arjang Tajbakhsh
# Studentnumbers: 4690923 & 4628853

def read_asc(file_nm):
    
    var = {"NROWS":0,
           "NCOLS":1,
           "XLLCORNER":2,
           "YLLCORNER":3,
           "CELLSIZE":4,
           "NODATA_VALUE":5}
    
    #Since the order of the info rows changes, must by able to assign them to the right place
    with open(file_nm) as fin: content = fin.readlines()
    mylist = [None]*6
    for i in range (6):
        my_split=content[i].split()
        mylist[var[my_split[0]]]=my_split[1]
    esri = (int(mylist[0]),int(mylist[1]),float(mylist[2]),float(mylist[3]),float(mylist[4]),int(mylist[5]))
    
    #In some files, the data is separated by '\n' to represent the next row and in 
    #others it is all continuous. This segment converts them all into the same format
    temp = content[6:]
    temp = ''.join(temp)
    content[6]=temp
    
    #Convert line of data to grid
    data = content[6].split()
    data_grid=[]
    for i in range(esri[0]):
        row=[]
        for j in range (esri[1]):
            row.append(int(data[i*esri[1]+j]))
        data_grid.append(row)
    #Add data grid to the rest of the information
    esri += (data_grid,)
    return esri

def rowcol_to_xy(cur_row, cur_col, rows, cols, xll, yll, size):
    x=xll+cur_col*size+size/2
    y=yll+(rows-cur_row)*size+size/2    
    return (x, y)

def marching_squares(rows, cols, xll, yll, size, nodataval, raster):
    #Store cases and their line segments in a dictionary
    cases = {0:[[]],
                1:[[(0,0.5),(0.5,0)]],
                2:[[(0.5,0),(1,0.5)]],
                3:[[(0,0.5),(1,0.5)]],
                4:[[(1,0.5),(0.5,1)]],
                5:[[(0.5,0),(1,0.5)],[(0.5,1),(0,0.5)]],
                6:[[(0.5,0),(0.5,1)]],
                7:[[(0.5,1),(0,0.5)]],
                8:[[(0.5,1),(0,0.5)]],
                9:[[(0.5,0),(0.5,1)]],
                10:[[(0.5,0),(0,0.5)],[(1,0.5),(0.5,1)]],
                11:[[(1,0.5),(0.5,1)]],
                12:[[(0,0.5),(1,0.5)]],
                13:[[(0.5,0),(1,0.5)]],
                14:[[(0,0.5),(0.5,0)]],
                15:[[]]}
    
    #Stores the individual line segments
    segments=[]
        
    for i in range(rows-1):
        for j in range(cols-1):
            val=raster[i][j]*8+raster[i][j+1]*4+raster[i+1][j+1]*2+raster[i+1][j]*1
            xy=rowcol_to_xy(i+1,j,rows,cols,xll,yll,size)
            #Some cases have two line segments
            for seg in cases[val]:
                #As long as the case has a line (i.e. is not 0 or 15) write it
                if seg <> []:
                    p1=[xy[0]+size*seg[0][0],xy[1]+size*seg[0][1]]
                    p2=[xy[0]+size*seg[1][0],xy[1]+size*seg[1][1]]
                    segments.append([p1,p2])
    return segments
    
def wkt(segment):
    return "LINESTRING(%f %f, %f %f)\n" % (segment[0][0],segment[0][1],segment[1][0],segment[1][1])

def write_segments(segments, out_file_nm):
    with open(out_file_nm, 'w') as fout:
        fout.write ("geometry\n")
        for seg in segments: fout.write(wkt(seg))

def convert(file_nm):
    (rows, cols, xll, yll, size, nodataval, data) =  read_asc(file_nm)
    segments = marching_squares(rows, cols, xll, yll, size, nodataval, data)
    write_segments(segments, "out.wkt")

def main():
    convert(raw_input("Which file to convert? >>>"))
    print "Done, result stored to out.wkt"

if __name__ == "__main__":
    main()