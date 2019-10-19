#!/bin/bash
module load python
for ((c=2;c<=15;c++))
do
cd Position_$c
cp ../Position_1/navigator.sh ./
bash navigator.sh
sleep 10
mv PES_energy.csv PES_energy_Position$c.csv
cd ..
done
