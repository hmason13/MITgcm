#!/bin/bash
#
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --cpus-per-task=1
#SBATCH --mem=6GB
#SBATCH --time=00:30:00
#SBATCH --job-name=bt-gyre-jul9
#SBATCH --mail-type=END
#SBATCH --mail-user=hcm7920@nyu.edu

module purge
module load netcdf-fortran/intel/4.5.3
module load openmpi/intel/4.0.5

# ln -s ../input/* .
mpiexec -n 16 ./mitgcmuv > output.txt





