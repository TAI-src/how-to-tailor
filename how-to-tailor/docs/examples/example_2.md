---
title: Building spatial design
authors:
  - Koen van der Blom
date: 2026-02-08
link: https://hdl.handle.net/1887/81789
id: 2
---

# [Building spatial design](https://hdl.handle.net/1887/81789)

## Problem Description

Optimise the spatial layout of a building to

* Minimise energy consumption for climate control, and
* Minimise the strain on the structure

## Why was tailoring needed?

Many infeasible solutions exist. No algorithm existed/was found that could handle both multiple objectives, and a mixed-variable search space.

## Baseline algorithm

SMS-EMOA. This performed best after initial tailoring steps needed to be able to run an algorithm at all, that were applied to both SMS-EMOA and NSGA-II.

## Tailoring process

* Design a superstructure **problem representation** to ensure the number of variables stays fixed (the existing representation would change the number of variables regularly). This made it possible to use standard EA frameworks .
* Modify algorithms designed for a single variable type to handle two variable types. (**Add existing** standard mutation + crossover **operators to handle variable types** the algorithm cannot handle natively.) This made it possible to run an algorithm at all.
* Add equal **penalty** value for any solution that is **infeasible**. This led to only a very small number of feasible solutions, and not much optimisation yet.
* **Penalty** value based on the number of **constraint violations** (larger penalty for more violations). This led to more feasible solutions, and actually being able to optimise something.
* **Design a problem-specific** initialisation **operator** to ensure all initial solutions are feasible. This, combined with the next three steps, led to much better Pareto front approximations.
* **Design a problem-specific** mutation **operator** for the binary variables to ensure (standard operator was used for continuous variables, since there were no constraints on those)
* **Remove the standard** crossover **operator**, because it would cause many constraint violations (a new problem-specific crossover operator might be designed later, but proved to be very difficult to do)
* **Add repair function** was used to proportionally scale the continuous variables after mutation to match an equality constraint on them.
* Tune algorithm parameters to further improve performance. This led to further Pareto front approximation improvements.
* Add a local search step to try to improve solutions further by fixing the binary variables and optimising the continuous variables within that subspace.. This did not make much of a difference in the quality of the Pareto front approximation.
* **Partial success**: Although the developed approach worked in principle, it was quite **limited in the size of the designs** it could handle. For larger designs more modifications would be needed to ensure the problem-specific operators would not get stuck in a (fairly) local region of the search space. This was because the probability of finding a feasible mutation decreased when more modifications were made to the parent. (For small enough designs, the whole space would be local enough for things to work.)

## What was tailored

_No response_

## Main problem characteristics

* Many hard constraints (simulator cannot evaluate the solution if these are violated) / Large part of the search space was infeasible. Checking if / how many constraints are violated is cheap.
* Mixed-variable search space (continuous + binary)
* Multiple objectives
* (Somewhat) expensive solution evaluations; with larger designs being more expensive. E.g., rough 1 second per evaluation for the smallest considered design, and roughly 40 seconds for the larger designs we considered. (Even the larger designs we considered are still relatively small for the considered problem.)
* Because of the above, we restricted ourselves to 2500 evaluations, but this was not a strict requirement.

## References

_No response_

## Author

Koen van der Blom
