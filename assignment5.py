class Point:

    def __init__(self,x,y,z):
        self.x =x
        self.y =y
        self.z =z

    def sqsum(self):
        return (self.x**2 + self.y**2 + self.z**2)
    
d=Point(1,3,5)
d.sqsum()
print(d.sqsum())