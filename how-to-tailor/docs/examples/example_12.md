---
title: Identifying several diverse solutions rather than a single good one
authors:
  - Carola Doerr
date: 2026-02-08
link: https://arxiv.org/abs/2502.13730
id: 12
---

# [Identifying several diverse solutions rather than a single good one](https://arxiv.org/abs/2502.13730)

## Problem Description

_No response_

## Why was tailoring needed?

Rather than outputting a single good solution, users (for example in engineering) may prefer to see a set of diverse solutions that are all reasonable alternatives. Common approaches such as multimodal optimizers or quality-diversity algorithms don't have a guarantee on the diversity in the configuration space, which we request to be a minimal distance between any two solutions in the batch that is output. We also investigated the quality of the batches that can be obtained from the search trajectories of high-performing solvers such as cma-es. Since none of these approaches gave satisfying results, we developed a parallel CMA-ES variant that uses cascading taboo regions that encode the diversity criterion. 

## Baseline algorithm

CMA-ES, because
1.  it is known to perform well when searching for a single good solution, 
2.  it is easy to adapt (well-maintained and documented code),
3. we are familiar enough with the algorithm to adjust it (and to trust its performance)

## Tailoring process

We tried several other ideas such as repelling swarm algorithms but after some initial tests decided to go with this algorithm and to tailor it. Some specific details had to be figured out, we used standard benchmarking routines in the development process. 
What was tailored (Problem model, mutation operator)
Algorithm (new: parallelization and cascading taboo regions)

## What was tailored

_No response_

## Main problem characteristics

* Choose most important ones
* Interest in having batches of diverse solutions came from infeasibility constraints that are not encoded in the objective function (e.g., manufacturing constraints)

## References

https://arxiv.org/abs/2502.13730 for an algorithm 
https://arxiv.org/abs/2408.16393 for why tailoring was needed
### Contact information (optional)
_No response_

## Author

Carola Doerr
_No response_
