# Tiny Quantum Simulator

A small quantum simulator built from scratch, assisted by AI, in Python using NumPy.

## What it does

The simulator represents a qubit as a complex-valued state vector
and implements basic quantum operations.

Currently it can:

- Represent |0> and |1> states
- Apply a Hadamard gate
- Create a superposition
- Calculate measurement probabilities
- Simulate repeated measurements
- Visualise measurement results using Matplotlib

## Technologies

- Python
- NumPy
- Matplotlib

## Example

Applying a Hadamard gate to |0> creates:

|ψ> = 1/√2 |0> + 1/√2 |1>

This means measuring the qubit gives approximately:

P(0) = 50%
P(1) = 50%

## Running the project

Create a virtual environment:

python -m venv .venv

Activate it and install the dependencies:

pip install numpy matplotlib

Then run:

python experiments.py