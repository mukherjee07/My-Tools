#!/bin/bash/
if [ -f energy.csv ]; then
rm energy.csv
fi
touch energy.csv
for ((c=2;c<=101;c++))
do
awk 'FNR=='$c' { print $1, $2 }' energyfile.txt >> energy.csv 
done
#making this into a proper CSV file
sed -i 's/ /,/' energy.csv
