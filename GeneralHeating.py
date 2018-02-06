"""

Function to add heat to the magma ocean at each timestep

This will model potential heat sources such as tidal heating, radiogenic heating, etc.

By: Viranga Perera & Alan P. Jackson

"""

from __future__ import division
import numpy as np
import sys

def GeneralHeating(GeneralHeatingSwitch, HeatingRate, timeStep):

    if np.isinf(timeStep):
        sys.exit()

    if GeneralHeatingSwitch == False:    
                
        GH = 0.0
        
    elif GeneralHeatingSwitch == True:

        GH = HeatingRate * timeStep
            
    return GH
