from pyquil import Program, WavefunctionSimulator
from pyquil.paulis import*
from pyquil.paulis import exponential_map
import numpy as np
wavefunction_simulator = WavefunctionSimulator()

program = Program(H(0),CNOT(0, 1))

z0 = (1-sZ(0))*0.5
z1 = (1-sZ(1))*0.5
xor = (1-sZ(0)*sZ(1))*0.5            

for observable in [z0, z1, xor]:
    expectation = WavefunctionSimulator().expectation(prep_prog=program, pauli_terms=observable)
    print(observable, '\t', expectation)
