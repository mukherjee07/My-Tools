#!/bin/bash

for ((c=1;c<=30;c++))
do
cd LiA$c
for ((j=1;j<=5;j++)) 
do
cd Li$j
if [ -f Final.xyz ]; then
echo " Li with $c atoms and conformer $j has converged. "
fi 
cd ..
done
cd ..
done
