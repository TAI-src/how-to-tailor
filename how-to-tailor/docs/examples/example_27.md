---
title: Real-time Dispatching of Ambulances
authors:
  - Yi Mei
date: 2026-04-07
link: https://dl.acm.org/doi/10.1145/3583131.3590434
id: 27
---

# [Real-time Dispatching of Ambulances](https://dl.acm.org/doi/10.1145/3583131.3590434)

## Problem Description

The application context is Emergency Medical Dispatch (EMD), a critical real-world operation managed by Emergency Services Providers (ESPs). The core problem is the real-time allocation of heterogeneous ambulance resources to dynamic and uncertain medical emergencies to minimize response times and, consequently, patient mortality.
**Specific Challenge**: EMD is an NP-hard dynamic optimization task where decisions must be made instantly as events occur (e.g., a new 111 call or an ambulance becoming free). We aim to automate five specific dispatch decisions (D1–D5):
D1: Decide whether to dispatch an ambulance immediately to a new emergency.
D2: Choose which ambulance to dispatch.
D3: Decide whether to dispatch a newly idle ambulance to a queued emergency.
D4: Choose which queued emergency to attend.
D5: Choose which facility an idle ambulance should return to if no emergencies are waiting.

## Why was tailoring needed?

Existing methods were insufficient for several reasons:
**"Black Box" Nature**: Techniques like Deep Reinforcement Learning (DRL) produce models that are incomprehensible to humans. This is unacceptable for ESPs because human dispatchers must be able to explain and audit their decisions, especially after fatal errors.
**Oversimplification (Representational Gap)**: Previous research often simplified the problem to make it solvable, such as discretizing the road network into grids or ignoring the heterogeneity of ambulances and emergencies. This created a large gap between the academic models and real-world complexity, reducing the practical value of the solutions.
**Lack of Flexibility**: Existing mathematical optimization techniques are often rigid and cannot easily adjust to the dynamic, uncertain nature of real-time EMD without computationally expensive re-optimization.
**Incomplete Scope**: Prior works often focused only on specific subsets of decisions (e.g., only relocation or only dispatch logic) rather than the comprehensive set of five decisions required for a holistic EMD policy.

## Baseline algorithm

We chose Genetic Programming Hyper-Heuristic (GPHH) as our baseline algorithm, due to the following reasons:
**Interpretability**: Unlike neural networks, GPHH evolves tree-based heuristics that can be read and understood as logic rules (e.g: if distance is X, do Y), meeting the audit requirements of ESPs.
**Scalability**: GPHH generates heuristics that scale well to large, realistic instances without requiring the problem simplifications (like grid discretization) common in other methods.
**Provenance**: It has been successfully applied to similar vehicle routing and scheduling domains, making it a strong candidate for EMD.

## Tailoring process

We tailored the GPHH algorithm through the following steps:
**Modular Multi-Tree Framework**: We developed a framework where an individual solution consists of five distinct trees (rules), one for each decision point (D1–D5). This allowed them to learn rules either individually (while keeping others fixed to manual defaults) or simultaneously.
**Domain-Knowledge-Driven Simulation**: To ensure realism, we collaborated with the Wellington Free Ambulance (WFA) service. This partnership helped understand the real-world factors and considerations in this problem, design the simulation environment and the "manual" baseline rules to closely approximate actual human decision-making patterns.
**Decision-Specific Terminal Sets**: We created distinct sets of terminal nodes (inputs) for each of the five rules. For instance, the rule for choosing an ambulance (D2) uses ambulance-specific features, while the rule for choosing a facility (D5) uses facility-based features.
**Simultaneous vs. Independent Learning**: We experimented with learning rules in isolation (e.g., GP-D1) versus simultaneously (GP-DA).

## What was tailored

**Genome Representation**: A multi-tree representation was adopted where a single individual contains a vector of up to five different decision trees.
**Terminal Sets**: Five unique terminal sets were tailored for the specific context of each decision (e.g., AC for ambulance capacity, RTT for response time, EL for escalation level).
**Simulation Environment (Fitness Evaluation)**: The Decision-Making Process (DMP) simulation was custom-built to mirror real-world dynamics, moving away from grid-based abstractions to a graph-based road network with continuous time.
**Objective Function**: The fitness function was tailored to minimise the average weighted response time, incorporating urgency weights derived from industry targets.

## Main problem characteristics

Emergency Medical Dispatch, Dynamic Optimisation, Genetic Programming, Hyper-Heuristic, Heterogeneous Fleet, Real-time Decision Making, Uncertainty, Interpretable AI, Vehicle Routing.

## References

Jordan MacLachlan, Yi Mei, Fangfang Zhang, Mengjie Zhang, and Jessica Signal. Learning emergency medical dispatch policies via genetic programming. In Proceedings of the ACM Genetic and Evolutionary Computation Conference (GECCO), pages 1409--1417. ACM, 2023.
### Contact information (optional)
yi.mei@vuw.ac.nz

## Author

Yi Mei
_No response_
