# Exact reconstruction of extension proposals

Sparse interval certificates for parametric biobjective optimisation: linear cell bounds and quantitative continuity

Antonio Clim — Journal of Global Optimization. Department of Economic Informatics and Cybernetics, Bucharest University of Economic Studies, Bucharest, Romania. Correspondence: antonio.clim@csie.ase.ro.

The following bounded proposal schedule is the retained implementation account from Online Resource 3, S26.2. Numerical optimisation supplies candidates; separate rational checks determine acceptance. This is not global optimality evidence.

<a id="variation-reconstruction"></a>

<a id="esm3-source-97"></a>

Numerical optimisation proposes candidates. The bounded proposal schedule tries the requested margin with a relative buffer of $10^{-6}$ and then without that buffer, using rational reconstruction denominator caps $10^{6}$, $10^{9}$ and $10^{12}$. One mass per knot is reconstructed as the exact complement of the others. Every attempted reconstruction is retained. Acceptance requires both the unchanged continuous checker and a separately implemented exact margin/rate gate. The latter tests the displayed quadratic inequality and the exact $\operatorname{Lip}_{\infty}$ formula in Online Resource 1, S22 on the final rational object. It does not trust the numerical objective, feasibility flag or Bernstein residuals.

