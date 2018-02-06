"""

Determine the correct surface temperature that matches the equilibrium energy loss of the Moon globally

Term "lid" used here since this function can be used either by quench crust or plag crust

By: Viranga Perera & Alan P. Jackson

"""

from __future__ import division

def SurfaceTemperature(Temperature_top_MO, Temperature_top_lid_guess, LidThickness, Diffusivity_lid, density_lid, Heat_capacity_lid, SB, Emissivity, Temperature_equl):

    if LidThickness != 0:
        
        tol = 0.01 # Tolerance parameter for accuracy of calculation
    
        fT = tol * 100 # Initialize varaible
    
        Tsurf = Temperature_top_lid_guess
    
        while (fT > tol):
        
            CondFlux = Diffusivity_lid * density_lid * Heat_capacity_lid * (Temperature_top_MO - Temperature_top_lid_guess) / LidThickness
    
            newTsurf = pow((CondFlux / (SB * Emissivity) + pow(Temperature_equl, 4.0)), 0.25)
        
            fT = abs((newTsurf - Tsurf) / Tsurf);
        	
            Tsurf = newTsurf
            
    elif LidThickness == 0:
        Tsurf = Temperature_top_MO
    	
    return Tsurf
