---
title: Drone and truck scheduling
authors:
  - Jacomine Grobler
date: 2026-02-11
link: _No response_
id: 20
---

# [Drone and truck scheduling](_No response_)

## Problem Description

One or more purpose-built trucks transports one or more drones with the purpose of completing customer deliveries. The optimisation process is concerned with allocating a customer delivery to either a drone or a truck and determining the best routes for all drones and trucks.
Various versions of the problem exist. Multiple trucks can be used resulting in a vehicle routing problem with drones. Interception models may apply e.g. the drone can intercept the truck en route to deliveries. Other constraints such as single deliveries per launch or time windows may also apply.

## Why was tailoring needed?

It is a discrete problem with many constraints. A problem-specific repair mechanism was needed.

## Baseline algorithm

Continuous CMAES, GCPSO, SaNSDE.

## Tailoring process

1. Problem representation - for the allocation variables the continuous search space was discretised and for the permutation variables a priority-based encoding was used.
2. Initialisation - population was initialised with heuristics e.g. nearest-neighbour and other constructive heuristics
3. Repair mechanism - specifically used for the constraint that only one drone delivery may be completed between two truck deliveries. Consecutive drone deliveries were converted to truck deliveries or the permutation was updated.
4. Problem-specific operators - these were designed to improve the efficiency of the search and address the issue that multiple solutions in continuous space maps to the same solution in the problem space. The operators designed were, for example, swop operators (swopping drone and truck deliveries or swopping two deliveries in the permutation).

## What was tailored

1. Problem representation 
2. Initialisation
3. Repair mechanism for constraint handling
4. Problem-specific operators

## Main problem characteristics

- Up to 1000 discrete variables
- Many complicated constraints
- Cheap fitness function
- Single and multi-objective versions
- 8 hrs of solving time allowed

## References

https://scholar.google.com/citations?view_op=view_citation&hl=en&user=_Fm9-S8AAAAJ&sortby=pubdate&citation_for_view=_Fm9-S8AAAAJ:qUcmZB5y_30C
https://scholar.google.com/citations?view_op=view_citation&hl=en&user=_Fm9-S8AAAAJ&sortby=pubdate&citation_for_view=_Fm9-S8AAAAJ:L8Ckcad2t8MC
### Contact information (optional)
Jacomine.grobler@gmail.com

## Author

Jacomine Grobler
_No response_
