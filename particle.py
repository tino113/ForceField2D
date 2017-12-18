"""
Particle Class definition
"""

class particle():
    
    pos = PVector(0,0)
    force = PVector(0,0)
    vel = PVector(0,0)
    col = color(255)
    
    def init(self):
            self.pos = PVector(0,0)
            self.force = PVector(0,0)
            self.vel = PVector(0,0)
            self.cols = color(255)
            
    def setPos(self,pos):
        self.pos = pos
    
    def setCol(self,col):
        self.col = col