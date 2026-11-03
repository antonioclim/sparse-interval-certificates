# Exact protocol reference for mathematical certificates

Sparse interval certificates for parametric biobjective optimisation: linear cell bounds and quantitative continuity.

Antonio Clim — Journal of Global Optimization.

Department of Economic Informatics and Cybernetics, Bucharest University of Economic Studies, Bucharest, Romania. Correspondence: antonio.clim@csie.ase.ro.

This technical reference accompanies Online Resource 1 and is supplied with Online Resource 10. The mathematical proofs and scientific scope remain in the review documents. The entries below retain the recorded operational contracts and execution descriptions; they do not claim a new software run.

Numbered formulas, reference numbers and proof references below follow Online Resource 1. In particular, “the proof above” in the adaptive arithmetic description refers to its Part A proof in that review document.

<a id="selector-cover-schema"></a>

## Selector cover and packing schemas

Scientific context: Online Resource 1, S2.3.

The cover and packing schemas are U2_UNRESTRICTED_SELECTOR_COVER_V1 and U2_UNRESTRICTED_SELECTOR_PACKING_V1. Upper, lower and minimum acceptance statuses remain distinct. Malformed points, schemas, proofs or unknown delegated statuses are invalid evidence, not RN refutations or nonminimality proofs. The checker shares preserved exact point arithmetic but imports no inventory or merging helper. This follows the untrusted-certificate architecture [3], without inheriting formal soundness.

<a id="compression-input-boundary"></a>

## Compression input boundary

Scientific context: Online Resource 1, S6.

The compressor requires the numerator and denominator arrays of each ordered R6 equalising policy to match (S15) exactly. Equivalent rescalings, pure policies and outside-W outputs fall outside this format; refusal asserts neither RN failure nor nonminimality. The positive and packing proofs are checked against original columns, without requiring the generator’s inventory or greedy trace.

<a id="one-cell-input-contract"></a>

## One cell input contract

Scientific context: Online Resource 1, S8.4.

Declare one or two distinct original identifiers in their original order and a rational closed span within the domain. Singletons use a separate pure query. Reject unknown fields, duplicate JSON keys, noncanonical rationals and invalid support order. The restricted instance copies the original data, changing only the interval. The wrapper binds the original digest, support and span; its one-cell R1 proof on that span binds the restricted digest and uses only declared originals. A valid singleton subset or reversed nested pair order is allowed. The unchanged R1 checker decides strict-policy acceptance.

<a id="one-cell-statuses"></a>

## One cell statuses

Scientific context: Online Resource 1, S8.4.

The statuses VERIFIED_ONE_CELL_AFFINE_RATIONAL_FEASIBILITY and VERIFIED_NO_ONE_CELL_AFFINE_RATIONAL_POLICY_ON_FIXED_SUPPORT concern exactly one declared support/span and one canonical formula. The exclusion leaves RN, arbitrary selectors, larger supports, multiple formulas and global minima undecided. Malformed evidence is INVALID; unsuccessful bounded discovery is UNKNOWN_ONE_CELL_ORACLE, with no feasibility verdict.

## Reference cited in these entries

[3] Li, W., Passmore, G.O., Paulson, L.C.: Deciding univariate polynomial problems using untrusted certificates in Isabelle/HOL. J. Autom. Reason. 62, 69–91 (2019). https://doi.org/10.1007/s10817-017-9424-6.
