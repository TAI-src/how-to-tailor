---
title: Aircraft design
authors:
  - Hauke Maathuis
date: 2026-02-08
link: https://arc.aiaa.org/doi/abs/10.2514/1.J065252
id: 5
---

# [Aircraft design](https://arc.aiaa.org/doi/abs/10.2514/1.J065252)

## Problem Description

The problem was to solve an optimisation problem to lower the weight of an aircraft wing. During this optimisation many constraints arising from multiple disciplines need to be taken into account to ensure feasibility of the design (e.g. structural stability, manufacturability, …). 

## Why was tailoring needed?

To reach the best design possible, one ideally wants to define as many design variables as possible to increase the design freedom of the system. That very quickly poses a high-dimensional design problem. Additionally, in BO black-box constraints are usually taken into account via separate surrogate models. In cases where the number of constraints is high (>10^3) this quickly becomes a bottleneck in terms of computational resources. 

## Baseline algorithm

Since the constraints computed via the respective disciplines can be either highly nonlinear, discontinuous or being computed via commercial solvers that do not provide gradients BO was chosen as a starting point.

## Tailoring process

Developed were two approaches that leverage dimensionality reduction in the input and/or output space, respectively, reducing the number of needed GPs. The acquisition function uses a trust region heuristic to mitigate the curse of dimensionality. 

## What was tailored

_No response_

## Main problem characteristics

* Cont. variables
* single objective
* “High-dimensionality”
* Budget is limited
* parallelisation possible

## References

_No response_
### Contact information (optional)
_No response_

## Author

Hauke Maathuis
_No response_
