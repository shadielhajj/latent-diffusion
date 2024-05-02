#!/bin/bash

# Download models and data

for var in "$@"
do
    echo "$var"
    case $var in

        celeba)
            cd data
            wget -O celeba_hq_256.tar.bz2 "https://www.dropbox.com/scl/fi/ad7138e2keg2nczs7hj64/celeba_hq_256.tar.bz2?rlkey=>
            tar jxvf celeba_hq_256.tar.bz2
            rm celeba_hq_256.tar.bz2
            cd ..
            ;;

        celeba_subset)
            cd data
            wget -O celeba_hq_256_subset.tar.bz2 "https://www.dropbox.com/scl/fi/2spsl21gyaltczzdczehd/celeba_hq_256_subset.>
            tar jxvf celeba_hq_256_subset.tar.bz2
            rm celeba_hq_256_subset.tar.bz2
            cd ..
            ;;

        vq_f4)
            cd models/first_stage_models
            wget https://ommer-lab.com/files/latent-diffusion/vq-f4.zip
            unzip vq-f4.zip -d vq-f4
            rm vq-f4.zip
            cd ..
            ;;

        *)
            echo -n "Unknow model ${$1}"
            ;;

    esac
done
