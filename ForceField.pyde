"""
Field Engine 2D

Create 'force fields' of arbitrary resolution use this to 
affect the positions and attributes of particles and simulations
https://github.com/tino113/forceField2D.git
"""
import particle
import fField2D

def unitTests():
    print("Begin Unit Testing!")
    
    #Init a new fField
    ff = fField2D()
    ff.init(10,10,PVector(0,0),width,height)
    
    #Test1: draw the field
    ff.drawField(color(0,255,255),1,1)
    
    #Test2: add some forces
    parts = particle.particle()
    parts.init()
    parts.initRandomLocs(PVector(0,0),PVector(width,height))
    ff.sumInputfs(parts.pos,parts.force)
    
def setup():
    size(500,500)
    clear()
    unitTests()