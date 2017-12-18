"""
Field Engine 2D

Create 'force fields' of arbitrary resolution use this to 
affect the positions and attributes of particles and simulations
https://github.com/tino113/forceField2D.git
"""
import particles
import fField2D

scaleFactor = 5

def unitTests():
    global scaleFactor
    print("Begin Unit Testing!")
    
    #Init a new fField
    ff = fField2D.fField2D()
    ff.init(10,10,PVector(0,0),width,height)
    
    #Test2: add some forces
    parts = particles.particles()
    parts.init(100)
    parts.initRandomLocs(PVector(0,0),PVector(width,height))
    parts.addRandomForces(PVector(-5,-5),PVector(5,5))
    parts.drawParts(3)
    parts.drawForces(2,scaleFactor)
    parts.drawVels(2,scaleFactor)
    ff.sumInputfs(parts)
    
    ff.drawField(color(0,255,255,200),2,scaleFactor)
    
def setup():
    size(500,500)
    clear()
    unitTests()