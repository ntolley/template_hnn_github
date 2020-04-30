import numpy as np
import os
import fileio, paramrw, params_default, param_gen_utils
import fnmatch
import datalad
from pathlib import Path

#Define template param file
base_param_path = os.path.abspath('../param/standard_params/18oct24_17nov13_jyrki_good_3trials_opt.param')
gid_dict, p = paramrw.read(base_param_path) 

#Random number generator inputs need to be ints, HNN won't recognize as floats
p['prng_seedcore_input_prox'] = 13
p['prng_seedcore_input_dist'] = 14
p['prng_seedcore_extpois'] = 4
p['prng_seedcore_extgauss'] = 4
p['prng_seedcore_evprox_1'] = 4
p['prng_seedcore_evdist_1'] = 4
p['prng_seedcore_evprox_2'] = 4
p['prng_seedcore_evdist_2'] = 0

# Store arrays off parameters to sweep over
p_array = p.copy() 


#Glob search for specific keys
sweep_params = [key for key in list(p.keys()) if fnmatch.fnmatch(key,'*gbar_ev*') and fnmatch.fnmatch(key,'*ampa*') and fnmatch.fnmatch(key,'*Pyr*')] 

#Update array dict and unpack into a list of each permutation
for s in sweep_params:
    p_array[s] = np.linspace(0,50,4)

p_array_unpacked = param_gen_utils.dict_expand(p_array)

#Unload parameters into directory
dir_name = 'gbarEvPyrAmpa_sweep'
file_dir = os.path.abspath('../param/{}'.format(dir_name) + '/')

if not os.path.exists(file_dir):
    os.mkdir(file_dir)

    count = 0
    for param_file in p_array_unpacked:
        temp_dict = param_file.copy()
        
        f_name = dir_name + str(count)

        #Edit dictionary names
        temp_dict['sim_prefix'] = f_name
        temp_dict['expmt_groups'] = '{' + f_name + '}'

        f_string= file_dir + f_name + '.param'
        #Create files
        paramrw.write(f_string,temp_dict,gid_dict)

        count += 1


