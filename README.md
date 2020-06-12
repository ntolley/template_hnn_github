# HNN Parameter Sweep

This repository contains scripts necessary to run hnn simulations with predefined parameters to sweep over.

## Usage
- All relevant scripts are found in the `/code` directory
1) First run `param_gen_script.py` by specifying the simulation parameters and values to sweep through
    - All permutations of the specified parameters will be stored under `/param/<dir name>` as .param files
2) Second execute `run_hnn_sweep.sh` by specifying the folder storing the .param files
    - Output will be stored under `/data/<dir name>`
