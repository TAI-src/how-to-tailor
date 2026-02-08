---
title: Antenna control
authors:
  - Laurens Bliek
date: 2026-02-08
link: https://doi.org/10.1109/TNNLS.2016.2615134
id: 4
---

# [Antenna control](https://doi.org/10.1109/TNNLS.2016.2615134)

## Problem Description

tune a phased array antenna to steer it towards a target satellite, for telecommunication

## Why was tailoring needed?

existing algorithms were either too inefficient, or required too many function evaluations

## Baseline algorithm

surrogate-based optimization. To reduce the required number of function evaluations.

## Tailoring process

* The goal was to develop an algorithm that is efficient in the number of required function evaluations, but also in the computation time needed to propose a new candidate solution.
* The chosen framework was the same as in surrogate-based optimization: start with a candidate solution, evaluate the solution, update a surrogate model on the data gathered so far, then use the surrogate model to guide the search towards the optimal solution. The idea was that this framework would need less function evaluations than other black-box optimization algorithms such as evolutionary algorithms, though this was not tested.
* The chosen surrogate model was a Random Fourier Expansion, as it is efficient to train and to update, does not slow down over time like Gaussian processes, and has theoretical guarantees available.
* The chosen acquisition function was a type of epsilon-greedy exploration with local perturbations. This allowed for a fast convergence towards a local optimum, while not getting stuck at a local optimum. It avoided the need of spending computation time on calculating covariances or optimizing surrogate model hyperparameters.
* Hyperparameters of the approach were chosen based on expertise and initial experiments. For example, the number of basis functions was a hyperparameter that needed to be chosen such that it balances computational efficiency and performance.
* What was not successful:

    * Nelder-Mead simplex method
    * Powell’s method
    * using a quadratic surrogate model
    * same as proposed approach but pure greedy (epsilon=0) → got stuck in local optima
    * Bayesian optimization with Gaussian processes
    * a more white-box approach that tried to linearize the problem

* **Result**

    * good enough solution found within 2 minutes, with 3000 function evaluations
    * solution 3000 times faster than Bayesian optimization with Gaussian processes
    * solution twice as good as a predict-then-optimize approach with the same surrogate model

## What was tailored

an algorithm was developed from scratch, with the same framework as other surrogate-based optimization algorithms.

## Main problem characteristics

* 24 continuous variables with lower and upper bounds defined and no other constraints
* relatively cheap but noisy objective
* black-box, single-objective, single-fidelity, no parallelization
* Time constraint of 2 minutes (8 years ago, maybe now it would be 1 second or something)
* Function evaluation constraint of 3000
* tested on a simulator, with the goal of eventually being applied on a physical system

## References

[optimal beam-forming network tuning](https://doi.org/10.1109/TNNLS.2016.2615134)
[more information on the application (not the algorithm)](https://opg.optica.org/jlt/abstract.cfm?uri=jlt-37-19-4976 )

### Contact information (optional)

_No response_

## Author

Laurens Bliek
_No response_
