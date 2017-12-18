"""
fField2D Class definition
"""
import cell

class fField2D():
    
    cells = []
    xyInds = []
    pos = PVector(0,0)
    resX = 0
    resY = 0
    w = 0
    h = 0
    cellw = 0
    cellh = 0
    numCells = 0
    
    def init(self,resX,resY,position = PVector(0,0),w = 100,h = 100):
        self.pos = position
        self.w = w
        self.h = h
        self.resX = resX
        self.resY = resY
        self.cellw = float(self.w) / self.resX 
        self.cellh = float(self.h) / self.resY
        self.numCells = self.resX * self.resY
        self.averagePsinCell = 0
        count = 0
        for y in range(resY):
            row = []
            for x in range(resX):
                c = cell.cell()
                c.init(self.pos+PVector(self.cellw *x ,self.cellh *y),self.cellw,self.cellh,PVector(0,0))
                row.append(count)
                self.cells.append(c)
                count += 1
            self.xyInds.append(row)
        
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
            
    def cellxy(self,x,y,type = 'LOOPING'):
        if type == 'LOOPING':
            if x < 0:
                x += self.resX
            elif x >= self.resX:
                x -= self.resX
            if y < 0:
                y += self.resY
            elif y >= self.resY:
                y -= self.resY
        else:
            if x < 0:
                x = 0
            elif x >= self.resX:
                x = self.resX-1
            if y < 0:
                y = 0
            elif y >= self.resY:
                y = self.resY-1
        return self.cells[self.xyInds[x][y]]
    
    def getCellxy(self,ind):
        for y in range(len(self.xyInds)):
            for x in range(len(self.xyInds[y])):
                if self.xyInds[y][x] == ind:
                    return (x,y)
    
    def damp(self, factor):
        for c in self.cells:
            c.force -= c.force * factor
            
    def calcPressure(self, parts, factor = 0.01):
        for c in self.cells:
            c.calcPartsInCell(parts)
        if self.numCells > 0:
            idealPressure = float(parts.numParts)/self.numCells
        if idealPressure > 0:
            for c in self.cells:
                c.pressure = float(c.partsInCell)/idealPressure
    
    def pressureForce(self, factor = 0.1):
        #force from high to low pressure
        for i in range(self.numCells):
            c = self.cells[i]
            myX = self.getCellxy(i)[0]
            myY = self.getCellxy(i)[1]
            count = 0
            for x in range(-3,4):
                for y in range(-3,4):
                    if not(x == 0 and y == 0):
                        c2 = self.cellxy(myX+x,myY+y,'Other')
                        tforce = PVector(0,0)
                        diff = 0
                        if c.pressure > c2.pressure:
                            diff = c.pressure - c2.pressure
                            tforce = (c2.centre - c.centre)
                        tforce.normalize()
                        tforce *= factor
                        count+=1
            c.addForce(tforce/count)
            
    def drawPressure(self,layer,lowPressure = color(0,0,255,100), highPressure = color(255,0,0,100)):
        layer.beginDraw()
        # draw each cell
        for c in self.cells:
            layer.noStroke()
            layer.fill(lerpColor(lowPressure,highPressure,c.pressure))
            layer.rect(c.origin.x,c.origin.y,c.w,c.h)
        layer.endDraw()
        
    def addRandomForces(self, s = PVector(0,0), e = PVector(0,0)):
        for c in self.cells:
            c.addForce(PVector(random(s.x,e.x),random(s.y,e.y)))
        
    def drawField(self,layer,col = color(0,255,255,255),weight = 1,vectMult = 1):
        col2 = col
        if alpha(col) < 255:
            col2 = color(red(col),green(col),blue(col),round(float(alpha(col))/2))
        layer.beginDraw()
        layer.strokeWeight(weight)
        layer.stroke(col)
        # draw each cell
        i = 0
        for c in self.cells:
            layer.noFill()
            layer.stroke(col2)
            layer.rect(c.origin.x,c.origin.y,c.w,c.h)
            layer.noStroke()
            layer.fill(col)
            layer.textSize(self.h/(self.resY*4))
            myX = self.getCellxy(i)[0]
            myY = self.getCellxy(i)[1]
            layer.text(str(myX)+","+str(myY),c.origin.x+4,c.origin.y + 14)
            eol = c.centre + c.force * vectMult
            eol2 = c.force * 0.2 * vectMult
            tri = eol - eol2
            layer.stroke(col)
            layer.line( c.centre.x , c.centre.y , eol.x, eol.y)
            norml = PVector(c.force.x,c.force.y)
            norml = norml.rotate(HALF_PI) * vectMult * 0.1
            layer.noStroke()
            layer.fill(col)
            layer.triangle( eol.x , eol.y,
                        tri.x + norml.x , tri.y + norml.y,
                        tri.x - norml.x , tri.y - norml.y )
            i+=1
                
        layer.endDraw()