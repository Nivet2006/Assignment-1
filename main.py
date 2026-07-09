from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

print("=" * 45)
print("        QUBIT STATE EXPLORER")
print("=" * 45)

print("\nChoose a Quantum Gate:")
print("1. X Gate")
print("2. Y Gate")
print("3. Z Gate")
print("4. Hadamard (H) Gate")
print("5. RY Gate")

choice = input("\nEnter your choice (1-5): ")

qc = QuantumCircuit(1)

if choice == "1":
    qc.x(0)
    gate = "X Gate"

elif choice == "2":
    qc.y(0)
    gate = "Y Gate"

elif choice == "3":
    qc.z(0)
    gate = "Z Gate"

elif choice == "4":
    qc.h(0)
    gate = "Hadamard Gate"

elif choice == "5":
    theta = float(input("Enter θ (in radians): "))
    qc.ry(theta, 0)
    gate = f"RY Gate (θ = {theta})"

else:
    print("Invalid choice!")
    exit()

print(f"\nSelected Gate: {gate}")

print("\nQuantum Circuit:\n")
print(qc.draw())

circuit_fig = qc.draw(output="mpl")
circuit_fig.savefig("circuit.png")
circuit_fig.show()

state = Statevector.from_instruction(qc)

bloch_fig = plot_bloch_multivector(state)
bloch_fig.savefig("bloch.png")
bloch_fig.show()

probabilities = state.probabilities()

print("\nMeasurement Probabilities")
print("-" * 30)
print(f"P(|0>) = {probabilities[0]:.4f}")
print(f"P(|1>) = {probabilities[1]:.4f}")

plt.figure(figsize=(6,4))
plt.bar(["|0>", "|1>"], probabilities)
plt.title("Measurement Probabilities")
plt.xlabel("Quantum State")
plt.ylabel("Probability")
plt.grid(axis="y")

plt.savefig("probabilities.png")
plt.show()

print("\nImages saved successfully:")
print("✓ circuit.png")
print("✓ bloch.png")
print("✓ probabilities.png")