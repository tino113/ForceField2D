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
        self.initRandomColors()
            
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

    def drawParts(self,sMult = 1):
        layer = createGraphics(width,height)
        layer.beginDraw()
        layer.clear()
        # draw each particle
        for p in self.particles:
            layer.strokeWeight(p.size * sMult)
            layer.stroke(p.col)
            layer.fill(p.col)
            layer.point( p.pos.x , p.pos.y )
        layer.endDraw()
        image(layer,0,0)
        
    def drawVels(self,s = 1,mult = 1,col = color(0,255,0,200)):
        layer = createGraphics(width,height)
        layer.beginDraw()
        layer.clear()
        layer.fill(col)
        layer.strokeWeight(s)
        layer.stroke(col)
        # draw each particle velocity
        for p in self.particles:
            eol = p.pos + p.vel * mult
            eol2 = p.vel * 0.2 * mult
            tri = eol - eol2
            layer.line( p.pos.x , p.pos.y, eol.x , eol.y )
            norml = PVector(p.vel.x,p.vel.y)
            norml = norml.rotate(HALF_PI) * mult * 0.1
            layer.triangle( eol.x , eol.y,
                            tri.x + norml.x , tri.y + norml.y,
                            tri.x - norml.x , tri.y - norml.y )
        layer.endDraw()
        image(layer,0,0)
        
    def drawForces(self,s = 1,mult = 1,col = color(255,0,255,200)):
        layer = createGraphics(width,height)
        layer.beginDraw()
        layer.clear()
        layer.fill(col)
        layer.strokeWeight(s)
        layer.stroke(col)
        # draw each particle velocity
        for p in self.particles:
            eol = p.pos + p.force * mult
            eol2 = p.force * 0.2 * mult
            tri = eol - eol2
            layer.line( p.pos.x , p.pos.y, eol.x , eol.y )
            norml = PVector(p.force.x,p.force.y)
            norml = norml.rotate(HALF_PI) * mult * 0.1
            layer.triangle( eol.x , eol.y,
                            tri.x + norml.x , tri.y + norml.y,
                            tri.x - norml.x , tri.y - norml.y )
        layer.endDraw()
        image(layer,0,0)
    
    def damp(self,factor):
        for p in self.particles:
            p.damp(factor)
    
    def simulate(self,timestep,speed = 1):
        for p in self.particles:
            p.simulate(timestep, speed)