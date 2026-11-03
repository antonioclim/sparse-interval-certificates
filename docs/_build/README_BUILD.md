# Rebuild the offline documentation

Canonical Markdown and data are read-only inputs. Python 3.11+ and Pandoc are required. This assembly exercised Pandoc 3.1.3. Equations additionally use installed pdfLaTeX with standalone/AMS packages and Poppler pdftocairo to produce vector SVG images. Reading the supplied HTML requires none of those build tools. The builder uses only the Python standard library. No route installs dependencies, accesses the network, runs GitHub Actions, executes scientific experiments or publishes files.

From the directory containing docs, choose a new destination:

```text
python docs/_build/build_docs.py --source docs --output "rebuilt docs"
```

The result preserves every canonical Markdown/data byte, regenerates the HTML tree with visible SVG mathematics and retained native MathML, checks relative targets and anchors, compares mathematical TeX annotations with Pandoc's parsed mathematics and closes a SHA-256 inventory. Source snapshots are compared after execution.

GitHub renders the canonical Markdown through its own renderer. The offline HTML uses local SVG images with exact LaTeX alternative labels. Native MathML and TeX annotations are retained in exact XML sidecars, rather than depending on browser MathML support for the visible rendering. This build does not fetch MathJax, KaTeX or a CDN script. TeX is compiled with shell escape disabled, bounded runtime and isolated temporary paths. Installed Computer Modern/AMS fonts and tools retain their own notices; this companion does not license those tools or fonts as new author material. Typeset formula inspection and office conversion remain distinct from a native-browser test; consult the actual assembly QA record for the renderer used.

The sources/commands in historical scientific components retain their own pinned environments and interpretation. This documentation builder does not replace them.
