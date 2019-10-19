#!/bin/bash
typeset -i job_no
squeue -p general-compute -u kmukherj > Job_cancel_list.txt
#the above is the list of jobs which are running in beta partition of the chemistry cluster
lines=$(wc -l Job_cancel_list.txt| cut -d " " -f 1)
echo $lines
for ((c=3;c<=$lines;c++))
do
job_no=$(awk 'FNR=='$c' {print $1}'< Job_cancel_list.txt)
#echo $job_no
#scancel -M chemistry -p beta $job_no 
# Cancelling all the recent jobs submitted 
done
#rm Job_cancel_list.txt
