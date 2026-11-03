# Recorded controls for mathematical certificate software

Sparse interval certificates for parametric biobjective optimisation: linear cell bounds and quantitative continuity.

Antonio Clim — Journal of Global Optimization.

Department of Economic Informatics and Cybernetics, Bucharest University of Economic Studies, Bucharest, Romania. Correspondence: antonio.clim@csie.ase.ro.

This technical reference accompanies Online Resource 1 and is supplied with Online Resource 10. The mathematical proofs and scientific scope remain in the review documents. The entries below retain the recorded operational contracts and execution descriptions; they do not claim a new software run.

Numbered formulas, reference numbers and proof references below follow Online Resource 1. In particular, “the proof above” in the adaptive arithmetic description refers to its Part A proof in that review document.

<a id="regularity-controls"></a>

## Regularity diagnostic controls

Scientific context: Online Resource 1, S22.3.

Thirty-three constructed cases, each run normally and with Python optimisation, gave 66 expected outcomes. They cover constant, affine and genuinely rational weights; endpoint maxima; denominator rescaling; support three; continuous corners; parameter rescaling; discontinuities; invalid binding; malformed rational/JSON representations; nonpositive denominators; coverage faults; and endpoint-negative residuals vanishing inside a cell. The 32 historical positive R14 objects also received accepted diagnostics. These finite implementation checks establish neither formal soundness nor comparative performance; the inherited objects are not new scientific instances.

<a id="bounded-discovery-failures"></a>

## Bounded discovery failures

Scientific context: Online Resource 1, S8.4.

Settings, source identities, controls and separate software findings are recorded in the receipts. Solver absence, exceptions, nonfinite output, exhausted budgets, failed reconstruction, no new cut or unknown checker status yield no proof. The checker needs no solver, generator, inventory or selector backend. This discovery/acceptance split implements neither (S48) nor (S50), guarantees no complete pair discovery and supplies no physical validation.

<a id="adaptive-arithmetic-checks"></a>

## Adaptive witness arithmetic checks

Scientific context: Online Resource 1, Adaptive witnesses and static objective coordinates, Part A, Arithmetic verification.

The accompanying standard-library calculation checks (A5)–(A7), the simplex identity (A3), endpoint optimum, perturbation bounds and six efficiency gaps over exact rationals. The proof above gives their implications; adaptive-policy optimality is not asserted.

