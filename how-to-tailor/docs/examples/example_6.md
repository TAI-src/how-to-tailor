---
title: MarioGAN
authors:
  - Vanessa Volz
date: 2026-02-08
link: https://arxiv.org/abs/1805.00728
id: 6
---

# [MarioGAN](https://arxiv.org/abs/1805.00728)

## Problem Description

Generate (snippets of) Super Mario levels.

## Why was tailoring needed?

Existing approaches usually use an encoding of the search space that maps tiles in the level directly to an entry in a matrix. This space then contains lots of unrealistic and unplayable levels, so it is unnecessarily big. We instead created a latent spaces that ideally only contains sensible levels and is easily searchable.

## Baseline algorithm

Algorithm was not tailored, just the encoding. Since it was then turned into a single-objective continuous problem, we use cma-es (state-of-the-art)

## Tailoring process

Colleagues had done latent variable search on another application, so we wanted to try it out here. There were some modifications later that changed the encoding further to prevent the creation of invalid levels (broken pipes). Lots of different objectives were also tried (since there is no clear given objective, it is a benchmarking problem)

## What was tailored

_No response_

## Main problem characteristics

* Instances exist, search space is scalable
* Simulation-based evaluation with big spikes (adding one more tile to a pipe might make it unplayable) and large plateaus
* Not terribly expensive, but also not cheap
* Non-normal noise distribution (simulation of playthroughs is non-deterministic, and Mario tends to get stuck at specific points)

## References

* https://arxiv.org/abs/1805.00728
* https://github.com/CIGbalance/DagstuhlGAN
* https://www.sciencedirect.com/science/article/pii/S1568494623001394
### Contact information (optional)
_No response_

## Author

Vanessa Volz
_No response_
