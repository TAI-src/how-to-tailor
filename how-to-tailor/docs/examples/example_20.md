---
title: Optimizing bags of points : example of the windfarm layout optimization
authors:
  - Rodolphe Le Riche
date: 2026-02-11
link: https://hal.science/hal-04830176
id: 20
---

# [Optimizing bags of points : example of the windfarm layout optimization](https://hal.science/hal-04830176)

## Problem Description

In the windfarm layout problem, one is looking for the number and positions of wind turbines that maximize power production, minimize cost and respect constraints on the turbine positions (exclusion regions). The difficulty comes, in part, from the nature of the optimization variables which are sets of continuous vectors. In other terms, we optimize over the space of sets of points. The number of points is an integer, each point is a continuous vector, there are symetries since the numbering of the points (turbines) does not matter. 

## Why was tailoring needed?

The nature of the variables (set of points) is not traditional 
The objective function is potentially costly to calculate if a true aerodynamic simulation is carried out.
The constraints are nonconvex. The feasible domain can be made of islands.
The objective function is black box (no specific mathematical properties besides the symetry with respect to point labelling)

## Baseline algorithm

A generic evolutionary algorithm and a generic Bayesian optimization algorithm

## Tailoring process

The basic idea is to handle set of points as discrete probability measures. This takes care of the peculiar nature of these variables, e.g., there is no longer any question about the labelling of points (of turbines in the application). 
Then the problem is to move is the space of discrete measures. The key ingredient to do this is through Wasserstein barycenters.
Evolutionary operators were redefined with Wasserstein barycenters.
Kernels handling discrete probability measures were created through sliced-Wasserstein distance and Maximum Mean Discrepancy.

## What was tailored

For evolutionary optimization : the variation operators and the encoding, together.
For Bayesian optimization : the Gaussian process kernel.

## Main problem characteristics

Handle sets of points through discrete probability densities and search operators adapted to such variables.
Applications to windfarm layout problem. Would apply to any problem of sensors/actuator location.

## References

- Babacar Sow, Rodolphe Le Riche, Julien Pelamatti, Sanaa Zannane and Merlin Keller, [Learning functions defined over sets of vectors with kernel methods](https://2023.uncecomp.org/proceedings/pdf/19939.pdf), 5 th ECCOMAS Thematic Conference on Uncertainty Quantification in Computational Sciences and Engineering (UNCECOMP 2023), Jun 2023, Athene, Greece. (also available as [HAL document emse-04043206.](https://hal.science/emse-04043206))
- Babacar Sow, Rodolphe Le Riche, Julien Pelamatti, Merlin Keller, Sanaa Zannane, [Optimization and metamodeling of functions defined over clouds of points](https://hal.science/hal-04830176), talk of R. Le Riche and J. Pelamatti at the [Workshop SAMOURAI](https://uq.math.cnrs.fr/dec24#leriche) Dec 2024, Institut Henri Poincaré, Paris, France Slides as HAL document no. hal-04830176.
- Babacar Sow, Rodolphe Le Riche, Julien Pelamatti, Merlin Keller and Sanaa Zannane, [Wasserstein-Based Evolutionary Operators for Optimizing Sets of Points: Application to Wind-Farm Layout Design](https://doi.org/10.3390/app14177916), Applied Sciences (as part of the Special Issue New Insights into Multidisciplinary Design Optimization), vol. 14, no. 7916, https://doi.org/10.3390/app14177916 , Sept. 2024.
### Contact information (optional)
leriche@emse.fr

## Author

Rodolphe Le Riche
_No response_
