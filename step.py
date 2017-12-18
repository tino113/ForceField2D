"""
Step Class definition
"""
import thread

class step():
    
    tStep = 0
    timeAdjust = 0
    simulationStepsPerSecond = 0
    simulationFixedTimestep = 0
    startT = 0
    currentT = 0
    deltaT = 0
    cumulativeDeltaT = 0
    lastTime = 0
    running = False
    
    def init(self, simulationFixedTimestep = 30, simulationStepsPerSecond = 30):
        self.simulationStepsPerSecond = simulationStepsPerSecond
        self.simulationFixedTimestep = simulationFixedTimestep
        self.tStep = 1/float(simulationFixedTimestep)
        self.timeAdjust = simulationStepsPerSecond/float(simulationFixedTimestep)
        
        self.startT = millis()
        self.currentT = millis()
        self.lastTime = self.currentT
    
    def doStep(self,function):
        self.currentT = millis()
        self.deltaT = (self.currentT - self.lastTime) * 0.001
        self.lastTime = self.currentT
        self.cumulativeDeltaT += self.deltaT
        
        if self.cumulativeDeltaT > self.tStep :
            for i in range(floor(self.cumulativeDeltaT / self.tStep)):
                function()
                self.cumulativeDeltaT -= self.tStep
    
    def threadedStep(self, function):
        self.running = True
        thread.start_new_thread( self.loopSteps, (function, ) )
    
    def loopSteps(self, function):
        while self.running:
            self.doStep(function)
        
        
    