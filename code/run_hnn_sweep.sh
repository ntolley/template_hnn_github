#!/bin/bash

#Identify folder with .param files to iterate over
export HNN_SWEEP_NAME=gbarEvPyrAmpa_reversed_inputs

export PARAM_PATH=$PWD/param/$HNN_SWEEP_NAME

#Setup location for hnn_out
mkdir $PWD/data/$HNN_SWEEP_NAME
export SYSTEM_USER_DIR=$PWD/data/$HNN_SWEEP_NAME

cd ~/bin/hnn_source_code
for pfile in $PARAM_PATH/*
    do  
        mpiexec nrniv -mpi -python -nobanner run.py $pfile
    done


