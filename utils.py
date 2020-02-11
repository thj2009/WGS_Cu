# Utility functions


import numpy as np

def read_file(datafile):
    Sorp_data = {}
    with open(datafile) as f:
        lines = f.read().splitlines()
    lines = [lines[i].split(',') for i in range(len(lines))]
    for i in range(len(lines[0])):
        ss = []
        for j in range(1, len(lines)):
            if i >= 4:
                ss.append(float(lines[j][i]))
            else:
                ss.append(lines[j][i])
        Sorp_data[lines[0][i]] = ss
        
    return Sorp_data


def modify_adsorbate(sorp_data):
    Exp = sorp_data['Exp']
    Adsorbate = sorp_data['Adsorbate']
    frag = sorp_data['frag']
    err_PW91 = sorp_data['err_PW91']
    act_Adsobate = []; act_err = []; act_exp = []
    for i in range(len(Adsorbate)):
        act_err.append(err_PW91[i]/float(frag[i]))
        act_exp.append(Exp[i]/float(frag[i]))
        if frag[i] == 1:
            act_Adsobate.append(Adsorbate[i])
        elif frag[i] == 2:
            act_Adsobate.append(Adsorbate[i][:-1])
    ss = {}
    ss['act_Adsorbate'] = act_Adsobate
    ss['act_err'] = act_err
    ss['act_exp'] = act_exp
    sorp_data.update(ss)


import math

# Feature Design Problem

def read_metal(metal_file):
    Metal = {}
    with open(metal_file, 'rb') as f:
        lines = f.read().splitlines()
    lines = [lines[i].split(',') for i in range(len(lines))]
    for line in lines:
        mm = {}
        mm['lattice_constant'] = float(line[1])
        mm['outer_electron'] = int(line[2])
        mm['inner_shell'] = int(line[3])
        mm['Struc'] = line[4]
        Metal[line[0]] = mm
    return Metal
        
def site_dis(sorp_data, metal_data):
    Metal = sorp_data['Metal']
    Metal_facet = sorp_data['Metal_Facet']
#    site = sorp_data['site']
    lattice_info = read_metal(metal_data)
    site_distance = []
    for i in range(len(Metal)):
        STRUC = lattice_info[Metal[i]]['Struc']
        l_c = lattice_info[Metal[i]]['lattice_constant']
#        print STRUC
#        if STRUC == 'FCC':
##            print Metal_facet[i]
#            if Metal_facet[i] == '111':
#                if site[i] == 'hallow':
#                    sl = l_c*math.sqrt(6)/6.
#                elif site[i] == 'top':
#                    sl = l_c*math.sqrt(2)/2.
#                elif site[i] == 'bridge':
#                    sl = l_c*math.sqrt(2)/4.
#            elif Metal_facet[i] == '100':
#                if site[i] == 'hallow':
#                    sl = l_c*math.sqrt(2)/2.
#                elif site[i] == 'top':
#                    sl = l_c*math.sqrt(2)/2.
#                elif site[i] == 'bridge':
#                    sl = l_c/2.
#        elif STRUC == 'HCP':
#            sl = l_c
        if STRUC == 'FCC':
            sl = l_c * math.sqrt(2)/2.
        elif STRUC == 'HCP':
            sl = l_c

        site_distance.append(sl)
    ss = {}
    ss['site_distance'] = site_distance
    sorp_data.update(ss)
    
def outer_electron(sorp_data, metal_data):
    ## Unfinished
    Metal = sorp_data['Metal']
    lattice_info = read_metal(metal_data)
    o_e = []
    for i in range(len(Metal)):
        o_e.append(lattice_info[Metal[i]]['outer_electron'])
    ss = {}
    ss['outer_electron'] = o_e
    sorp_data.update(ss)

def inner_shell(sorp_data, metal_data):
    ## Unfinished
    Metal = sorp_data['Metal']
    lattice_info = read_metal(metal_data)
    i_s = []
    for i in range(len(Metal)):
        i_s.append(lattice_info[Metal[i]]['inner_shell'])
    ss = {}
    ss['inner_shell'] = i_s
    sorp_data.update(ss)  


def coordination_num(sorp_data, metal_data):
    Metal = sorp_data['Metal']
    Metal_facet = sorp_data['Metal_Facet']
#    site = sorp_data['site']
    lattice_info = read_metal(metal_data)
    coord_num = []
    for i in range(len(Metal)):
        STRUC = lattice_info[Metal[i]]['Struc']
#        print STRUC
        
        if STRUC == 'FCC':
            if Metal_facet[i] == '111':
                cn = 9
            elif Metal_facet[i] == '100':
                cn = 8
            elif Metal_facet[i] == '553':
                cn = 7
            elif Metal_facet[i] == '110':
                cn = 7
            elif Metal_facet[i] == '211':
                cn = 7
        if STRUC == 'HCP':
            cn = 9
#        if STRUC == 'BCC':
#            cn = 
        coord_num.append(cn)
    ss = {}
    ss['coord_num'] = coord_num
    sorp_data.update(ss)


