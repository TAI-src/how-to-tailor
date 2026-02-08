---
title: HPO for a speaker diarization model for emergency medical systems
authors:
  - Anja Jankovic
date: 2026-02-08
link: _No response_
id: 9
---

# [HPO for a speaker diarization model for emergency medical systems](_No response_)

## Problem Description

In real-life applications, such as in emergency medical system dialogues, multiple speakers interact in dynamic and noisy environments. Speech processing systems in these settings therefore focus on two main questions: (1) who is speaking at a given time? and (2) what is being said? The first goal is approached by Speaker Diarization systems. 
Within a collaboration with the Helmholtz Biomedical Institute and in the scope of a bigger project on AI in emergency medicine, a student created a speaker diarization system that would help parse the conversations of paramedics in the field. The optimization problem in our particular use-case was hyperparameter optimization of an open-source pre-trained speech embedding model PyAnnote (see below if this is really tailoring or not).

## Why was tailoring needed?

According to the discussion about tailoring, this concrete example is either not considered to be proper tailoring (by some) or is considered the “lightest” tailoring approach (by others). In this particular case, the baseline approach worked off-the-shelf already, namely PyAnnote could be fine-tuned on the real-world datasets of interest. The only “tailoring” was applying an automated HPO technique to find a setting yielding better overall accuracy of the model. 

## Baseline algorithm

We used the HPO facade of SMAC3 (BO with Sobol initial design, RF as surrogate, logEI as AF, and other specific design choices)  to optimize HPs for the segmentation pipeline and for the clustering pipeline separately. We optimized for accuracy, i.e., we minimized the diarization error rate.

## Tailoring process

Nothing was really tailored, pretty much just applied as is. Leading me to believe that as soon as we can say that we “applied as is” we are not in the tailoring domain anymore.

## What was tailored

_No response_

## Main problem characteristics

* Mixed search space (discrete/continuous)
* Low-dimensional
* Medium to high evaluation cost (fine tuning can take hours, inference is a bit fast)
* Parallelisation possible

## References

_No response_
### Contact information (optional)
_No response_

## Author

Anja Jankovic
_No response_
