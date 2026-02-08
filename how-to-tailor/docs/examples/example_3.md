---
title: Combined Topology and Fibre-Orientation via Moving Morphable Components and Lamination Parameters
authors:
  - Iván Olarte Rodríguez, Gokhan Serhat, Mariusz Bujny, Thomas Baeck, Elena Raponi
date: 2026-02-08
links: https://github.com/BayesOptApp/Topology_Optimization/tree/main
id: 3
---

# [Combined Topology and Fibre-Orientation via Moving Morphable Components and Lamination Parameters](https://github.com/BayesOptApp/Topology_Optimization/tree/main)

## Problem Description

The idea is to optimize the topology or layout of a structure and the internal material layout. The topology was modelled via Moving Morphable Components (MMCs) wherein prescribed shapes are used to deform and move throughout a design 2D space. On the other hand, the fiber orientation was optimized by using the Lamination Parameter Formulation, which requires setting two parameters with global effects at some master nodes and the local fiber orientations are found by interpolation of these two parameters with respect to proximality to the master nodes.

## Why was tailoring needed?

* Normally, Topology Optimization requires more than 1000 design variables in most used formulations for this matter. Therefore, the Moving Morphable Components formulation was used to reduce dimensionality in a way that is tractable for black-box optimizers, but paying the cost of a much more reduced solution space.
* Simulation malfunctions required to be included as “objective constraints” since some design combinations are numerically infeasible in the way the structure became kinematic and the underlying boundary conditions of the Finite Element solver weren’t fulfilled. By evaluating the target for those sections of the search space, the algorithms get stuck since the target values are uninformative. For surrogate assisted optimization this is a big problem due to spurious correlations and discontinuities.

## Baseline algorithm

_No response_

## Tailoring process

* Changed the target into a piecewise definition by evaluating first if the underlying structure complied with the boundary conditions. In other words, at least there was material connecting the structure from the support and there was material next to the load application.
* We adapted the function to handle constraints in an Augmented Lagrangian Fashion. We observed not so many works in the intersection of small feasible regions of search spaces and high-dimensional settings. However this may be counterproductive for Bayesian Optimization due to the discontinuity of the intersection of the feasible and unfeasible regions.
<img width=554 height=649 alt=Image src="https://github.com/user-attachments/assets/d2045a44-795e-414e-aa53-a79aea2b0fb0" />

## What was tailored

_No response_

## Main problem characteristics

* Continuous formulation of an inherent combinatorial high-dimensional space.
* Small feasible region or highly constrained
* Not all the search space can be evaluated and are meaningful.

## References

_No response_

## Author

Iván Olarte Rodríguez, Gokhan Serhat, Mariusz Bujny, Thomas Baeck, Elena Raponi
