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
simulationFixedTimestep = 30
speed = 1

debugLayer = PGraphics
drawLayer = PGraphics

scaleFactor = 4

def unitTests():
    global scaleFactor
    global ff
    global parts
    global debugLayer
    global drawLayer
    print("Begin Unit Testing!")
    
    #Init a new fField
    ff = fField2D.fField2D()
    ff.init(10,10,PVector(0,0),width,height)
    
    #Test2: add some forces
    parts = particles.particles()
    parts.init(100)
    parts.initRandomLocs(PVector(0,0),PVector(width,height))
    parts.addRandomForces(PVector(-10,-10),PVector(10,10))
    #parts.drawForces(debugLayer,2,scaleFactor)
    #parts.drawVels(debugLayer,2,scaleFactor)
    #parts.drawParts(drawLayer,3)
    ff.sumInputfs(parts)
    
    #ff.drawField(debugLayer,color(0,255,255,200),2,scaleFactor)
    
def setup():
    global scaleFactor
    global ff
    global parts
    global lastTime
    global cumulativeDeltaT
    global debugLayer
    global drawLayer
    frameRate(30)
    size(500,500)
    clear()
    
    debugLayer = createGraphics(width,height)
    drawLayer = createGraphics(width,height)
    
    unitTests()
    lastTime = millis()
    cumulativeDeltaT = 0
    
def simulationStep(deltaT):
    parts.simulate(deltaT)
    parts.damp(0.05)
    
    #loop the world
    for p in parts.particles:
        if p.pos.x < 0:
            p.pos.x += width
        elif p.pos.x > width:
            p.pos.x -= width
        if p.pos.y < 0:
            p.pos.y += height
        elif p.pos.y > height:
            p.pos.y -= height
    
def draw():
    global scaleFactor
    global ff
    global parts
    global simulationFixedTimestep
    global startTime
    global lastTime
    global cumulativeDeltaT
    global debugLayer
    global drawLayer
    global speed
    clear()
    tStep = 1/float(simulationFixedTimestep)
    
    debugLayer.beginDraw()
    debugLayer.clear()
    debugLayer.endDraw()
    
    drawLayer.beginDraw()
    drawLayer.clear()
    drawLayer.endDraw()
    
        
    #parts.drawForces(debugLayer,2,scaleFactor)
    parts.drawVels(debugLayer,2,scaleFactor)
    parts.drawParts(drawLayer,3)
    ff.drawField(debugLayer,color(0,255,255,100),2,scaleFactor)
    currentT = millis()
    deltaT = (currentT - lastTime) * 0.001
    cumulativeDeltaT += deltaT
    lastTime = currentT
    
    if cumulativeDeltaT > tStep :
        for i in range(floor(cumulativeDeltaT / tStep)):
            simulationStep(speed)
            cumulativeDeltaT -= tStep
            
    image(debugLayer,0,0)
    image(drawLayer,0,0)