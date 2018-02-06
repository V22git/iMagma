# -*- coding: utf-8 -*-

"""
Impacts Magma (iMagma): A Simple Lunar Magma Ocean Cooling Code with Impacts

By: Viranga Perera & Alan P. Jackson
Modified: September 19, 2017

The MAIN script needs to be called with certain input parameters (see below) 
MAIN usually called using ParameterSearchHEAD.py

"""
####### PYTHON IMPORTS ##############################################################################################################################

from __future__ import division
import numpy as np
#import pandas as pd
import datetime
import csv
import ast

#####################################################################################################################################################


####### iMAGMA DETAILS ##############################################################################################################################

iMagma_version = 4.95

#####################################################################################################################################################


####### SUPPORT MODULES #############################################################################################################################

import SolidusTemperature as ST                         # Calculates solidus temperature as a function of radius and the remaining liquid fraction
import SurfaceTemperature as SurfTemperature            # Calculated the surface temperature that matches the equilibrium radiation of the Moon
import Impacts as I                                     # Functions to determine energy added by impacts and number of hole puncturing impacts
import QuenchCrust as QC                                # Functions to determine quench crust conditions
import RayleighNumber as Ra                             # Function to calculate Rayleigh number
import GeneralHeating as GH                             # Function to calculate additional heating of the magma ocean
    
#####################################################################################################################################################
    

####### INPUT PARAMETERS ############################################################################################################################    
            
with open('inputFile.csv', 'r') as f:
    reader = csv.reader(f)
    InputParameters = next(reader)

homePath = str(InputParameters[0])
UserPath = str(InputParameters[1])
ImpactsSwitch = ast.literal_eval(InputParameters[2])
QuenchSwitch = ast.literal_eval(InputParameters[3])
GeneralHeatingSwitch = ast.literal_eval(InputParameters[4])
adiabslope = float(InputParameters[5])
MO_depth_initial = float(InputParameters[6])
MO_depth_plagBuild = float(InputParameters[7])
density_MO = float(InputParameters[8])
Heat_fusion_MO = float(InputParameters[9])
Heat_capacity_MO = float(InputParameters[10])
therm_exp_coeff_MO = float(InputParameters[11])
Diffusivity_MO = float(InputParameters[12])
dy_viscosity_MO = float(InputParameters[13])
Temperature_equl = float(InputParameters[14])
Diffusivity_crust = float(InputParameters[15])
density_crust = float(InputParameters[16])
Heat_capacity_crust = float(InputParameters[17])
Emissivity = float(InputParameters[18])
mass2area = float(InputParameters[19])
acc_grav = float(InputParameters[20])
Temperature_melt = float(InputParameters[21])
Diffusivity_quench = float(InputParameters[22])
density_quench = float(InputParameters[23])
Heat_capacity_quench = float(InputParameters[24])
Max_Quench_Thickness = float(InputParameters[25])
vol_increments = int(InputParameters[26])
percMO_remain_end = float(InputParameters[27])
plag_holeFill_vs_gblCrust = float(InputParameters[28])
ImpactsFile = str(InputParameters[29])
RunNumber = int(InputParameters[30])
LargestImpactorSize = float(InputParameters[31])
MoonLocationDebrisCalc = float(InputParameters[32])
HeatingRate = float(InputParameters[33])
KineticEnergySwitch = ast.literal_eval(InputParameters[34])
KEefficiency = float(InputParameters[35])
plag_fraction = float(InputParameters[36])
                        
#####################################################################################################################################################            

                        
####### DEFINED CONSTANTS ###########################################################################################################################
        
# Moon constants
Radius_moon = 1737.4e3                # Radius of the Moon (m)
        
# Phyiscal constants
SB = 5.670367e-8                      # Stefan-Boltzmann constant (W/m^2*K^4)
        
surfArea_Moon = 4 * np.pi * pow(Radius_moon, 2)                                                       # Surface area of the Moon (m^2)

MO_volume_initial = (4/3) * np.pi * (pow(Radius_moon, 3) - pow(Radius_moon - MO_depth_initial, 3))   # Initial volume of magma ocean
    
MO_mass_initial = MO_volume_initial *  density_MO
    
#####################################################################################################################################################
    
    
####### INITIALIZATIONS #############################################################################################################################
    
TimeStamp_start = datetime.datetime.now()
    
MO_volume_current = MO_volume_initial                                # Current volume of magma ocean
CrustalThickness = 0                                                 # Initial crustal thickness
CrustThicknessImpMoon = 0                                            # Initial impacted Moon crustal thickness
CrustalThickness_global = 0                                          # Initial global crustal thickness
fractionLiquid = 1                                                   # Initiallized remaining magma ocean liquid fraction
CMB = Radius_moon - MO_depth_initial                                 # Initial solid interior-magma ocean boundary
ellapsedTime = 0                                                     # Variable to track ellapsed time
timeStep = 3.154e7                                                   # Timestep (sec)--will be updated in script
timeStep_tol = 0.02                                                  # Timestep error tolerance (currently set to 2%)
volSize = MO_volume_initial / vol_increments                         # Size of constant volume increment that will be iterated over
    
Ra_number = 0                                                        # Initiallized Rayleigh number (updated right away)
quenchThickness = 0                                                  # Initiallized quench crust thickness (updated right away)
Reduce_Global_Quench_Due_Impacts = 0                                 # Initiallized quench thickness that should be reduced due to impacts
vol_Quench_excavated = 0                                             # Initiallized volumen of quench excavated by impacts
TotalHoleArea = 0                                                    # Initiallized total area of impact generated holes
HoleThickness_times_HoleArea_Sum = 0                                 # Initiallized sum of hole thickness multiplied by hole area
    
CMB_array = []                                                       # Array for CMB location over time
Time_array = []                                                      # Array for ellapsed time
Time_array_holes = []                                                # Array for tracking ellapsed time for holes tracker
Time_array_impactedCrust = []                                        # Array for tracking ellapsed time for holes tracker
LiqFrac_array = []                                                   # Array for liquid fraction over time
CrustalThickness_array = []                                          # Array for crustal thickness of non-impacted Moon over time
CrustalThickness_Impacted_array = []                                 # Array for crustal thickness of impacted Moon over time
CrustalThickness_Global_array = []                                   # Array for crustal thickness of whole Moon over time
CMB_Temperature_array = []                                           # Array for temperature at solid interior-magma ocean boundary over time
holeTracker = []                                                     # Array for holes to be tracked
holeAreaTracker_array = []                                           # Array for area of holes over time
holeThicknessTracker_array = []                                      # Array for thickness of holes over time
holeTemperatureTracker_array = []                                    # Array for temperature of holes over time
holeAreaCreatedTracker_array = []                                    # Array for area per timestep of holes created at each timestep over time
holeTrackerElements_array = []                                       # Array for tracking number of holes in holeTracker over time

CumMassAddedImpacts = 0                                              # Initiallized total mass added by impacts    
CumEnergyAddedImpacts = 0                                            # Initiallized total energy added by impacts    
CumEnergyDumped = 0                                                  # Initiallized total energy dumped
CumGenHeatAdded = 0                                                  #
CrustBuildOn = 0                                                     # Switch to track when crust building turns on
crystHoleCrust = 0                                                   # Initiallized fraction of plag that should go to holes
holeTrackerRest = 0                                                  # Variable used to reset the holeTracker once when plag building starts
totalHoleAreaCum = 0                                                 # Cumulative hole area added to the surface of the Moon
totalHoleAreaCum_array = []                                          # Array for cumulative hole area added over time
 
AlanData = np.genfromtxt(homePath + ImpactsFile, skip_header=1, delimiter=',')       # Import Alan's impacts table (used by Impacts function)

#####################################################################################################################################################
    
    
######################## MAIN ###################### MAIN ######################## MAIN #############################################################
    
# Initial temperature at the solid interior-magma ocean boundary
CMB_Temperature = ST.SolidusTemperature(CMB, fractionLiquid)                                                   
    
# Main Loop (iterate over the number of volume increments defined above)
for interations in range(0, vol_increments):
        
    # Switch to make sure timestep correct before proceeding
    timestepAcceptable = False
            
    solidifMass = volSize * density_MO
    solidifEnergy = solidifMass * Heat_fusion_MO
            
    # Current volumne of solid interior
    Core_volume = (4/3) * np.pi * pow(CMB, 3)
            
    # In the beginning, all solidifying magma falls inward to the solid interior (done until magma ocean depth is equal to MO_depth_plagBuild)
    if (CMB < (Radius_moon - MO_depth_plagBuild)):
        crystCore2Crust = 1                                                                                  
                
    # When solid interior is large enough & is within depth for plagioclase crystallization, 
    # then 55% of solidifying magma goes to the solid interior while the rest builds plagioclase crust
    elif (CMB >= (Radius_moon - MO_depth_plagBuild)):
            
        if CrustBuildOn == 0:
            TimeCrustStart = ellapsedTime
            crustBuildingStartTime_yrs = TimeCrustStart / 3.154e7
            CrustBuildOn = 1
            CrustalThickness = quenchThickness   # Done so that the global quench just before plag crust is preserved
                        
        # Set fraction of the solidifying material that goes to the solid interior
        crystCore2Crust = 1 - plag_fraction
            
        # If there are no holes, then all of the solidifying material that isn't going to the solid interior builds plagioclase crust globally
        if not holeTracker:                                                                
            crystGlobCrust = 1 - crystCore2Crust
            
        # If there are holes, then some of the plagioclase will fill into the holes as well as building more global crust
        elif holeTracker:
                
            distriFactor = plag_holeFill_vs_gblCrust * TotalHoleArea/surfArea_Moon
                
            if distriFactor > 1:
                distriFactor = 1
                
            crystHoleCrust = (1 - crystCore2Crust) * distriFactor
                
            if (surfArea_Moon - TotalHoleArea) / surfArea_Moon <= 1e-6:
                crystGlobCrust = 0
                
            else:
                crystGlobCrust = 1 - crystCore2Crust - crystHoleCrust
                                        
        CrustalThickness += (crystGlobCrust * (density_MO / density_crust) * volSize) / (4 * np.pi * pow(Radius_moon, 2) - TotalHoleArea)
        
                                                        
    # Update CMB location by adding new core volume (from solidification)
    CMB = pow( ( (3 * (Core_volume + crystCore2Crust * volSize)) / (4 * np.pi) ), (1/3) )
        
    # Reduce magma ocean volume by the volume of the material that solidified
    MO_volume_current -= volSize
        
    # If volume of the magma ocean is less than 0 then stop the iterations
    if MO_volume_current < (percMO_remain_end/100) * MO_volume_initial:
        break    
                    
    # Remaining magma ocean liquid fraction
    fractionLiquid = MO_volume_current / MO_volume_initial
            
    # Calculate the current temperature at the CMB
    Solidus_temperature = ST.SolidusTemperature(CMB, fractionLiquid)                                               
            
    # Difference in temperature between the previous CMB location and the new location
    Temperature_change = CMB_Temperature - Solidus_temperature 
            
    # Set new CMB temperature at the current CMB temperature
    CMB_Temperature = Solidus_temperature
            
    # Calculate temperature at the top of magma ocean by following the adiabat up
    Temperature_top_MO = CMB_Temperature - adiabslope * (Radius_moon - CMB)
            
    # Energy released by cooling the magma ocean (note need to add the volume of part that solidified since it has to be cooled too) 
    coolingEnergy = density_MO * (MO_volume_current + volSize) * Heat_capacity_MO * Temperature_change
        
    # Current depth of the magma ocean
    current_MO_depth = Radius_moon - CMB - CrustalThickness_global
        
    # Calculate Rayleigh number
    Ra_number = Ra.RayleighNumber(acc_grav, density_MO, therm_exp_coeff_MO, (CMB_Temperature - Temperature_top_MO), current_MO_depth, dy_viscosity_MO, Diffusivity_MO)
        

    # Need a loop to find the correct timestep to use
    while (timestepAcceptable == False):
            
        holeTracker_copy = holeTracker
        HoleThickness_times_HoleArea_array = []
        MassQuenchAdded = 0
        MassImpactors_thisTimestep = 0
        EnergyImpactors_thisTimestep = 0
        AreaHolesAdded_thisTimestep = 0
            
        # If there are holes, need to make their quench crusts thicker at this timestep when no plag and increase thickness due to plag when that has started
        # Also, use this opportunity to update the temperatures at the top of each hole
        if holeTracker_copy:
                
            for idxHoles, valHoles in enumerate(holeTracker_copy):
                
                if CrustBuildOn == 0:
                        
                    # If hole quench crust thickness is less than max thickness value
                    if holeTracker_copy[idxHoles][1] < Max_Quench_Thickness:
                        
                        PresentQuenchThickness_inHole = QC.QuenchCrust(CMB_Temperature, Temperature_top_MO, current_MO_depth, Heat_capacity_MO, Heat_fusion_MO, density_MO, \
                                                                        Diffusivity_MO, Ra_number, Emissivity, SB, Temperature_equl, Diffusivity_quench, density_quench, \
                                                                        Heat_capacity_quench, Temperature_melt, Max_Quench_Thickness, timeStep)
                            
                        PresentTemperature_top_quench_inHole = SurfTemperature.SurfaceTemperature(Temperature_top_MO, holeTracker_copy[idxHoles][2], PresentQuenchThickness_inHole, \
                                                                                                    Diffusivity_quench, density_quench, Heat_capacity_quench, SB, Emissivity, \
                                                                                                    Temperature_equl)    
                            
                        LastQuenchThickness_inHole = holeTracker_copy[idxHoles][1]
                            
                        # Mass of new quench added is additional thickness added (present thickness minus old thickness) multiplied by area of hole and density of quench
                        MassQuenchAdded += (PresentQuenchThickness_inHole - LastQuenchThickness_inHole) * holeTracker_copy[idxHoles][0] * density_quench
                            
                        holeTracker_copy[idxHoles][1] = PresentQuenchThickness_inHole
                        holeTracker_copy[idxHoles][2] = PresentTemperature_top_quench_inHole
                            
        
                    # Else if hole quench crust thickness is greater than or equal to max thickness value
                    elif holeTracker_copy[idxHoles][1] >= Max_Quench_Thickness:
                        holeTracker_copy[idxHoles][1] = Max_Quench_Thickness
                        
                        
                elif CrustBuildOn == 1:
                        
                    holeTracker_copy[idxHoles][1] += (crystHoleCrust * (density_MO / density_crust) * volSize) / TotalHoleArea
                        
                    HoleThickness_times_HoleArea_array.append(holeTracker_copy[idxHoles][1] * holeTracker_copy[idxHoles][0])
                    
                    holeTracker_copy[idxHoles][2] = SurfTemperature.SurfaceTemperature(Temperature_top_MO, holeTracker_copy[idxHoles][2], holeTracker_copy[idxHoles][1], \
                                                                                        Diffusivity_crust, density_crust, Heat_capacity_crust, SB, Emissivity, \
                                                                                        Temperature_equl)
            
        # HOW MUCH GLOBAL QUENCH CRUST IS PRESENT?
                
        # Only makes sense to look at quench crust before plagioclase crust begins to form
        if CrustBuildOn == 0 and QuenchSwitch == True:
                    
            # Calculate global quench crust thickness add (or subtracted)
            PresentQuenchThickness = QC.QuenchCrust(CMB_Temperature, Temperature_top_MO, current_MO_depth, Heat_capacity_MO, Heat_fusion_MO, density_MO, Diffusivity_MO, Ra_number, \
                                                        Emissivity, SB, Temperature_equl, Diffusivity_quench, density_quench, Heat_capacity_quench, Temperature_melt, Max_Quench_Thickness, \
                                                        timeStep)
                
            PresentTemperature_top_quench = SurfTemperature.SurfaceTemperature(Temperature_top_MO, Temperature_top_MO, quenchThickness, Diffusivity_quench, density_quench, \
                                                                                Heat_capacity_quench, SB, Emissivity, Temperature_equl)    
                
            # Mass of new quench added 
            # Equal to thinkness of new quench (present minus old value), multiplied by surface area of Moon minus surface area of holes, multiplied by density of quench
            if (quenchThickness < Max_Quench_Thickness):
                MassQuenchAdded += (PresentQuenchThickness - quenchThickness) * (surfArea_Moon - TotalHoleArea) * density_quench
            
            
        # If conduction has started or there is quench crust...
        if CrustBuildOn == 1 and ImpactsSwitch == True:
                
            [areaHoles, MassImpactors_thisTimestep, EnergyImpactors_thisTimestep] = I.PuncturingImpacts(ellapsedTime/3.154e7, timeStep/3.154e7, mass2area, AlanData)
                
            AreaHolesAdded_thisTimestep += areaHoles
                                                                                
            # If areaHoles is 0 then skip
            if areaHoles != 0:
                    
                # The crust that was present before the impact cannot just disappear, here it will be spreadout over the rest of the Moon
                    
                vol_Crust_excavated_inHoleAreas = (TotalHoleArea / surfArea_Moon) * areaHoles * (HoleThickness_times_HoleArea_Sum / TotalHoleArea)
                    
                vol_Crust_excavated_nonImpactedAreas = ((surfArea_Moon - TotalHoleArea) / surfArea_Moon) * areaHoles * CrustalThickness
                    
                vol_Crust_excavated = vol_Crust_excavated_inHoleAreas + vol_Crust_excavated_nonImpactedAreas
                                                                                                    
                Extra_Crust_Due_Impacts = vol_Crust_excavated / surfArea_Moon
                
                for valHoles in holeTracker_copy:
                    valHoles[1] += Extra_Crust_Due_Impacts
                    valHoles[0] = valHoles[0] * (1 - (areaHoles / surfArea_Moon))
                    
                PresentQuenchThickness_inHole = QC.QuenchCrust(CMB_Temperature, Temperature_top_MO, current_MO_depth, Heat_capacity_MO, Heat_fusion_MO, density_MO, Diffusivity_MO, \
                                                                Ra_number, Emissivity, SB, Temperature_equl, Diffusivity_quench, density_quench, Heat_capacity_quench, Temperature_melt, \
                                                                Max_Quench_Thickness, timeStep)
                            
                PresentTemperature_top_quench_inHole = SurfTemperature.SurfaceTemperature(Temperature_top_MO, Temperature_top_MO, PresentQuenchThickness_inHole, \
                                                                                            Diffusivity_quench, density_quench, Heat_capacity_quench, SB, Emissivity, Temperature_equl)    
                    
                # Note that area of new hole is going to be reduced by a factor depending on the area that already has holes                                                                
                holeTracker_copy.append( [areaHoles, PresentQuenchThickness_inHole, PresentTemperature_top_quench_inHole] )
                    
                # Mass of new quench added is additional thickness added multiplied by the area of hole, multiplied by density of quench
                MassQuenchAdded += PresentQuenchThickness_inHole * areaHoles * density_quench

        elif quenchThickness != 0 and ImpactsSwitch == True:
                
            [areaHoles, MassImpactors_thisTimestep, EnergyImpactors_thisTimestep] = I.PuncturingImpacts(ellapsedTime/3.154e7, timeStep/3.154e7, mass2area, AlanData)
                
            AreaHolesAdded_thisTimestep += areaHoles
                                                                                                                                                                                            
            # If areaHoles is 0 then skip
            if areaHoles != 0:                    
                    
                if TotalHoleArea != 0:
                    # Quench that was present before the impact cannot just disappear
                        
                    vol_Quench_excavated_inHoleAreas = (TotalHoleArea / surfArea_Moon) * areaHoles * (HoleThickness_times_HoleArea_Sum / TotalHoleArea)
                        
                    vol_Quench_excavated_nonImpactedAreas = ((surfArea_Moon - TotalHoleArea) / surfArea_Moon) * areaHoles * quenchThickness
                        
                    vol_Quench_excavated = vol_Quench_excavated_inHoleAreas + vol_Quench_excavated_nonImpactedAreas
                                                                                                                                                                                                        
                    for valHoles in holeTracker_copy:
                        valHoles[0] = valHoles[0] * (1 - (areaHoles / surfArea_Moon))
                        
                    
                PresentQuenchThickness_inHole = QC.QuenchCrust(CMB_Temperature, Temperature_top_MO, current_MO_depth, Heat_capacity_MO, Heat_fusion_MO, density_MO, Diffusivity_MO, \
                                                                Ra_number, Emissivity, SB, Temperature_equl, Diffusivity_quench, density_quench, Heat_capacity_quench, Temperature_melt, \
                                                                Max_Quench_Thickness, timeStep)
                            
                PresentTemperature_top_quench_inHole = SurfTemperature.SurfaceTemperature(Temperature_top_MO, Temperature_top_MO, PresentQuenchThickness_inHole, \
                                                                                            Diffusivity_quench, density_quench, Heat_capacity_quench, SB, Emissivity, Temperature_equl)    
                                         
                holeTracker_copy.append( [areaHoles, PresentQuenchThickness_inHole, PresentTemperature_top_quench_inHole] )
            
                # Mass of new quench added is additional thickness added multiplied by the area of hole, multiplied by density of quench MINUS
                # Mass of quench that was present but was melted by impacts
                MassQuenchAdded += PresentQuenchThickness_inHole * areaHoles * density_quench - density_quench * vol_Quench_excavated
            
        # Heat of fusion energy for the additional quench crust that formed in this timestep
        quenchFormEnergy = MassQuenchAdded * Heat_fusion_MO
            
        # General heating
        AdditionalHeating = GH.GeneralHeating(GeneralHeatingSwitch, HeatingRate, timeStep)
                                                                                                                                                            
        # Energy to be released from the top (heat of fusion, secular cooling, heat of fusion of quench, additional heat)    
        # quenchFormEnergy is negative because Stefan problem already has dumped that much energy
        Energy2Dump = solidifEnergy + coolingEnergy - quenchFormEnergy + AdditionalHeating
        
        # If switch on, also add kinetic energy imparted by impacts
        if KineticEnergySwitch == True:
            Energy2Dump += KEefficiency * EnergyImpactors_thisTimestep

                                                                                
        # RELEASE ENERGY
                        
        # Pick energy dumping mechanism (radiation or conduction)
        if quenchThickness == 0 and CrustBuildOn == 0:
                    
            Rad_Flux = Emissivity * SB * (pow(Temperature_top_MO, 4) - pow(Temperature_equl, 4))
                    
            Lum_Radiation = surfArea_Moon * Rad_Flux
                    
            # Time needed to release energy through radiation
            time2Dump = Energy2Dump / Lum_Radiation
                                                
                                    
        elif QuenchSwitch == True and CrustBuildOn == 0:

            # If user wants to include impacts    
            if ImpactsSwitch == True:       
                     
                # Find what the surface temperature is...
                Temperature_top_quench = SurfTemperature.SurfaceTemperature(Temperature_melt, Temperature_melt, quenchThickness, Diffusivity_quench, density_quench, \
                                                                                Heat_capacity_quench, SB, Emissivity, Temperature_equl)                                
                                                                                                                  
                TotalHoleArea = 0
                Lum_holes = 0
                        
                for idx, rowVal in enumerate(holeTracker_copy):
                        
                    TotalHoleArea += rowVal[0]
                        
                    # if there is quench crust on top of hole...
                    if rowVal[1] != 0:
                        Lum_holes += rowVal[0] * Diffusivity_quench * density_quench * Heat_capacity_quench * (Temperature_melt - rowVal[2]) / rowVal[1]
                        
                    # if there isn't any quench crust on top of hole...
                    elif rowVal[1] == 0:
                        Lum_holes += rowVal[0] * Emissivity * SB * (pow(Temperature_top_MO, 4) - pow(Temperature_equl, 4))
                            
                Lum_cond_restMoon = (surfArea_Moon - TotalHoleArea) * Diffusivity_quench * density_quench * Heat_capacity_quench * (Temperature_melt - Temperature_top_quench) / quenchThickness
                        
                Lum_tot = Lum_holes + Lum_cond_restMoon
                    
                if surfArea_Moon < TotalHoleArea:
                    print("Warning: Total Hole Area Exceeds Total Surface Area of Moon (Quench Phase)")
                    quit()                    
                    
            # If not including impacts, then they have no effect
            else:                           
                                                                               
                Lum_tot = surfArea_Moon * Diffusivity_quench * density_quench * Heat_capacity_quench * (Temperature_melt - PresentTemperature_top_quench) / quenchThickness
            
            # Time needed to release energy through conduction
            time2Dump = Energy2Dump / Lum_tot
                
                                                                   
        elif CrustBuildOn == 1:             
                    
            # If user wants to include impacts
            if ImpactsSwitch == True:       
                            
                # Find what the surface temperature is...
                Temperature_top_crust = SurfTemperature.SurfaceTemperature(Temperature_top_MO, Temperature_top_MO, CrustalThickness, \
                                                                                Diffusivity_crust, density_crust, Heat_capacity_crust, SB, Emissivity, Temperature_equl)
                            
                TotalHoleArea = 0
                Lum_holes = 0
                                                
                for idx, rowVal in enumerate(holeTracker_copy):
                        
                    TotalHoleArea += rowVal[0]
                        
                    # if there is crust on top of hole...
                    if rowVal[1] != 0:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                        Lum_holes += rowVal[0] * Diffusivity_crust * density_crust * Heat_capacity_crust * (Temperature_melt - rowVal[2]) / rowVal[1]
                                        
                    # if there is no quench crust on top of hole...
                    elif rowVal[1] == 0:
                        Lum_holes += rowVal[0] * Emissivity * SB * (pow(Temperature_top_MO, 4) - pow(Temperature_equl, 4))
                            
                Lum_cond_restMoon = (surfArea_Moon - TotalHoleArea) * Diffusivity_crust * density_crust * Heat_capacity_crust * (Temperature_top_MO - Temperature_top_crust) / CrustalThickness
                        
                Lum_tot = Lum_holes + Lum_cond_restMoon
                        
                if surfArea_Moon < TotalHoleArea:
                    print("Warning: Total Hole Area Exceeds Total Surface Area of Moon (Plag Phase)")
                    quit()
                    
            # If not including impacts, then they have no effect
            elif ImpactsSwitch == False:
                            
                # Find what the surface temperature is...
                Temperature_top_crust = SurfTemperature.SurfaceTemperature(Temperature_top_MO, Temperature_top_MO, CrustalThickness, Diffusivity_crust, density_crust, \
                                                                            Heat_capacity_crust, SB, Emissivity, Temperature_equl)                          
                                                                            
                Lum_tot = surfArea_Moon * Diffusivity_crust * density_crust * Heat_capacity_crust * (Temperature_top_MO - Temperature_top_crust) / CrustalThickness
            
            # Time needed to release energy through conduction
            time2Dump = Energy2Dump / Lum_tot

        
        # Check if timestep is acceptable
        tolLevel = time2Dump * timeStep_tol
            
        if (timeStep <= time2Dump + tolLevel) and (timeStep >= time2Dump - tolLevel):               
            timestepAcceptable = True
            holeTracker = holeTracker_copy
                
            if CrustBuildOn == 1 and ImpactsSwitch == True:
                HoleThickness_times_HoleArea_Sum = sum(HoleThickness_times_HoleArea_array)
            
        else:                    
            timeStep = time2Dump
        
        
    # Update global quench crust thickness
    if QuenchSwitch == True and (quenchThickness < Max_Quench_Thickness):
        quenchThickness += (PresentQuenchThickness - quenchThickness) - Reduce_Global_Quench_Due_Impacts
        
        
    if QuenchSwitch == True:
        # Reduce magma ocean volume by the volume of the additional quench that solidified during this timestep
        MO_volume_current -= MassQuenchAdded / density_MO 
        
        # If volume of the magma ocean is less than 0 then stop the iterations
        if MO_volume_current < (percMO_remain_end/100) * MO_volume_initial:
            break    
                    
        # Remaining magma ocean liquid fraction
        fractionLiquid = MO_volume_current / MO_volume_initial        
                
                
    # CrustalThickness is only the thickness in non-hole areas so the actual gloabl crustal thickness is an average...        
    if CrustBuildOn == 1 and holeTracker:
                                                
        CrustalThickness = CrustalThickness + Extra_Crust_Due_Impacts #- Reduce_Global_Crust_Due_Impacts
        CrustThicknessImpMoon = HoleThickness_times_HoleArea_Sum / TotalHoleArea
            
        # Add impacted crustal thickness to array
        CrustalThickness_Impacted_array.append(CrustThicknessImpMoon)
        Time_array_impactedCrust.append(ellapsedTime)
            
        CrustalThickness_global = (CrustalThickness * (surfArea_Moon - TotalHoleArea) / surfArea_Moon) + (CrustThicknessImpMoon * TotalHoleArea / surfArea_Moon)
            
    else:
        CrustalThickness_global = CrustalThickness
        
                
    # Check to see if there are holes that have hole thickness about equal to the non-impacted surface crustal thickness
    # If so, remove those holes from holeTracker
    if CrustBuildOn == 0:
            
        # Keep only holes that have less quench than the global quench crust thickness
        holeTracker = [item for item in holeTracker if item[1] < quenchThickness]
                            
    elif CrustBuildOn == 1:
            
        # Keep only holes that have less crust than the global non-impacted crustal thickness
        holeTracker = [item for item in holeTracker if item[1] < CrustalThickness]
            
        
    if holeTracker:
        # Add total hole area to array
        tempHolder = np.array(holeTracker)
        
        holeAreaTracker_array.append((sum(tempHolder[:,0]) / surfArea_Moon) * 100)
        holeThicknessTracker_array.append(sum(tempHolder[:,1]) / len(tempHolder[:,1]))
        holeTemperatureTracker_array.append(sum(tempHolder[:,2]) / len(tempHolder[:,2]))
        
        holeTrackerElements_array.append(len(tempHolder))
        
        # Add area of holes added during this timestep to array
        holeAreaCreatedTracker_array.append(AreaHolesAdded_thisTimestep/(timeStep/3.154e7))
        
        # Cumulative hole area added to the Moon over time
        totalHoleAreaCum += AreaHolesAdded_thisTimestep
        totalHoleAreaCum_array.append((totalHoleAreaCum/surfArea_Moon)*100)
        
        Time_array_holes.append(ellapsedTime)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    # Add crustal thickness to array
    CrustalThickness_array.append(CrustalThickness)
                
    # Add global crustal thickness to array
    CrustalThickness_Global_array.append(CrustalThickness_global)
        
    # Add CMB temperature to array
    CMB_Temperature_array.append(CMB_Temperature)
                
    # Add new CMB location to array
    CMB_array.append(CMB)  
        
    # Add new liquid fraction to array
    LiqFrac_array.append(fractionLiquid)

    # Updated total mass added by impacts
    CumMassAddedImpacts += MassImpactors_thisTimestep
    
    # Updated total energy added by impacts
    CumEnergyAddedImpacts += KEefficiency * EnergyImpactors_thisTimestep
    
    # Updated total energy added by general heating
    CumGenHeatAdded += AdditionalHeating    
        
    # Updated total energy dumped
    CumEnergyDumped += Energy2Dump
        
    # Updated ellapsed time
    ellapsedTime += time2Dump
            
    # Store ellapsed time in array
    Time_array.append(ellapsedTime)
             
#####################################################################################################################################################
    
    
####### POST-PROCESSING #############################################################################################################################                   
    
# Mass bookkeeping
Mass_solid_interior_added = density_MO * (4/3) * np.pi * (pow(CMB, 3) - pow(Radius_moon - MO_depth_initial, 3)) 
    
Mass_crust_in_holes = 0
Last_Total_Hole_Area = 0
    
# The way this is done, there will be some error since assuming all crust density is plagioclase density
for valHoles in holeTracker:
    Mass_crust_in_holes += valHoles[0] * valHoles[1] * density_crust
    Last_Total_Hole_Area += valHoles[0]

Mass_crust_nonImpacted = CrustalThickness * (surfArea_Moon - Last_Total_Hole_Area) * density_crust
    
Mass_remaining_liquid = fractionLiquid * MO_volume_initial * density_MO
    
Mass_final_MO_crystallized = Mass_solid_interior_added + Mass_crust_in_holes + Mass_crust_nonImpacted + Mass_remaining_liquid

percSurfwithHoles = (Last_Total_Hole_Area / surfArea_Moon) * 100

    
plotTime = np.asarray(Time_array)
plotLiqFrac = np.asarray(LiqFrac_array)
plotCrustalThickness = np.asarray(CrustalThickness_array)
plotCrustalThickness_impacted = np.asarray(CrustalThickness_Impacted_array)
plotCrustalThickness_global = np.asarray(CrustalThickness_Global_array)
plotCMB_Temperature = np.asarray(CMB_Temperature_array)
plot_holeAreaTracker = np.asarray(holeAreaTracker_array)
plot_holeThicknessTracker = np.asarray(holeThicknessTracker_array)
plot_holeTemperatureTracker = np.asarray(holeTemperatureTracker_array)
plot_holeAreaCreatedTracker = np.asarray(holeAreaCreatedTracker_array)
plot_totalHoleAreaCum = np.asarray(totalHoleAreaCum_array)
plot_holeTrackerElements = np.asarray(holeTrackerElements_array)
plotTime_holes = np.asarray(Time_array_holes)
plotTime_impactedCrust = np.asarray(Time_array_impactedCrust)

# Write to a CSV file 
Output_file = np.vstack((plotTime, plotLiqFrac))
Output_file4 = np.vstack((plotTime, plotCMB_Temperature))
Output_file7 = np.vstack((plotTime, plotCrustalThickness, plotCrustalThickness_global))
Output_file8 = np.vstack((plotTime_holes, plot_holeAreaTracker, plot_holeThicknessTracker, plot_holeTemperatureTracker, \
                            plot_holeAreaCreatedTracker, plot_totalHoleAreaCum, plot_holeTrackerElements))
Output_file9 = np.vstack((plotTime_impactedCrust, plotCrustalThickness_impacted))

if ImpactsSwitch == True and QuenchSwitch == True:
    np.savetxt(UserPath + "wImpacts_wQuench.csv", Output_file, delimiter=",")
    np.savetxt(UserPath + "wImpacts_wQuench_TemperatureCMB.csv", Output_file4, delimiter=",")
    np.savetxt(UserPath + "wImpacts_wQuench_CrustalThickness.csv", Output_file7, delimiter=",")
    np.savetxt(UserPath + "wImpacts_wQuench_HoleTracker.csv", Output_file8, delimiter=",")
    np.savetxt(UserPath + "wImpacts_wQuench_impactedCrust.csv", Output_file9, delimiter=",")
                    
elif ImpactsSwitch == False and QuenchSwitch == True:
    np.savetxt(UserPath + "noImpacts_wQuench.csv", Output_file, delimiter=",")
    np.savetxt(UserPath + "noImpacts_wQuench_TemperatureCMB.csv", Output_file4, delimiter=",")
    np.savetxt(UserPath + "noImpacts_wQuench_CrustalThickness.csv", Output_file7, delimiter=",")
    
elif ImpactsSwitch == False and QuenchSwitch == False:
    np.savetxt(UserPath + "noImpacts_noQuench.csv", Output_file, delimiter=",")
    np.savetxt(UserPath + "noImpacts_noQuench_TemperatureCMB.csv", Output_file4, delimiter=",")
    np.savetxt(UserPath + "noImpacts_noQuench_CrustalThickness.csv", Output_file7, delimiter=",")
    
#####################################################################################################################################################
    
ellapsedTime_yrs = ellapsedTime/3.154e7
    
TimeStamp_end = datetime.datetime.now()
    
scriptRunDuration = TimeStamp_end - TimeStamp_start

tempArray = np.array([RunNumber, iMagma_version, scriptRunDuration.total_seconds(), vol_increments, timeStep_tol*100, ImpactsSwitch, QuenchSwitch, \
                        GeneralHeatingSwitch, LargestImpactorSize, MoonLocationDebrisCalc, mass2area, MO_depth_initial, MO_depth_plagBuild, \
                        plag_fraction, percMO_remain_end, Max_Quench_Thickness, density_MO, density_crust, density_quench, Heat_fusion_MO, \
                        Heat_capacity_MO, Heat_capacity_crust, Heat_capacity_quench, therm_exp_coeff_MO, Diffusivity_MO, Diffusivity_crust, \
                        Diffusivity_quench, dy_viscosity_MO, adiabslope, Temperature_melt, Temperature_equl, Emissivity, MO_mass_initial, \
                        Mass_final_MO_crystallized, CumMassAddedImpacts, CumEnergyAddedImpacts, HeatingRate, CumGenHeatAdded, fractionLiquid*100, \
                        crustBuildingStartTime_yrs, percSurfwithHoles, ellapsedTime_yrs, CrustalThickness_global])
                                                
# Append output to the CSV file                                                                    
with open(UserPath + 'scoreCard.csv', 'a') as f:
    np.savetxt(f, tempArray.reshape(1, tempArray.shape[0]), delimiter=',', fmt='%.7e')
