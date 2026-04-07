---
title: Optimal control of combined heat and power station operation
authors:
  - Jakub Kudela
date: 2026-04-07
link: https://doi.org/10.1007/s11081-023-09848-2
id: 28
---

# [Optimal control of combined heat and power station operation](https://doi.org/10.1007/s11081-023-09848-2)

## Problem Description

Scheduling of the operations of an combined heat and power station (used in a district heating network).

## Why was tailoring needed?

One could possibly write the whole problem as one large mixed-integer programming problem and try and use an off-the-shelf solver. The problem with this approach is twofold - coming up with a proper formulation is nontrivial and the resulting problem will be very large (in terms of numbers of variables, constraints).

## Baseline algorithm

N/A

## Tailoring process

The tailoring process entailed decomposition of the problem into two separate levels that could both be efficiently solved by standard methods. 
The lower-level (optimal operational setup for a given configuration) was a small-scale MILP that was solved by multiparametric programming (https://en.wikipedia.org/wiki/Parametric_programming, specifically MPT3 https://www.mpt3.org/). 
The upper-level problem (scheduling of the operations of specific parts of the system) could then be formulated as a dynamic programming problem and solved by a standard DP routine (there was uncertainty in the formulation, but it only concerned the objective values, not the state transitions, so the algorithm could also be run in a forward regime).
The (possibly infinite-time) problem was then solved in a standard rolling-horizon fashion.
Possible pitfalls
The main pitfall in the approach is the assumption that the state space for the upper level problem is not too large. Adding components that need to be considered in the upper level problem leads to exponential explosion of the state space (the "curse of dimensionality" in DP). There are approaches to address this, but would require substantial modification of the upper-level problem.

## What was tailored

Problem formulation, decomposition and selection of appropriate methods.

## Main problem characteristics

operational scheduling; time-depended constraints; energy system

## References

_No response_
### Contact information (optional)
jakub.kudela@vutbr.cz

## Author

Jakub Kudela
_No response_
