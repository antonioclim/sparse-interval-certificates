# R13 and R14 validation control records

Article: Sparse interval certificates for parametric biobjective optimisation: linear cell bounds and quantitative continuity.

Author: Antonio Clim. Journal of Global Optimization.

This technical documentation accompanies Online Resource 2 and is supplied with Online Resource 10. It retains the complete migrated text and displayed table values from the source-bound 28-page ESM2 presentation. The scientific release 1.1.0 and its named archives are unchanged. No experiment or timing run was performed by this migration.

<a id="s14-5"></a>
## S14.5 Complete R13 control bank

These same-host banks address different questions and contain overlapping constructed examples, so their counts must not be summed as disjoint instances. The reference RN classifier has separately written rational, quadratic-field and event arithmetic; it imports no producer geometry, discovery or point arithmetic. The final production gate deliberately shares R1 acceptance arithmetic. Geometry and LP oracles use exhaustive small-system vertex construction rather than production discovery.

| Bank | Executed count | Result |
| --- | --- | --- |
| Separate geometry oracle | 97 fixtures in two row orders | 194 comparisons passed |
| Separate LP oracle | 111 fixtures in three seeded orders | 333 comparisons passed |
| Separate dual checks | 105 identities and 105 mutations | All identities accepted and mutations rejected |
| Separate Farkas checks | Six identities and 24 mutations | All identities accepted and mutations rejected |
| Global producer vs RN oracle | 49 instances, 23 true and 26 false | All classifications agreed; 95 malformed objects rejected |
| Owner geometry | 290 synthetic oracle comparisons | Passed; four input-type controls rejected |
| Owner LP | 126 fixtures, three seeds | 378 comparisons passed; 376 malformed controls rejected |
| Owner integrated producer | 18 mode-and-fixture executions | Passed; all 26 observed R1 calls used at most four columns |

Exact displayed cells: [s14_5_controls.csv](../data/esm2/s14_5_controls.csv).

<a id="s15-6"></a>
## S15.6 Complete R14 control bank

Hashed reference arithmetic and inherited fixtures identify this regression: 97 geometry, 111 LP and 49 RN fixtures reused from the earlier separate-code audit. Rerunning them against R14 does not create new scientific instances. The reference RN classifier uses its own rational/quadratic-field arithmetic and imports no production discovery or checker arithmetic for verdicts. Final acceptance deliberately shares the unchanged R1 gate.

| Separate-code check | Final result |
| --- | --- |
| Geometry in original and reversed row orders | 194 agreements |
| LP in two randomisation modes and three seeds | 666 agreements |
| Sparse duals and altered dual values | 105 accepted identities and 105 rejections |
| Infeasible cores and altered Farkas objects | 6 accepted identities and 24 rejections |
| Global RN with exact clipping | 49 oracle agreements and 95 malformed-proof rejections |
| Global RN with optional proposals | The same 49 agreements and 95 rejections |
| Deliberately malformed geometric proposals | 14 direct rejections and 14 correct fallbacks |
| Missing optional dependency | 2 correct fallbacks |
| Resource or interruption exceptions | 3 propagated without a mathematical verdict |
| Targeted LP hint scenarios | 14 successful checks across both modes |
| Invalid LP arguments or core metadata | 14 rejections |
| Paired versus single shifted construction | 10 identical-object comparison pairs |
| Explicit interior construction | 18 exact confirmations |

Exact displayed cells: [s15_6_controls.csv](../data/esm2/s15_6_controls.csv).

These rows overlap. The geometry regression observed 166 accepted proposals and 28 exact fallbacks. The producer regression observed 58 accepted proposals and 30 fallbacks in its 88 certified-path geometry calls; these counts refer to its own inherited 49-case bank, which differs from the benchmark bank. Six additional valid proposal constructions include a 160-bit thin full-dimensional polytope, positive-proportional rows and duplicated candidate vertices. Boolean and floating original coefficients are rejected before proposal generation.

