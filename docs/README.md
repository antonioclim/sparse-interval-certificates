# Technical documentation for sparse interval certificates

<a id="documentation-index"></a>

This documentation accompanies **Sparse interval certificates for parametric biobjective optimisation: linear cell bounds and quantitative continuity**, by **Antonio Clim**, prepared for the **Journal of Global Optimization**. Affiliation: Department of Economic Informatics and Cybernetics, Bucharest University of Economic Studies, Bucharest, Romania. Correspondence: antonio.clim@csie.ase.ro.

The three thematic supplementary PDFs retain the scientific statements, arguments, measurement contracts and balanced results. This technical companion supplies expanded formats, complete tables, source records and reproduction detail. Article Appendices A-C are separate components of the article, rather than replacements for Online Resources 1-3.

Start with the [claim and evidence reading map](review/claim-evidence-map.md#review-reading-map) to locate each claim's indispensable proof and evidence. The map organises access to the review record; it does not make scientific dependencies optional or substitute page counts for the difficulty of checking the work.

Read this file on GitHub or open [the offline HTML index](html/index.html) after extracting the complete documentation tree. The HTML is generated from the canonical Markdown. Mathematical expressions use locally typeset SVG images with exact LaTeX labels and preserved MathML sidecars, without a network-dependent renderer. Full evidence can be read without executing the scientific software.

<a id="claim-and-resource-map"></a>

## Scientific reading map

| Scientific question | Primary review location | Expanded technical route |
|---|---|---|
| Central linear certificate bound, continuity conversion and quadratic obstructions | Main manuscript and article Appendices A-C | Mathematical format, example and validation documents below |
| Complementary proof languages, minimum claims and regularity | Online Resource 1 | Formats, exact-example expansions and regularity records |
| Implemented algorithms, comparison design and adverse computational outcomes | Online Resource 2 | Complete V2/V3 and speculative-study tables, historical controls and replay guides |
| Conditional extensions and bounded application studies | Online Resource 3 | Extension reconstruction, application admission and source ledgers |
| Original software, retained observations and proof records | Online Resources 4-9 | [Asset map](distribution/scope-and-assets.md#named-assets) |
| Compatibility, current document assembly and this documentation | Online Resource 10 | [Environments and routes](reproduction/environment-and-routes.md#reading-and-replay) |

<a id="documentation-catalogue"></a>

## Document catalogue

| Readable document | Canonical Markdown source |
|---|---|
| [Application admission and prospective models](applications/admission-and-prospective-models.md) | `applications/admission-and-prospective-models.md` |
| [Complete speculative discovery results](benchmarks/speculative-complete-results.md) | `benchmarks/speculative-complete-results.md` |
| [Complete V2 and V3 displayed results](benchmarks/v2-v3-complete-results.md) | `benchmarks/v2-v3-complete-results.md` |
| [Distribution scope and research assets](distribution/scope-and-assets.md) | `distribution/scope-and-assets.md` |
| [Constructed frozen-policy validation example](examples/frozen-policy-validation.md) | `examples/frozen-policy-validation.md` |
| [Figure reconstruction and provenance](figures/reconstruction-and-provenance.md) | `figures/reconstruction-and-provenance.md` |
| [Mathematical rendering tools and font notices](licences/math-rendering-notices.md) | `licences/math-rendering-notices.md` |
| [Exact protocol reference for mathematical certificates](reference/esm1-protocols.md) | `reference/esm1-protocols.md` |
| [Recorded controls for mathematical certificate software](reproducibility/esm1-controls.md) | `reproducibility/esm1-controls.md` |
| [Application source and reconstruction ledgers](reproduction/application-source-ledgers.md) | `reproduction/application-source-ledgers.md` |
| [Reproduction environments and route boundaries](reproduction/environment-and-routes.md) | `reproduction/environment-and-routes.md` |
| [Implementation replay and source records](reproduction/implementation-records.md) | `reproduction/implementation-records.md` |
| [Speculative study source records](reproduction/speculative-study.md) | `reproduction/speculative-study.md` |
| [V2 and V3 evidence records and reproduction](reproduction/v2-v3.md) | `reproduction/v2-v3.md` |
| [Claim and evidence reading map](review/claim-evidence-map.md) | `review/claim-evidence-map.md` |
| [Historical verification evidence](validation/historical-evidence.md) | `validation/historical-evidence.md` |
| [R13 and R14 validation control records](validation/r13-r14-controls.md) | `validation/r13-r14-controls.md` |
| [Exact reconstruction of extension proposals](verification/extension-reconstruction.md) | `verification/extension-reconstruction.md` |

<a id="documentation-identity-and-limits"></a>

## Identity and limits

D3 identifies the DOI-bound document-assembly stage prepared for distribution 1.2.0. The version DOI [10.5281/zenodo.23921914](https://doi.org/10.5281/zenodo.23921914) was reserved in the author-supplied Zenodo draft export used for this build; the corresponding [version record](https://zenodo.org/records/23921914) and GitHub v1.2.0 release identify this technical documentation and scientific companion. Publication status is verified separately through the services. Journal status is separate. The named scientific distribution 1.1.0 assets remain unchanged, with their own historical DOI. [Distribution scope and licences](distribution/scope-and-assets.md#rights) records source-specific rights and excluded material.

An exact stored-input result does not itself establish a population or deployment claim. Historical timing observations remain historical; documentation migration does not rerun them. Native Word/Windows testing and external human replication remain outside the recorded local scope. Mathematical claims are supported by the supplied arguments and computational evidence; AI-assisted output is not independent external evidence or formal verification. See the manuscript's unchanged assistance declaration for the author-approved scope.

<a id="documentation-build"></a>

## Rebuild this rendition

Use Python and Pandoc, with the supplied TeX/Poppler mathematics route when equations are present, from a directory containing the complete docs tree:

```text
python docs/_build/build_docs.py --source docs --output "rebuilt docs"
```

The output destination must not exist. The builder preserves Markdown and data bytes, regenerates HTML and checks local targets, anchors, source-math annotations and the complete inventory. It does not run a scientific experiment. Build details are in [the build guide](_build/README_BUILD.md).
