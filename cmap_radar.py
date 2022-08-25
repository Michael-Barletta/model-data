import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
#Table of various radar colormaps

def transparent_white(cmap):
    #Set white colors to transparent given list of RGB lists
    #by converting R,G,B to R,G,B,A
    cmap_new=[(rgb+[0]) if rgb==[255,255,255] else (rgb+[255]) for i,rgb in enumerate(cmap)]
    return cmap_new

def refl_codebr(levels = np.arange(-15,86,1), return_array = False):
    '''Reflectivity colormap based on "Code BR" color table
    Source: http://almanydesigns.com/grx/reflectivity/ 
    Designed for use from -15 to 85 dBZ, with steps every 1 dBZ
    Options: return_array (T/F)
        False: return cmap, norm, and list of contour fill levels
        True: return raw array of RGB values (0-1, normalized by 255)
    '''
    refl_levs = levels
    c=[[
    #0,0,0],[ #-15
    6,0,8],[
    13,0,16],[
    19,0,24],[
    25,1,32],[
    31,1,40],[
    38,1,48],[
    44,1,55],[
    50,1,63],[
    56,1,71],[
    61,3,78],[ #-5	
    61,9,84],[
    62,16,89],[
    62,22,95],[
    63,28,100],[
    63,35,106],[ #0
    64,41,111],[
    64,47,117],[
    64,53,123],[
    65,60,128],[
    65,66,134],[ #+5
    66,72,139],[
    66,79,145],[
    66,85,150],[
    67,91,156],[
    67,97,162],[ #+10
    73,113,171],[
    78,129,180],[
    84,145,190],[
    89,161,199],[
    95,176,209],[ #+15
    100,192,218],[
    106,208,228],[
    111,214,232],[ #+18
    92,214,185],[
    72,213,138],[ #+20
    53,213,91],[ 
    17,213,24],[ #+22
    16,204,23],[
    16,195,22],[
    15,186,21],[ #+25
    15,177,19],[
    14,168,18],[
    13,158,17],[
    13,149,16],[
    12,140,15],[
    12,131,14],[
    11,122,13],[
    10,113,12],[
    10,103,10],[
    #9,94,9],[
    29,104,9],[ #+35
    81,131,8],[
    132,157,7],[
    183,184,5],[
    234,210,4],[
    255,226,0],[ #+40
    255,217,0],[
    255,207,0],[
    255,197,0],[
    255,187,0],[
    255,177,0],[
    255,167,0],[
    255,157,0],[
    255,147,0],[
    255,137,0],[
    255,128,0],[ #+50
    255,0,0],[
    240,0,0],[
    224,0,0],[
    208,0,0],[
    192,0,0],[
    176,0,0],[
    160,0,0],[
    144,0,0],[
    128,0,0],[
    113,0,0],[ #+60
    255,255,255],[
    255,228,255],[
    255,200,255],[
    255,173,255],[
    255,145,255],[
    255,117,255],[
    248,91,248],[
    241,65,241],[
    234,39,233],[
    225,11,227],[  #+70
    178,0,255],[
    159,0,245],[
    139,0,235],[
    119,0,224],[
    99,0,214],[  #+75
    5,236,241],[
    5,215,220],[
    4,195,199],[
    4,175,178],[
    3,154,157],[
    3,134,136],[
    2,114,115],[
    2,93,95],[
    1,73,74],[
    1,53,53]] #+85
    if return_array:
        return (np.array(c)/255.)
    else:
        cmap_refl = mpl.colors.ListedColormap(np.array(c)/255.)
        cmap_refl.set_under((1,1,1,0)) #set values lower than min to transparent white
        norm_refl = mpl.colors.BoundaryNorm(refl_levs, ncolors = len(c))
        return (cmap_refl, norm_refl, refl_levs)

def refl_codebr_ma5(levels = np.arange(5,86,1), return_array = False):
    '''Reflectivity colormap based on "Code BR" color table
    Source: http://almanydesigns.com/grx/reflectivity/ 
    Designed for use from 5 to 85 dBZ, with steps every 1 dBZ
    Same as refl_codebr, but omits lower end of color table (for values above +5 dBZ)
    Options: return_array (T/F)
        False: return cmap, norm, and list of contour fill levels
        True: return raw array of RGB values (0-1, normalized by 255)
    '''
    refl_levs = levels 
    c = refl_codebr(return_array = True)[20:]
    if return_array:
        return (c)
    else:
        cmap_refl = mpl.colors.ListedColormap(c)
        cmap_refl.set_under((1,1,1,0)) #set values lower than min to transparent white
        norm_refl = mpl.colors.BoundaryNorm(refl_levs, ncolors = len(c))
        return (cmap_refl, norm_refl, refl_levs)

def refl_codebr_m5_85(levels = np.arange(-5,86,1), return_array = False):
    '''Reflectivity colormap based on "Code BR" color table
    Source: http://almanydesigns.com/grx/reflectivity/ 
    Designed for use from -5 to 85 dBZ, with steps every 1 dBZ
    Same as refl_codebr, but omits lower end of color table (for values above -5 dBZ)
    Options: return_array (T/F)
        False: return cmap, norm, and list of contour fill levels
        True: return raw array of RGB values (0-1, normalized by 255)
    '''
    refl_levs = levels 
    c = refl_codebr(return_array = True)[10:]
    if return_array:
        return (c)
    else:
        cmap_refl = mpl.colors.ListedColormap(c)
        cmap_refl.set_under((1,1,1,0)) #set values lower than min to transparent white
        norm_refl = mpl.colors.BoundaryNorm(refl_levs, ncolors = len(c))
        return (cmap_refl, norm_refl, refl_levs)

def refl_codebr_m5_45(levels = np.arange(-5,46,1), return_array = False):
    '''Reflectivity colormap based on "Code BR" color table
    Source: http://almanydesigns.com/grx/reflectivity/ 
    Designed for use from -5 to 45 dBZ, with steps every 1 dBZ
    Same as refl_codebr, but omits lower and upper ends of color table (for values between -5 and +45 dBZ)
    Options: return_array (T/F)
        False: return cmap, norm, and list of contour fill levels
        True: return raw array of RGB values (0-1, normalized by 255)
    '''
    refl_levs = levels 
    c = refl_codebr(return_array = True)[10:50]
    if return_array:
        return c
    else:
        cmap_refl = mpl.colors.ListedColormap(c)
        cmap_refl.set_under((1,1,1,0)) #set values lower than min to transparent white
        norm_refl = mpl.colors.BoundaryNorm(refl_levs, ncolors = len(c))
        return (cmap_refl, norm_refl, refl_levs)

def rvel_blue_red(levels = np.arange(-40,41,2), return_array = False, set_transparent_white = True):
    '''Radial velocity colormap (also useful for frontogenesis, etc)
    Source: my own creation (by Massey Bartolini)
    Designed for use for a centered range above/below zero, with 20 steps each side of zero (41 levels total)
    [e.g., levels = np.arange(-40,41,2) or levels = np.arange(-20,21,1)]
    Colors range from purple to dark blue to light blue to white/clear to orange-red to red to magenta
    Options: return_array (T/F)
        False: return cmap, norm, and list of contour fill levels
        True: return raw array of RGB values (0-1, normalized by 255)
    set_transparent_white (T/F) - whether to set white colors near zero to transparent
    '''
    rvel_levs = levels
    c=[[
    59,0,86],[ #-20
    64,0,101],[
    68,0,116],[
    72,0,131],[
    76,0,146],[
    77,2,162],[
    69,10,182],[
    60,18,203],[
    51,26,223],[
    42,34,243],[
    43,50,254],[ #-10
    54,73,254],[
    65,97,255],[
    76,121,255],[
    87,145,255],[
    116,167,255],[
    151,189,255],[
    185,211,255],[
    220,233,255],[
    #255,255,255],[ #-1 #have to comment out one of these to make the colormap work
    255,255,255],[ #-1
    255,255,255],[ #+1
    255,233,220],[
    255,211,185],[
    255,189,151],[
    255,167,116],[
    255,145,87],[
    255,121,76],[
    255,97,65],[
    254,73,54],[
    254,50,43],[ #+10
    243,34,42],[
    223,26,51],[
    203,18,60],[
    182,10,69],[
    162,2,77],[
    146,0,76],[
    131,0,72],[
    116,0,68],[
    101,0,64],[
    86,0,59]]
    if set_transparent_white: c = transparent_white(c)
    if return_array:
        return (np.array(c)/255.)
    else:
        cmap_rvel = mpl.colors.ListedColormap(np.array(c)/255.)
        norm_rvel = mpl.colors.BoundaryNorm(rvel_levs, ncolors = len(c))
        return (cmap_rvel, norm_rvel, rvel_levs)

zdr_levs_default = [-4.0,-2.0,-0.5,0.0,0.3,0.6,1.0,1.5,2.0,2.5,3.0,4.0,5.0,6.0,8.0,20.0]
def zdr_mrms(levels = zdr_levs_default, return_array = False):
    '''Differential reflectivity (ZDR) using color table from MRMS operational product viewer
    Source: https://mrms.nssl.noaa.gov/qvs/product_viewer/index.php
    Designed for use from -4 to 20 dB, with non-uniform steps
    Options: return_array (T/F)
        False: return cmap, norm, and list of contour fill levels
        True: return raw array of RGB values (0-1, normalized by 255)
    '''
    zdr_levs = levels
    zdr_colors = [[64,64,64], 
              [156,156,156], 
              [201,201,201], 
              [137,121,176], 
             [0,0,146],
             [75,150,206],
             [130,252,212],
             [125,216,104],
             [255,255,122],
             [241,149,86],
             [200,42,29],
             [158,31,20],
             [232,136,188],
             [255,255,255],
             [109,18,121]]
    if return_array:
        return (np.array(zdr_colors)/255.)
    else:
        cmap_zdr = mpl.colors.ListedColormap(np.array(zdr_colors)/255.)
        norm_zdr = mpl.colors.BoundaryNorm(zdr_levs, ncolors = len(zdr_colors))
        return (cmap_zdr, norm_zdr, zdr_levs)

kdp_levs_default = [-3.0,-2.0,-0.51,-0.5,0,0.25,0.5,1.0,1.5,2.0,2.55,3.0,4.0,5.0,7.5,10.0,100.0]
def kdp_mrms(levels = kdp_levs_default, return_array = False):
    '''Differential phase shift (KDP) using color table from MRMS operational product viewer
    Source: https://mrms.nssl.noaa.gov/qvs/product_viewer/index.php
    Designed for use from -3 to 100 deg/km, with non-uniform steps
    Options: return_array (T/F)
        False: return cmap, norm, and list of contour fill levels
        True: return raw array of RGB values (0-1, normalized by 255)
    '''
    kdp_levs = levels
    kdp_colors = [[142,142,142],
              [120,120,120], 
              [50,50,50], 
              [68,7,4], 
             [149,31,48],
             [194,76,94],
             [213,112,160],
             [160,126,181],
             [140,251,254],
             [90,187,173],
             [115,242,77],
             [254,251,84],
             [239,136,56],
             [246,196,138],
             [110,18,120],
             [0,0,147]]
    if return_array:
        return (np.array(kdp_colors)/255.)
    else:
        cmap_kdp = mpl.colors.ListedColormap(np.array(kdp_colors)/255.)
        norm_kdp = mpl.colors.BoundaryNorm(kdp_levs, ncolors = len(kdp_colors))
        return (cmap_kdp, norm_kdp, kdp_levs)

rhohv_levs_default = [0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.75, 0.80, 0.85, 0.90, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.00]
def rhohv_turbo(levels = rhohv_levs_default, return_array = False):
    '''Correlation coefficient (rho_hv) using matplotlib turbo colortable
    with levels roughly matching MRMS operational product viewer
    Source: https://mrms.nssl.noaa.gov/qvs/product_viewer/index.php
    Designed for use from 0.2 to 1.0, with non-uniform steps
    Options: return_array (T/F)
        False: return cmap, norm, and list of contour fill levels
        True: return raw array of RGB values (0-1, normalized by 255)
    '''
    rhohv_levs = levels
    if return_array:
        return (plt.cm.turbo(np.linspace(0,1,len(rhohv_levs))))
    else:
        cmap_rhohv = 'turbo'
        norm_rhohv = mpl.colors.BoundaryNorm(rhohv_levs, ncolors = plt.cm.turbo.N)
        return (cmap_rhohv, norm_rhohv, rhohv_levs)