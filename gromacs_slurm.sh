#!/bin/sh
#SBATCH --time=01:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --partition=beta
#SBATCH --clusters=chemistry
#SBATCH --account=pi-hachmann
#SBATCH --job-name="gromacs-test"
#SBATCH --error=gromacs_t1.err                    
#SBATCH --output=gromacs_t1.out
##SBATCH --mail-user=username@buffalo.edu
##SBATCH --mail-type=END
##SBATCH --exclude=cpn-p27-14-02,cpn-p27-14-01,cpn-p27-10-01,cpn-p27-10-02

echo "SLURM_JOB_ID="$SLURM_JOB_ID
echo "SLURM_JOB_NODELIST"=$SLURM_JOB_NODELIST
echo "SLURM_NNODES"=$SLURM_NNODES
echo "SLURMTMPDIR="$SLURMTMPDIR

echo "working directory = "$SLURM_SUBMIT_DIR

module load intel-mpi/4.1.3 mkl/11.2 intel/12.1 gromacs/5.1.1
module list
#
export I_MPI_PMI_LIBRARY=/usr/lib64/libpmi.so
echo "Launch GROMACS with srun"
NPROCS=`srun --nodes=${SLURM_NNODES} bash -c 'hostname' |wc -l`
echo NPROCS=$NPROCS
#I_MPI_DEBUG=4

gmx grompp -f npt.mdp -c nvt.gro -p 5methane_GMX.top -o md_8.tpr
#grompp_d -p topol -maxwarn 5
#gmx mdrun  -ntomp 25 -ntmpi 1 -deffnm md_0_1
srun mdrun_mpi -v -deffnm md_8
#gmx mdrun -ntomp 25 -ntmpi 1  -v -deffnm md_0_1

#
echo "All Done!"
