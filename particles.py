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
            p = particle.particle()
            p.init()
            self.particles.append(p)
    
    def initRandomLocs(self, f = PVector(0,0), t = PVector(0,0)):
        for i in range(self.numParts):
            self.particles[i].setPos(PVector(random(f.x,t.x),random(f.y,t.y)))
            
    def addRandomVels(self, s = PVector(0,0), e = PVector(0,0)):
        for i in range(self.numParts):
            self.particles[i].addVel(PVector(random(s.x,e.x),random(s.y,e.y)))
            
    def addRandomForces(self, s = PVector(0,0), e = PVector(0,0)):
        for i in range(self.numParts):
            self.particles[i].addForce(PVector(random(s.x,e.x),random(s.y,e.y)))

    def initRandomColors(self):
        for i in range(self.numParts):
            r = random(0,255)
            g = random(0,255)
            b = random(0,255)
            self.particles[i].setCol(color(r,g,b))
            
    def getPositions(self):
        positions = []
        for p in self.particles:
            positions.append(p.pos)
        return positions
    
    def getForces(self):
        forces = []
        for p in self.particles:
            forces.append(p.force)
        return forces
    
    def getColors(self):
        colors = []
        for p in self.particles:
            colors.append(p.col)
        return colors