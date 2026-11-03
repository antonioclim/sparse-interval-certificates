# Reproduction environments and route boundaries

<a id="reading-and-replay"></a>

## Read first and execute only the intended route

The Markdown files are the canonical technical text. The `html/index.html` entry point is a generated offline rendition of the same documentation. Mathematical expressions are locally typeset SVG with exact LaTeX labels and retained MathML XML sidecars. Tables and mathematical expressions can be read without installing or running the scientific software. Relative links work after extracting the complete documentation tree.

The current private submission-kit driver is `01_Submission/05_Reproduction_Verification/RUN_CURRENT_REPRODUCTION_D3.py`; its current author source closure is `01_Submission/03_Author_Sources/Current_D3`. From the extracted kit root, choose a fresh output directory outside the source tree:

```text
python 01_Submission/05_Reproduction_Verification/RUN_CURRENT_REPRODUCTION_D3.py --package . --output "../rebuilt current D3 documents"
```

The GitHub and Zenodo scientific companion uses the same relative command from its `current_editorial_candidate` root, with a separate public source profile. The private author profile must not be copied into that public companion.

From the extracted Online Resource 10 root, use its public source closure and entry point:

```text
python Reproduction_Verification/RUN_CURRENT_REPRODUCTION_D3.py --output "../rebuilt public D3 documents"
```

That public route can additionally bind the supplied references with `--documents CURRENT_REFERENCE_ROOT`. Read the component README for its exact profile and optional figure-reference arguments.

Earlier B3, B4, C1, D1 and D2Audit routes retain their original fixed input/output guards. They remain upstream or historical stages and must not be repinned to make a different document revision pass. Actual replay results are reported in the supplied current assembly receipts; the command above does not claim a new experiment or an execution on the reader's machine.

<a id="scientific-environments"></a>

## Distinct environment requirements

| Task | Recorded requirements or boundary |
|---|---|
| Read the documentation | Markdown viewer, or a browser displaying local SVG images for the generated HTML; no network-dependent mathematical renderer |
| Check complete kit inventory | Python standard library; use the current kit's `VERIFY_KIT.py` instructions |
| Reconstruct current native documents | Python and `lxml`; follow the current assembly entry point and its source closure |
| Generate the current native figures | Python, NumPy, Matplotlib and lxml, with the supplied fonts and inputs |
| Export and compare figure PDF/PNG | Additional LibreOffice Draw, Poppler and PyMuPDF tools as listed in the kit dependency matrix |
| Rebuild offline documentation HTML | Python standard library and Pandoc 3.1.3, plus installed pdfLaTeX/AMS/standalone and Poppler for mathematical SVG output; tool versions are recorded in the build receipt |
| Replay archived scientific components | Follow the component's unchanged instructions and its own environment; the document environment is not a substitute |

The captured package versions in the kit describe the executed Linux host, rather than a complete installer lock or a test on every supported platform. The previous full document/figure environment recorded Python 3.12.14, NumPy 2.3.5, Matplotlib 3.10.8, lxml 6.1.1, Pillow 12.3.0, pypdf 6.10.0 and PyMuPDF 1.26.6. The fixed package baseline is Python 3.11 or later; the recorded execution does not establish a separate Python 3.11 test.

The speculative numerical proposal route and classifier fitting have their own additional dependencies, recorded in their preserved components. A standard-library proof-checking route does not imply that numerical proposal generation or model fitting is dependency-free.

<a id="new-output-and-guards"></a>

## Output directories and integrity guards

Use a new output destination. Retain the source archive and its complete closure before replay. Current checkers distinguish a wrong or malformed input, an unverified object, resource failure and `UNKNOWN` from a mathematical negative verdict. Closed inventories reject changed or additional source files where their contract requires a fixed source set.

No documentation build installs dependencies, contacts the network, runs GitHub Actions or submits a manuscript. The optional reconstruction routes remain separate from the author's submission workflow.

<a id="limits"></a>

## What a successful local replay establishes

Byte-identical native output verifies that the specified source route reconstructed the recorded document or proof object. A PDF hash binds a supplied reference file; it does not itself inspect its layout. Figure appearance comparisons concern the specified renderer and inputs. Replaying a stored proof does not reproduce historical wall-clock measurements, independently establish a theorem or constitute external human replication.

Native Microsoft Word on Windows and external human replication remain outside the recorded local checks. The theoretical deterministic near-linear geometric construction remains distinct from the supplied quadratic clipping implementation. Restricted-source reconstruction remains separate from the packaged-subset mode.
