class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)


pt = Point()
pt.set_coords(1, 2)
print(pt.__dict__)
print(pt.get_coords())


pt2 = Point()
pt2.set_coords(3, 5)
print(pt2.__dict__)
print(pt2.get_coords())
