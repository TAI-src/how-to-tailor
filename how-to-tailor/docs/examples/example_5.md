---
title: Optimization of a GC-MS (mass spectrometer) for high-throughput analysis of biomedical samples - Development of ParEGO
authors:
  - Joshua Knowles
date: 2026-02-08
link: https://ieeexplore.ieee.org/document/1583627/
id: 5
---

# [Optimization of a GC-MS (mass spectrometer) for high-throughput analysis of biomedical samples - Development of ParEGO](https://ieeexplore.ieee.org/document/1583627/)

## Problem Description

Configure the parameters of an analytical instrument (a GC-MS machine) such that it would obtain a high-resolution identification of all the constituents of a complex sample (such as human blood with all the metabolic products in it identified). No simulator of the GC-MS was available or would be realistic. Only one GC-MS machine was available (i.e., parallelization is not possible). Evaluation of one configuration on one sample requires of the order of 15 minutes to 75 minutes, depending on settings. Minimizing the processing time of the GC-MS machine to produce its output was an additional important objective.

## Why was tailoring needed?

Baselines considered were multiobjective evolutionary algorithms. The motivations were three-fold
* No analytical function: black-box setting
* Multiple objectives, at least 3: number of peaks, signal-to-noise, processing time
* Familiarity with multiobjective EAs
Tailoring was needed because these methods require order 1000’s of evaluations and are not designed for optimization under a much more limited budget. Our budget was set at 120 experiments, initially.

## Baseline algorithm

_No response_

## Tailoring process

* We first tailored PAES, PESA, and NSGA-II as leading EMO algorithms of the time
* Mostly this is about reducing the population size significantly, and trying to find reasonable mutation rates. All of this was done in simulation of course, because you cannot tune on the real problem!
* We then investigated single-objective methods for expensive problems. We chose to adapt EGO (Jones et al), which by today’s classification is a Bayesian optimization method, but at that time was known as a DACE-model- or Kriging-metamodel-based method. 
* We then tailored (really, generalized) EGO for the multiobjective case by introducing a randomized sampling of scalarization functions, and
* Adding archiving methods, and
* Experimenting with searching over the Kriging metamodel (“acquistion function”) with alternatives to branch-and-bound or downhill simplex (used in the original EGO paper); eventually we used an inner EA with niching to ensure good search of this multimodal landscape. 

## What was tailored

_No response_

## Main problem characteristics

* Problem properties
    * Blackbox - a real physical experiment
    * No gradients
    * No models (initially)
    * Noisy
    * List of feasible algorithms: PAES, PESA, NSGA-II, or adapt EGO to the multiobjective case, i.e., develop ParEGO
    * Existing alternatives / solutions: none
* Search space
    * Continuous / mixed
    * Low - up to 15
* Objective Space
    * 3 objectives - finding good tradeoffs very important 
    * 15 minutes-75 minutes for one evaluation (of all objectives) of one solution
    * Noise in fitness evaluation
    * The definition of the objective(s) were changing during the first few evaluations as we honed our ability to measure signal-noise ratio and to count peaks in the output chromatograms.
* Constraints
    * Constraint-types: mixed. Some constraints were known a priori; some we learnt as we progressed, i.e., the machine failed for some settings
* User needs
    * Biggest factor was time on the machine. We needed to optimize the settings for a much larger study so that thousands of samples could be analysed using the “optimal” settings. We had weeks to achieve this.
    * So all tuning and algorithm design decisions have to be made offline, e.g. using either intuition or tuning on other functions.
    * A team with very different expertise was needed to undertake this whole process of developing an optimized GC-MS setting. Communication was very challenging. 
A notable remark from the senior scientist (to me) was, “Josh, your algorithm appears to be doing entirely random experiments”. (I suggest, now that ParEGO is quite well established, he was wrong. But of course it looked like that from an onlooker perspective).
Notice that to tune and compare algorithms, we simplified functions in the multiobjective EA test suites of the day. The simplification is motivated and described properly in the ParEGO paper cited above.

## References

Closed-Loop, Multiobjective Optimization of Analytical Instrumentation:  Gas Chromatography/Time-of-Flight Mass Spectrometry of the Metabolomes of Human Serum and of Yeast Fermentations
Steve O'Hagan, Warwick B. Dunn, Marie Brown, Joshua D. Knowles, and Douglas B. Kell. Analytical Chemistry 2005 77 (1), 290-303. DOI: [10.1021/ac049146x](https://pubs.acs.org/doi/10.1021/ac049146x)
ParEGO: a hybrid algorithm with on-line landscape approximation for expensive multiobjective optimization problems
Joshua Knowles. IEEE Transactions on Evolutionary Computation 2006 10(1), 50-66.  [doi: 10.1109/TEVC.2005.851274](https://ieeexplore.ieee.org/document/1583627/)
### Contact information (optional)
_No response_

## Author

Joshua Knowles
_No response_
