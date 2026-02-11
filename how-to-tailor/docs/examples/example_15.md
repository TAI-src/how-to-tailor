---
title: Electric Motor Design Optimization
authors:
  - Tea Tušar
date: 2026-02-08
link: https://dis.ijs.si/tea/Publications/Tusar23Multistep.pdf
id: 15
---

# [Electric Motor Design Optimization](https://dis.ijs.si/tea/Publications/Tusar23Multistep.pdf)

## Problem Description

The goal was to find a design of a synchronous electric motor for power steering systems that minimizes costs and satisfies all constraints. While computing the costs was rather straightforward, checking the feasibility of solutions required time-consuming simulations.  

## Why was tailoring needed?

Although the company was already using surrogate-based optimization before our collaboration, the severe constraints were making it hard to find high-quality solutions in reasonable time. The tailoring made it possible to find designs that were 10% cheaper of the ones used by the company. 

## Baseline algorithm

lq-CMA-ES [Hansen2019], which uses a surrogate model and also supports constraints

## Tailoring process

Tailoring was performed on the evaluation of solutions rather than the optimization algorithm. The evaluation of solutions was split into five steps. If after any step, the solution was found to be infeasible, the evaluation stopped there and a penalty was added to the objective. The steps were:
1. Executing a quick Python script to check feasibility with regard to magnet placement. Checking this before evaluating a solution with the simulator was particularly helpful because we could avoid some simulation errors. About 17.5% of solutions were discarded after this step, which spared about 8 minutes of time per solution. 
2.  Executing a simulation with Ansys to compute the properties of the electrical motor design. This took about 1 minute when successful and considerably longer when the design was infeasible. About 29.4% of solutions were discarded after this step, which spared about 7 minutes of time per solution.
3. Computing the costs with a quick Python script. 
4. Checking solution robustness. This consisted of running parallel simulations with Ansys that took about 7 minutes per solution. This step was tailored further (compared to previous experiments done by the company) by adapting the mesh size as some additional experiments showed that we could gain about half the time without losing too much information. 
5.  Computing some additional properties with a quick Python script and checking final solution feasibility.
The **objective function** was tailored to accommodate some “soft” constraints as well as penalize infeasible solutions (the earlier a solution was found to be infeasible, the larger the penalty). 
Because of the limited time at our disposal, we didn’t attempt to tune the optimization algorithm.

## What was tailored

_No response_

## Main problem characteristics

Problem definition
* 13 variables
    * 12 “continuous” (were discretized in evaluations, but were treated as continuous by the optimization algorithm)
    * 1 discrete (ordered, not combinatorial)
* 1 objective (costs)
* 2 “soft” constraints, whose violation was added to the main objective
* 10 “hard” constraints
Other properties 
* The constraints were multimodal and hard to satisfy
* While we were working on a single problem instance, the company had many instances to solve that could be handled in the same way
* We could only afford to run the algorithm a handful of times, for a few thousand evaluations each
* The code cannot be disclosed

## References

[Hansen2019] Nikolaus Hansen. 2019. A global surrogate assisted CMA-ES. V Proceedings of the 2019 Genetic and Evolutionary Computation Conference. ACM, New York, NY, USA, 664–672. https://doi.org/10.1145/3321707.3321842 
### Contact information (optional)
_No response_

## Author

Tea Tušar
_No response_
