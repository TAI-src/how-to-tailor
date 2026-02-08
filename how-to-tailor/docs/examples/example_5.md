---
title: Optimizing Container turnover rate for a container yard by tuning parameters of a blackbox decision support system
authors:
  - Inneke Van Nieuwenhuyse
date: 2026-02-08
link: _No response_
id: 5
---

# [Optimizing Container turnover rate for a container yard by tuning parameters of a blackbox decision support system](_No response_)

## Problem Description

Company running a container yard in port of Antwerp decides where to put incoming containers on the yard based upon a black-box decision support system. The system requires 6 parameters as input, and then decides on the best spot for each container coming in (based on weight, port of destination,...).  The input parameters have been fixed for a long time, and have been decided upon using some rough-cut search. The location decisions  have an important impact on the container turnover rate (= the number of containers that can be handled per hour by the cranes used for put-away/pick-up of containers). The company wishes to optimize the inputs in order to maximize the resulting container turnover rate. A simulation model (expensive in run time) is available to evaluate how a change in inputs affects the outcome. 

## Why was tailoring needed?

 Very flat response surface, 6 dimensional space, optimizing MEI using local optimization from different starting points BUT no significant improvements

## Baseline algorithm

LHS design (20 points) as starting design; BO with stochastic kriging (GP with heterogenous noise) as surrogate model and Modified Expected Improvement (MEI) as AF
Heterogenous noise present (but rather small), number of dimensions doable for GP, continuous inputs and output

## Tailoring process

* triangulation points: explodes! So not very useful for this nr of dimensions
* pattern search = very useful

## What was tailored

_No response_

## Main problem characteristics

* Heterogenous noise
* 6 dimensions
* continuous search space

## References

_No response_
### Contact information (optional)
_No response_

## Author

Inneke Van Nieuwenhuyse
_No response_
