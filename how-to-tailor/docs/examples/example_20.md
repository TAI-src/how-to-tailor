---
title: Kriging-Assisted Level Set Topology Optimization for Crashworthiness
authors:
  - Elena Raponi
date: 2026-02-11
link: https://www.sciencedirect.com/science/article/pii/S0045782519300726
id: 20
---

# [Kriging-Assisted Level Set Topology Optimization for Crashworthiness](https://www.sciencedirect.com/science/article/pii/S0045782519300726)

## Problem Description

The problem concerns topology optimization of mechanical structures under static and dynamic loading, with particular focus on crashworthiness. The goal is to determine the optimal material distribution within a prescribed design domain while satisfying a volume constraint and structural connectivity requirements.
In the static case, compliance minimization of a cantilever beam is considered. In the dynamic crash case, the objective is to minimize pole intrusion during impact, modeled via nonlinear finite element simulations.
The structure is represented using Moving Morphable Components (MMCs) embedded in a Level Set framework, resulting in a reduced design space. Evaluations require high-fidelity FEM simulations (CalculiX or LS-DYNA), making each function call computationally expensive.
[Raponi et al. - 2019 - Kriging-assisted topology optimization of crash st.pdf](https://github.com/user-attachments/files/25231852/Raponi.et.al.-.2019.-.Kriging-assisted.topology.optimization.of.crash.st.pdf)

## Why was tailoring needed?

The first reason why tailoring was needed was to reduce the dimensionality of the problem. A level-set based parametrization using MMCs allows to control multiple points of a discretized design space (on which we want to find the optimal material distribution) simultaneously.
The second reason was to enforce connectivity (inactive) and volume (active) constraints efficiently, in order to avoid wasting expensive evaluations in infeasible regions.

## Baseline algorithm

The baseline algorithm is the standard Efficient Global Optimization (EGO) framework, belonging to the Bayesian optimization (BO) algorithm class, using:
- Initial Design of Experiments (Optimal Latin Hypercube Sampling),
- Kriging/Gaussian process regression (GPR) surrogate modeling with MLE hyperparameter estimation,
- Standard Expected Improvement (EI) acquisition function,
- Infill point selection via global optimization (Differential Evolution),
For comparison, CMA-ES with exterior penalty for constraints was also used as a non-surrogate baseline.
The choice of the BO algorithm was dictated by the high cost of function evaluations, that are based on runs of a numerical simulator. BO is particularly well suited for low-budget scenarios.

## Tailoring process

### PARAMETRIZATION:
The structural parametrization was critical to make surrogate-based optimization feasible. 
- A natural starting point in topology optimization is a density-based representation (e.g., SIMP), where each finite element has an associated density variable. This makes the number of variables extremely large (thousands of elements) and GPR surrogates (and BO in general) scale poorly in high dimensions.
- To enable surrogate modeling, the representation was tailored to use Moving Morphable Components (MMCs) within a Level Set framework. A drawback of this parametrization is that it is heavily tailored to the application because it only allows for obtaining beam-like structures (for example, car chassis portions) which does not cover different types of material distributions, required by other specific applications.
### CONSTRAINTS:
- Initial attempt: Standard EI not considering connectivity constraint. Applying standard EGO with standard constrained expected improvement (CEI) only considering the volume (active) constraint still led to many infill points in disconnected regions. CEI uses a probabilistic model of the volume constraint and combines it multiplicatively with EI to guide search toward feasible regions. Most likely this initial attempt did not work because of the out-of-scale objective values of disconnected structures, which were difficult to model by the surrogate model. This wasted expensive evaluations.
- Filtering infeasible DoE samples: Infeasible designs were removed before surrogate construction. This improved model quality but did not prevent infeasible infill proposals.
- Penalty inside objective (unsuccessful for crash case): Adding penalty terms directly to the objective degraded surrogate quality and created landscapes alternating almost flat landscapes and high jumps at the boundaries between feasibility and feasibility, which hindered acquisition optimization.
- Development of Expected Improvement for Connected Designs (EICD): A graph-based connectivity check was introduced. Disconnected candidates were penalized at the acquisition level rather than the objective level. This avoided FEM calls for infeasible structures. This worked and the tailoring (connectivity check) was highly specific to the considered application.
- Final combined acquisition (EICD + CEI): The tailored acquisition ensured both connectivity and volume feasibility before committing to expensive FEM evaluation. These two constraints were handled with different techniques, EICD and CEI respectively, because of their different way of influencing the search of the optimum. Not standard practice. This progression led to a significantly improved convergence behavior under the limited evaluation budget.

## What was tailored

- Acquisition function: Modified from standard EI to Expected Improvement for Connected Designs (EICD), Constrained Expected Improvement (CEI), and a final combined feasibility-aware acquisition (EICD + CEI).
- Constraint handling: Connectivity handled at acquisition level using graph-based representation.Volume handled probabilistically via surrogate modeling.
- Problem representation: Adoption of Moving Morphable Components within a Level Set framework to reduce dimensionality and make surrogate modeling tractable.
- Initialization strategy: Feasible-only DoE filtering.
The surrogate model itself (Kriging) and the algorithm used to optimize the acquisition function (DE) remained standard; tailoring focused on feasibility-aware infill and structural representation.

## Main problem characteristics

engineering, topology optimization, nonlinear, expensive evaluations, high-dimensional, discontinuous

## References

X. Guo, W. Zhang, W. Zhong, Doing topology optimization explicitly and geometrically - A new moving morphable components based
framework, J. Appl. Mech. 81 (8) (2014) 081009, http://dx.doi.org/10.1115/1.4027609.
M.P. Bendsøe, O. Sigmund, Topology Optimization - Theory, Methods, and Applications, second ed., Springer, 2004.
M. Bujny, N. Aulig, M. Olhofer, F. Duddeck, Identification of optimal topologies for crashworthiness with the evolutionary level set method,
Int. J. Crashworthiness 23 (4) (2018) 395–416, http://dx.doi.org/10.1080/13588265.2017.1331493.
### Contact information (optional)
e.raponi@liacs.leidenuniv.nl

## Author

Elena Raponi
_No response_
