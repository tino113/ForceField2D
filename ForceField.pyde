"""
Field Engine 2D

Create 'force fields' of arbitrary resolution use this to 
affect the positions and attributes of particles and simulations
https://github.com/tino113/forceField2D.git
"""
import particles
import fField2D

ff = fField2D.fField2D()
parts = particles.particles()
startTime = 0
lastTime = 0
cumulativeDeltaT = 0
simulationFixedTimestep = 20

scaleFactor = 20

def unitTests():
    global scaleFactor
    global ff
    global parts
    print("Begin Unit Testing!")
    
    #Init a new fField
    ff = fField2D.fField2D()
    ff.init(10,10,PVector(0,0),width,height)
    
    #Test2: add some forces
    parts = particles.particles()
    parts.init(100)
    parts.initRandomLocs(PVector(0,0),PVector(width,height))
    parts.addRandomForces(PVector(-1,-1),PVector(1,1))
    parts.drawForces(2,scaleFactor)
    parts.drawVels(2,scaleFactor)
    parts.drawParts(3)
    ff.sumInputfs(parts)
    
    ff.drawField(color(0,255,255,200),2,scaleFactor)
    
def setup():
    global scaleFactor
    global ff
    global parts
    global lastTime
    global cumulativeDeltaT
    frameRate(30)
    size(500,500)
    clear()
    unitTests()
    lastTime = millis()
    cumulativeDeltaT = 0
    
def simulationStep(deltaT):
    parts.simulate(deltaT, 0.5)
    parts.damp(0.05)
    
def draw():
    global scaleFactor
    global ff
    global parts
    global simulationFixedTimestep
    global startTime
    global lastTime
    global cumulativeDeltaT
    clear()
        
    parts.drawForces(2,scaleFactor)
    parts.drawVels(2,scaleFactor)
    parts.drawParts(3)
    ff.drawField(color(0,255,255,200),2,scaleFactor)
    
    deltaTime = millis() - lastTime
    
    if cumulativeDeltaT > 1/simulationFixedTimestep : 
        simulationStep(cumulativeDeltaT)
    else:
        cumulativeDeltaT += deltaTime