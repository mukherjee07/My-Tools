#!/bin/bash
#####THE GOAL OF THIS CODE IS TO ADD SAME NUMBER OF LI ATOMS TO THE DOWN SIDE OF NTCDA BASE STRUCTURE ESSENTIALLY JUST 
##### MAKING THE Z AXIS COORDINATE NEGATIVE. THIS WOULD ONLY BE APPLICABLE FOR EVEN NUMBER OF ATOMS
declare -i c
c=3
# c is the counter for folder
while [ $c -le 30 ] 
do
cd LiA$c
for ((t=1;t<=5;t++))
do
cd Li$t
total_atoms=$(awk 'FNR==1 {print $1}' 10_Li.xyz)
total_atoms=${total_atoms#0}
declare -i Num_Li
declare -i R
Num_Li=$[ $total_atoms - 25 ]
j=$[ $c -1 ]
for ((k=1;k<=$Num_Li;k++))
### k is the Li row number
do
R=$[ 26 + $k ]
echo $R
cd ../../LiA$j/Li$t/
X=$(awk 'FNR=='$R' { print $2 }' 10_Li.xyz)
Y=$(awk 'FNR=='$R' { print $3 }' 10_Li.xyz)
Z=$(awk 'FNR=='$R' { print $4 }' 10_Li.xyz)
cd ../../LiA$c/Li$t/
echo " Li $X $Y -$Z" >> 10_Li.xyz
done
declare -i New_atoms
New_atoms=$[ $total_atoms + $Num_Li ]
sed -i '1s/'$total_atoms'/'$New_atoms'/' 10_Li.xyz
cd ..
done
cd ..
c=$[ $c + 2 ]
done
