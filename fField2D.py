"""
fField2D Class definition
"""
import cell

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
                c = cell.cell()
                c.init()
                self.cells.append(c)
        
    # parameters in the form of lists of forces recived and applied as well as a list of objects to affect
    def sumInputfs(self,parts):
        for p in parts.particles:
            # check which cell the particle belongs to
            for c in self.cells:
                if c.posInCell(p.pos):
                    pass
                    
            # add the force to the cell
    
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
                vect = self.cells[y*self.resX+x].origin * vectMult
                cellCentre = PVector(cellw *x + halfCellw, cellh *y + halfCellh)
                layer.line( cellCentre.x , cellCentre.y , cellCentre.x + vect.x, cellCentre.y + vect.y)
        layer.endDraw()
        image(layer,self.pos.x,self.pos.y)