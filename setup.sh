#!/bin/bash

# Prepare Environment
apt-get -y install nano unzip psmisc libsm6 libxrender1 libfontconfig1 libxtst6

conda env create -f environment.yaml
source activate ldm

pip install tensorboard vastai gpustat
