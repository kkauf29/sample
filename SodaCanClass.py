###
# Kim Kaufmam
# Creates the SodaCan class with the attributes canHeight, canRadius and the 
# methods getSurfaceArea and getVolume 

from math import pi 

class SodaCan:
    def __init__(self, canHeight, canRadius):
        """this constructor creates the canHeight and canRadius attributes"""
        self._canHeight = canHeight
        self._canRadius = canRadius
        
    def getSurfaceArea(self):
        """this method uses objects' attributes of canRadius and canHeight in a formula that returns the surface area of the can"""
        canSurfaceArea = (2 * pi * self._canRadius * self._canHeight) + (2 * pi * self._canRadius * self._canRadius)
        canSurfaceArea = round(canSurfaceArea, 2)
        return canSurfaceArea
            
        
    def getVolume(self):
        """this method uses objects' attributes of canRadius and canHeight in a formula that returns the volume of the can"""
        canVolume = pi * self._canRadius * self._canRadius * self._canHeight
        canVolume = round(canVolume, 2)
        return canVolume
    
            
        
