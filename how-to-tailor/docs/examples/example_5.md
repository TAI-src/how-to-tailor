---
title: Engine design optimization
authors:
  - Robin Purshouse
date: 2026-02-08
link: https://doi.org/10.1016/j.ejor.2022.08.032
id: 5
---

# [Engine design optimization](https://doi.org/10.1016/j.ejor.2022.08.032)

## Problem Description

Optimization of the hardware and control system for a new 1.0 litre 3-cylinder gasoline direct injection (GDI) turbocharged engine with a low-pressure exhaust gas recirculation (LP EGR) system for Ford Motor Company
A multi-objective optimization problem seeking to minimize fuel consumption and NOx emissions over a two-minute dynamic duty cycle, subject to five constraints (turbine inlet temperature, number of knock occurrences, peak cylinder pressure, peak cylinder pressure rise, total work). Seven decision variables are defined: four define the hardware choices of cylinder compression ratio, turbo machinery and EGR cooler sizing; three relate to control variables that parameterise the engine control logic.

## Why was tailoring needed?

Combination of problem features not yet addressed by an available algorithm: multi-objective, constrained, mixed-integer, expensive

## Baseline algorithm

ParEGO (was already implemented in the Tigon library that underpins our Liger open-source MCDM workflow tool being developed in collaboration with Ford)

## Tailoring process

* The Tigon ParEGO implementation uses ACROMUSE as the internal optimizer (this is standard for Tigon but not the vanilla ParEGO)
* Integrated two constraint handling alternatives: penalty function and probability of feasibility (the penalty function approach turned out to be more effective)
* For the mixed integer representation, the surrogate assumed a continuous surface based on an integer coding, but ACROMUSE was fitted with existing discrete variation operators from the literature: Yu & Gen’s discrete crossover and Rudolph’s discrete mutation
* For the evaluation, we collaborated with Hartree to develop an HPC plug-in for the Liger workflow software
* Benchmarking (against existing Ford methods: DoE and NSGA-II) was done using the speed reducer and OSY problems (which have similar features to the real-world problem, although only the speed reducer problem has a (single) discrete decision variable)

## What was tailored

_No response_

## Main problem characteristics

* Multi-objective (discovered post hoc to have a convex Pareto front - we used an infinity norm for the scalarising function but the problem would likely benefit from using the 1-norm)
* Constrained (discovered post hoc that four constraints are active)
* Mixed-integer (four discrete and three continuous)
* Expensive (several hours to evaluate a single design over HPC; nominal budget of 500 design alternatives)
* Nominal candidate design available (which turned out to be dominated)

## References

https://doi.org/10.1016/j.ejor.2022.08.032; https://doi.org/10.1016/j.asoc.2020.106851; https://github.com/ligerdev/liger; https://www.apcuk.co.uk/impact/funded-projects/ford-motor-company-dynamo/ (note that the engine model is proprietary to Ford; the model was developed by collaborators at the University of Bath as part of the project and is implemented in Mathworks Matlab Simulink, including a physics-based co-simulation model developed in Ricardo WAVE-RT).
### Contact information (optional)
_No response_

## Author

Robin Purshouse
_No response_
