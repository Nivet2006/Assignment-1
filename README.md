# Qubit State Explorer

## Overview

This project was developed as part of the **QuantumX Session 2 Coding Assignment**. It is my first hands-on project using **Qiskit** and quantum computing concepts.

The goal of this project is to explore how different quantum gates affect the state of a single qubit. Starting with a qubit in the **|0⟩** state, the program allows the user to apply various quantum gates and observe how the qubit changes through circuit visualization, Bloch sphere representation, and measurement probabilities.

---

## Objective

The objective of this assignment is to gain practical experience with the fundamentals of quantum computing by:

* Creating a single-qubit quantum circuit.
* Applying different quantum gates.
* Understanding how each gate changes the qubit state.
* Visualizing the final quantum state.
* Calculating the probability of measuring **|0⟩** and **|1⟩**.

---

## Features

* Interactive command-line interface.
* Supports the following quantum gates:

  * X Gate
  * Y Gate
  * Z Gate
  * Hadamard (H) Gate
  * RY Gate (with user-defined rotation angle)
* Displays the generated quantum circuit.
* Visualizes the qubit on the Bloch Sphere.
* Calculates measurement probabilities.
* Generates a probability graph.
* Saves output images for documentation.

---

## Technologies Used

* Python 3
* Qiskit
* Qiskit Aer
* Matplotlib

---

## Installation

Install the required packages:

```bash
pip install qiskit qiskit-aer matplotlib pylatexenc
```

---

## Running the Program

Execute the program using:

```bash
python main.py
```

Choose one of the available quantum gates when prompted.

If the **RY Gate** is selected, enter the rotation angle in radians.

---

## How the Program Works

1. A quantum circuit with one qubit is created.
2. The user selects a quantum gate.
3. The selected gate is applied to the qubit.
4. The program calculates the final quantum state.
5. The quantum circuit is displayed.
6. The Bloch Sphere visualization is generated.
7. The probabilities of measuring **|0⟩** and **|1⟩** are calculated and displayed.
8. A probability graph is generated and saved.

---

## Project Structure

```
Assignment-1/
│
├── main.py
├── README.md
├── H gate/
├── RY gate/
├── X gate/
├── Y gate/
└── Z gate/
```

---

