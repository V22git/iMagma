"""
By: Viranga Perera & Alan P. Jackson
"""

# Determine Rayleigh number

from __future__ import division

# Rayleigh number without internal heating term
def RayleighNumber(acc_grav, density, therm_exp_coeff, temperature_diff, length_scale, dy_viscosity, therm_diffusivity):
    
    Ra = (acc_grav * density * therm_exp_coeff * temperature_diff * pow(length_scale, 3) ) / (dy_viscosity * therm_diffusivity) 
    
    return Ra
