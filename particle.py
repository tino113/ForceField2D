"""
Particle Class definition
"""

class particle():
    
    pos = PVector(0,0)
    force = PVector(0,0)
    vel = PVector(0,0)
    col = color(255)
    size = 1
    
    def init(self):
            self.pos = PVector(0,0)
            self.force = PVector(0,0)
            self.vel = PVector(0,0)
            self.cols = color(255)
            self.size = 1
            
    def setPos(self,pos):
        self.pos = pos
    
    def setCol(self,col):
        self.col = col
        
    def addVel(self,vel):
        self.vel += vel

    def addForce(self,force):
        self.force += force
    
    def forceToVel(self):
        self.vel += self.force
        self.force = PVector(0,0)
        
    def damp(self,factor):
        self.force -= self.vel * factor
    
    def simulate(self,speed):
        self.pos += self.vel * speed
        self.forceToVel()