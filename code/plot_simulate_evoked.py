"""
===============
Simulate dipole
===============

This example demonstrates how to simulate a dipole for evoked-like
waveforms using HNN-core.
"""

# Authors: Mainak Jas <mainak.jas@telecom-paristech.fr>
#          Sam Neymotin <samnemo@gmail.com>

import os.path as op

###############################################################################
# Let us import hnn_core

import hnn_core
from hnn_core import simulate_dipole, read_params, Network

hnn_core_root = op.join(op.dirname(hnn_core.__file__), '..')

import numpy as np

###############################################################################
# Then we read the parameters file
params_fname = op.join(hnn_core_root, 'param', 'default.json')
params = read_params(params_fname)
print(params)

###############################################################################
# This is a lot of parameters! We can also filter the
# parameters using unix-style wildcard characters
print(params['L2Pyr_soma*'])

###############################################################################
# Now let's simulate the dipole
# You can simulate multiple trials in parallel by using n_jobs > 1
net = Network(params)
dpls = simulate_dipole(net, n_jobs=1, n_trials=1)
print(dpls)
print(type(dpls))
###############################################################################
# and then plot it
#import matplotlib.pyplot as plt
#fig, axes = plt.subplots(2, 1, sharex=True, figsize=(6, 6))
idx = 0
for dpl in dpls:
	dpl.write('dpl{}'.format(idx))
	idx +=1
#    dpl.plot(ax=axes[0], layer='agg')
#net.plot_input(ax=axes[1])

#plt.show()



