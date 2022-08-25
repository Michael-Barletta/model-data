import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from matplotlib import cm
#List of various colormaps for atmospheric variables
#can search for temperature, moisture (PW, etc), wind, CAPE, precip (snow, freezing rain, etc)

def transparent_white(cmap):
    #Set white colors to transparent given list of RGB lists
    #by converting R,G,B to R,G,B,A
    cmap_new=[(rgb+[0]) if rgb==[255,255,255] else (rgb+[255]) for i,rgb in enumerate(cmap)]
    return cmap_new

#****** precipitation colormaps ******
snow_levs_default = [0, 0.1, 1.0, 2.0, 3.0, 4.0, 6.0, 8.0, 12.0, 18.0, 24.0, 30.0, 36.0, 48.0, 60.0, 72.0, 96.0]
def snow_nws(levels = snow_levs_default, return_array = False, omit_trace = True):
    '''Snowfall colormap using standard NWS snowfall color table
    Source: https://www.nohrsc.noaa.gov/snowfall_v2/ or https://www.weather.gov/aly/winter
    Designed for use between 0 and 96 inches, with non-uniform steps (smaller for lower amounts)
    Total of 16 colors
    Options: return_array (T/F)
        False: return cmap, norm, and list of contour fill levels
        True: return raw array of RGB values (0-1, normalized by 255)
    omit_trace (T/F) - whether to show lowest color (white) for trace amounts
    '''
    snow_levs = levels
    nws_snow_colors = ['#ffffff', '#c4ddeb', '#77bbdd', '#4394c9', '#246aab', '#363ca6', '#faffa1', '#ffcf00', '#ff9200', '#f20002', '#bb0018', '#8b1221', '#5c241d', '#d6cfff', '#b296de', '#9a62b3']
    c = np.array([mpl.colors.to_rgb(hxc) for hxc in nws_snow_colors])
    if omit_trace:
        c = c[1:]
        snow_levs = snow_levs[1:]
    if return_array:
        return (c)
    else:
        cmap_snow = mpl.colors.ListedColormap(c)
        if omit_trace: cmap_snow.set_under((1,1,1,0)) #set values below min to transparent white
        norm_snow = mpl.colors.BoundaryNorm(snow_levs, ncolors = len(c))
        return (cmap_snow, norm_snow, snow_levs)

frzr_levs_default = [0, 0.01, 0.1, 0.25, 0.5, 0.75, 1.0, 2.0, 5.0] #inches
def frzr_nws(levels = frzr_levs_default, return_array = False, omit_trace = True):
    '''Freezing rain colormap using standard NWS freezing rain color table
    Source: https://www.weather.gov/aly/winter
    Designed for use between 0 and 5 inches, with non-uniform steps (smaller for lower amounts)
    Total of 8 colors
    Options: return_array (T/F)
        False: return cmap, norm, and list of contour fill levels
        True: return raw array of RGB values (0-1, normalized by 255)
    omit_trace (T/F) - whether to show lowest color (white) for trace amounts
    '''
    frzr_levs = levels
    #nws_ice_colors = ['#ffffff', '#f0f34d', '#ffca00', '#ff0000', '#d8000c', '#b665ff', '#9a00d1', '#4f1b75'] #0.25-0.5 and 0.5-0.75 are very similar here, trying a different color for 0.5-0.75 below
    nws_ice_colors = ['#ffffff', '#f0f34d', '#ffca00', '#ff0000', '#bb0018', '#b665ff', '#9a00d1', '#4f1b75']
    c = np.array([mpl.colors.to_rgb(hxc) for hxc in nws_ice_colors])
    if omit_trace:
        c = c[1:]
        frzr_levs = frzr_levs[1:]
    if return_array:
        return (c)
    else:
        cmap_frzr = mpl.colors.ListedColormap(c)
        if omit_trace: cmap_frzr.set_under((1,1,1,0)) #set values below min to transparent white
        norm_frzr = mpl.colors.BoundaryNorm(frzr_levs, ncolors = len(c))
        return (cmap_frzr, norm_frzr, frzr_levs)

precip_levs_default = [0, 0.01, 0.1, 0.25, 0.50, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0, 10.0, 15.0, 20.0, 30.0]
def precip_nws(levels = precip_levs_default, return_array = False, omit_trace = True):
    '''Precipitation/rainfall colormap using standard NWS precip. color table used in web graphics
    Source: https://www.weather.gov/aly/maps
    Designed for use between 0 and 30 inches, with non-uniform steps (smaller for lower amounts)
    Total of 15 colors
    Options: return_array (T/F)
        False: return cmap, norm, and list of contour fill levels
        True: return raw array of RGB values (0-1, normalized by 255)
    omit_trace (T/F) - whether to show lowest color (white) for trace amounts
    '''
    precip_levs = levels
    nws_apcp_colors = [[255,255,255], 
        [206,232,195],
        [173,215,161],
        [135,194,126],
        [85,160,92],
        [46,107,52],
        [254,250,153],
        [247,206,102],
        [239,147,79],
        [233,91,59],
        [197,50,42],
        [158,31,44],
        [102,16,39],
        [53,5,46],
        [69,8,111],
        [249,220,253]]
    c = np.array(nws_apcp_colors)/255.
    if omit_trace:
        c = c[1:]
        precip_levs = precip_levs[1:]
    if return_array:
        return (c)
    else:
        cmap_precip = mpl.colors.ListedColormap(c)
        if omit_trace: cmap_precip.set_under((1,1,1,0)) #set values below min to transparent white
        norm_precip = mpl.colors.BoundaryNorm(precip_levs, ncolors = len(c))
        return (cmap_precip, norm_precip, precip_levs)

precip_levs_default = [0, 0.01, 0.1, 0.25, 0.50, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.5, 3.0, 4.0, 5.0, 7.0, 10.0, 15.0, 20.0, 30.0]
def precip_wpc(levels = precip_levs_default, return_array = False, omit_trace = True):
    '''Precipitation/rainfall colormap using standard WPC precip. color table used in web graphics
    Source: https://www.wpc.ncep.noaa.gov/qpf/day1-7.shtml
    Designed for use between 0 and 30 inches, with non-uniform steps (smaller for lower amounts)
    Total of 19 colors
    Options: return_array (T/F)
        False: return cmap, norm, and list of contour fill levels
        True: return raw array of RGB values (0-1, normalized by 255)
    omit_trace (T/F) - whether to show lowest color (white) for trace amounts
    '''
    precip_levs = levels
    wpc_apcp_colors = [[255,255,255],
            [159,252,78],
            [92,200,59],
            [61,136,37],
            [36,76,135],
            [70,140,247],
            [80,175,234],
            [110,235,237],
            [135,106,200],
            [137,52,230],
            [128,23,135],
            [128,23,14],
            [190,39,27],
            [221,79,37],
            [239,132,50],
            [196,137,47],
            [249,216,73],
            [255,255,85],
            [244,177,182]]
    c = np.array(wpc_apcp_colors)/255.
    if omit_trace:
        c = c[1:]
        precip_levs = precip_levs[1:]
    if return_array:
        return (c)
    else:
        cmap_precip = mpl.colors.ListedColormap(c)
        if omit_trace: cmap_precip.set_under((1,1,1,0)) #set values below min to transparent white
        norm_precip = mpl.colors.BoundaryNorm(precip_levs, ncolors = len(c))
        return (cmap_precip, norm_precip, precip_levs)

def ptype_allmixes(return_colors = False):
    '''Precipitation-type colormap using different colors for all possible p-type categories from HRRR/HRRRE output
    Options: return_colors(T/F)
        False: return cmap, norm, list of contour fill levels, list of tick locations and tick labels
        True: return list of matplotlib colors
    '''
    # 0 = NP, 1 = SN, 2 = IP, 3 = IP+SN, 4 = ZR, 5 = ZR+SN, 6 = ZR+IP, 7 = ZR+IP+SN, 8 = RA, 9 = RA+SN, 10 = RA+IP, 11 = RA+IP+SN
    ptype_colors = [(1,1,1,0),'tab:blue','mediumslateblue','darkslateblue','mediumvioletred','mediumorchid','darkmagenta','orchid','tab:green','darkturquoise','turquoise','cyan']
    ptype_levels = [-1,0,1,2,3,4,5,6,7,8,9,10,11]
    ptype_ticks  = [-0.5,0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5]
    ptype_labels = ['NP','SN','IP','IP/SN','ZR','ZR/SN','ZR/IP','ZR/IP/SN','RA','RA/SN','RA/IP','RA/IP/SN']
    if return_colors:
        return (ptype_colors)
    else:
        cmap_ptype = mpl.colors.ListedColormap(ptype_colors)
        norm_ptype = mpl.colors.BoundaryNorm(ptype_levels, ncolors = len(ptype_colors))
        return (cmap_ptype, norm_ptype, ptype_levels, ptype_ticks, ptype_labels)

#****** temperature colormaps ******
def temperature_m60f_120f(levels = np.arange(-60,121,1), return_array = False):
    '''Temperature colormap (degF)
    Source: my own creation (by Massey Bartolini)
    Designed for a temperature range from -60 to +120 degF, with steps every 1 F
    Options: return_array (T/F)
        False: return cmap, norm, and list of contour fill levels
        True: return raw array of RGB values (0-1, normalized by 255)
    '''
    temp_levs = levels
    c=[[255,255,255],[ #-60 F
    255,255,240],[
    255,255,225],[
    255,255,210],[
    255,255,195],[
    255,255,180],[
    255,255,165],[
    255,255,150],[
    255,255,135],[
    255,255,121],[
    214,246,135],[ #-50 F
    200,243,137],[
    186,241,139],[
    172,238,140],[
    158,236,142],[
    145,234,144],[
    131,231,146],[
    117,229,147],[
    103,226,149],[
    89,224,151],[
    10,226,177],[ #-40 F
    21,229,181],[
    31,231,185],[
    42,234,189],[
    52,236,193],[
    63,238,197],[
    73,241,201],[
    83,243,205],[
    94,246,209],[
    104,248,213],[
    85,232,218],[ #-30 F
    82,223,211],[
    80,214,204],[
    77,205,198],[
    75,196,191],[
    74,187,185],[
    73,178,178],[
    72,169,172],[
    70,160,165],[
    69,151,158],[
    #66,124,162],[ #-20 F
    #79,115,164],[
    #93,107,166],[
    #106,98,168],[
    #120,89,170],[
    #133,80,173],[
    #147,71,175],[
    #160,62,177],[
    #174,53,179],[
    #187,44,182],[
    70,140,162],[ #-20 F
    80,138,165],[
    91,132,168],[
    107,123,172],[
    123,116,175],[
    139,114,178],[
    155,108,182],[
    171,98,185],[
    177,87,188],[
    187,70,192],[
    195,0,185],[ #-10 F
    188,0,179],[
    181,0,172],[
    174,0,166],[
    167,0,160],[
    160,0,153],[
    153,0,147],[
    146,0,140],[
    138,0,134],[
    131,0,128],[
    116,1,131],[ #0 F
    119,3,140],[
    122,4,150],[
    125,6,159],[
    128,7,168],[
    131,9,177],[
    134,10,186],[
    137,12,196],[
    140,13,205],[
    143,15,214],[
    131,15,230],[ #10 F
    117,14,230],[
    102,12,231],[
    88,10,231],[
    73,8,232],[
    58,7,232],[
    44,5,233],[
    29,3,233],[
    15,2,234],[
    0,0,234],[
    0,20,246],[ #20 F
    0,40,248],[
    0,60,250],[
    0,75,251],[
    0,90,252],[
    0,105,253],[
    0,117,254],[
    0,129,255],[
    0,140,255],[
    0,150,255],[ 
    0,195,255],[ #30 F
    0,220,255],[
    #0,255,255],[ #32 F	
    0,200,195],[ #32+ F
    0,190,165],[
    0,184,134],[
    0,170,119],[
    0,155,103],[
    0,142,89],[
    0,132,76],[
    0,122,63],[
    7,117,0],[ #40 F
    11,120,0],[
    15,123,0],[
    23,128,0],[
    31,133,0],[
    39,137,0],[
    46,142,0],[
    54,146,0],[
    62,151,0],[
    70,155,0],[
    77,181,0],[ #50 F
    86,188,0],[
    94,196,0],[
    103,203,0],[
    111,211,0],[
    120,218,0],[
    128,226,0],[
    137,233,0],[
    145,241,0],[
    154,248,0],[
    195,255,0],[ #60 F
    201,255,8],[
    207,255,17],[
    213,255,25],[
    219,255,34],[
    225,255,42],[
    231,255,51],[
    237,255,59],[
    244,255,67],[
    250,255,76],[
    255,219,84],[ #70 F
    255,210,76],[
    255,201,67],[
    255,192,59],[
    255,182,51],[
    255,173,42],[
    255,164,34],[
    255,155,25],[
    255,145,17],[
    255,136,8],[
    255,107,0],[ #80 F
    251,97,0],[
    245,86,0],[
    240,75,0],[
    235,64,0],[
    230,54,0],[
    225,43,0],[
    220,32,0],[
    214,21,0],[
    209,11,0],[
    205,0,136],[ #90 F
    210,0,148],[
    215,0,159],[
    220,0,171],[
    225,0,182],[
    230,0,194],[
    235,0,205],[
    240,0,217],[
    246,0,228],[
    251,0,240],[
    223,0,233],[ #100 F
    219,0,231],[
    211,0,229],[
    202,0,225],[
    192,0,222],[
    183,0,219],[
    174,0,216],[
    165,0,212],[
    155,0,209],[
    146,0,206],[
    157,85,211],[ #110 F
    168,104,216],[
    179,123,221],[
    190,142,226],[
    201,161,231],[
    212,180,236],[
    223,199,241],[
    234,218,246],[
    245,237,251],[
    255,255,255]] #120 F
    if return_array:
        return (np.array(c)/255.)
    else:
        cmap_temp = mpl.colors.ListedColormap(np.array(c)/255.)
        norm_temp = mpl.colors.BoundaryNorm(temp_levs, ncolors = len(c))
        return (cmap_temp, norm_temp, temp_levs)

#****** temperature advection / frontogenesis colormaps ******
def blue_red(levels = np.arange(-5,5.1,0.25), return_array = False, set_transparent_white = True):
    '''Temperature advection colormap (also useful for frontogenesis, Q-vectors, etc)
    Source: my own creation (by Massey Bartolini)
    Designed for use for a centered range above/below zero, with 20 steps each side of zero (41 levels total)
    [e.g., levels = np.arange(-5,5.1,0.25) or levels = np.arange(-20,21,1)]
    Colors range from purple to dark blue to light blue to white/clear to orange-red to red to magenta
    Options: return_array (T/F)
        False: return cmap, norm, and list of contour fill levels
        True: return raw array of RGB values (0-1, normalized by 255)
    set_transparent_white (T/F) - whether to set white colors near zero to transparent
    '''
    BuRd_levs = levels
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
        cmap_BuRd = mpl.colors.ListedColormap(np.array(c)/255.)
        norm_BuRd = mpl.colors.BoundaryNorm(BuRd_levs, ncolors = len(c))
        return (cmap_BuRd, norm_BuRd, BuRd_levs)


def pwat_72mm_every4mm(levels = np.arange(0, 73, 4), return_array = False):
    '''Precipitable water colormap (IWV)
    Source: my own creation (by Massey Bartolini)
    Designed for use from 0 to 72 mm, with steps every 4 mm
    Colormap is a combination of brown colors for low PW and reversed viridis for high PW
    Options: return_array (T/F)
        False: return cmap, norm, and list of contour fill levels
        True: return raw array of RGB values (0-1, normalized by 255)
    '''
    pw_levs = levels
    c=[[60,30,0],[
    82,51,20],[
    105,71,40],[
    127,92,60],[
    149,115,83],[
    172,137,106],[
    194,160,129],[
    215,182,151],[
    235,204,173],[
    255,226,195]]
    c=np.array(c)/255.

    #Concatenate with viridis
    c=np.concatenate([c,cm.viridis_r(np.arange(270))[::10,0:3]])
    if return_array:
        return (c)
    else:
        cmap_pw = mpl.colors.ListedColormap(c)
        norm_pw = mpl.colors.BoundaryNorm(pw_levs, ncolors = len(c))
        return (cmap_pw, norm_pw, pw_levs)

def pwat_72mm(levels = np.arange(0, 73, 2), return_array = False):
    '''Precipitable water colormap (IWV)
    Source: my own creation (by Massey Bartolini)
    Designed for use from 0 to 72 mm, with steps every 2 mm
    Identical to pwat_72mm_every4mm, but with double the colors
    Colormap is a combination of brown colors for low PW and reversed viridis for high PW
    Options: return_array (T/F)
        False: return cmap, norm, and list of contour fill levels
        True: return raw array of RGB values (0-1, normalized by 255)
    '''
    pw_levs = levels
    c=[[60,30,0],[
    71,40,10],[
    81,51,21],[
    91,61,31],[
    101,71,41],[
    112,81,51],[
    122,92,62],[
    132,102,72],[
    142,112,82],[
    153,122,93],[
    163,133,103],[
    173,143,113],[
    183,153,123],[
    194,163,134],[
    204,174,144],[
    214,184,154],[
    224,194,165],[
    235,204,175],[
    245,215,185],[
    255,225,195]]
    c=np.array(c)/255.

    #Concatenate with viridis
    c=np.concatenate([c,cm.viridis_r(np.arange(260))[::5,0:3]])
    if return_array:
        return (c)
    else:
        cmap_pw = mpl.colors.ListedColormap(c)
        norm_pw = mpl.colors.BoundaryNorm(pw_levs, ncolors = len(c))
        return (cmap_pw, norm_pw, pw_levs)