# AI Search Coursework - Travelling Salesman Problem

This repository contains a collection of algorithms and city files developed for solving the Travelling Salesman Problem (TSP). The TSP is a well-known problem in computational mathematics, where the goal is to find the shortest possible route that visits a set of cities and returns to the origin city.

## Contents
- `city-files/`: A directory containing various city files representing different TSP scenarios.
- `Algorithm_A.py`: A Genetic Algorithm approach for solving TSP.
- `Algorithm_B.py`: An Ant Colony Optimization approach for solving TSP.
- `Algorithm_A_enhanced.py`: An enhanced version of the Genetic Algorithm.
- `Algorithm_B_enhanced.py`: An enhanced version of the Ant Colony Optimization.
- `runtime_info/`: Contains runtime information for Algorithms A_enhanced and B_enhanced.

## Algorithm Enhancements
### Algorithm A (Genetic Algorithm) Enhancements:
- **Tournament Selection**: Replaces Roulette Wheel Selection for more efficient chromosome selection.
- **Mutations**: Introduces random mutations post-crossover for potential route improvement.
- **Generation Cycles**: Restarts the population every few cycles, keeping only the top performers.
- **Dynamic Iterations & Population**: Scales based on the number of cities to avoid local optima.

### Algorithm B (Ant Colony Optimization) Enhancements:
- **Ant System Construction**: Involves initial pheromone deposit and heuristic desirability matrix.
- **Parameter Tweaking**: Adjustments in Dorigo's alpha and beta values for optimization.
- **Ranked Based Ant System**: Implements a competitive ranking system among ants, influencing pheromone concentration.

## Running the Algorithms
1. **Choose an Algorithm**: Select the Python file corresponding to the algorithm you wish to run.
2. **Specify City File**: Modify the `city_file` variable in the chosen algorithm to the desired city file from `city-files/`.
3. **Set Runtime Conditions**: Adjust the runtime parameters in the algorithm file to suit your requirements.

## Note
The enhanced versions of both algorithms are designed to provide more efficient and potentially more optimal solutions compared to their standard counterparts, especially for complex or larger city files.

---

Sidharth Rao
