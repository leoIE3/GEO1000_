# GEO1000 - Assignment 4
# Author:
# Studentnumber:

import math


class Point(object):
    def __init__(self, x, y):
        """Constructor"""
        self.x = x
        self.y = y

    def __str__(self):
        """Well Known Text of this point
        """
        return "POINT({} {})".format(self.x, self.y)

    def __eq__(self, other):
        """Compare values (this object instance == other instance?).
        
        :param other: the point to compare with
        :type other: Point
        
        Returns True/False
        """
        if self.x == other.x and self.y==other.y:
            return True
        else:
            return False
        

    def distance(self, other):
        """Returns distance as float to the *other* point 
        (assuming Euclidean geometry)

        :param other: the point to compute the distance to
        :type other: Point
        """
        dx=self.x-other.x
        dy=self.y-other.y
        return math.sqrt(dx**2+dy**2)
        


class Circle(object):
    def __init__(self, center, radius):
        """Constructor"""
        self.center = center
        self.radius = float(radius)

    def __str__(self):
        """Returns WKT str, discretizing the circle into straight
        line segments
        """
        N = 400
        step = 2.0 * math.pi / N
        pts = []
        for i in range(N):
            pts.append(Point(self.center.x + math.cos(i * step) * self.radius, 
                             self.center.y + math.sin(i * step) * self.radius))
        pts.append(pts[0])
        coordinates = ["{0} {1}".format(pt.x, pt.y) for pt in pts]
        coordinates = ", ".join(coordinates)
        return "POLYGON(({0}))".format(coordinates)

    def covers(self, pt):
        """Returns True when the circle covers point *pt*, 
        False otherwise

        Note that we consider points that are near to the boundary of the 
        circle also to be covered by the circle
        (arbitrary epsilon to use: 1e-8).
        """
#        dx=self.center.x-pt.x
#        dy=self.center.y-pt.y
#        distance=math.sqrt(dx**2+dy**2)
         
        if round(self.center.distance(pt),8)<=round(self.radius,8):
            return True
        else:
            return False

    def area(self):
        """Returns area as float of this circle
        """
        return float(math.pi*self.radius**2)
        # Your implementation here

    def perimeter(self):
        """Returns perimeter as float of this circle
        """
        return float(2*math.pi*self.radius)
    
class Triangle(object):
    def __init__(self, p0, p1, p2):
        """Constructor
        
        Arguments: p0, p1, p2 -- Point instances
        """
        self.p0, self.p1, self.p2 = p0, p1, p2

    def __str__(self):
        """String representation
        """
        points = ["{0.x} {0.y}".format(pt) for pt in (self.p0, self.p1, self.p2, self.p0)]
        return "POLYGON(({0}))".format(", ".join(points))

    def circumcircle(self):
        """Returns Circle instance that intersects the 3 points of the triangle
        """
        #for X
        coef1_x=(self.p0.x**2+self.p0.y**2)*(self.p1.y-self.p2.y)
        coef2_x=(self.p1.x**2+self.p1.y**2)*(self.p2.y-self.p0.y)
        coef3_x=(self.p2.x**2+self.p2.y**2)*(self.p0.y-self.p2.y)
        #for y
        coef1_y=(self.p0.x**2+self.p0.y**2)*(self.p2.x-self.p1.x)
        coef2_y=(self.p1.x**2+self.p1.y**2)*(self.p0.x-self.p2.x)
        coef3_y=(self.p2.x**2+self.p2.y**2)*(self.p1.x-self.p0.x)
        
        
        #calculation of the circumcenter
        D=2.0*(self.p0.x*(self.p1.y-self.p2.y)+self.p1.x*(self.p2.y-self.p0.y)+self.p2.x*(self.p0.y-self.p1.y))
        ux=(coef1_x+coef2_x+coef3_x)/D
        uy=(coef1_y+coef2_y+coef3_y)/D
        
        #Radius
        A=math.sqrt((self.p0.x-self.p1.x)**2+(self.p0.y-self.p1.y)**2)
        B=math.sqrt((self.p1.x-self.p2.x)**2+(self.p1.y-self.p2.y)**2)
        C=math.sqrt((self.p0.x-self.p2.x)**2+(self.p0.y-self.p2.y)**2)
        radius=(A*B*C)/(math.sqrt((A+B+C)*(B+C-A)*(C+A-B)*(A+B-C)))
        #print ux,uy,radius
        
        return Circle(Point(ux,uy),radius)
        
        # Your implementation here

    def area(self):
        """Area of this triangle, using heron's formula."""
        A=math.sqrt((self.p0.x-self.p1.x)**2+(self.p0.y-self.p1.y)**2)
        B=math.sqrt((self.p1.x-self.p2.x)**2+(self.p1.y-self.p2.y)**2)
        C=math.sqrt((self.p0.x-self.p2.x)**2+(self.p0.y-self.p2.y)**2)
        S=(A+B+C)/2
        return math.sqrt(S*(S-A)*(S-B)*(S-C))
        # Your implementation here

    def perimeter(self):
        """Perimeter of this triangle (float)"""
        A=math.sqrt((self.p0.x-self.p1.x)**2+(self.p0.y-self.p1.y)**2)
        B=math.sqrt((self.p1.x-self.p2.x)**2+(self.p1.y-self.p2.y)**2)
        C=math.sqrt((self.p0.x-self.p2.x)**2+(self.p0.y-self.p2.y)**2)
        return (A+B+C)
        # Your implementation here


class DelaunayTriangulation(object):
    def __init__(self, points):
        """Constructor"""
        self.triangles = []
        self.points = points

    def triangulate(self):
        """Triangulates the given set of points.

        This method takes the set of points to be triangulated 
        (with at least 3 points) and for each 3-group of points instantiates 
        a triangle and checks whether the triangle conforms to Delaunay 
        criterion. If so, the triangle is added to the triangle list.

        To determine the 3-group of points, the group3 function is used.

        Returns None
        """
        # pre-condition: we should have at least 3 points
        i=0
        lista_t=[]
        assert len(self.points) > 2
        #print self.points[1].x
        gen=group3(len(self.points))
       # print range(math.factorial(len(self.points))/(math.factorial(3)*math.factorial(len(self.points)-3)))
        #print math.factorial(3)
        #print math.factorial(len(self.points)-3)
        for ite in range(math.factorial(len(self.points))/(math.factorial(3)*math.factorial(len(self.points)-3))):
            pos1,pos2,pos3=next(gen)
            #temp=[(self.points[pos1],(self.points[pos2].x,self.points[pos2].y),(self.points[pos3].x,self.points[pos3].y)]
            t=Triangle(self.points[pos1],self.points[pos2],self.points[pos3])
            if not self.are_collinear(self.points[pos1],self.points[pos2],self.points[pos3]):
                #print 'hello'
           # print self.points[pos1],self.points[pos2],self.points[pos3]
           # print self.points[1]
           # print t,pos1,pos2,pos3
                if self.is_delaunay(t):
                    #print t
                    self.triangles.append(t)
        #print lista_t   
                
        # Your implementation here

    def is_delaunay(self, tri):
        """Does a triangle *tri* conform to the Delaunay criterion?
        
        Algorithm:
        
        Are 3 points of the triangle collinear?
            No:
                Get circumcircle
                Count number of points inside circumcircle
                if number of points inside == 3:
                    Delaunay
                else:
                    not Delaunay
            Yes:
                not Delaunay
        
        Arguments:
            tri -- Triangle instance
        Returns:
            True/False
        """
        circumcircle=tri.circumcircle()
        count=0
        for point in (tri.p0,tri.p1,tri.p2):
            if circumcircle.covers(point):
                #print 'yes'
                count+=1
        if count==3:
            #print count
            return True
        else:
            return False
         #Your implementation here

    def are_collinear(self, pa, pb, pc):
        """Orientation test to determine whether 3 points are collinear
        (on a straight line).
        
        Note that we consider points that are nearly collinear also to be on 
        a straight line (arbitrary epsilon to use: 1e-8).
        
        Returns True / False
        """
        t=Triangle(pa,pb,pc)
        area=t.area()
        #print area
        if round(area,8)>0:
            return False
        else:
            return True
        # Your implementation here

    def output_points(self, open_file_obj):
        """Outputs the points of the triangulation to an open file.
        """
        #print self.triangles[1]
        open_file_obj.write('wkt\n')
        for i in range(len(self.triangles)):
            open_file_obj.write('%s\n%s\n%s\n'%(self.triangles[i].p0,self.triangles[i].p1,self.triangles[i].p2))
            
        # Your implementation here

    def output_triangles(self, open_file_obj):
        """ Outputs the triangles of the triangulation to an open file object .
        Use a tab as delimiter of the values to be written .
            """
        open_file_obj.write('wkt\ttid\tarea\tperimeter\n')
        for i in range(len(self.triangles)):
            open_file_obj.write('%s\t%d\t%s\t%s\n'%(self.triangles[i],i,self.triangles[i].area(),self.triangles[i].perimeter()))
        # Your implementation here

    def output_circumcircles(self, open_file_obj):
        """Outputs the circumcircles of the triangles of the triangulation
        to an open file object.


        Use a tab as delimiter of the values to be written.
        """
        open_file_obj.write('wkt tid area perimeter\n')
        for i in range(len(self.triangles)):
            open_file_obj.write('%s\t%d\t%s\t%s\n'%(self.triangles[i].circumcircle(),i,self.triangles[i].area(),self.triangles[i].perimeter()))
        # Your implementation here


def group3(N):
    """Returns a generator object with 3-tuples with indices to form 3-groups
    of a list of length N.

    Total number of tuples that is generated: N! / (3! * (N-3)!)

    For N = 3: [(0, 1, 2)]
    For N = 4: [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
    For N = 5: [(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 2, 3), 
                (0, 2, 4), (0, 3, 4), (1, 2, 3), (1, 2, 4), 
                (1, 3, 4), (2, 3, 4)]

    Example use:

        >>> for item in group3(3):
        ...     print item
        ... 
        (0, 1, 2)

    """
    # See for more information about generators for example:
    # https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
    for i in xrange(N - 2):
        for j in xrange(i+1, N - 1):
            for k in xrange(j+1, N):
                yield (i, j, k)


def make_random_points(n):
    """Makes n points distributed randomly in x,y between [0,1000]

    Note, no duplicate points will be created, but might result in slightly 
    less than the n number of points requested.
    """
    import random
    pts = list(set([Point(random.randint(0,1000),
                          random.randint(0,1000)) for i in xrange(n)]))
    return pts


def main(n):
    """Perform triangulation of n points and write the resulting geometries
    to text files.
    """
    pts = make_random_points(n)
    
    dt = DelaunayTriangulation(pts)
    dt.triangulate()
    # using the with statement, we do not need to close explicitly the file
    # see e.g. this blog post:
    # https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/
    with open("points.wkt", "w") as fh:
        dt.output_points(fh)
    with open("triangles.wkt", "w") as fh:
        dt.output_triangles(fh)
    with open("circumcircles.wkt", "w") as fh:
        dt.output_circumcircles(fh)


def _test():
    # If you want, you can write tests in this function
    pass


if __name__ == "__main__":
    main(50)
