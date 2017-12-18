"""
Particles Class definition
"""

import particle

class particles():
    
    particles = []
    numParts = 0
    
    def init(self, numParts):
        self.numParts = numParts
        for i in range(numParts):
            p = particle()
            p.init()
            self.particles.append(p)
    
    def initRandomLocs(self, f = PVector(0,0), t = PVector(0,0)):
        for i in range(self.numParts):
            self.particles[i].setPos(random(f,t))

    def initRandomColors(self):
        for i in range(self.numParts):
            r = random(0,255)
            g = random(0,255)
            b = random(0,255)
            self.particles[i].setCol(color(r,g,b))