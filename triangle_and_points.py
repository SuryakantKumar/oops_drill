import math


class Triangle:
    def __init__(self):
        '''Create an instance of list of points'''
        self.points = []

    def add_points(self, point):
        '''Add point to list of points'''
        if len(self.points) < 3:
            self.points.append(point)

    def perimeter(self):
        '''Compute parameter of triangle'''
        point1, point2, point3 = tuple(self.points)
        x1, y1 = point1
        x2, y2 = point2
        x3, y3 = point3

        first_side = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        second_side = math.sqrt((x2-x3)**2 + (y2-y3)**2)
        third_side = math.sqrt((x1-x3)**2 + (y1-y3)**2)

        perimeter = first_side + second_side + third_side

        return round(perimeter, 2)

    def __eq__(self, triangle):
        '''Check for equality of points of two triangles'''
        return set(self.points) == set(triangle.points)


t1 = Triangle()
t1.add_points((0, 0))
t1.add_points((0, 3))
t1.add_points((4, 0))
print(t1.perimeter())

t2 = Triangle()
t2.add_points((1, 2))
t2.add_points((2, 1))
t2.add_points((1, 5))
print(t2.perimeter())

# print(t1.is_equal(t2))

t3 = Triangle()
t3.add_points((1, 2))
t3.add_points((2, 1))
t3.add_points((1, 5))


print(t1 == t3)
# print(t1.is_equal(t3))
# print(t3.is_equal(t1))

print(t2 == t3)
