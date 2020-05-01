#!/bin/bash

#Identify folder with .param files to iterate over
export HNN_SWEEP_NAME=gbarEvPyrAmpa_sweep


export PARAM_PATH=$PWD/param/$HNN_SWEEP_NAME
export PARAM_NAMES=(`ls $PARAM_PATH`)

#Setup location for hnn_out
mkdir data/$HNN_SWEEP_NAME
export SYSTEM_USER_DIR=$PWD/data/$HNN_SWEEP_NAME

for pfile in "${PARAM_NAMES[@]}"
    do
        mpiexec -np 16 nrniv -mpi -python -nobanner run.py $PARAM_PATH/$pfile hnn_sweep.cfg
    done


