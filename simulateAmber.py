from simtk.openmm.app import *
from simtk.openmm import *
from simtk.unit import *
from sys import stdout

prmtop = AmberPrmtopFile('10_Li.prmtop')
inpcrd = AmberInpcrdFile('10_Li.inpcrd')
system = prmtop.createSystem(nonbondedMethod=CutoffNonPeriodic ,nonbondedCutoff=0.5*nanometer, constraints=None)
integrator = LangevinIntegrator(300*kelvin, 1/picosecond, 0.002*picoseconds)
simulation = Simulation(prmtop.topology, system, integrator)
simulation.context.setPositions(inpcrd.positions)
if inpcrd.boxVectors is not None:
    simulation.context.setPeriodicBoxVectors(*inpcrd.boxVectors)
simulation.minimizeEnergy()
simulation.reporters.append(PDBReporter('output2.pdb', 2000))
simulation.reporters.append(StateDataReporter(stdout, 2000, step=True, potentialEnergy=True, temperature=True))
for i in range(100):
  integrator.setTemperature(3*(100-i)*kelvin)  
  simulation.step(1000)
