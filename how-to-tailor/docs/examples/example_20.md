---
title: Sum of squares data clustering problems
authors:
  - Marcus Gallagher
date: 2026-02-11
link: https://marcusgal.github.io/ess_clustering.html
id: 20
---

# [Sum of squares data clustering problems](https://marcusgal.github.io/ess_clustering.html)

## Problem Description

Clustering is a very common problem in machine learning and data analysis. It is closely related to the facility location problem, assuming a continuous search space and uncapacitated facilities.  Given a finite dataset of n data points located in p-dimensional continuous space together with a second set of k points (aka cluster centers), the clustering problem is to determine the positions of the cluster centers such that the mean sum of Euclidean distances (L2 Norm) between each data point and its nearest cluster center is minimized.  This is an unconstrained, continuous optimization problem of dimensionality kp. A candidate solution vector, x' can be represented by concatenating the p-dimensional coordinates of the cluster centers. An instance of this problem type is uniquely specified by a dataset and choosing a value of k.

## Why was tailoring needed?

The amount of tailoring required is perhaps relatively small compared to many real-world optimisation problems. It is needed to avoid some difficulties with the sensibility of the search space and objective function.
(i) Data range, search space bounds.
The problem is unconstrained, but the range of the data should be considered. If cluster centers are placed well outside the range of the data, they will not be closest for any center and therefore have no effect on the objective function (i.e. neutral/flat regions on the landscape). This suggests that the algorithm should be initialised within the data range. Soft boundary constraints can also be used if the algorithm requires or can benefit from them.
(ii) Edge case: equal values.
If two cluster centers have exactly the same value, the computation of the objective function is unclear because there is not a unique minimum distance for some data points. For example, cluster centers cannot be all initially placed at the origin.
(iii) Feasible solutions?
If one of more cluster centers are not closest to any data point, they are effectively not part of the solution. If a solution must include exactly k cluster centers, this would need to be included as a constraint. This is typical in facility location in operations research but atypical in clustering. Not enforcing this means that the effective dimensionality of the final solutions is not fixed.

## Baseline algorithm

Focus was on the problems rather than algorithms. CMA-ES, k-means (though not black box) because it is very standard in ML.

## Tailoring process

A soft boundary calculated in two ways: (i) using the maximum range over all data variables; (ii) normalizing the data and then using [0,1] as the bound.
Random initialization (standard so not really tailoring)
Checks to raise a warning during runs if the algorithm was finding solutions that did not use all k cluster centers.

## What was tailored

Soft boundary constraints
Check on solution sensibility during run, possibly resulting in early termination or restarts.

## Main problem characteristics

Continuous, unconstrained, multi-modal, data-driven; scalable

## References

@article{gallagher2016towards,
  title={Towards improved benchmarking of black-box optimization algorithms using clustering problems},
  author={Gallagher, Marcus},
  journal={Soft Computing},
  volume={20},
  number={10},
  pages={3835--3849},
  year={2016},
  publisher={Springer Berlin Heidelberg Berlin/Heidelberg}
}
@inproceedings{vermetten2025standardized,
  title={A standardized benchmark set of clustering problem instances for comparing black-box optimizers},
  author={Vermetten, Diederick and Dinu, Catalin-Viorel and Gallagher, Marcus},
  booktitle={Proceedings of the 18th ACM/SIGEVO Conference on Foundations of Genetic Algorithms},
  pages={297--307},
  year={2025}
}
### Contact information (optional)
marcusg@uq.edu.au

## Author

Marcus Gallagher
_No response_
