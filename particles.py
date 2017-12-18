"""
Particles Class definition
"""

import particle

class particles():
    
    particles = []
    minX = 0
    maxX = 0
    minY = 0
    maxY = 0
    numParts = 0
    
    def init(self, numParts):
        self.numParts = numParts
        for i in range(numParts):
            p = particle.particle()
            p.init()
            self.particles.append(p)
            
    def checkMinMax(self,pos):
        if pos.x < self.minX:
            self.minX = pos.x
        elif pos.x > self.maxX:
            self.maxX = pos.x
        if pos.y < self.minY:
            self.minY = pos.y
        elif pos.y > self.maxY:
            self.maxY = pos.y
    
    def initRandomLocs(self, f = PVector(0,0), t = PVector(0,0)):
        for i in range(self.numParts):
            self.particles[i].setPos(PVector(random(f.x,t.x),random(f.y,t.y)))
            self.checkMinMax(self.particles[i].pos)
            
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

    def drawParts(self,s = 1,col = color(255)):
        layer = createGraphics(ceil(self.maxX-self.minX),ceil(self.maxY-self.minY))
        layer.beginDraw()
        layer.clear()
        layer.noFill()
        layer.strokeWeight(s)
        layer.stroke(col)
        # draw each particle
        for p in self.particles:
            layer.point( p.pos.x , p.pos.y )
        layer.endDraw()
        image(layer,floor(self.minX),floor(self.minX))
        
    def drawVels(self,s = 1,mult = 1,col = color(0,255,0,200)):
        layer = createGraphics(ceil(self.maxX-self.minX),ceil(self.maxY-self.minY))
        layer.beginDraw()
        layer.clear()
        layer.noFill()
        layer.strokeWeight(s)
        layer.stroke(col)
        # draw each particle velocity
        for p in self.particles:
            layer.line( p.pos.x , p.pos.y, p.pos.x + p.vel.x * mult , p.pos.y + p.vel.y * mult )
        layer.endDraw()
        image(layer,floor(self.minX),floor(self.minX))
        
    def drawForces(self,s = 1,mult = 1,col = color(255,0,255,200)):
        layer = createGraphics(ceil(self.maxX-self.minX),ceil(self.maxY-self.minY))
        layer.beginDraw()
        layer.clear()
        layer.noFill()
        layer.strokeWeight(s)
        layer.stroke(col)
        # draw each particle velocity
        for p in self.particles:
            layer.line( p.pos.x , p.pos.y, p.pos.x + p.force.x * mult , p.pos.y + p.force.y * mult )
        layer.endDraw()
        image(layer,floor(self.minX),floor(self.minX))