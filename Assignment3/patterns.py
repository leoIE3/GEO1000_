# GEO1000 - Assignment 3
# Authors: Leonardo Melo & Arjang Tajbakhsh
# Studentnumbers: 4690923 & 4628853

def wkt(x, y, size):
    p1= str(x-size) + " " + str(y-size)
    p2= str(x+size) + " " + str(y-size)
    p3= str(x+size) + " " + str(y+size)
    p4= str(x-size) + " " + str(y+size)
    
    return "POLYGON((%s, %s, %s, %s, %s))\n" % (p1, p2, p3, p4, p1)

def pattern_a(l, x, y, size, ratio, file_nm):
    if l==0:
        pass
    else:
        #Order of corners doesn't matter with this layer
        with open(file_nm,'a') as fout: fout.write(wkt(x,y,size))
        pattern_a(l-1,x-size,y-size,size/float(ratio),ratio,file_nm)
        pattern_a(l-1,x+size,y-size,size/float(ratio),ratio,file_nm)            
        pattern_a(l-1,x+size,y+size,size/float(ratio),ratio,file_nm)
        pattern_a(l-1,x-size,y+size,size/float(ratio),ratio,file_nm)

def pattern_b(l, x, y, size, ratio, file_nm):
    if l==0:
        pass
    else:
        #Order of corners doesn't matter with this layer
        pattern_b(l-1,x-size,y-size,size/float(ratio),ratio,file_nm)
        pattern_b(l-1,x+size,y-size,size/float(ratio),ratio,file_nm)            
        pattern_b(l-1,x+size,y+size,size/float(ratio),ratio,file_nm)
        pattern_b(l-1,x-size,y+size,size/float(ratio),ratio,file_nm)
        with open(file_nm,'a') as fout: fout.write(wkt(x,y,size))

def pattern_c(l, x, y, size, ratio, file_nm):
    if l==0:
        pass
    else: 
        #Order of corners matters with this layer
        pattern_c(l-1,x-size,y+size,size/float(ratio),ratio,file_nm)
        pattern_c(l-1,x+size,y+size,size/float(ratio),ratio,file_nm)
        with open(file_nm,'a') as fout: fout.write(wkt(x,y,size))
        pattern_c(l-1,x+size,y-size,size/float(ratio),ratio,file_nm)            
        pattern_c(l-1,x-size,y-size,size/float(ratio),ratio,file_nm)
            
def main(n=4, x=0, y=0, size=10, ratio=2):
    out_file_nms = ['pattern_a.txt', 'pattern_b.txt', 'pattern_c.txt']
    funcs = [pattern_a, pattern_b, pattern_c]
    for file_nm, func in zip(out_file_nms, funcs):
        with open(file_nm,'w') as fout: fout.write('geometry\n')
        func(n,x,y,size,ratio,file_nm)

if __name__ == "__main__":
    main()
