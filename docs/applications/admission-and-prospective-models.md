# Application admission and prospective models

Sparse interval certificates for parametric biobjective optimisation: linear cell bounds and quantitative continuity

Antonio Clim — Journal of Global Optimization. Department of Economic Informatics and Cybernetics, Bucharest University of Economic Studies, Bucharest, Romania. Correspondence: antonio.clim@csie.ase.ro.

The expanded application discussion accompanies Online Resource 3, S24. These are prospective models and admission requirements. The reviewed PDF retains their affine contract, scientific limits and concise interpretation; no additional application experiment is reported.

<a id="admission-and-prospective-models"></a>

<a id="esm3-source-142"></a>

## S24.1 Scope and evidence status

<a id="esm3-source-143"></a>

An application must give the finite catalogue and interval assertion a defensible meaning. S23 establishes an efficient rule’s strict unsupportedness in the retained tables, without necessary support changes. S9.2 records uniformly dominated alternatives and pure witnesses. The following two scenarios specify prospective models and validation requirements.

<a id="esm3-source-144"></a>

## S24.2 A common finite-catalogue model

<a id="esm3-source-145"></a>

Let a fixed catalogue contain alternatives indexed by $j$, including a fixed reference, and let $k=1,2$ index two losses to be minimised. Suppose that each alternative has a loss $L_{kgj}$ in context $g=0,1$, and that the context proportion is $t$. If the within-context distributions and evaluation rules remain fixed, the mixture losses are

<a id="esm3-source-146"></a>

$$
f_{kj}(t)=(1-t)L_{k0j}+tL_{k1j},\qquad k=1,2.
$$

<a id="esm3-source-147"></a>

Finite empirical counts or measurements encoded at a declared rational resolution give rational coefficients. A documented rational interval within $[0,1]$ specifies the allowed context proportions. Subtracting the reference losses produces the affine columns required by the certificate model. Rational encoding makes acceptance exact for that table; it does not make the table a population truth. Validated upper envelopes can provide a separate route for specified uncertainty or nonlinear differences under S25.1–S25.3; their error assumptions must be justified and do not follow from rational encoding.

<a id="esm3-source-148"></a>

An accepted positive object establishes that, at every parameter in the interval, the reference is excluded from every optimum of a nonnegative normalised weighted sum, including tied optima. Pareto efficiency of the reference is a separate condition to check. The certificate describes an improving convex mixture as mathematical evidence. It does not by itself choose a preferred catalogue member or establish that the mixture can be implemented.

<a id="esm3-source-149"></a>

## S24.3 Admission questions for an application

<a id="esm3-source-150"></a>

Fix the catalogue and reference before evaluating the interval claim. The core guarantee concerns an explicit list. A fixed finite implicit catalogue additionally requires validatable identities, reconstructible losses and global exact pricing for negative verdicts (S25.5 and S26). Adding alternatives, changing admissibility or retraining with the parameter changes the represented problem and is outside that extension.

<a id="esm3-source-151"></a>

What are the losses? Define two quantities with common, documented evaluation populations within each context. Record units, denominators, exclusions and the treatment of failed observations. Conditional metrics whose denominators vary with $t$ need not have the affine mixture form above.

<a id="esm3-source-152"></a>

Specify the contexts, justify fixed within-context losses and choose the interval from the sensitivity question or external information. A convenient interval is not an estimated operating range without supporting evidence.

<a id="esm3-source-153"></a>

Which phenomenon can the model exhibit? Check whether an objective difference row is constant or the two rows are merely positive rescalings of fixed vectors. These structures can rule out the adaptivity or support-change phenomenon being sought, even when exact certificates remain useful.

<a id="esm3-source-154"></a>

Retain the original loss table, its encoding and the accepted object. Check that object against the table, distinguishing negative obstructions from rejection, timeout and UNKNOWN. Minimum-cell claims require separate exclusion evidence.

<a id="esm3-source-155"></a>

Specify uncertainty analysis, evaluation design and feasible actions. Using certificate weights as randomised actions additionally requires admissible randomisation and losses linear in its probabilities. Continuous weights alone do not guarantee feasible physical transitions.

<a id="esm3-source-156"></a>

## S24.4 Potential model for sensors and communications

<a id="esm3-source-157"></a>

A prospective sensing or communications catalogue could use absolute ranging or estimation error per trial, with a declared finite penalty for missing estimates, and packet-loss frequency per trial. Both losses must cover all trials in each of two recorded propagation contexts. Error conditional on successful reception has a changing denominator and needs a separate model check. Admission requires measurements for every configuration in both contexts, justified context definitions and mixture interval, and treatment of measurement resolution and uncertainty. Configuration-dependent context distributions would require revising the fixed-loss assumption. The weighted-sum exclusion and separate Pareto checks are those of S24.2. This scenario has not been executed; the UWB pilot uses fixed observation-count cost as its second objective and supplies none of these additional results.

<a id="esm3-source-158"></a>

## S24.5 Potential model for operational services and security

<a id="esm3-source-159"></a>

A prospective service or security catalogue could comprise fixed verification or service policies, with mean completion latency per request and unsuccessful-request frequency in two documented workload contexts. Declare the deadline and treatment of failed or unfinished requests. Fixed within-context loss tables then yield affine objectives as the workload-context proportion varies. Weighted-sum exclusion has the meaning stated in S24.2; it establishes neither safer service, smaller production losses nor economic savings.

<a id="esm3-source-160"></a>

The affine assumption is substantive: changing workload proportions can alter queueing, resource contention or the responses of interacting components. If these effects make the within-context losses depend on $t$, the displayed mixture model is not justified without further modelling. Validation would require independent workload evaluation, uncertainty treatment and tests of the assumed loss representation. Operational switching or randomisation between policies would require its own feasibility and security assessment. No workload dataset or experiment for this scenario is reported here.

<a id="esm3-source-161"></a>

## S24.6 What the structural limits contribute to practice

<a id="esm3-source-162"></a>

The static-coordinate result in Online Resource 1, Part B, Propositions B1–B2 and the positive-row-rescaling test in S23.5 identify what an application can demonstrate before a computational campaign is designed. In particular, a changing error measure paired with a fixed acquisition price cannot establish separation from every constant mixture, and pure positive row rescaling cannot force support changes. These restrictions do not invalidate the encoded exclusion question.

<a id="esm3-source-163"></a>

Accepted objects certify their stated claims for the encoded catalogue and interval. Workflow improvement also requires a supported decision, a valid model and measured costs. Economic impact, population validity and deployment benefits require further evidence; prospective models remain distinct from executed studies.

