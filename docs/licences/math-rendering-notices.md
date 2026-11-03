# Mathematical rendering tools and font notices

<a id="rendering-scope"></a>

The offline documentation's mathematical SVG images are generated from the exact LaTeX expressions in the canonical Markdown. Pandoc also exports corresponding MathML XML sidecars with their TeX annotations. The visible SVG avoids reliance on an online renderer or browser support for MathML. Mathematical LaTeX remains available in image alternative text and in the canonical Markdown.

The build uses installed Pandoc, pdfLaTeX with the `standalone`, `amsmath` and `amssymb` packages, and Poppler `pdftocairo`. It does not bundle those executable tools or redistribute a replacement TeX/font installation. Installed Computer Modern and AMS fonts retain their existing identity and notices; the generated glyph outlines are not presented as newly authored font material.

The supplied [TeX Live font-package copyright and licence record](texlive-fonts-recommended-copyright.txt) is retained verbatim from the actual rendering environment. It includes the Computer Modern attribution and naming conditions. The record is third-party notice material and is outside any blanket licence for newly authored project text or code.

<a id="build-and-inspection-boundary"></a>

The documentation build receipt records the actual tool versions, exact mathematical expressions, SVG/MathML hashes and local reference checks. Formula-level inspection and an office HTML-to-PDF reading check are distinct from a native browser test. The actual assembly QA record states which checks were executed. No global browser, screen-reader or operating-system compatibility claim follows from the static build.

TeX compilation uses shell escape disabled, an isolated temporary directory, a bounded runtime and checks rejecting file-access/control commands in mathematical expressions. The documentation build performs no network access, package installation or scientific experiment.
