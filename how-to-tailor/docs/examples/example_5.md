---
title: Brachytherapy treatment planning
authors:
  - Anton Bouter
date: 2026-02-08
link: https://www.sciencedirect.com/science/article/pii/S1538472123016781
id: 5
---

# [Brachytherapy treatment planning](https://www.sciencedirect.com/science/article/pii/S1538472123016781)

## Problem Description

Brachytherapy is a form of internal radiation therapy, which is used to treat patients with, e.g., prostate, cervical, or breast cancer. Radiation is delivered by a radioactive source that is guided through catheters inserted into the target volume. Optimization parameters are so-called dwell times, which determine for how long the radioactive source is halted at each of the predetermined dwell positions, delivering dose to the tissue surrounding the dwell position. Objectives concern delivering a sufficient amount of dose to the target volume, and sparing the surrounding healthy organs, based on values specified by a clinical protocol.

## Why was tailoring needed?

Conventional methods optimize a simplified objective function that does not correlate well with values in clinical protocol that are evaluated by clinicians. Relative weights between clinical aims are difficult to establish and depend on patient characteristics that are difficult to establish.

## Baseline algorithm

Multi-objective real-valued gene-pool optimal mixing evolutionary algorithm (MO-RV-GOMEA). Was shown to perform best among multi-objective EAs. Key strength is the gene-pool optimal mixing (GOM) variation operator, offering high selection pressure and structure-informed variation.

## Tailoring process

* **Problem formulation**: Aggregation of clinical aims into 2/3 objectives that are optimized in a worst-case manner with respect to aim in clinical protocol. Due to worst-case formulation, objective value indicates whether all clinical aims are satisfied. Many-objective optimization with 10-20 objectives was attempted, but did not have satisfactory results in the most interesting region of the search space.
* **Additional constraints/objectives** were added in an iterative process, e.g., to prevent dose hotspots or excessive dose in specific regions. Satisfaction of all aims in the clinical protocol was not sufficient to obtain high-quality treatment plans.
* **Parallelisation of evaluation function**: Clinical workflow requires optimization within at most a few minutes, which initial implementations did not satisfy. This parallelisation requires full knowledge of the dose calculation model used during the evaluation.
* Dependency structure: Knowledge of the optimization problem is used to specify a dependency structure for the GOM variation operator, based on Euclidean distance of dwell positions in 3D space.
* Partial evaluations: More efficient evaluation after partial variation, as is done in GOM. Requires problem knowledge.
* Tuning of population size/hyperparameters

## What was tailored

_No response_

## Main problem characteristics

* Real-valued
* 100-500 dimensional depending on patient
* Multi/many-objective
* Non-convex
* Constrained (generally easy to satisfy)
* Adjustable accuracy of objective function for higher computational cost
* Parallelisation beyond population-level; resulting in relatively inexpensive evaluation
* <5min runtime budget

## References

_No response_
### Contact information (optional)
_No response_

## Author

Anton Bouter
_No response_
