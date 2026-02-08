---
title: Energy System Optimization
authors:
  - Mathijs de Weerdt
date: 2026-02-08
link: https://tulipaenergy.github.io/TulipaEnergyModel.jl/stable/
id: 16
---

# [Energy System Optimization](https://tulipaenergy.github.io/TulipaEnergyModel.jl/stable/)

## Problem Description

Determine the optimal investment and operation decisions  for different types of assets in the energy system (production, consumption, conversion, storage, and transport), while minimizing loss of load. It can support governments and network system operators.

## Why was tailoring needed?

Tailoring was needed because of the scale of the problem:
* Geographically: the power system in Europe is connected, allowing the use of generators in other countries when local generation is low (traded via energy markets). Investment decisions in one country are thus influenced by what happens in other countries. Decisions on investments in transmission capacity require an appropriate model of the high voltage network within each country.
* Horizon: an investment in a new power plant has an impact for 30-50 years into the future.
* Time resolution: because electricity used should be equal to electricity produced at all times, and renewable energy production may significantly change from one hour to the next, hourly resolution is needed.
* Technical details: generation and storage have additional constraints (e.g. ramping and state of charge, respectively), which connect decisions on one time slot to the next.
* Stochasticity: the computation is based on predictions of demand and weather/climate across the whole horizon, but we have no single perfect prediction for these, so need to take this uncertainty into account, e.g. by taking into account multiple scenarios.
* Ideally multiple solutions are presented, because of unmodeled preferences
* Ideally also the time at which the investments should be made is determined, but we usually just use one or two moments for this

## Baseline algorithm

The default is to model this as a single mixed-integer linear program, because many decisions are binary (e.g. use a certain production or not) and the objective and some constraints are naturally linear (e.g. balance in the system), while others can be reasonably approximated with a linear constraint (e.g. power flow).

## Tailoring process

Mainly we have been tailoring the model:
* not use integer / binary variables, so the problem can be represented as an LP
* From multi-objective to single-objective: although minimizing loss of load (i.e., not meeting demand) is a separate objective to minimizing investment costs and minimizing operational costs, these are all modeled as a single objective.
* reformulate constraints: more tight formulations (taken from different sources in the literature)
* from stochastic to deterministic: use a single deterministic input for demand and weather (= renewable capacity) - this was still quite large, so we modeled future periods by a smaller set of representative periods — finding these requires some intelligent preprocessing of the data (still working on doing this for a stochastic model variant)
* further reduce number of variables and constraints: 
    * allow the user to decide on the geographical scale/details, time resolution, horizon, and technical details
    * enable the user to formulate flexible use of time resolution: different time resolutions for different locations (e.g. when deciding on investments for the Netherlands, have 4-hourly time resolution for countries far away)
**Not successful:**
* using (primal-dual) learning to predict the outcome or bounds of the operation subproblem/simulation
* alternatives for finding good representatives periods

## What was tailored

_No response_

## Main problem characteristics

* dimensions: millions of variables and constraints (including the “simulator”)
* explicit knowledge of the constraints (the simulator is in fact making the decisions on hour-to-hour operations, which is modeled as part of the optimization problem)
* stochastic/uncertainty in input parameters (…)
* more or less linear constraints and objective
* need to be able to explain decisions to a board of experts/directors, possibly government
* runtime budget: up to a week (but better would be the time to get a cup of coffee)

## References

[https://tulipaenergy.github.io/TulipaEnergyModel.jl/stable/40-scientific-foundation/45-scientific-references/](https://tulipaenergy.github.io/TulipaEnergyModel.jl/stable/40-scientific-foundation/45-scientific-references/)
### Contact information (optional)
_No response_

## Author

Mathijs de Weerdt
_No response_
