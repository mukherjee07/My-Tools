#!/bin/bash
#typeset -i job_no
#squeue -p skylake -u kmukherj > Job_cancel_list.txt
#the above is the list of jobs which are running in beta partition of the chemistry cluster
#lines=$(wc -l Job_cancel_list.txt| cut -d " " -f 1)
#while :
#do
#if [ $lines -le 60 ]; then
#echo "go ahead you can submit the job"
#break
#fi
#done
    while :
    do
	
    	no_jobs=$(squeue -u kmukherj -M chemistry -p beta |grep -v JOBID|grep Li|wc -l)  # get the number of running job
    	#no_jobs=`scavq |grep scav|wc -l`  # get the number of running job
    	#no_jobs=`scavq |grep S2|wc -l`  # get the number of running job
	
    	#echo $no_jobs
    	no_job=${no_jobs#0}  # changing the string to a numerical value
    	max_job=64
	
    	#echo $no_jobs "this is  the number of jobs running"
    	if test $no_jobs -eq '0'; then
    	    break          #Abandon the loop.
    	fi
	
    	if test $no_job -lt $max_job; then
    	    #echo $no_jobs "Great, now we can run more jobs. More cores available!!!!"
	    
    	    break          #Abandon the loop.
    	fi
    	#echo $no_jobs "Gotta wait. No more cores available!!!!"
	sleep 60
    done
    echo "Wow"
