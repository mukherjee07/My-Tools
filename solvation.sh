#!/bin/bash

# load modules
echo "Loading modules ..."

#module load python/anaconda
#module use //projects/hachmann/atif/privatemodules
#module use /user/m27/privatemodules
#module load openbabel
#module load orca

ulimit -s unlimited
module list

cur_dir=$(pwd)  # get the cuurent directory and store
msg1='$'
  
## now read lines of the smiles only data file
readarray a < hbd_smiles.smi
len=${#a[@]}
#temp=199
for ((i=1173;i<1188;i++)) 
do
    #mkdir -p $i
    cd $i
 ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####     #####
     ###### write the slurm code for ORCA to  file  ##### #####
 ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####
    echo "#!/bin/bash
#SBATCH --job-name=solva_$i
#SBATCH --output=sol_solvation$i.out
#SBATCH --error=sol_solvation$i.err
#SBATCH --clusters=chemistry
#SBATCH --partition=beta --qos=beta
#SBATCH --account=hachmann
#SBATCH --tasks-per-node=4
#SBATCH --constraint=CPU-E5-2650v4

#sed -i '1,2d' optb.xyz   # removing the first 2 lines of the xyz file

echo \"! PBE0 Def2-SVP D3 CPCM(Water)
% base \\\"sol_p_water\\\"                                                        
*xyzfile 0 1 optb.xyz 

$ new_job
! PBE0 Def2-SVP D3 CPCM(Hexane)
% base \\\"sol_np_hexane\\\"
*xyzfile 0 1 optb.xyz                                                         

\" > solvation$i.inp
    
cur_dir=$msg1(pwd)
cd /gpfs/scratch/adityaso/solubility_temp1
mkdir -p solvation$i
cd solvation$i  
cp ${msg1}cur_dir/solvation$i.inp .
cp ${msg1}cur_dir/optb.xyz .
INFILE=solvation$i.inp 
" > orca_solvation_$i.slurm
		
cat $cur_dir/slurm.rest >> orca_solvation_$i.slurm    # slurm.rest contains rest of ORCA slurm script
echo "cp *.gbw ${msg1}cur_dir/. ">> orca_solvation_$i.slurm



##########################

    
    ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####     #####
    ###### End of Slurm script writing  ##### ##### ##### ##### #####
    ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####

    
    ## delay the runs if the jobs exceed 980 jobs
    ## important step here. 
    
    while :
    do
	
    	no_jobs=$(squeue -u adityaso -M chemistry -p beta |grep -v JOBID|grep sol|wc -l)  # get the number of running job
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
    sbatch orca_solvation_$i.slurm    
    #submit the job. Each job for each polymer

    
    #uname -a
    ## change back to the original directory
    cd $cur_dir
    
done


