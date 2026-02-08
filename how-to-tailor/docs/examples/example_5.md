---
title: Deep RL in Ludii (general game playing)
authors:
  - Dennis Soemers
date: 2026-02-08
link: https://journals.sagepub.com/doi/10.3233/ICG-220197
id: 5
---

# [Deep RL in Ludii (general game playing)](https://journals.sagepub.com/doi/10.3233/ICG-220197)

## Problem Description

learning to play board games (**policies and/or value functions**) in the Ludii system: a single system with ~**1400 distinct** games described in its custom game description language (a DSL). Ludii compiles game description files into runnable simulators.

## Why was tailoring needed?

biquitous assumption in pretty much the entire Deep RL field is that, when we have a domain (e.g., a particular game), we can precisely enumerate or define the whole action space. This is necessary for the established approach (which the entire field follows) for discrete-action-space tasks, where the number of output nodes of a neural network is equal to the number of actions. **This is impossible in Ludii: from a game description file, I cannot automatically infer the action space of the entire game a priori. I can only, given a current state, generate a list of legal moves for that particular state**. Hence: **don’t even know how many output nodes my neural network needs**.

## Baseline algorithm

AlphaZero-like training of a neural network with policy and state value heads, combined with MCTS.

## Tailoring process

we could make a reasonable approximation of the action space that works okay for many games. But there are new risks that were never considered as possibilities by established deep RL methodologies: we sometimes have multiple different actions mapping to a single output node in the policy head. This raises questions about how to train that node (if one action is really good but the other really bad, should the output node have a high or low probability? Probably naively going in between is not great). There is also interesting interaction with the MCTS component, because it searches for a specific state at a time, and actually is able to distinguish between the actions that a DNN cannot distinguish between. 
	Alternative solution is to include an actual feature-based representation of actions, and swap the action over to the input instead of the output. But then we need one forwards pass per action per state, instead of just one per state (giving outputs for all actions in parallel). Only explored this with linear functions, not DNNs.

## What was tailored

problem description was tailored in the sense that we really want to use Ludii (no other system exists with anywhere close to as many different games). Given that constraint, tailoring of neural network architecture, training algorithm, and integration with search became necessary.

## Main problem characteristics

* Sequential decision-making.
* Discrete action space.
* Lots of problem instances (~1400 distinct board games) described in a single DSL.
* Somewhat inefficient simulator (due to need to compile from DSL).
* No automated inferencing (DSL is not logic-based).

## References

_No response_
### Contact information (optional)
_No response_

## Author

Dennis Soemers
_No response_
