import os
import re
import sys
import fileinput
search="Li"
jobname="job-name"
XYZ="10_Li.xyz"
slurm="slurm-orca"
x=100 #x is the variable for the starting value of axial distance betweeen NTCDA plane and Lithium atom
y=100.2 #y is the variable for the end of axial distance

def changexyz(file,str1,pattern):
	for line in fileinput.input(file,inplace=1):
		if pattern in line:
			line="Li 0.0000 1.0800 "+str(str1)
			sys.stdout.write(line)		
			
		

def changeslurm(file,str1,pattern):
	for line in fileinput.input(file,inplace=1):
		if pattern in line:
			line="#SBATCH --job-name=Z_"+str(str1)+"\n"
			pass
		sys.stdout.write(line)
		
#def changeslurm(str1):
while (x <= 100.2):
	print(x)
	str1=str(x)
	str2="Z"+str1
	changeslurm(slurm,x,jobname)
	changexyz(XYZ,x,search)
	os.mkdir(str2) # making the directory an e.g. would be Z120 
	os.system('cp slurm-orca 10_Li.xyz inp_ut.inp ' +str2+'/') #copying relevant files in the directory
	x=x+0.1 #updating x at the end 
