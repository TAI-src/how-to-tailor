---
title: Closed-loop optimization methods
authors:
  - Joshua Knowles
  - various co-authors at the time
  - Richard Allmendinger
date: 2026-02-08
link: https://dl.acm.org/doi/abs/10.1109/MCI.2009.933095
id: 18
---
# [Closed-loop optimization methods](https://dl.acm.org/doi/abs/10.1109/MCI.2009.933095)


  
## Problem description
  
During the period 2004-2009, I worked with biologists, analytical chemists, and food scientists, developing methods to optimize instruments, experimental protocols, or actual products experimentally, a setup sometimes also called closed-loop optimization.

I co-authored quite a number of papers during this period, both in applications journals and in the evolutionary computation literature, and supervised the PhD thesis listed above. Some of these works are summarised and collected in the first reference above. It has a lot to do with tailoring (but also aiming for as much generality as possible). 
  
## Why was tailoring needed?
  
Tailoring is needed for a cluster of reasons in these kind of applications
* Very blackbox nature of the problem
* Limited budget / expensive 
* Possibility of experiments breaking equipment resulting in no evaluation… or worse
* Experiments depend on resources that themselves depend on purchasing, storing or manufacturing consumables; construction of subparts of the solution which then becomes a fixed thing (possibly with reuse capability but also shelf-life); storing and planning how to use these partial solutions; scheduling of experimental staff time.
* Experiments may be anything from one-at-a-time to very highly parallel, but that is dictated by the platform; it’s not a free choice as it is in many simulation environments.
  
  
## Baseline algorithm
  
* We mostly tailored simple EAs, or EAs with niching, or multiobjective EAs. The motivation for this was the blackbox nature of the problems and our familiarity with these methods. However, we looked for generality of the tailoring methods/steps to all the characteristics listed above.
* Later on, we tailored Bayesian optimization methods like ParEGO.
  
  
## Tailoring process
  
 In this line of work, we have developed algorithms (or “tailored” methods), and theory (or technical motivation or principles) in the following related areas:
  
* Ephemeral resource constraints. This is where evaluations depend on resources. If the resources are not there, the experiment (evaluation) cannot be done. (They are a kind of dynamic constraint). We have classified many types and developed methods that work with different EAs.
* Safe optimization. This is where it is possible to permanently lose members of your EA population (e.g., consider the solutions are reconfigurable nano-robots and some of them may break irreplaceably)
* Heterogeneous objectives. Often in closed-loop problems, the objectives of a single solution cannot or may not be evaluated at the same time. (Some may be much cheaper or less time consuming to evaluate than others). So we need better asynchronous EAs or EMO methods to be designed.
  
Our tailoring has included the incorporation of reinforcement learning methods, scheduling/planning methods, and other heuristics or procedures, into evolutionary and Bayesian optimization methods.
  
  
## What was tailored?
  
_No response_
  
## Main problem characteristics
  
_No response_
  
## References
  
* J. Knowles, "Closed-loop evolutionary multiobjective optimization," in IEEE Computational Intelligence Magazine, vol. 4, no. 3, pp. 77-91, Aug. 2009, doi: [10.1109/MCI.2009.933095](https://dl.acm.org/doi/abs/10.1109/MCI.2009.933095).
* Allmendinger, Richard. Tuning evolutionary search for closed-loop optimization. The University of Manchester (United Kingdom), 2012. [PDF](https://staff.cs.manchester.ac.uk/~jknowles/PhD_Richard.pdf)
* Allmendinger, Richard, and Joshua D. Knowles. "Evolutionary Search in Lethal Environments." In IJCCI (ECTA-FCTA), pp. 63-72. 2011. [PDF](https://www.scitepress.org/Papers/2011/36730/36730.pdf)
* Allmendinger, Richard, and Joshua Knowles. "‘Hang on a minute’: Investigations on the effects of delayed objective functions in multiobjective optimization." In International Conference on Evolutionary Multi-Criterion Optimization, pp. 6-20. Berlin, Heidelberg: Springer Berlin Heidelberg, 2013. [PDF](https://www.researchgate.net/profile/Joshua-Knowles/publication/259982630_%27Hang_On_a_Minute%27_Investigations_on_the_Effects_of_Delayed_Objective_Functions_in_Multiobjective_Optimization/links/55977b9008ae21086d2216c2/Hang-On-a-Minute-Investigations-on-the-Effects-of-Delayed-Objective-Functions-in-Multiobjective-Optimization.pdf)
* Allmendinger, Richard, and Joshua Knowles. "Policy learning in resource-constrained optimization." In Proceedings of the 13th annual conference on Genetic and evolutionary computation, pp. 1971-1978. 2011. https://dl.acm.org/doi/pdf/10.1145/2001576.2001841
* Richard Allmendinger, Joshua Knowles; On Handling Ephemeral Resource Constraints in Evolutionary Search. Evol Comput 2013; 21 (3): 497–531. doi: https://doi.org/10.1162/EVCO_a_00097
* Kim, Youngmin, Richard Allmendinger, and Manuel López-Ibáñez. "Safe learning and optimization techniques: Towards a survey of the state of the art." In International Workshop on the Foundations of Trustworthy AI Integrating Learning, Optimization and Reasoning, pp. 123-139. Cham: Springer International Publishing, 2020. https://arxiv.org/pdf/2101.09505
  
## Contact information (optional)
  
Joshua Knowles
  

