
class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def MoveLocation(self, delX, delY):
        return Location(self.x + delX, self.y + delY)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def DistanceFrom(self, other):
        otherX, otherY = other.getX(), other.getY()
        distance = ((otherX - self.getX())**2 + (otherY - self.getY())**2)**(1/2)

        return distance
        
    def __str__(self):
        return f"X = {self.getX()} , Y = {self.getY()}"
    
    def __repr__(self):
            return self.__str__()
        

