"""
Field Engine 2D

Create 'force fields' of arbitrary resolution use this to 
affect the positions and attributes of particles and simulations
https://github.com/tino113/forceField2D.git
"""
import particles
import fField2D
import step

ff = fField2D.fField2D()
parts = particles.particles()
speed = 1
partStp = step.step()
cellStp = step.step()

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
    ff.init(5,5,PVector(0,0),width,height)
    
    #Test2: add some forces
    parts = particles.particles()
    parts.init(100)
    parts.initRandomLocs(PVector(0,0),PVector(width,height))
    parts.addRandomForces(PVector(-5,-5),PVector(5,5))
    #parts.drawForces(debugLayer,2,scaleFactor)
    #parts.drawVels(debugLayer,2,scaleFactor)
    #parts.drawParts(drawLayer,3)
    #ff.sumInputfs(parts)
    
    #ff.drawField(debugLayer,color(0,255,255,200),2,scaleFactor)
    
def setup():
    global scaleFactor
    global ff
    global parts
    global debugLayer
    global drawLayer
    global partStp
    global cellStp
    size(500,500)
    clear()
    
    debugLayer = createGraphics(width,height)
    drawLayer = createGraphics(width,height)
    
    partStp = step.step()
    partStp.init(30,30)
    
    cellStp = step.step()
    cellStp.init(60,60)
    
    unitTests()
    lastTime = millis()
    cumulativeDeltaT = 0
    
def particleSimulation(speed):
    global ff
    global parts
    parts.simulate(speed)
    parts.addFieldForces(ff)
    parts.damp(0.02)
    
    
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
            
def fieldSimulation(speed):
    ff.damp(0.00001)
    
def draw():
    global scaleFactor
    global ff
    global parts
    global debugLayer
    global drawLayer
    global speed
    global partStp
    global cellStp
    clear()
        
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
    
    cellStp.doStep(lambda: fieldSimulation(speed))
    partStp.doStep(lambda: particleSimulation(speed))
            
    image(debugLayer,0,0)
    image(drawLayer,0,0)