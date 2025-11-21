from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import DensityMatrix
import numpy as np

# 1. Create a Quantum Circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# 2. IMPORTANT: Explicitly instruct the simulator to save the density matrix
qc.save_density_matrix()

# 3. Initialize the AerSimulator with the 'density_matrix' method
sim = AerSimulator(method="density_matrix")

# 4. Run the circuit and get the result
result = sim.run(qc).result()

# 5. Access the density matrix using the identified correct path
#    result.results is a list of ExperimentResult objects
#    result.results[0].data contains the data from the first experiment
#    .density_matrix is the attribute holding the DensityMatrix object
dm = DensityMatrix(result.results[0].data.density_matrix)

print("Successfully retrieved Density Matrix:")
print(dm)

# You can also convert it to a NumPy array if needed
dm_array = np.asarray(dm)
print("\nDensity Matrix (as NumPy array):\n", dm_array)

# Example: Accessing an off-diagonal element
element = dm_array[0, -1]
print("\nOff-diagonal element [0, -1]:", element)
