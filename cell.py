"""
Cell Class definition
"""

class cell():
    
    origin = PVector(0,0)
    w = 0
    h = 0
    force = PVector(0,0)
    partsInCell = 0
    
    def init(self,origin = PVector(),w = 1,h = 1, force = PVector(0,0)):
        self.origin = origin
        self.w = w
        self.h = h
        self.force = force
        
    def getOrigin(self):
        return self.origin
        
    def addForce(self,force):
        self.force += force
        
    def posInCell(self,pos):
        if pos.x > self.origin.x and pos.x < self.origin.x + self.w and pos.y > self.origin.y and pos.y < self.origin.y + self.h:
            return True        
        return False
    
    def incrParts(self):
        self.partsInCell += 1
    
    def averageForce(self):
        if self.partsInCell > 0:
            self.force = PVector(self.force.x / self.partsInCell,self.force.y / self.partsInCell)
            return True
        return False