import numpy as np
# representing 0 and 1 probabilties
zero = np.array([1, 0], dtype=complex)
#one = np.array([0, 1], dtype=complex)

#print(zero)
#print(one)

#the Hadamard gate
H = (1 / np.sqrt(2)) * np.array([
    [1, 1],
    [1, -1]
], dtype=complex)
result = H @ zero
#prints superposition
#print(result)

#calculate measurement probabilities
def measurement_probabilities(state):
    probabilities = np.abs(state) ** 2
    return probabilities

probabilities = measurement_probabilities(result)

print(probabilities)

# generate an actual measurement

def measure(state):
    probabilities = np.abs(state) ** 2

    outcome = np.random.choice(
        [0, 1],
        p=probabilities
    )

    return outcome

for _ in range(10):
    print(measure(result))