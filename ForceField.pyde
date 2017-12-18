"""
Field Engine 2D

Create 'force fields' of arbitrary resolution use this to 
affect the positions and attributes of particles and simulations
https://github.com/tino113/forceField2D.git
"""
import particles
import fField2D

def unitTests():
    print("Begin Unit Testing!")
    
    #Init a new fField
    ff = fField2D.fField2D()
    ff.init(10,10,PVector(0,0),width,height)
    
    #Test1: draw the field
    ff.drawField(color(0,255,255),1,1)
    
    #Test2: add some forces
    parts = particles.particles()
    parts.init(200)
    parts.initRandomLocs(PVector(0,0),PVector(width,height))
    parts.addRandomForces(PVector(-1,-1),PVector(1,1))
    ff.sumInputfs(parts)
    
def setup():
    size(500,500)
    clear()
    unitTests()