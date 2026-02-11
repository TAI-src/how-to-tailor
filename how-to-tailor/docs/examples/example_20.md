---
title: Tune SVM with Gaussian Kernel
authors:
  - Tobias Glasmachers
date: 2026-02-11
link: _No response_
id: 20
---

# [Tune SVM with Gaussian Kernel](_No response_)

## Problem Description

When training a support vector machine with Gaussian kernel, (at least) two parameters need tuning: the regularization parameter $ and the parameter $\gamma$ of the Gaussian kernel (x, x') = \exp(-\gamma \|x'-x\|^2)$. We have a large body of prior knowledge about this problem, partly coming from experience, partly from theoretical analysis.

## Why was tailoring needed?

Tailoring makes sense because there is a lot of prior knowledge that can be exploitet. When done naively, the runtime can be excessive, and it is dominated by very few evaluations.
The kernel parameter $\sigma$ is related to $\gamma$ through $\gamma = \frac{1}{2\sigma^2}$. A good starting point for $\sigma$ is a quantile of the distribution of pairwise distances of data points, but it may deviate by, say, an order of magniture. On the other hand, there is no good guideline for an initial value or a range of $.
The parameters do not need high precision. Both of them can be restricted to a grid on a log-scale, i.e., to powers of two. This also indicates that we may wish to work with $\log_2(C)$ and $\log_2(\gamma)$, restricted to the lattice $\mathbb{Z}^2$.
A wider kernel (smaller $\gamma$) usually requires a larger value of $, and the relationship is roughly linear on the log-scale: good configurations are usually found on a line of the form $\log(C) + \log(\gamma) = \text{const}$.
The established (naive) standard procedure for tuning the parameters is grid search, with a validation (or cross-validation) error as the objective function. The landscape is typically (mostly) unimodal, with the bottom of the valley mostly consisting of noise (static noise coming from the data split for cross validation). There may be a (bad) local optimum at one of the bounds, in the form of an unbounded plateau, corresponding to undesirable classifiers (constrant classifier following the majority class, or one-nearest-neighbor). It is easy to check such solutions and to stop the grid from extending further in that direction.
The evalation time can depend in an extremely non-linear fashion on the configuration, ranging from seconds to days. Training a single model with small $\gamma$ and large $ often takes the lion's share of the overall time. Evaluating such configurations without need should therefore be avoided.

## Baseline algorithm

The baseline is to run grid search with a step size of one on a rather large grid, or on a grid that extends dynamically if the optimum is on the boundary. Since grid search is embarassingly parallel, multi-core systems can be leveraged.

## Tailoring process

All of the above can be cast into an optimiization strategy as follows: start with a coarse grid search on a wide grid, say, in steps of three (factors of ^3 = 8$), centered on a reasonable guess for $\gamma$ based on the data and on  = 1$. Extend the grid as long as the optimum is on the boundary, hence avoinding computationally costly data points unless the objective guides us there. Once we found a local optimum, refine the grid to a step size of one. Reuse solutions already evaluated on the coarse grid. Potentially refine by moving along the above-mentioned diagonal.
Of course, the problem can also be solved with an EA, with Bayesian optimization, or other techniques. In that case, the log-encoding should be used and the step size should be lower bounded by one. Care should be taken to avoid the evaluation of unnecessarily expensive data points.

## What was tailored

* problem encoding, using log-scale for both variables
* multi-stage strategy, coarse to fine
* avoid extremely costly evaluations if possible

## Main problem characteristics

* mostly unimodal structure
* a bit noisy, so fine-tuning is meaningless
* reasonable starting point and range known for one parameter
* target precision is known
* evaluation costs depend on the search point, with extreme differences

## References

There is excessive literature on tuning SVM kernel parameters with various methods, e.g., by minimizing generalization bounds. However, the robust standard techique of grid search and cross-validation is featured in many papers, most of which focus on something else in their experiments.
### Contact information (optional)
_No response_

## Author

Tobias Glasmachers
_No response_
