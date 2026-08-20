import numpy as np
import matplotlib.pyplot as plt

# Start with the |0> state
zero = np.array([1, 0], dtype=complex)

# Hadamard gate
H = (1 / np.sqrt(2)) * np.array([
    [1, 1],
    [1, -1]
], dtype=complex)

# Apply H to |0>
state = H @ zero

# Perform 1,000 measurements
results = []

for _ in range(1000):
    probabilities = np.abs(state) ** 2

    outcome = np.random.choice(
        [0, 1],
        p=probabilities
    )

    results.append(outcome)

# Count the results
number_of_zeros = results.count(0)
number_of_ones = results.count(1)

print("Zeros:", number_of_zeros)
print("Ones:", number_of_ones)

# Create the bar chart
plt.bar(
    ["0", "1"],
    [number_of_zeros, number_of_ones]
)

plt.xlabel("Measurement outcome")
plt.ylabel("Count")
plt.title("Measurement of a Qubit in Superposition")

#plt.show()

#add the pauli-X gate
X = np.array([
    [0, 1],
    [1, 0]
], dtype=complex)

#state = X @ zero
#state = X @ one
#print(state)

# create a quibit class
class Qubit:

    def __init__(self, state):
        self.state = state

    def apply_gate(self, gate):
        self.state = gate @ self.state

    def probabilities(self):
        return np.abs(self.state) ** 2

    def measure(self):
        probabilities = self.probabilities()

        return np.random.choice(
            [0, 1],
            p=probabilities
        )

qubit = Qubit(zero)

qubit.apply_gate(H)

print(qubit.state)
print(qubit.probabilities())
print(qubit.measure())