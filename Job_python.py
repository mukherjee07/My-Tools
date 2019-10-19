""" 
A function to find number of Jobs of running user "kmukherj" in Skylake cluster and then resubmit jobs if its less than say 60 or N.
This N would be a user input. 
"""
import subprocess
import os
import math


os.system("typeset -i job_no")
os.system("squeue -p general-compute -u kmukherj > Job_cancel_list.txt")
#the above is the list of jobs which are running in beta partition of the chemistry cluster
lines=$(wc -l Job_cancel_list.txt| cut -d " " -f 1)
echo $lines
for ((c=2;c<=$lines;c++))
do
job_no=$(awk 'FNR=='$c' {print $1}'< Job_cancel_list.txt)
#scancel -p general-compute $job_no 
# Cancelling all the recent jobs submitted 
done
rm Job_cancel_list.txt
