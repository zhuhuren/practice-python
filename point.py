import math

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY
    def __str__(self):
        return 'x = {}, y = {}'.format(self.x, self.y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def distanceFromPoint(self, target):
        dist = math.sqrt((self.x - target.x)**2 + (self.y - target.y)**2)
        return dist
    
    def reflect_x(self):
        return Point(self.x, -self.y)
    
    def slope_from_origin(self):
        return self.y / self.x

    def pt_slope_to_y(self, slope):
        return self.y - slope * self.x

    def midpoint(self, target):
        return Point((self.x + target.x)/2, (self.y + target.y)/2)
    
    def get_line_to(self, target):
        slope = (self.y - target.y)/(self.x - target.x)
        pt = self if target.x == 0 else target
        return slope, pt.y - slope * pt.x

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

def three_pt_circle(pt1, pt2, pt3):
    s1a = pt1.get_line_to(pt2)[0]
    print('s1a: ', s1a)
    s1 = - (1 / s1a)
    print('s1: ', s1)
    mpt1 = pt1.midpoint(pt2)
    print('mpt1: ', mpt1)
    y1 = mpt1.pt_slope_to_y(s1)
    print('y1: ', y1)
    s2a = pt2.get_line_to(pt3)[0]
    print('s2a: ', s2a)
    s2 = - (1 / s2a)
    print('s2: ', s2)
    mpt2 = pt2.midpoint(pt3)
    print('mpt2: ', mpt2)
    y2 = mpt2.pt_slope_to_y(s2)
    print('y2: ', y2)
    x = (y2-y1) / (s1 - s2)
    y = (s2 * y1 - s1 * y2) / (s2 - s1)
    pt = Point(x, y)
    radius = pt.distanceFromPoint(pt1)
    return str(pt), radius
    

if __name__ == '__main__':
    p = Point(3, 5)
    print(p)
    print(p.reflect_x())
    print(Point(4, 10).slope_from_origin())
    print(Point(4, 11).get_line_to(Point(6, 15)))
    p.move(-3, -8)
    print(three_pt_circle(Point(2, 8), Point(4, 15), Point(9, 17)))
    


