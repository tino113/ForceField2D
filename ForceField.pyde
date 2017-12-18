"""
Field Engine 2D

Create 'force fields' of arbitrary resolution use this to 
affect the positions and attributes of particles and simulations
https://github.com/tino113/forceField2D.git
"""

class fField2D():
    
    cells = []
    pos = PVector(0,0)
    resX = 0
    resY = 0
    w = 0
    h = 0
    
    def init(self,resX,resY,position = PVector(0,0),w = width,h = height):
        self.pos = position
        self.w = w
        self.h = h
        self.resX = resX
        self.resY = resY
        for y in range(resY):
            row = []
            for x in range(resX):
                row.append([PVector(0,0)])
            self.cells.append(row)
                
        
    # parameters in the form of lists of forces recived and applied as well as a list of objects to affect
    def sumInputfs(self,positions,forces):
        pass
    
    def applyOutputfs(self,positions):
        pass
        
    def drawField(self,col,vectMult,weight):
        layer = PGraphics.create()
        layer.beginDraw()
        layer.strokeWeight(weight)
        layer.stroke(col)
        # draw each cell
        for y in range(self.resY):
            for x in range(self.resX):
                pass
        layer.rect()
        layer.endDraw()
        image(layer)
        

def unitTests():
    print("Begin Unit Testing!")
    
    #Init a new fField
    ff = fField2D()
    ff.init(10,10)
    
    #Test1: ????
    
def setup():
    size(500,500)
    unitTests()