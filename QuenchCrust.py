"""
Quench crust calculations for the lunar magma ocean cooling

By: Viranga Perera & Alan P. Jackson
Modified: June 20, 2017

Finds the equilibrium thickness of quench crust. Finds the conductive heat flux of the magma ocean and uses
the Nusselt number to find the convective heat flux of the magma ocean. That flux needs to go through the
quench crust and also radiatively from the top of the quench crust as well.

Also, finds time it would take to form a given thickness of quench crust using the Stefan problem.

"""

from __future__ import division
#import numpy as np
#import math
#from scipy.optimize import fsolve

def QuenchCrust(CMB_Temperature, Temperature_top_MO, current_MO_depth, Heat_capacity_MO, Heat_fusion_MO, density_MO, Diffusivity_MO, Ra_number, \
                Emissivity, SB, Temperature_equl, Diffusivity_quench, density_quench, Heat_capacity_quench, Temperature_melt, Max_Quench_Thickness, timeStep):

    # Calculate the conductive heat flux of the magma ocean
    cond_flux_MO = Diffusivity_MO * density_MO * Heat_capacity_MO * (CMB_Temperature - Temperature_melt) / current_MO_depth
    
    if cond_flux_MO < 0:
        print('CMB_Temperature: ', CMB_Temperature)
        print('Temperature_melt: ', Temperature_melt)
        print('current_MO_depth: ', current_MO_depth)
    
    # Calculate Nusselt number [from Niemela et al 2000] 
    Nu = 0.124 * pow(Ra_number, 0.309)    
    
    # Calculate the convective heat flux of the magma ocean
    convec_flux_MO = Nu * cond_flux_MO
    
    # Calculate temperature at the top of quench crust
    EqulTemperature_top_quench = pow((convec_flux_MO/(Emissivity * SB)) + pow(Temperature_equl, 4), (1/4))
    
    # Calculate quench crust thickness
    EqulQuenchThickness = Diffusivity_quench * density_quench * Heat_capacity_quench * (Temperature_melt - EqulTemperature_top_quench) / convec_flux_MO
    
    # Very thick quench crust will sink (e.g. Hawaiian and Io lava) so we need to cap it at some reasonable thickness
    if EqulQuenchThickness > Max_Quench_Thickness:
        EqulQuenchThickness = Max_Quench_Thickness
    
    ## How long does it take for quenchThickness of crust to form?
    #def f(lambda_1):
    #    eqLHS = (Heat_fusion_MO * np.sqrt(np.pi)) / (Heat_capacity_quench * (Temperature_melt - EqulTemperature_top_quench))        
    #    eqRHS = np.exp(-(lambda_1**2)) / (lambda_1 * math.erf(lambda_1))
    #    return eqLHS - eqRHS
    #        
    #lambda_1_guess = 0.1
    #lambda_1 = fsolve(f, lambda_1_guess)[0]
    #    
    #EqulQuenchFormTime = pow(EqulQuenchThickness/(2*lambda_1),2) / Diffusivity_quench
    #
    #if EqulQuenchFormTime > timeStep:
    #    PresentQuenchThickness = 2 * lambda_1 * pow(timeStep * Diffusivity_quench, (1/2))
    #    
    #elif EqulQuenchFormTime <= timeStep:
    #    PresentQuenchThickness = EqulQuenchThickness
    #
    ## Very thick quench crust will sink (e.g. Hawaiian and Io lava) so we need to cap it at some reasonable thickness
    #if PresentQuenchThickness > Max_Quench_Thickness:
    #    PresentQuenchThickness = Max_Quench_Thickness
                                                                                                
    return EqulQuenchThickness
