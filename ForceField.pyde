"""
Field Engine 2D

Create 'force fields' of arbitrary resolution use this to 
affect the positions and attributes of particles and simulations
https://github.com/tino113/forceField2D.git
"""
import particle

class fField2D():
    
    cells = []
    pos = PVector(0,0)
    resX = 0
    resY = 0
    w = 0
    h = 0
    
    def init(self,resX,resY,position = PVector(0,0),w = 100,h = 100):
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
        
    def drawField(self,col,vectMult = 1,weight = 1):
        cellw = float(self.w-1) / self.resX 
        cellh = float(self.h-1) / self.resY
        halfCellw = cellw/2
        halfCellh = cellh/2
        layer = createGraphics(self.w,self.h)
        layer.beginDraw()
        layer.clear()
        layer.noFill()
        layer.strokeWeight(weight)
        layer.stroke(col)
        # draw each cell
        for y in range(self.resY):
            for x in range(self.resX):
                layer.rect(cellw *x ,cellh *y, cellw,cellh)
                vect = self.cells[y][x][0] * vectMult
                cellCentre = PVector(cellw *x + halfCellw, cellh *y + halfCellh)
                layer.line( cellCentre.x , cellCentre.y , cellCentre.x + vect.x, cellCentre.y + vect.y)
        layer.endDraw()
        image(layer,self.pos.x,self.pos.y)

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
    ff.sumInputfs(particles.pos,particles.force)
    
def setup():
    size(500,500)
    clear()
    unitTests()