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
    cellw = 0
    cellh = 0
    
    def init(self,resX,resY,position = PVector(0,0),w = 100,h = 100):
        self.pos = position
        self.w = w
        self.h = h
        self.resX = resX
        self.resY = resY
        self.cellw = float(self.w) / self.resX 
        self.cellh = float(self.h) / self.resY
        for y in range(resY):
            row = []
            for x in range(resX):
                c = cell.cell()
                c.init(self.pos+PVector(self.cellw *x ,self.cellh *y),self.cellw,self.cellh,PVector(0,0))
                self.cells.append(c)
        
    # parameters in the form of lists of forces recived and applied as well as a list of objects to affect
    def sumInputfs(self,parts):
        for c in self.cells:
            for p in parts.particles:
            # check which cell the particle belongs to
                if c.posInCell(p.pos):
                    # add the force to the cell
                    c.addForce(p.force)
                    c.incrParts()
            c.averageForce()
            
    def damp(self, factor):
        for c in self.cells:
            c.force -= c.force * factor       
        
    def drawField(self,layer,col = color(0,255,255,255),weight = 1,vectMult = 1):
        halfCellw = self.cellw/2
        halfCellh = self.cellh/2
        col2 = col
        if alpha(col) < 255:
            col2 = color(red(col),green(col),blue(col),round(float(alpha(col))/2))
        layer.beginDraw()
        layer.strokeWeight(weight)
        layer.stroke(col)
        # draw each cell
        for c in self.cells:
            layer.noFill()
            layer.stroke(col2)
            layer.rect(c.origin.x,c.origin.y,c.w,c.h)
            cellCentre = PVector(c.origin.x + halfCellw, c.origin.y + halfCellh)
            eol = cellCentre + c.force * vectMult
            eol2 = c.force * 0.2 * vectMult
            tri = eol - eol2
            layer.stroke(col)
            layer.line( cellCentre.x , cellCentre.y , eol.x, eol.y)
            norml = PVector(c.force.x,c.force.y)
            norml = norml.rotate(HALF_PI) * vectMult * 0.1
            layer.noStroke()
            layer.fill(col)
            layer.triangle( eol.x , eol.y,
                        tri.x + norml.x , tri.y + norml.y,
                        tri.x - norml.x , tri.y - norml.y )
                
        layer.endDraw()