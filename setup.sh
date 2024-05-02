#!/bin/bash

# Prepare Environment
apt-get -y install nano unzip psmisc libsm6 libxrender1 libfontconfig1 libxtst6

conda env create -f environment.yaml

# https://stackoverflow.com/questions/34534513/calling-conda-source-activate-from-bash-script
eval "$(conda shell.bash hook)"
conda activate ldm

pip install tensorboard vastai gpustat
