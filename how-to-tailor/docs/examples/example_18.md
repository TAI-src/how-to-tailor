---
title: Bayesian Optimization with Gaussian Processes for Protein Design
authors:
  - Carolin Benjamins
date: 2026-02-11
link: https://www.mlsb.io/papers_2024/Bayesian_Optimisation_for_Protein_Sequence_Design:_Gaussian_Processes_with_Zero-Shot_Protein_Language_Model_Prior_Mean.pdf
id: 18
---

# [Bayesian Optimization with Gaussian Processes for Protein Design](https://www.mlsb.io/papers_2024/Bayesian_Optimisation_for_Protein_Sequence_Design:_Gaussian_Processes_with_Zero-Shot_Protein_Language_Model_Prior_Mean.pdf)

## Problem Description

From a pool of candidate protein sequences, find the best one. The general search space is mutating an amino acid in the sequence.
We only target mutating one protein wild type.

## Why was tailoring needed?

1. Representations could be very long, normally, proteins are represented as the sequence (could get up to 700 dimensions). 
1. Some form of prior knowledge in the form of protein language models available, so we aim to include this to speed up the optimization.

## Baseline algorithm

BO with a GP and specific fingerprint/string kernels.

## Tailoring process

1. Identify possible modeling obstacles when using a GP. 
2. Identify prior knowledge.

## What was tailored

1. Adapt the representation/encoding: From the raw string representation of the protein as a sequence of amino acids, represent the variant as the mutation code. We only look at single mutations. This reduces the feature vector/dimensions from up to 700 to 3, which is much better consumable by the GP. In addition, by inspecting the protein landscapes from datasets, it is evident, that the location of the mutation plays a major role. Encoding the location directly should assist optimization.
2. Use the protein language model's predictions as the prior mean to prime the mode. Interpolate between this prior and a standard constant mean, and adapt this interpolation coefficient based on the observed data (simply included in the fitting process).

## Main problem characteristics

combinatorial, high-dimensional, protein design

## References

Abstract: https://scholar.google.com/citations?view_op=view_citation&hl=de&user=nx_Xq8YAAAAJ&citation_for_view=nx_Xq8YAAAAJ:8k81kl-MbHgC
### Contact information (optional)
_No response_

## Author

Carolin Benjamins
_No response_
