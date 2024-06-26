#!/bin/bash

apt-get -y install unzip

# Download models and data

for var in "$@"
do
    echo "$var"
    case $var in

        celeba)
            cd data
            wget -O celeba_hq_256.tar.bz2 "https://www.dropbox.com/scl/fi/ad7138e2keg2nczs7hj64/celeba_hq_256.tar.bz2?rlkey=gmjetlznmz6hdputf1gmhtyrc&st=3ijc4183&dl=0"
            tar jxvf celeba_hq_256.tar.bz2
            # rm celeba_hq_256.tar.bz2
            cd ..
            ;;

        vq_f4)
            cd models/first_stage_models
            wget https://ommer-lab.com/files/latent-diffusion/vq-f4.zip
            unzip vq-f4.zip -d vq-f4
            # rm vq-f4.zip
            cd ../..
            ;;

        *)
            echo -n "Unknow model ${$1}"
            ;;

    esac
done
