"""
By: Viranga Perera & Alan P. Jackson
"""

from __future__ import division
import numpy as np
                
# Hole puncturing impacts
def PuncturingImpacts(ellapsedTime, timestep, mass2area, AlanData):
    
    # Read the last time available in table
    lastTimeInTable = AlanData[-1,0]


    # Read Table for Values
    if ellapsedTime <= lastTimeInTable:

        # Search the table for the ellapsed time that is within the tolerance set above
        rowIndicies = np.where(AlanData[:,0] <= ellapsedTime + (timestep/2) )[0]

        # If no impacts at this time...
        if rowIndicies.size == 0:
            areaHoles = 0
            MassImpacts = 0
            EnergyImpacts = 0
            
        # If there are impacts...
        else:
            # Choose the row index by picking the time in the table that is closest to the ellapsed time
            correctRowNumber = max(rowIndicies)
        
            # Select the mass per time of the successful match and multiply by the timestep
            MassImpacts = AlanData[correctRowNumber,1] * timestep

            # Select the energy per time of the successful match and multiply by the timestep
            EnergyImpacts = AlanData[correctRowNumber,2] * timestep   
    
            # Convert the total mass accreted during this timestep to an area using the predefined constant
            areaHoles = MassImpacts / mass2area


    # Use Decaying Rates (since beyond data in table)
    elif ellapsedTime > lastTimeInTable:
        
        # Last mass per time available multiplied by last time divided by current ellapsed time
        # That gives current mass per time that is multiplied by the timestep
        MassImpacts = (AlanData[-1,1] * AlanData[-1,0] / ellapsedTime) * timestep
        
        # Last energy per time available multiplied by last time divided by current ellapsed time
        # That gives current energy per time that is multiplied by the timestep
        EnergyImpacts = (AlanData[-1,2] * AlanData[-1,0] / ellapsedTime) * timestep
        
        # Convert the total mass accreted during this timestep to an area using the predefined constant
        areaHoles = MassImpacts / mass2area
    

    return areaHoles, MassImpacts, EnergyImpacts
