import numpy as np
import scipy
from scipy.signal import decimate
from scipy import interpolate
import h5py
import pandas as pd
import os
from os.path import isfile, join
from os import listdir
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import os
import itertools
sns.set()


#Takes in a .param dictionary, parameter sweeps defined by an array of values, generates all combinations 
def dict_expand(array_dict):
    dict_list = []

    array_keys = [param_key for param_key in list(array_dict.keys()) if type(array_dict[param_key]) == np.ndarray]
    array_vals = [array_dict[param_key] for param_key in array_keys]
    param_combos = list(itertools.product(*array_vals))

    for combo in param_combos:
        temp_dict = array_dict.copy()
        for param_idx in range(len(array_keys)):
            temp_dict[array_keys[param_idx]] = combo[param_idx]

        dict_list.append(temp_dict)

    return dict_list
