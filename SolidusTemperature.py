"""
Determine solidus temperature (in K) inside the Moon for a given radius (in meters)
and fraction of liquid remaining in the magma ocean

By: Viranga Perera & Alan P. Jackson

"""

from __future__ import division

def SolidusTemperature(radius, fractionLiquid):
    radius_km = radius / 1000 
    
    # Equation #3 in Elkins-Tanton et al. 2011
    solidusTemperature = -1.3714e-4 * pow(radius_km, 2) - 0.1724 * radius_km + 1861 - (4.4 / (0.2 * fractionLiquid + 0.01)) + 273.15    
    
    return solidusTemperature
