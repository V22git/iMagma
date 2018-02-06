"""
Plot maker for JGR-Planets publication

By: Viranga Perera & Alan P. Jackson
Modified: December 5, 2017

"""
from __future__ import division
import numpy as np
import matplotlib
matplotlib.use('Agg')   # Used for .eps files
import matplotlib.pyplot as plt
from matplotlib import gridspec

# Define path
UserPath = '/home/viranga/'

# Specify which plot to make (O is for all)
whichPlotsToMake = 6

# Set font
plt.rcParams["font.family"] = "serif"

# Calculate surface area of the Moon
Radius_moon = 1737.4e3                # Radius of the Moon (m)
surfArea_Moon = 4 * np.pi * pow(Radius_moon, 2)
circum_Moon = 2 * np.pi * Radius_moon

# Calculate percentage change
def PerChange(currentValues, compareValue):
    
    PercentChangeValues = np.empty([len(currentValues),1])
    
    for idx_p, val in enumerate(currentValues):
    
        PercentChangeValues[idx_p] = ((val - compareValue) / compareValue) * 100
    
    return PercentChangeValues



# Figure #1A
if (whichPlotsToMake == 1) or (whichPlotsToMake == 0):

    # Plot controls
    AxIncreFontSize = 17     # Plot axis increment font size
    AxLabelFontSize = 20     # Plot axis label font size

    plt.figure(11)

    # Get data
    Moon_100km_10Re = np.genfromtxt(UserPath + 'iMagma4/AlanData_100km_10Re.csv', delimiter=',', skip_header=1)
    Moon_500km_10Re = np.genfromtxt(UserPath + 'iMagma4/AlanData_500km_10Re.csv', delimiter=',', skip_header=1)
    Earth_100km_10Re = np.genfromtxt(UserPath + 'iMagma4/EarthData_100km_10Re.csv', delimiter=',', skip_header=1)
    Earth_500km_10Re = np.genfromtxt(UserPath + 'iMagma4/EarthData_500km_10Re.csv', delimiter=',', skip_header=1)

    # Line Plots
    plt.loglog(Moon_100km_10Re[:,0], Moon_100km_10Re[:,1], color='#db6d00', linewidth=2, label='Moon (LD = 100 km)')
    plt.loglog(Moon_500km_10Re[:,0], Moon_500km_10Re[:,1], color='#006ddb', linewidth=2, label='Moon (LD = 500 km)')
    plt.loglog(Earth_100km_10Re[:,0], Earth_100km_10Re[:,1], color='#009292', linewidth=2, label='Earth (LD = 100 km)')
    plt.loglog(Earth_500km_10Re[:,0], Earth_500km_10Re[:,1], color='#920000', linewidth=2, label='Earth (LD = 500 km)')

    # Background impact rate (based on Ryder 2002)
    plt.plot((1e0, 1e10), (2e10, 2e10), 'k', linestyle = '--', linewidth = 3, label='Background Rate')   
  
    #plt.ticklabel_format(axis='x', style='sci', scilimits=(0,0))
    plt.xlabel('Time (years)', fontsize = AxLabelFontSize)
    plt.xticks(fontsize = AxIncreFontSize)
    plt.xlim(1e1, 1e8)

    plt.ylabel('Mass Accretion Rate (kg/yr)', fontsize = AxLabelFontSize)
    plt.yticks(fontsize = AxIncreFontSize)
    #plt.ylim(0, 3.5e8)

    legend = plt.legend(shadow=True, fontsize = 'large', bbox_to_anchor=[0.01, 0.05], loc='lower left')

    fontNote = {'family': 'serif', 'color': 'k', 'weight': 'normal', 'size': 24}
    plt.text(3e6, 1e18, '10 $R_e$', fontdict=fontNote)

    plt.show()

    # Save current plot to eps
    plotName = UserPath + 'DebrisEvolution_Mass_10Re.eps'
    plt.savefig(plotName, bbox_inches='tight')
    plt.close()


# Figure #1B
if (whichPlotsToMake == 1) or (whichPlotsToMake == 0):

    # Plot controls
    AxIncreFontSize = 17     # Plot axis increment font size
    AxLabelFontSize = 20     # Plot axis label font size

    plt.figure(12)

    # Get data
    Moon_100km_60Re = np.genfromtxt(UserPath + 'iMagma4/AlanData_100km_60Re.csv', delimiter=',', skip_header=1)
    Moon_500km_60Re = np.genfromtxt(UserPath + 'iMagma4/AlanData_500km_60Re.csv', delimiter=',', skip_header=1)
    Earth_100km_60Re = np.genfromtxt(UserPath + 'iMagma4/EarthData_100km_60Re.csv', delimiter=',', skip_header=1)
    Earth_500km_60Re = np.genfromtxt(UserPath + 'iMagma4/EarthData_500km_60Re.csv', delimiter=',', skip_header=1)

    # Line Plots
    plt.loglog(Moon_100km_60Re[:,0], Moon_100km_60Re[:,1], color='#db6d00', linewidth=2, label='Moon (LD = 100 km)')
    plt.loglog(Moon_500km_60Re[:,0], Moon_500km_60Re[:,1], color='#006ddb', linewidth=2, label='Moon (LD = 500 km)')
    plt.loglog(Earth_100km_60Re[:,0], Earth_100km_60Re[:,1], color='#009292', linewidth=2, label='Earth (LD = 100 km)')
    plt.loglog(Earth_500km_60Re[:,0], Earth_500km_60Re[:,1], color='#920000', linewidth=2, label='Earth (LD = 500 km)')     

    # Background impact rate (based on Ryder 2002)                             
    plt.plot((1e1, 1e10), (2e10, 2e10), 'k', linestyle = '--', linewidth = 3, label='Background Rate')

    #plt.ticklabel_format(axis='x', style='sci', scilimits=(0,0))
    plt.xlabel('Time (years)', fontsize = AxLabelFontSize)
    plt.xticks(fontsize = AxIncreFontSize)
    plt.xlim(0, 1e8)

    plt.ylabel('Mass Accretion Rate (kg/yr)', fontsize = AxLabelFontSize)
    plt.yticks(fontsize = AxIncreFontSize)
    #plt.ylim(0, 3.5e8)

    #legend = plt.legend(loc='upper right', shadow=True, fontsize = 'x-large')

    fontNote = {'family': 'serif', 'color': 'k', 'weight': 'normal', 'size': 24}
    plt.text(3e6, 1e18, '60 $R_e$', fontdict=fontNote)

    plt.show()

    # Save current plot to eps
    plotName = UserPath + 'DebrisEvolution_Mass_60Re.eps'
    plt.savefig(plotName, bbox_inches='tight')
    plt.close()


# Figure #2A
if (whichPlotsToMake == 2) or (whichPlotsToMake == 0):

    # Plot controls
    AxIncreFontSize = 17     # Plot axis increment font size
    AxLabelFontSize = 20     # Plot axis label font size

    plt.figure(21, figsize=[7.25, 5.75])

    # Get data
    noImpacts_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_n/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImpacts_ke9_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_iA/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImpacts_ke7_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_iB/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImpacts_ke6_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_iC/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImpacts_ke5_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_iD/GrandScoreCard.csv', delimiter=',', skip_header=1)

    wImpacts_ke9_500km_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_iA_500/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImpacts_ke7_500km_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_iB_500/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImpacts_ke6_500km_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_iC_500/GrandScoreCard.csv', delimiter=',', skip_header=1)

    # Sort data from lowest to highest number of volume segments
    noImpacts_CT = noImpacts_CT[noImpacts_CT[:,3].argsort()]
    wImpacts_ke9_CT = wImpacts_ke9_CT[wImpacts_ke9_CT[:,3].argsort()]
    wImpacts_ke7_CT = wImpacts_ke7_CT[wImpacts_ke7_CT[:,3].argsort()]
    wImpacts_ke6_CT = wImpacts_ke6_CT[wImpacts_ke6_CT[:,3].argsort()]
    wImpacts_ke5_CT = wImpacts_ke5_CT[wImpacts_ke5_CT[:,3].argsort()]

    wImpacts_ke9_500km_CT = wImpacts_ke9_500km_CT[wImpacts_ke9_500km_CT[:,3].argsort()]
    wImpacts_ke7_500km_CT = wImpacts_ke7_500km_CT[wImpacts_ke7_500km_CT[:,3].argsort()]
    wImpacts_ke6_500km_CT = wImpacts_ke6_500km_CT[wImpacts_ke6_500km_CT[:,3].argsort()]

    # Scatter Plots
    plt.scatter(noImpacts_CT[:,3], noImpacts_CT[:,41]/1e6, s=110, marker='o', facecolor='k', edgecolor='k', label='$No\/Impacts$')
    plt.scatter(wImpacts_ke9_CT[:,3], wImpacts_ke9_CT[:,41]/1e6, s=110, marker='v', facecolor='#009292', edgecolor='#009292', label='$k = 10^9$ & LD = 100 km')    
    plt.scatter(wImpacts_ke7_CT[:,3], wImpacts_ke7_CT[:,41]/1e6, s=110, marker='s', facecolor='#920000', edgecolor='#920000', label='$k = 10^7$ & LD = 100 km')
    plt.scatter(wImpacts_ke6_CT[:,3], wImpacts_ke6_CT[:,41]/1e6, s=110, marker='>', facecolor='#006ddb', edgecolor='#006ddb', label='$k = 10^6$ & LD = 100 km')
    plt.scatter(wImpacts_ke5_CT[:,3], wImpacts_ke5_CT[:,41]/1e6, s=110, marker='D', facecolor='#db6d00', edgecolor='#db6d00', label='$k = 10^5$ & LD = 100 km')

    plt.scatter(wImpacts_ke9_500km_CT[:,3], wImpacts_ke9_500km_CT[:,41]/1e6, s=110, marker='v', linewidth='2', facecolor='none', edgecolor='#009292', label='$k = 10^9$ & LD = 500 km')
    plt.scatter(wImpacts_ke7_500km_CT[:,3], wImpacts_ke7_500km_CT[:,41]/1e6, s=110, marker='s', linewidth='2', facecolor='none', edgecolor='#920000', label='$k = 10^7$ & LD = 500 km')
    plt.scatter(wImpacts_ke6_500km_CT[:,3], wImpacts_ke6_500km_CT[:,41]/1e6, s=110, marker='>', linewidth='2', facecolor='none', edgecolor='#006ddb', label='$k = 10^6$ & LD = 500 km')

    # Line Plots
    plt.plot(noImpacts_CT[:,3], noImpacts_CT[:,41]/1e6, color='k')
    plt.plot(wImpacts_ke9_CT[:,3], wImpacts_ke9_CT[:,41]/1e6, color='#009292')    
    plt.plot(wImpacts_ke7_CT[:,3], wImpacts_ke7_CT[:,41]/1e6, color='#920000')
    plt.plot(wImpacts_ke6_CT[:,3], wImpacts_ke6_CT[:,41]/1e6, color='#006ddb')
    plt.plot(wImpacts_ke5_CT[:,3], wImpacts_ke5_CT[:,41]/1e6, color='#db6d00')

    plt.plot(wImpacts_ke9_500km_CT[:,3], wImpacts_ke9_500km_CT[:,41]/1e6, color='#009292', linestyle='--')    
    plt.plot(wImpacts_ke7_500km_CT[:,3], wImpacts_ke7_500km_CT[:,41]/1e6, color='#920000', linestyle='--')
    plt.plot(wImpacts_ke6_500km_CT[:,3], wImpacts_ke6_500km_CT[:,41]/1e6, color='#006ddb', linestyle='--')
 
    plt.ticklabel_format(axis='x', style='sci', scilimits=(0,0))
    plt.xlabel('Volume Segments', fontsize = AxLabelFontSize)
    plt.xticks(fontsize = AxIncreFontSize)
    plt.xlim(0, 8e5)

    plt.ylabel('LMO Solidification Time (Myr)', fontsize = AxLabelFontSize)
    plt.yticks(fontsize = AxIncreFontSize)
    #plt.ylim(0, 3.5e8)

    #legend = plt.legend(loc='upper right', shadow=True, fontsize = 'x-large', scatterpoints = 1)
 
    plt.show()

    # Save current plot to eps
    plotName = UserPath + 'CoolingTime_CT.eps'
    plt.savefig(plotName, bbox_inches='tight')
    plt.close()


# Figure #2B
if (whichPlotsToMake == 2) or (whichPlotsToMake == 0):

    # Plot controls
    AxIncreFontSize = 17     # Plot axis increment font size
    AxLabelFontSize = 20     # Plot axis label font size

    plt.figure(22, figsize=[7.25, 5.75])

    # Get data
    noImpacts_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_n/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImpacts_ke9_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_iA/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImpacts_ke7_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_iB/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImpacts_ke6_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_iC/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImpacts_ke5_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_iD/GrandScoreCard.csv', delimiter=',', skip_header=1)

    wImpacts_ke9_500km_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_iA_500/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImpacts_ke7_500km_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_iB_500/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImpacts_ke6_500km_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_iC_500/GrandScoreCard.csv', delimiter=',', skip_header=1)

    # Sort data from lowest to highest number of volume segments
    noImpacts_CT = noImpacts_CT[noImpacts_CT[:,3].argsort()]
    wImpacts_ke9_CT = wImpacts_ke9_CT[wImpacts_ke9_CT[:,3].argsort()]
    wImpacts_ke7_CT = wImpacts_ke7_CT[wImpacts_ke7_CT[:,3].argsort()]
    wImpacts_ke6_CT = wImpacts_ke6_CT[wImpacts_ke6_CT[:,3].argsort()]
    wImpacts_ke5_CT = wImpacts_ke5_CT[wImpacts_ke5_CT[:,3].argsort()]

    wImpacts_ke9_500km_CT = wImpacts_ke9_500km_CT[wImpacts_ke9_500km_CT[:,3].argsort()]
    wImpacts_ke7_500km_CT = wImpacts_ke7_500km_CT[wImpacts_ke7_500km_CT[:,3].argsort()]
    wImpacts_ke6_500km_CT = wImpacts_ke6_500km_CT[wImpacts_ke6_500km_CT[:,3].argsort()]

    # Scatter Plots
    plt.scatter(noImpacts_CT[:,3], PerChange(noImpacts_CT[:,41], noImpacts_CT[-1,41]), s=110, marker='o', facecolor='k', edgecolor='k', label='$No\/Impacts$')
    plt.scatter(wImpacts_ke9_CT[:,3], PerChange(wImpacts_ke9_CT[:,41], wImpacts_ke9_CT[-1,41]), s=110, marker='v', facecolor='#009292', edgecolor='#009292', label='$k=10^9$, $LD=100$')    
    plt.scatter(wImpacts_ke7_CT[:,3], PerChange(wImpacts_ke7_CT[:,41], wImpacts_ke7_CT[-1,41]), s=110, marker='s', facecolor='#920000', edgecolor='#920000', label='$k=10^7$, $LD=100$')
    plt.scatter(wImpacts_ke6_CT[:,3], PerChange(wImpacts_ke6_CT[:,41], wImpacts_ke6_CT[-1,41]), s=110, marker='>', facecolor='#006ddb', edgecolor='#006ddb', label='$k=10^6$, $LD=100$')
    plt.scatter(wImpacts_ke5_CT[:,3], PerChange(wImpacts_ke5_CT[:,41], wImpacts_ke5_CT[-1,41]), s=110, marker='D', facecolor='#db6d00', edgecolor='#db6d00', label='$k=10^5$, $LD=100$')

    plt.scatter(wImpacts_ke9_500km_CT[:,3], PerChange(wImpacts_ke9_500km_CT[:,41], wImpacts_ke9_500km_CT[-1,41]), s=110, marker='v', linewidth='2', facecolor='none', edgecolor='#009292', label='$k=10^9$, $LD=500$')
    plt.scatter(wImpacts_ke7_500km_CT[:,3], PerChange(wImpacts_ke7_500km_CT[:,41], wImpacts_ke7_500km_CT[-1,41]), s=110, marker='s', linewidth='2', facecolor='none', edgecolor='#920000', label='$k=10^7$, $LD=500$')
    plt.scatter(wImpacts_ke6_500km_CT[:,3], PerChange(wImpacts_ke6_500km_CT[:,41], wImpacts_ke6_500km_CT[-1,41]), s=110, marker='>', linewidth='2', facecolor='none', edgecolor='#006ddb', label='$k=10^6$, $LD=500$')

    # -2% and 0% reference lines
    plt.plot((-2, 8.2e5), (-2, -2), 'k', linestyle = '--', linewidth = 3)
    plt.plot((-2, 8.2e5), (0, 0), 'k', linewidth = 3)

    plt.ticklabel_format(axis='x', style='sci', scilimits=(0,0))
    plt.xlabel('Volume Segments', fontsize = AxLabelFontSize)
    plt.xticks(fontsize = AxIncreFontSize)
    plt.xlim(0, 8e5)
     
    #plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
    plt.ylabel('Compared to Most Vol. Seg. (%)', fontsize = AxLabelFontSize)
    plt.yticks(fontsize = AxIncreFontSize)
    plt.ylim(-15, 1)

    legend = plt.legend(loc='lower right', shadow=True, fontsize = 'large', scatterpoints = 1)

    plt.show()

    # Save current plot to eps
    plotName = UserPath + 'CompareToMostVolSeg_CT.eps'
    plt.savefig(plotName, bbox_inches='tight')
    plt.close()


# Figure #3
if (whichPlotsToMake == 3) or (whichPlotsToMake == 0):

    # Plot controls
    AxIncreFontSize = 17     # Plot axis increment font size
    AxLabelFontSize = 20     # Plot axis label font size

    plt.figure(3)

    # Get data
    wImpacts_ke9_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_iA/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImpacts_ke7_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_iB/GrandScoreCard.csv', delimiter=',', skip_header=1)    
    wImpacts_ke6_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_iC/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImpacts_ke5_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_iD/GrandScoreCard.csv', delimiter=',', skip_header=1)

    wImpacts_100km_rest = np.genfromtxt(UserPath + 'wKineticEnergy/iMagma4_KE_A/GrandScoreCard.csv', delimiter=',', skip_header=1)

    wImpacts_ke9_500km_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_iA_500/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImpacts_ke7_500km_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_iB_500/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImpacts_k3e6_500km_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_iF_500/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImpacts_ke6_500km_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_iC_500/GrandScoreCard.csv', delimiter=',', skip_header=1)

    wImpacts_500km_rest = np.genfromtxt(UserPath + 'Converge/iMagma4_iE_500/GrandScoreCard.csv', delimiter=',', skip_header=1)

    # Scatter Plots
    plt.scatter(wImpacts_ke9_CT[2,10], wImpacts_ke9_CT[2,40], s=170, marker='s', facecolor='#db6d00', edgecolor='k', label='Largest Debris = 100 km')    
    plt.scatter(wImpacts_100km_rest[2,10], wImpacts_100km_rest[2,40], s=170, marker='s', facecolor='#db6d00', edgecolor='k')
    plt.scatter(wImpacts_100km_rest[1,10], wImpacts_100km_rest[1,40], s=170, marker='s', facecolor='#db6d00', edgecolor='k')
    plt.scatter(wImpacts_100km_rest[0,10], wImpacts_100km_rest[0,40], s=170, marker='s', facecolor='#db6d00', edgecolor='k')
    plt.scatter(wImpacts_ke7_CT[2,10], wImpacts_ke7_CT[2,40], s=170, marker='s', facecolor='#db6d00', edgecolor='k')
    plt.scatter(wImpacts_100km_rest[3,10], wImpacts_100km_rest[3,40], s=170, marker='s', facecolor='#db6d00', edgecolor='k')
    plt.scatter(wImpacts_ke6_CT[7,10], wImpacts_ke6_CT[7,40], s=170, marker='s', facecolor='#db6d00', edgecolor='k')
    plt.scatter(wImpacts_100km_rest[4,10], wImpacts_100km_rest[4,40], s=170, marker='s', facecolor='#db6d00', edgecolor='k')
    plt.scatter(wImpacts_ke5_CT[4,10], wImpacts_ke5_CT[4,40], s=170, marker='s', facecolor='#db6d00', edgecolor='k')

    plt.scatter(wImpacts_ke9_500km_CT[8,10], wImpacts_ke9_500km_CT[8,40], s=170, marker='o', facecolor='none', edgecolor='#006ddb', linewidth='4', label='Largest Debris = 500 km')
    plt.scatter(wImpacts_500km_rest[2,10], wImpacts_500km_rest[2,40], s=170, marker='o', facecolor='none', edgecolor='#006ddb', linewidth='4')
    plt.scatter(wImpacts_500km_rest[1,10], wImpacts_500km_rest[1,40], s=170, marker='o', facecolor='none', edgecolor='#006ddb', linewidth='4')
    plt.scatter(wImpacts_500km_rest[0,10], wImpacts_500km_rest[0,40], s=170, marker='o', facecolor='none', edgecolor='#006ddb', linewidth='4')
    plt.scatter(wImpacts_ke7_500km_CT[7,10], wImpacts_ke7_500km_CT[7,40], s=170, marker='o', facecolor='none', edgecolor='#006ddb', linewidth='4')
    plt.scatter(wImpacts_k3e6_500km_CT[10], wImpacts_k3e6_500km_CT[40], s=170, marker='o', facecolor='none', edgecolor='#006ddb', linewidth='4')
    plt.scatter(wImpacts_ke6_500km_CT[5,10], wImpacts_ke6_500km_CT[5,40], s=170, marker='o', facecolor='none', edgecolor='#006ddb', linewidth='4')

    plt.xscale('log')
    plt.xlabel('$k$ (kg/m$^2$)', fontsize = AxLabelFontSize)
    plt.xticks(fontsize = AxIncreFontSize)
    plt.xlim(9e4, 2e9)

    plt.ylabel('Area with Holes (% Lunar Surface)', fontsize = AxLabelFontSize)
    plt.yticks(fontsize = AxIncreFontSize)
    plt.ylim(0, 100)

    legend = plt.legend(loc='upper right', shadow=True, fontsize = 'large', scatterpoints = 1)

    plt.show()

    # Save current plot to eps
    plotName = UserPath + 'SurfaceAreaWithHoles.eps'
    plt.savefig(plotName, bbox_inches='tight')
    plt.close()


# Figure #4
if (whichPlotsToMake == 4) or (whichPlotsToMake == 0):

    # Plot controls
    AxIncreFontSize = 17     # Plot axis increment font size
    AxLabelFontSize = 20     # Plot axis label font size
    
    plt.figure(4)
    
    # Get data
    Lindy = np.genfromtxt(UserPath + 'ParaSearch/NoImpacts/iMagma4_M/1/noImpacts_noQuench.csv', delimiter=',')
    Lindy_wQuench = np.genfromtxt(UserPath + 'ParaSearch/NoImpacts/iMagma4_B/1/noImpacts_wQuench.csv', delimiter=',')
    #Lindy_w250surfTemp = np.genfromtxt(UserPath + 'ParaSearch/NoImpacts/iMagma4_M/5/noImpacts_noQuench.csv', delimiter=',')
    #Lindy_w250surfTemp_wQuench = np.genfromtxt(UserPath + 'ParaSearch/NoImpacts/iMagma4_B/5/noImpacts_wQuench.csv', delimiter=',')
    
    # Plot
    plt.semilogx(Lindy[0,:]/3.154e7, Lindy[1,:]*100, '#006ddb', linewidth = 5, label='EBY11')
    plt.semilogx(Lindy_wQuench[0,:]/3.154e7, Lindy_wQuench[1,:]*100, '#db6d00', linestyle='--', linewidth = 5, label='EBY11 w/Quench')
    #plt.semilogx(Lindy_w250surfTemp[0,:]/3.154e7, Lindy_w250surfTemp[1,:]*100, '#0000CD', linestyle='--', linewidth = 4, label='CM w/HST')
    #plt.semilogx(Lindy_w250surfTemp_wQuench[0,:]/3.154e7, Lindy_w250surfTemp_wQuench[1,:]*100, '#0000CD', linestyle='--', linewidth = 4, label='CM w/HST & w/Quench')
    
    # Plot controls
    plt.show()
    
    plt.gca().invert_yaxis()
    
    plt.ylabel('Remaining LMO (%)', fontsize = AxLabelFontSize)
    plt.yticks(np.arange(0, 110, 10), fontsize = AxIncreFontSize)
    plt.ylim(0,100)
    
    plt.xlabel('Time (Years)', fontsize = AxLabelFontSize)
    plt.xlim(1e0,1e8)
    plt.xticks(fontsize = AxIncreFontSize)
    
    legend = plt.legend(loc='upper right', shadow=True, fontsize = 'large')
    
    # Save current plot to eps
    plotName = UserPath + 'LMO_FractRemain_overTime.eps'
    plt.savefig(plotName, bbox_inches='tight')
    plt.close()

        
# Figure #5
if (whichPlotsToMake == 5) or (whichPlotsToMake == 0):

    # Plot controls
    AxIncreFontSize = 17     # Plot axis increment font size
    AxLabelFontSize = 20     # Plot axis label font size
    
    plt.figure(5)
    fig, ax = plt.subplots()
    
    # Get data
    crust_noImpacts = np.genfromtxt(UserPath + 'Converge/iMagma4_n/3/noImpacts_wQuench_CrustalThickness.csv', delimiter=',')
    crust_k_1e9 = np.genfromtxt(UserPath + 'Converge/iMagma4_iA/3/wImpacts_wQuench_CrustalThickness.csv', delimiter=',')
    crust_k_1e7 = np.genfromtxt(UserPath + 'Converge/iMagma4_iB/3/wImpacts_wQuench_CrustalThickness.csv', delimiter=',')
    crust_k_1e6 = np.genfromtxt(UserPath + 'Converge/iMagma4_iC/12/wImpacts_wQuench_CrustalThickness.csv', delimiter=',')
    crust_k_1e5 = np.genfromtxt(UserPath + 'Converge/iMagma4_iD/9/wImpacts_wQuench_CrustalThickness.csv', delimiter=',')
    
    # Plot    
    ax.semilogx(crust_noImpacts[0,:]/3.154e7, crust_noImpacts[2,:]/1e3, 'k', linewidth = 4, label='$No\/Impacts$')
    ax.semilogx(crust_k_1e9[0,:]/3.154e7, crust_k_1e9[2,:]/1e3, '#009292', linestyle='--', linewidth = 4, label='$k = 10^9$')
    ax.semilogx(crust_k_1e7[0,:]/3.154e7, crust_k_1e7[2,:]/1e3, '#920000', linewidth = 4, label='$k = 10^7$')
    ax.semilogx(crust_k_1e6[0,:]/3.154e7, crust_k_1e6[2,:]/1e3, '#006ddb', linewidth = 4, label='$k = 10^6$')
    ax.semilogx(crust_k_1e5[0,:]/3.154e7, crust_k_1e5[2,:]/1e3, '#db6d00', linewidth = 4, label='$k = 10^5$')
    
    # Plot controls    
    legend = plt.legend(loc='upper left', shadow=True, fontsize = 'x-large')
    
    plt.ylabel('Crustal Thickness (km)', fontsize = AxLabelFontSize)
    plt.yticks(fontsize = AxIncreFontSize)
    #plt.yticks(np.arange(0, 110, 10), fontsize = AxIncreFontSize)
    #plt.ylim(0,5)
    
    plt.xlabel('Time (years)', fontsize = AxLabelFontSize)
    plt.xticks(fontsize = AxIncreFontSize)
    plt.xlim(1e4,1e8)
        
    plt.show()
    
    # Save current plot to eps
    plotName = UserPath + 'CrustalThickness_overTime.eps'
    plt.savefig(plotName, bbox_inches='tight')
    plt.close()


# Figure #6
if (whichPlotsToMake == 6) or (whichPlotsToMake == 0):

    # Plot controls
    AxIncreFontSize = 17     # Plot axis increment font size
    AxLabelFontSize = 20     # Plot axis label font size
    
    plt.figure(6)
    fig, ax = plt.subplots()

    # Get data
    holeTracker_k1e5 = np.genfromtxt(UserPath + 'histogramRuns/hist_3/1/wImpacts_wQuench_FinalHoleTrackerArray.csv', delimiter=',', skip_header=0)
    holeTracker_k3e5 = np.genfromtxt(UserPath + 'histogramRuns/hist_3/2/wImpacts_wQuench_FinalHoleTrackerArray.csv', delimiter=',', skip_header=0)
    holeTracker_k1e6 = np.genfromtxt(UserPath + 'histogramRuns/hist_2/1/wImpacts_wQuench_FinalHoleTrackerArray.csv', delimiter=',', skip_header=0)
    holeTracker_k3e6 = np.genfromtxt(UserPath + 'histogramRuns/hist_2/2/wImpacts_wQuench_FinalHoleTrackerArray.csv', delimiter=',', skip_header=0)
    holeTracker_k1e7 = np.genfromtxt(UserPath + 'histogramRuns/hist_1/1/wImpacts_wQuench_FinalHoleTrackerArray.csv', delimiter=',', skip_header=0)
    holeTracker_k3e7 = np.genfromtxt(UserPath + 'histogramRuns/hist_1/2/wImpacts_wQuench_FinalHoleTrackerArray.csv', delimiter=',', skip_header=0)
    holeTracker_k1e8 = np.genfromtxt(UserPath + 'histogramRuns/hist_1/3/wImpacts_wQuench_FinalHoleTrackerArray.csv', delimiter=',', skip_header=0)
    holeTracker_k3e8 = np.genfromtxt(UserPath + 'histogramRuns/hist_1/4/wImpacts_wQuench_FinalHoleTrackerArray.csv', delimiter=',', skip_header=0)
    holeTracker_k1e9 = np.genfromtxt(UserPath + 'histogramRuns/hist_1/5/wImpacts_wQuench_FinalHoleTrackerArray.csv', delimiter=',', skip_header=0)
    
    crustalThickness_k1e5 = np.genfromtxt(UserPath + 'histogramRuns/hist_3/1/wImpacts_wQuench_CrustalThickness.csv', delimiter=',', skip_header=0)
    crustalThickness_k3e5 = np.genfromtxt(UserPath + 'histogramRuns/hist_3/2/wImpacts_wQuench_CrustalThickness.csv', delimiter=',', skip_header=0)
    crustalThickness_k1e6 = np.genfromtxt(UserPath + 'histogramRuns/hist_2/1/wImpacts_wQuench_CrustalThickness.csv', delimiter=',', skip_header=0)
    crustalThickness_k3e6 = np.genfromtxt(UserPath + 'histogramRuns/hist_2/2/wImpacts_wQuench_CrustalThickness.csv', delimiter=',', skip_header=0)
    crustalThickness_k1e7 = np.genfromtxt(UserPath + 'histogramRuns/hist_1/1/wImpacts_wQuench_CrustalThickness.csv', delimiter=',', skip_header=0)
    crustalThickness_k3e7 = np.genfromtxt(UserPath + 'histogramRuns/hist_1/2/wImpacts_wQuench_CrustalThickness.csv', delimiter=',', skip_header=0)
    crustalThickness_k1e8 = np.genfromtxt(UserPath + 'histogramRuns/hist_1/3/wImpacts_wQuench_CrustalThickness.csv', delimiter=',', skip_header=0)
    crustalThickness_k3e8 = np.genfromtxt(UserPath + 'histogramRuns/hist_1/4/wImpacts_wQuench_CrustalThickness.csv', delimiter=',', skip_header=0)
    crustalThickness_k1e9 = np.genfromtxt(UserPath + 'histogramRuns/hist_1/5/wImpacts_wQuench_CrustalThickness.csv', delimiter=',', skip_header=0)

    # Get final non-impacted crustal thickness
    final_nonImp_crustalThickness_k1e5 = crustalThickness_k1e5[1,-1]
    final_nonImp_crustalThickness_k3e5 = crustalThickness_k3e5[1,-1]
    final_nonImp_crustalThickness_k1e6 = crustalThickness_k1e6[1,-1]
    final_nonImp_crustalThickness_k3e6 = crustalThickness_k3e6[1,-1]
    final_nonImp_crustalThickness_k1e7 = crustalThickness_k1e7[1,-1]
    final_nonImp_crustalThickness_k3e7 = crustalThickness_k3e7[1,-1]
    final_nonImp_crustalThickness_k1e8 = crustalThickness_k1e8[1,-1]
    final_nonImp_crustalThickness_k3e8 = crustalThickness_k3e8[1,-1]
    final_nonImp_crustalThickness_k1e9 = crustalThickness_k1e9[1,-1]
    
    # Sort holeTracker by thickness of holes (second column)
    holeTracker_k1e5 = holeTracker_k1e5[holeTracker_k1e5[:,1].argsort()]
    holeTracker_k3e5 = holeTracker_k3e5[holeTracker_k3e5[:,1].argsort()]
    holeTracker_k1e6 = holeTracker_k1e6[holeTracker_k1e6[:,1].argsort()]
    holeTracker_k3e6 = holeTracker_k3e6[holeTracker_k3e6[:,1].argsort()]
    holeTracker_k1e7 = holeTracker_k1e7[holeTracker_k1e7[:,1].argsort()]
    holeTracker_k3e7 = holeTracker_k3e7[holeTracker_k3e7[:,1].argsort()]
    holeTracker_k1e8 = holeTracker_k1e8[holeTracker_k1e8[:,1].argsort()]
    holeTracker_k3e8 = holeTracker_k3e8[holeTracker_k3e8[:,1].argsort()]
    holeTracker_k1e9 = holeTracker_k1e9[holeTracker_k1e9[:,1].argsort()]

    # Plot
    cummulativeArea_list_1e5 = []
    cummulativeArea_1e5 = 0
    
    for rowNum, rowValue in enumerate(holeTracker_k1e5):
        cummulativeArea_1e5 += rowValue[0]
        cummulativeArea_list_1e5.append(cummulativeArea_1e5)
    
    cummulativeArea_list_3e5 = []
    cummulativeArea_3e5 = 0
    
    for rowNum, rowValue in enumerate(holeTracker_k3e5):
        cummulativeArea_3e5 += rowValue[0]
        cummulativeArea_list_3e5.append(cummulativeArea_3e5)

    cummulativeArea_list_1e6 = []
    cummulativeArea_1e6 = 0

    for rowNum, rowValue in enumerate(holeTracker_k1e6):
        cummulativeArea_1e6 += rowValue[0]
        cummulativeArea_list_1e6.append(cummulativeArea_1e6)

    cummulativeArea_list_3e6 = []
    cummulativeArea_3e6 = 0
    
    for rowNum, rowValue in enumerate(holeTracker_k3e6):
        cummulativeArea_3e6 += rowValue[0]
        cummulativeArea_list_3e6.append(cummulativeArea_3e6)

    cummulativeArea_list_1e7 = []
    cummulativeArea_1e7 = 0

    for rowNum, rowValue in enumerate(holeTracker_k1e7):
        cummulativeArea_1e7 += rowValue[0]
        cummulativeArea_list_1e7.append(cummulativeArea_1e7)

    cummulativeArea_list_3e7 = []
    cummulativeArea_3e7 = 0
    
    for rowNum, rowValue in enumerate(holeTracker_k3e7):
        cummulativeArea_3e7 += rowValue[0]
        cummulativeArea_list_3e7.append(cummulativeArea_3e7)
    
    cummulativeArea_list_1e8 = []
    cummulativeArea_1e8 = 0
    
    for rowNum, rowValue in enumerate(holeTracker_k1e8):
        cummulativeArea_1e8 += rowValue[0]
        cummulativeArea_list_1e8.append(cummulativeArea_1e8)

    cummulativeArea_list_3e8 = []
    cummulativeArea_3e8 = 0
    
    for rowNum, rowValue in enumerate(holeTracker_k3e8):
        cummulativeArea_3e8 += rowValue[0]
        cummulativeArea_list_3e8.append(cummulativeArea_3e8)
    
    cummulativeArea_list_1e9 = []
    cummulativeArea_1e9 = 0

    for rowNum, rowValue in enumerate(holeTracker_k1e9):
        cummulativeArea_1e9 += rowValue[0]
        cummulativeArea_list_1e9.append(cummulativeArea_1e9)

    # Add surface area of Moon for last point (i.e. non-impacted crustal thickness)
    cummulativeArea_list_1e5.append(surfArea_Moon)
    cummulativeArea_list_3e5.append(surfArea_Moon)
    cummulativeArea_list_1e6.append(surfArea_Moon)
    cummulativeArea_list_3e6.append(surfArea_Moon)
    cummulativeArea_list_1e7.append(surfArea_Moon)
    cummulativeArea_list_3e7.append(surfArea_Moon)
    cummulativeArea_list_1e8.append(surfArea_Moon)
    cummulativeArea_list_3e8.append(surfArea_Moon)
    cummulativeArea_list_1e9.append(surfArea_Moon)

    # Convert lists into numpy arrays
    cummulativeArea_array_1e5 = np.asarray(cummulativeArea_list_1e5)
    cummulativeArea_array_3e5 = np.asarray(cummulativeArea_list_3e5)
    cummulativeArea_array_1e6 = np.asarray(cummulativeArea_list_1e6)
    cummulativeArea_array_3e6 = np.asarray(cummulativeArea_list_3e6)
    cummulativeArea_array_1e7 = np.asarray(cummulativeArea_list_1e7)
    cummulativeArea_array_3e7 = np.asarray(cummulativeArea_list_3e7)
    cummulativeArea_array_1e8 = np.asarray(cummulativeArea_list_1e8)
    cummulativeArea_array_3e8 = np.asarray(cummulativeArea_list_3e8)
    cummulativeArea_array_1e9 = np.asarray(cummulativeArea_list_1e9)

    # Add non-impacted crustal thickness
    holeTracker_k1e5 = np.vstack([holeTracker_k1e5, [-999, final_nonImp_crustalThickness_k1e5, -999]])
    holeTracker_k3e5 = np.vstack([holeTracker_k3e5, [-999, final_nonImp_crustalThickness_k3e5, -999]])
    holeTracker_k1e6 = np.vstack([holeTracker_k1e6, [-999, final_nonImp_crustalThickness_k1e6, -999]])
    holeTracker_k3e6 = np.vstack([holeTracker_k3e6, [-999, final_nonImp_crustalThickness_k3e6, -999]])
    holeTracker_k1e7 = np.vstack([holeTracker_k1e7, [-999, final_nonImp_crustalThickness_k1e7, -999]])
    holeTracker_k3e7 = np.vstack([holeTracker_k3e7, [-999, final_nonImp_crustalThickness_k3e7, -999]])
    holeTracker_k1e8 = np.vstack([holeTracker_k1e8, [-999, final_nonImp_crustalThickness_k1e8, -999]])
    holeTracker_k3e8 = np.vstack([holeTracker_k3e8, [-999, final_nonImp_crustalThickness_k3e8, -999]])
    holeTracker_k1e9 = np.vstack([holeTracker_k1e9, [-999, final_nonImp_crustalThickness_k1e9, -999]])

    # Plot
    ax.semilogy(holeTracker_k1e5[:,1]/1e3, (cummulativeArea_array_1e5/surfArea_Moon)*100, color='#009292', linewidth = 4, label='$k = 10^5$')
    #ax.semilogy(holeTracker_k3e5[:,1]/1e3, (cummulativeArea_array_3e5/surfArea_Moon)*100, linewidth = 4, label='$k = 3x10^5$')
    ax.semilogy(holeTracker_k1e6[:,1]/1e3, (cummulativeArea_array_1e6/surfArea_Moon)*100, color='#920000', linewidth = 4, label='$k = 10^6$')
    #ax.semilogy(holeTracker_k3e6[:,1]/1e3, (cummulativeArea_array_3e6/surfArea_Moon)*100, linewidth = 4, label='$k = 3x10^6$')
    ax.semilogy(holeTracker_k1e7[:,1]/1e3, (cummulativeArea_array_1e7/surfArea_Moon)*100, color='#006ddb', linewidth = 4, label='$k = 10^7$')
    #ax.semilogy(holeTracker_k3e7[:,1]/1e3, (cummulativeArea_array_3e7/surfArea_Moon)*100, linewidth = 4, label='$k = 3x10^7$')
    #ax.semilogy(holeTracker_k1e8[:,1]/1e3, (cummulativeArea_array_1e8/surfArea_Moon)*100, linewidth = 4, label='$k = 10^8$')
    #ax.semilogy(holeTracker_k3e8[:,1]/1e3, (cummulativeArea_array_3e8/surfArea_Moon)*100, linewidth = 4, label='$k = 3x10^8$')
    ax.semilogy(holeTracker_k1e9[:,1]/1e3, (cummulativeArea_array_1e9/surfArea_Moon)*100, color='#db6d00', linewidth = 4, label='$k = 10^9$')

    # GRAIL
    GRAIL_crustModel1 = np.genfromtxt('Model1_thick.dat', delimiter='\t')
    GRAIL_crustModel2 = np.genfromtxt('Model2_thick.dat', delimiter='\t')
    GRAIL_crustModel3 = np.genfromtxt('Model3_thick.dat', delimiter='\t')
    GRAIL_crustModel4 = np.genfromtxt('Model4_thick.dat', delimiter='\t')

    GRAIL_gridSpacing = 0.25 # degrees per bin

    GRAIL_crustModel1_Array = np.empty([721, 1441])
    arrayCol = 0
    arrayRow = 0

    for rowNum, rowValue in enumerate(GRAIL_crustModel1):
        GRAIL_crustModel1_Array[arrayRow, arrayCol] = rowValue
        arrayCol += 1
        
        if arrayCol == 1441:
            arrayCol = 0
            arrayRow += 1

    GRAIL_crustModel2_Array = np.empty([721, 1441])
    arrayCol = 0
    arrayRow = 0

    for rowNum, rowValue in enumerate(GRAIL_crustModel2):
        GRAIL_crustModel2_Array[arrayRow, arrayCol] = rowValue
        arrayCol += 1
        
        if arrayCol == 1441:
            arrayCol = 0
            arrayRow += 1

    GRAIL_crustModel3_Array = np.empty([721, 1441])
    arrayCol = 0
    arrayRow = 0

    for rowNum, rowValue in enumerate(GRAIL_crustModel3):
        GRAIL_crustModel3_Array[arrayRow, arrayCol] = rowValue
        arrayCol += 1
        
        if arrayCol == 1441:
            arrayCol = 0
            arrayRow += 1

    GRAIL_crustModel4_Array = np.empty([721, 1441])
    arrayCol = 0
    arrayRow = 0

    for rowNum, rowValue in enumerate(GRAIL_crustModel4):
        GRAIL_crustModel4_Array[arrayRow, arrayCol] = rowValue
        arrayCol += 1
        
        if arrayCol == 1441:
            arrayCol = 0
            arrayRow += 1

#    plt.figure(61)
#    plt.imshow(GRAIL_crustModel1_Array)
#    plt.show()
#    plotName = UserPath + 'GRAIL_test.eps'
#    plt.savefig(plotName, bbox_inches='tight')
#    plt.close()

    Moon_areaProjection_Array = np.empty([721, 1441])

    area_of_bin_at_equator = pow( (circum_Moon/360) * GRAIL_gridSpacing, 2)

    for rowNum, rowValue in enumerate(Moon_areaProjection_Array):
        Moon_areaProjection_Array[rowNum, :] = np.sin( (np.pi / 2) * ( (rowNum+1) / 361) ) * area_of_bin_at_equator

#    averageGRAIL_crustThick = np.sum( np.multiply(GRAIL_crustModel1_Array, Moon_areaProjection_Array) ) / surfArea_Moon
#    print('average: ', averageGRAIL_crustThick)

    arrayCol = 0
    arrayRow = 0
    GRAIL1_crust_and_area_Array = np.empty([1038961, 2])

    for rowNum, rowValue in enumerate(GRAIL1_crust_and_area_Array):
        GRAIL1_crust_and_area_Array[rowNum,0] = Moon_areaProjection_Array[arrayRow, arrayCol]
        GRAIL1_crust_and_area_Array[rowNum,1] = GRAIL_crustModel1_Array[arrayRow, arrayCol]

        arrayCol += 1

        if arrayCol == 1441:
            arrayCol = 0
            arrayRow += 1

    arrayCol = 0
    arrayRow = 0
    GRAIL2_crust_and_area_Array = np.empty([1038961, 2])
    
    for rowNum, rowValue in enumerate(GRAIL2_crust_and_area_Array):
        GRAIL2_crust_and_area_Array[rowNum,0] = Moon_areaProjection_Array[arrayRow, arrayCol]
        GRAIL2_crust_and_area_Array[rowNum,1] = GRAIL_crustModel2_Array[arrayRow, arrayCol]
        
        arrayCol += 1
        
        if arrayCol == 1441:
            arrayCol = 0
            arrayRow += 1

    arrayCol = 0
    arrayRow = 0
    GRAIL3_crust_and_area_Array = np.empty([1038961, 2])
    
    for rowNum, rowValue in enumerate(GRAIL3_crust_and_area_Array):
        GRAIL3_crust_and_area_Array[rowNum,0] = Moon_areaProjection_Array[arrayRow, arrayCol]
        GRAIL3_crust_and_area_Array[rowNum,1] = GRAIL_crustModel3_Array[arrayRow, arrayCol]
        
        arrayCol += 1
        
        if arrayCol == 1441:
            arrayCol = 0
            arrayRow += 1

    arrayCol = 0
    arrayRow = 0
    GRAIL4_crust_and_area_Array = np.empty([1038961, 2])
    
    for rowNum, rowValue in enumerate(GRAIL4_crust_and_area_Array):
        GRAIL4_crust_and_area_Array[rowNum,0] = Moon_areaProjection_Array[arrayRow, arrayCol]
        GRAIL4_crust_and_area_Array[rowNum,1] = GRAIL_crustModel4_Array[arrayRow, arrayCol]
        
        arrayCol += 1
        
        if arrayCol == 1441:
            arrayCol = 0
            arrayRow += 1

    # Sort by thickness of crust (second column)
    GRAIL1_crust_and_area_Array = GRAIL1_crust_and_area_Array[GRAIL1_crust_and_area_Array[:,1].argsort()]
    GRAIL2_crust_and_area_Array = GRAIL2_crust_and_area_Array[GRAIL2_crust_and_area_Array[:,1].argsort()]
    GRAIL3_crust_and_area_Array = GRAIL3_crust_and_area_Array[GRAIL3_crust_and_area_Array[:,1].argsort()]
    GRAIL4_crust_and_area_Array = GRAIL4_crust_and_area_Array[GRAIL4_crust_and_area_Array[:,1].argsort()]

    # Plot
    cummulativeArea_list_GRAIL_1 = []
    cummulativeArea_GRAIL_1 = 0

    for rowNum, rowValue in enumerate(GRAIL1_crust_and_area_Array):
        cummulativeArea_GRAIL_1 += rowValue[0]
        cummulativeArea_list_GRAIL_1.append(cummulativeArea_GRAIL_1)

    cummulativeArea_list_GRAIL_2 = []
    cummulativeArea_GRAIL_2 = 0

    for rowNum, rowValue in enumerate(GRAIL2_crust_and_area_Array):
        cummulativeArea_GRAIL_2 += rowValue[0]
        cummulativeArea_list_GRAIL_2.append(cummulativeArea_GRAIL_2)

    cummulativeArea_list_GRAIL_3 = []
    cummulativeArea_GRAIL_3 = 0

    for rowNum, rowValue in enumerate(GRAIL3_crust_and_area_Array):
        cummulativeArea_GRAIL_3 += rowValue[0]
        cummulativeArea_list_GRAIL_3.append(cummulativeArea_GRAIL_3)

    cummulativeArea_list_GRAIL_4 = []
    cummulativeArea_GRAIL_4 = 0

    for rowNum, rowValue in enumerate(GRAIL4_crust_and_area_Array):
        cummulativeArea_GRAIL_4 += rowValue[0]
        cummulativeArea_list_GRAIL_4.append(cummulativeArea_GRAIL_4)

    # Convert lists into numpy arrays
    cummulativeArea_array_GRAIL_1 = np.asarray(cummulativeArea_list_GRAIL_1)
    cummulativeArea_array_GRAIL_2 = np.asarray(cummulativeArea_list_GRAIL_2)
    cummulativeArea_array_GRAIL_3 = np.asarray(cummulativeArea_list_GRAIL_3)
    cummulativeArea_array_GRAIL_4 = np.asarray(cummulativeArea_list_GRAIL_4)

    # Plot
    ax.semilogy(GRAIL1_crust_and_area_Array[:,1], (cummulativeArea_array_GRAIL_1/surfArea_Moon)*100, color='k', linestyle='-', linewidth = 3, label='$GRAIL\/Model\/1$')
    #ax.semilogy(GRAIL2_crust_and_area_Array[:,1], (cummulativeArea_array_GRAIL_2/surfArea_Moon)*100, color='b', linestyle='--', linewidth = 3, label='GRAIL Model 2')
    ax.semilogy(GRAIL3_crust_and_area_Array[:,1], (cummulativeArea_array_GRAIL_3/surfArea_Moon)*100, color='k', linestyle='--', linewidth = 3, label='$GRAIL\/Model\/3$')
    #ax.semilogy(GRAIL4_crust_and_area_Array[:,1], (cummulativeArea_array_GRAIL_4/surfArea_Moon)*100, color='r', linestyle='--', linewidth = 3, label='GRAIL Model 4')

    # Plot controls
    legend = plt.legend(loc='lower right', shadow=True, fontsize = 'large')
    
    plt.ylabel('Percentage of Lunar Surface', fontsize = AxLabelFontSize)
    plt.yticks(fontsize = AxIncreFontSize)
    #plt.yticks(np.arange(0, 110, 10), fontsize = AxIncreFontSize)
    plt.ylim(1e-3, 1e2)
    
    plt.xlabel('Crustal Thickness (km)', fontsize = AxLabelFontSize)
    plt.xticks(fontsize = AxIncreFontSize)
    plt.xlim(0, 100)

    plt.show()
    
    # Save current plot to eps
    plotName = UserPath + 'Final_CrustalThickness_Histogram.eps'
    plt.savefig(plotName, bbox_inches='tight')
    plt.close()


# Figure #7
if (whichPlotsToMake == 7) or (whichPlotsToMake == 0):

    # Plot controls
    AxIncreFontSize = 10     # Plot axis increment font size
    AxLabelFontSize = 12     # Plot axis label font size
    solidLineWidth = 3
    dashLineWidth = 4

    fig = plt.figure(7)
    gs = gridspec.GridSpec(2, 2, height_ratios=[2, 1, 2, 1])

    # Get data
    noImp_MOdepth = np.genfromtxt(UserPath + 'ParaSearch/NoImpacts/iMagma4_nu_A/GrandScoreCard.csv', delimiter=',', skip_header=1)
    noImp_TempEqul = np.genfromtxt(UserPath + 'ParaSearch/NoImpacts/iMagma4_nu_B/GrandScoreCard.csv', delimiter=',', skip_header=1)
    noImp_PlagDepth = np.genfromtxt(UserPath + 'ParaSearch/NoImpacts/iMagma4_nu_C/GrandScoreCard.csv', delimiter=',', skip_header=1)
    noImp_QuenchThick = np.genfromtxt(UserPath + 'ParaSearch/NoImpacts/iMagma4_nu_D/GrandScoreCard.csv', delimiter=',', skip_header=1)
    noImp_Emissivity = np.genfromtxt(UserPath + 'ParaSearch/NoImpacts/iMagma4_nu_E/GrandScoreCard.csv', delimiter=',', skip_header=1)
    noImp_Tmelt = np.genfromtxt(UserPath + 'ParaSearch/NoImpacts/iMagma4_nu_F/GrandScoreCard.csv', delimiter=',', skip_header=1)
    noImp_Hfus = np.genfromtxt(UserPath + 'ParaSearch/NoImpacts/iMagma4_nu_G/GrandScoreCard.csv', delimiter=',', skip_header=1)
    noImp_cMO = np.genfromtxt(UserPath + 'ParaSearch/NoImpacts/iMagma4_nu_H/GrandScoreCard.csv', delimiter=',', skip_header=1)
    noImp_cCrust = np.genfromtxt(UserPath + 'ParaSearch/NoImpacts/iMagma4_nu_I/GrandScoreCard.csv', delimiter=',', skip_header=1)
    noImp_cQuench = np.genfromtxt(UserPath + 'ParaSearch/NoImpacts/iMagma4_nu_J/GrandScoreCard.csv', delimiter=',', skip_header=1)
    noImp_Viscosity = np.genfromtxt(UserPath + 'ParaSearch/NoImpacts/iMagma4_nu_K/GrandScoreCard.csv', delimiter=',', skip_header=1)
    noImp_Adiabat = np.genfromtxt(UserPath + 'ParaSearch/NoImpacts/iMagma4_nu_L/GrandScoreCard.csv', delimiter=',', skip_header=1)
    
    wImp_MOdepth = np.genfromtxt(UserPath + 'ParaSearch/wImpacts/iMagma4_iota_A/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImp_TempEqul = np.genfromtxt(UserPath + 'ParaSearch/wImpacts/iMagma4_iota_B/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImp_PlagDepth = np.genfromtxt(UserPath + 'ParaSearch/wImpacts/iMagma4_iota_C/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImp_QuenchThick = np.genfromtxt(UserPath + 'ParaSearch/wImpacts/iMagma4_iota_D/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImp_Emissivity = np.genfromtxt(UserPath + 'ParaSearch/wImpacts/iMagma4_iota_E/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImp_Tmelt = np.genfromtxt(UserPath + 'ParaSearch/wImpacts/iMagma4_iota_F/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImp_Hfus = np.genfromtxt(UserPath + 'ParaSearch/wImpacts/iMagma4_iota_G/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImp_cMO = np.genfromtxt(UserPath + 'ParaSearch/wImpacts/iMagma4_iota_H/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImp_cCrust = np.genfromtxt(UserPath + 'ParaSearch/wImpacts/iMagma4_iota_I/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImp_cQuench = np.genfromtxt(UserPath + 'ParaSearch/wImpacts/iMagma4_iota_J/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImp_Viscosity = np.genfromtxt(UserPath + 'ParaSearch/wImpacts/iMagma4_iota_K/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImp_Adiabat = np.genfromtxt(UserPath + 'ParaSearch/wImpacts/iMagma4_iota_L/GrandScoreCard.csv', delimiter=',', skip_header=1)
 
    # Set nominal case, to be used to calculate percentage change of variable   
    noImpNominalCase = noImp_MOdepth[4,:]
    wImpNominalCase = wImp_MOdepth[3,:]
       
    # Plot Axis1
    ax1 = plt.subplot(gs[0])    
    ax1.plot(PerChange(noImp_TempEqul[:,30], noImpNominalCase[30]), PerChange(noImp_TempEqul[:,41], noImpNominalCase[41]), color='#920000', linestyle='-', linewidth = solidLineWidth, label='Equl Rad Temp')
    ax1.plot(PerChange(noImp_PlagDepth[:,12], noImpNominalCase[12]), PerChange(noImp_PlagDepth[:,41], noImpNominalCase[41]), color='k', linestyle='-', linewidth = solidLineWidth, label='Plag Depth')
    ax1.plot(PerChange(noImp_Hfus[:,19], noImpNominalCase[19]), PerChange(noImp_Hfus[:,41], noImpNominalCase[41]), color='#006ddb', linestyle='--', linewidth = dashLineWidth, label='Heat Fusion')
    ax1.plot(PerChange(noImp_cMO[:,20], noImpNominalCase[20]), PerChange(noImp_cMO[:,41], noImpNominalCase[41]), color='#009292', linestyle='--', linewidth = dashLineWidth, label='Heat Cap. MO')
    ax1.plot(PerChange(noImp_cCrust[:,21], noImpNominalCase[21]), PerChange(noImp_cCrust[:,41], noImpNominalCase[41]), color='#009292', linestyle='-', linewidth = solidLineWidth, label='Heat Cap. Crust')
    ax1.plot(PerChange(noImp_Tmelt[:,29], noImpNominalCase[29]), PerChange(noImp_Tmelt[:,41], noImpNominalCase[41]), color='#920000', linestyle='--', linewidth = dashLineWidth, label='Quench Melt')
    ax1.plot(PerChange(noImp_Emissivity[:,31], noImpNominalCase[31]), PerChange(noImp_Emissivity[:,41], noImpNominalCase[41]), color='#db6d00', linestyle='--', linewidth = dashLineWidth, label='Emissivity')

    # Plot Axis2
    ax2 = plt.subplot(gs[1])    
    ax2.plot(PerChange(wImp_TempEqul[:,30], wImpNominalCase[30]), PerChange(wImp_TempEqul[:,41], wImpNominalCase[41]), color='#920000', linestyle='-', linewidth = solidLineWidth, label='Equl Rad Temp')
    ax2.plot(PerChange(wImp_PlagDepth[:,12], wImpNominalCase[12]), PerChange(wImp_PlagDepth[:,41], wImpNominalCase[41]), color='k', linestyle='-', linewidth = solidLineWidth, label='Plag Depth')    
    ax2.plot(PerChange(wImp_Hfus[:,19], wImpNominalCase[19]), PerChange(wImp_Hfus[:,41], wImpNominalCase[41]), color='#006ddb', linestyle='--', linewidth = dashLineWidth, label='Heat Fusion')
    ax2.plot(PerChange(wImp_cMO[:,20], wImpNominalCase[20]), PerChange(wImp_cMO[:,41], wImpNominalCase[41]), color='#009292', linestyle='--', linewidth = dashLineWidth, label='Heat Cap. MO')
    ax2.plot(PerChange(wImp_cCrust[:,21], wImpNominalCase[21]), PerChange(wImp_cCrust[:,41], wImpNominalCase[41]), color='#009292', linestyle='-', linewidth = solidLineWidth, label='Heat Cap. Crust')
    ax2.plot(PerChange(wImp_Tmelt[:,29], wImpNominalCase[29]), PerChange(wImp_Tmelt[:,41], wImpNominalCase[41]), color='#920000', linestyle='--', linewidth = dashLineWidth, label='Quench Melt')
    ax2.plot(PerChange(wImp_Emissivity[:,31], wImpNominalCase[31]), PerChange(wImp_Emissivity[:,41], wImpNominalCase[41]), color='#db6d00', linestyle='--', linewidth = dashLineWidth, label='Emissivity')

    # Plot Axis3
    ax3 = plt.subplot(gs[2])
    ax3.plot(PerChange(noImp_MOdepth[:,11], noImpNominalCase[11]), PerChange(noImp_MOdepth[:,41], noImpNominalCase[41]), color='#006ddb', linestyle='-', linewidth = solidLineWidth, label='MO Depth')
    ax3.plot(PerChange(noImp_cQuench[:,22], noImpNominalCase[22]), PerChange(noImp_cQuench[:,41], noImpNominalCase[41]), color='k', linestyle='--', linewidth = dashLineWidth, label='Heat Cap. Quench')
    ax3.plot(PerChange(noImp_QuenchThick[:,15], noImpNominalCase[15]), PerChange(noImp_QuenchThick[:,41], noImpNominalCase[41]), color='#db6d00', linestyle='-', linewidth = solidLineWidth, label='Quench Thickness')
    ax3.plot(PerChange(noImp_Adiabat[:,28], noImpNominalCase[28]), PerChange(noImp_Adiabat[:,41], noImpNominalCase[41]), color='#808080', linestyle='-', linewidth = solidLineWidth, label='Adiabat Slope')

    # Plot Axis4
    ax4 = plt.subplot(gs[3])
    ax4.plot(PerChange(wImp_MOdepth[:,11], wImpNominalCase[11]), PerChange(wImp_MOdepth[:,41], wImpNominalCase[41]), color='#006ddb', linestyle='-', linewidth = solidLineWidth, label='MO Depth')
    ax4.plot(PerChange(wImp_cQuench[:,22], wImpNominalCase[22]), PerChange(wImp_cQuench[:,41], wImpNominalCase[41]), color='k', linestyle='--', linewidth = dashLineWidth, label='Heat Cap. Quench')    
    ax4.plot(PerChange(wImp_QuenchThick[:,15], wImpNominalCase[15]), PerChange(wImp_QuenchThick[:,41], wImpNominalCase[41]), color='#db6d00', linestyle='-', linewidth = solidLineWidth, label='Quench Thickness')
    ax4.plot(PerChange(wImp_Adiabat[:,28], wImpNominalCase[28]), PerChange(wImp_Adiabat[:,41], wImpNominalCase[41]), color='#808080', linestyle='-', linewidth = solidLineWidth, label='Adiabat Slope')

    # Plot controls    
    legend1 = ax2.legend(bbox_to_anchor=(1.1, 0.5), loc='center left', ncol=1, handlelength=3, fontsize='x-small')

    legend2 = ax4.legend(bbox_to_anchor=(1.1, 0.5), loc='center left', ncol=1, handlelength=3, fontsize='x-small')

    ax1.annotate('LMO Solidification Time Change (%)', xy=(-0.17, 0.1), xycoords='axes fraction', fontsize=AxLabelFontSize,
                horizontalalignment='center', verticalalignment='center', rotation=90)

    ax3.annotate('Variable Change (%)', xy=(1.1, -0.5), xycoords='axes fraction', fontsize=AxLabelFontSize,
                horizontalalignment='center', verticalalignment='center')

    ax1.annotate('No Impacts', xy=(0.5, 1.1), xycoords='axes fraction', fontsize=AxLabelFontSize,
                horizontalalignment='center', verticalalignment='center')

    ax2.annotate('With Impacts', xy=(0.5, 1.1), xycoords='axes fraction', fontsize=AxLabelFontSize,
                horizontalalignment='center', verticalalignment='center')

    # Axis1
    ax1.tick_params(axis='both', which='major', labelsize=AxIncreFontSize)
    ax1.set_yticks(np.arange(-60, 100, 20))     
    ax1.set_xticks(np.arange(-100, 125, 25))
    ax1.set_ylim(-60,80)
    ax1.set_xlim(-100,100)
    #ax1.grid()

    # Axis2
    ax2.tick_params(axis='both', which='major', labelsize=AxIncreFontSize)
    ax2.set_yticks(np.arange(-60, 100, 20))   
    ax2.set_xticks(np.arange(-100, 125, 25))    
    ax2.set_ylim(-60,80)
    ax2.set_xlim(-100,100)
    #ax2.grid()

    # Axis3
    ax3.tick_params(axis='both', which='major', labelsize=AxIncreFontSize)
    ax3.set_yticks(np.arange(-3, 6, 3))
    ax3.set_xticks(np.arange(-75, 75, 25))
    ax3.set_ylim(-3,3)
    ax3.set_xlim(-75,50)
    #ax3.grid()

    # Axis4
    ax4.tick_params(axis='both', which='major', labelsize=AxIncreFontSize)
    ax4.set_yticks(np.arange(-3, 6, 3))
    ax4.set_xticks(np.arange(-75, 75, 25))
    ax4.set_ylim(-3,3)
    ax4.set_xlim(-75,50)
    #ax4.grid()

    plt.show()

    # Save current plot to eps
    plotName = UserPath + 'ParameterSensitivity.eps'
    plt.savefig(plotName, bbox_inches='tight')
    plt.close()


# Figure #8A
if (whichPlotsToMake == 8) or (whichPlotsToMake == 0):

    # Plot controls
    AxIncreFontSize = 17     # Plot axis increment font size
    AxLabelFontSize = 20     # Plot axis label font size

    plt.figure(81)

    # Get data
    Moon_100km_10Re = np.genfromtxt(UserPath + 'iMagma4/AlanData_100km_10Re.csv', delimiter=',', skip_header=1)
    Moon_500km_10Re = np.genfromtxt(UserPath + 'iMagma4/AlanData_500km_10Re.csv', delimiter=',', skip_header=1)
    Earth_100km_10Re = np.genfromtxt(UserPath + 'iMagma4/EarthData_100km_10Re.csv', delimiter=',', skip_header=1)
    Earth_500km_10Re = np.genfromtxt(UserPath + 'iMagma4/EarthData_500km_10Re.csv', delimiter=',', skip_header=1)

    # Line Plots
    plt.loglog(Moon_100km_10Re[:,0], Moon_100km_10Re[:,2], color='#db6d00', linewidth=2, label='Moon (LD = 100 km)')
    plt.loglog(Moon_500km_10Re[:,0], Moon_500km_10Re[:,2], color='#006ddb', linewidth=2, label='Moon (LD = 500 km)')
    plt.loglog(Earth_100km_10Re[:,0], Earth_100km_10Re[:,2], color='#009292', linewidth=2, label='Earth (LD = 100 km)')
    plt.loglog(Earth_500km_10Re[:,0], Earth_500km_10Re[:,2], color='#920000', linewidth=2, label='Earth (LD = 500 km)')   
  
    #plt.ticklabel_format(axis='x', style='sci', scilimits=(0,0))
    plt.xlabel('Time (years)', fontsize = AxLabelFontSize)
    plt.xticks(fontsize = AxIncreFontSize)
    #plt.xlim(0, 9e5)

    plt.ylabel('Energy Accretion Rate (J/yr)', fontsize = AxLabelFontSize)
    plt.yticks(fontsize = AxIncreFontSize)
    #plt.ylim(0, 3.5e8)

    legend = plt.legend(loc='lower left', shadow=True, fontsize = 'x-large')

    fontNote = {'family': 'serif', 'color': 'k', 'weight': 'normal', 'size': 24}
    plt.text(3e6, 1e26, '10 $R_e$', fontdict=fontNote)

    plt.show()

    # Save current plot to eps
    plotName = UserPath + 'DebrisEvolution_Energy_10Re.eps'
    plt.savefig(plotName, bbox_inches='tight')
    plt.close()


# Figure #8B
if (whichPlotsToMake == 8) or (whichPlotsToMake == 0):

    # Plot controls
    AxIncreFontSize = 17     # Plot axis increment font size
    AxLabelFontSize = 20     # Plot axis label font size

    plt.figure(82)

    # Get data
    Moon_100km_60Re = np.genfromtxt(UserPath + 'iMagma4/AlanData_100km_60Re.csv', delimiter=',', skip_header=1)
    Moon_500km_60Re = np.genfromtxt(UserPath + 'iMagma4/AlanData_500km_60Re.csv', delimiter=',', skip_header=1)
    Earth_100km_60Re = np.genfromtxt(UserPath + 'iMagma4/EarthData_100km_60Re.csv', delimiter=',', skip_header=1)
    Earth_500km_60Re = np.genfromtxt(UserPath + 'iMagma4/EarthData_500km_60Re.csv', delimiter=',', skip_header=1)

    # Line Plots
    plt.loglog(Moon_100km_60Re[:,0], Moon_100km_60Re[:,2], color='#db6d00', linewidth=2, label='Moon (LD = 100 km)')
    plt.loglog(Moon_500km_60Re[:,0], Moon_500km_60Re[:,2], color='#006ddb', linewidth=2, label='Moon (LD = 500 km)')
    plt.loglog(Earth_100km_60Re[:,0], Earth_100km_60Re[:,2], color='#009292', linewidth=2, label='Earth (LD = 100 km)')
    plt.loglog(Earth_500km_60Re[:,0], Earth_500km_60Re[:,2], color='#920000', linewidth=2, label='Earth (LD = 500 km)')     

    #plt.ticklabel_format(axis='x', style='sci', scilimits=(0,0))
    plt.xlabel('Time (years)', fontsize = AxLabelFontSize)
    plt.xticks(fontsize = AxIncreFontSize)
    #plt.xlim(0, 9e5)

    plt.ylabel('Energy Accretion Rate (J/yr)', fontsize = AxLabelFontSize)
    plt.yticks(fontsize = AxIncreFontSize)
    #plt.ylim(0, 3.5e8)

    #legend = plt.legend(loc='upper right', shadow=True, fontsize = 'x-large')

    fontNote = {'family': 'serif', 'color': 'k', 'weight': 'normal', 'size': 24}
    plt.text(3e6, 1e26, '60 $R_e$', fontdict=fontNote)

    plt.show()

    # Save current plot to eps
    plotName = UserPath + 'DebrisEvolution_Energy_60Re.eps'
    plt.savefig(plotName, bbox_inches='tight')
    plt.close()


# Figure #9
if (whichPlotsToMake == 9) or (whichPlotsToMake == 0):

    # Plot controls
    AxIncreFontSize = 17     # Plot axis increment font size
    AxLabelFontSize = 20     # Plot axis label font size

    plt.figure(9)

    # Get data

    # No impacts
    noImpacts = np.genfromtxt(UserPath + 'Converge/iMagma4_n/GrandScoreCard.csv', delimiter=',', skip_header=1) 
    
    # With kinetic energy added
    wKineticEnergy_1 = np.genfromtxt(UserPath + 'wKineticEnergy/iMagma4_KE_B/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wKineticEnergy_point5 = np.genfromtxt(UserPath + 'wKineticEnergy/iMagma4_KE_C/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wKineticEnergy_point1 = np.genfromtxt(UserPath + 'wKineticEnergy/iMagma4_KE_D/GrandScoreCard.csv', delimiter=',', skip_header=1)

    # Without kinetic energy
    wImpacts_ke9_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_iA/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImpacts_ke7_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_iB/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImpacts_ke6_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_iC/GrandScoreCard.csv', delimiter=',', skip_header=1)
    wImpacts_ke5_CT = np.genfromtxt(UserPath + 'Converge/iMagma4_iD/GrandScoreCard.csv', delimiter=',', skip_header=1)
    
    wImpacts_restWithoutKE = np.genfromtxt(UserPath + 'wKineticEnergy/iMagma4_KE_A/GrandScoreCard.csv', delimiter=',', skip_header=1)    

    # No impacts reference line
    plt.plot((1e4, 1e10), (noImpacts[2,41]/1e6, noImpacts[2,41]/1e6), 'k', linestyle = '--', linewidth = 3, label='No Impacts')

    # Scatter Plots
    plt.scatter(wKineticEnergy_1[:,10], wKineticEnergy_1[:,41]/1e6, s=170, marker='D', facecolor='#db6d00', edgecolor='k', label='$\lambda_{KE}$ = 1')
    plt.scatter(wKineticEnergy_point5[:,10], wKineticEnergy_point5[:,41]/1e6, s=170, marker='v', facecolor='#006ddb', edgecolor='k', label='$\lambda_{KE}$ = 0.5')
    plt.scatter(wKineticEnergy_point1[:,10], wKineticEnergy_point1[:,41]/1e6, s=170, marker='s', facecolor='#009292', edgecolor='k', label='$\lambda_{KE}$ = 0.1')
    
    plt.scatter(wImpacts_ke9_CT[2,10], wImpacts_ke9_CT[2,41]/1e6, s=170, marker='o', facecolor='#920000', edgecolor='k', label='No KE Added')    
    plt.scatter(wImpacts_ke7_CT[2,10], wImpacts_ke7_CT[2,41]/1e6, s=170, marker='o', facecolor='#920000', edgecolor='k')
    plt.scatter(wImpacts_ke6_CT[7,10], wImpacts_ke6_CT[7,41]/1e6, s=170, marker='o', facecolor='#920000', edgecolor='k')
    plt.scatter(wImpacts_ke5_CT[4,10], wImpacts_ke5_CT[4,41]/1e6, s=170, marker='o', facecolor='#920000', edgecolor='k')
    
    plt.scatter(wImpacts_restWithoutKE[:,10], wImpacts_restWithoutKE[:,41]/1e6, s=170, marker='o', facecolor='#920000', edgecolor='k')

    # Plot controls
    plt.xscale('log')
    plt.xlabel('$k$ (kg/m$^2$)', fontsize = AxLabelFontSize)
    plt.xticks(fontsize = AxIncreFontSize)
    plt.xlim(9e4, 2e9)

    plt.ylabel('LMO Solidification Time (Myr)', fontsize = AxLabelFontSize)
    plt.yticks(fontsize = AxIncreFontSize)
    #plt.ylim(0, 100)

    legend = plt.legend(loc='lower right', shadow=True, fontsize = 'large', scatterpoints = 1)

    plt.show()

    # Save current plot to eps
    plotName = UserPath + 'wKineticEnergy.eps'
    plt.savefig(plotName, bbox_inches='tight')
    plt.close()


# Figure #10
if (whichPlotsToMake == 10) or (whichPlotsToMake == 0):

    plt.figure(10)

    # Plot controls
    AxIncreFontSize = 17     # Plot axis increment font size
    AxLabelFontSize = 20     # Plot axis label font size
    
    # Number of different heating rates
    Num_HeatRates_noImpacts = 23
    Num_HeatRates_ke7 = 17
    Num_HeatRates_ke7_wKE = 10
    Num_HeatRates_ke6 = 20
    Num_HeatRates_ke6_wKE = 13
    Num_HeatRates_ke5 = 8
    Num_HeatRates_ke5_wKE = 4
          
    # Initialize empty arrays
    noImpactsArray = np.empty([Num_HeatRates_noImpacts,2])
    wImpactsArray_ke7 = np.empty([Num_HeatRates_ke7,2])
    wImpactsArray_ke7_wKE = np.empty([Num_HeatRates_ke7_wKE,2])
    wImpactsArray_ke6 = np.empty([Num_HeatRates_ke6,2])
    wImpactsArray_ke6_wKE = np.empty([Num_HeatRates_ke6_wKE,2])
    wImpactsArray_ke5 = np.empty([Num_HeatRates_ke5,2])
    wImpactsArray_ke5_wKE = np.empty([Num_HeatRates_ke5_wKE,2])
 
    # Get data
    for toImpactorNot in range(2):

        # Choose with (1) or without (0) impacts sets
        if toImpactorNot == 0:
            typeSelect = 'wHeating/iMagma4_heat_D/'
            
            # Go through the different parameter search runs
            for i in range(0, Num_HeatRates_noImpacts):

                temp_data = np.genfromtxt(UserPath + typeSelect + 'GrandScoreCard.csv', delimiter=',', skip_header=1)

                noImpactsArray[i,0] = temp_data[i,36]
                noImpactsArray[i,1] = temp_data[i,41]

        elif toImpactorNot == 1:
            
            # ke7
            typeSelect = 'wHeating/iMagma4_heat_C/'

            for i in range(0, Num_HeatRates_ke7):

                temp_data = np.genfromtxt(UserPath + typeSelect + 'GrandScoreCard.csv', delimiter=',', skip_header=1)

                wImpactsArray_ke7[i,0] = temp_data[i,36]
                wImpactsArray_ke7[i,1] = temp_data[i,41]

            # ke7 with kinetic energy
            typeSelect = 'wHeating/iMagma4_heat_B/'

            for i in range(0, Num_HeatRates_ke7_wKE):

                temp_data = np.genfromtxt(UserPath + typeSelect + 'GrandScoreCard.csv', delimiter=',', skip_header=1)

                wImpactsArray_ke7_wKE[i,0] = temp_data[i,36]
                wImpactsArray_ke7_wKE[i,1] = temp_data[i,41]


            # ke6
            typeSelect = 'wHeating/iMagma4_heat_E/'

            for i in range(0, Num_HeatRates_ke6):

                temp_data = np.genfromtxt(UserPath + typeSelect + 'GrandScoreCard.csv', delimiter=',', skip_header=1)

                wImpactsArray_ke6[i,0] = temp_data[i,36]
                wImpactsArray_ke6[i,1] = temp_data[i,41]

            # ke6 with kinetic energy
            typeSelect = 'wHeating/iMagma4_heat_A/'

            for i in range(0, Num_HeatRates_ke6_wKE):

                temp_data = np.genfromtxt(UserPath + typeSelect + 'GrandScoreCard.csv', delimiter=',', skip_header=1)

                wImpactsArray_ke6_wKE[i,0] = temp_data[i,36]
                wImpactsArray_ke6_wKE[i,1] = temp_data[i,41]

            # ke5
            typeSelect = 'wHeating/iMagma4_heat_F/'

            for i in range(0, Num_HeatRates_ke5):

                temp_data = np.genfromtxt(UserPath + typeSelect + 'GrandScoreCard.csv', delimiter=',', skip_header=1)

                wImpactsArray_ke5[i,0] = temp_data[i,36]
                wImpactsArray_ke5[i,1] = temp_data[i,41]

            # ke5 with kinetic energy
            typeSelect = 'wHeating/iMagma4_heat_G/'

            for i in range(0, Num_HeatRates_ke5_wKE):

                temp_data = np.genfromtxt(UserPath + typeSelect + 'GrandScoreCard.csv', delimiter=',', skip_header=1)

                wImpactsArray_ke5_wKE[i,0] = temp_data[i,36]
                wImpactsArray_ke5_wKE[i,1] = temp_data[i,41]


 
    # Plot
    plt.scatter(noImpactsArray[:,0]/1e12, noImpactsArray[:,1]/1e6, s=80, marker='o', facecolor='#db6d00', edgecolor='k', label='$No\/Impacts$')
    plt.scatter(wImpactsArray_ke7[:,0]/1e12, wImpactsArray_ke7[:,1]/1e6, s=90, marker='v', facecolor='#006ddb', edgecolor='k', label='$k = 10^7$ ($\lambda_{KE} = 0$)')
    plt.scatter(wImpactsArray_ke7_wKE[:,0]/1e12, wImpactsArray_ke7_wKE[:,1]/1e6, s=90, marker='v', facecolor='none', linewidth='2', edgecolor='#006ddb', label='$k = 10^7$ ($\lambda_{KE} = 1$)')
    plt.scatter(wImpactsArray_ke6[:,0]/1e12, wImpactsArray_ke6[:,1]/1e6, s=80, marker='D', facecolor='#009292', edgecolor='k', label='$k = 10^6$ ($\lambda_{KE} = 0$)')
    plt.scatter(wImpactsArray_ke6_wKE[:,0]/1e12, wImpactsArray_ke6_wKE[:,1]/1e6, s=80, marker='D', facecolor='none', linewidth='2', edgecolor='#009292', label='$k = 10^6$ ($\lambda_{KE} = 1$)')
    plt.scatter(wImpactsArray_ke5[:,0]/1e12, wImpactsArray_ke5[:,1]/1e6, s=80, marker='s', facecolor='#920000', edgecolor='k', label='$k = 10^5$ ($\lambda_{KE} = 0$)')
    plt.scatter(wImpactsArray_ke5_wKE[:,0]/1e12, wImpactsArray_ke5_wKE[:,1]/1e6, s=80, marker='s', facecolor='none', linewidth='2', edgecolor='#920000', label='$k = 10^5$ ($\lambda_{KE} = 1$)')
 
    plt.xlabel('Additional Heating (TW)', fontsize = AxLabelFontSize)
    plt.xticks(np.arange(0, 26, 2), fontsize = AxIncreFontSize)
    plt.xlim(0, 24)

    plt.ylabel('LMO Solidification Time (Myr)', fontsize = AxLabelFontSize)
    plt.yticks(np.arange(0, 420, 60), fontsize = AxIncreFontSize)
    plt.ylim(0, 360)
    
    legend = plt.legend(loc='upper right', shadow=True, fontsize = 'large', scatterpoints = 1)
 
    plt.show()

    # Save current plot to eps
    plotName = UserPath + 'ExtraHeating.eps'
    plt.savefig(plotName, bbox_inches='tight')
    plt.close()
