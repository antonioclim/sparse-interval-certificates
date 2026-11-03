#!/usr/bin/env python3
"""Merge canonical Markdown documentation and build a deterministic offline HTML tree.

Python standard library and Pandoc are required. No installation, network, browser
service, GitHub Actions, publication or scientific experiment is performed.
Existing source trees are read-only. The output must not already exist.
"""
from __future__ import annotations
import argparse
from collections import Counter
from hashlib import sha256
from html import escape, unescape
from html.parser import HTMLParser
import json
import math
import os
from pathlib import Path
import posixpath
import re
import shutil
import subprocess
import tempfile
from urllib.parse import quote, unquote, urlsplit, urlunsplit

FIXED_DATE='2026-11-03'
IGNORED_ROOTS={'html','_build'}
IGNORED_FILES={'CONTENTS_SHA256.json','DOCUMENTATION_BUILD_RECEIPT.json'}
CSS='''html{font-size:16px;color:#161616;background:#fff}body{max-width:72rem;margin:0 auto;padding:1.5rem 2rem 4rem;font-family:Georgia,"Times New Roman",serif;line-height:1.55}main{min-width:0}h1,h2,h3,h4{color:#111;line-height:1.25;break-after:avoid}h1{font-size:2rem;margin:1rem 0 1.2rem}h2{font-size:1.45rem;margin-top:2rem}h3{font-size:1.15rem;margin-top:1.6rem}p,ul,ol{margin:0.85rem 0}a{color:#064f83;text-underline-offset:0.14em}a:focus{outline:2px solid #064f83;outline-offset:3px}nav{font:0.9rem/1.5 system-ui,sans-serif;margin-bottom:1.4rem;display:flex;flex-wrap:wrap;gap:0.4rem 1.2rem}nav a{white-space:nowrap}pre{padding:0.9rem;background:#f4f5f6;border:1px solid #ddd;overflow:auto;line-height:1.4}code{font-family:ui-monospace,Consolas,monospace;font-size:0.88em}p code,li code,td code{overflow-wrap:anywhere}table{border-collapse:collapse;display:block;max-width:100%;overflow-x:auto;font-size:0.91rem;margin:1.2rem 0;font-variant-numeric:tabular-nums}th,td{padding:0.55rem 0.7rem;border:1px solid #ccc;vertical-align:top}th{background:#e9edf0;text-align:left}tbody tr:nth-child(even){background:#fafafa}img,svg{max-width:100%;height:auto}.typeset-math img.math-svg{vertical-align:middle}.typeset-math.display-math{display:block;text-align:center;max-width:100%;overflow-x:auto;margin:1rem 0}.typeset-math.inline-math{white-space:nowrap}.typeset-math [hidden]{display:none!important}math{font-size:1.05em}math[display="block"]{display:block;max-width:100%;overflow-x:auto;margin:1rem 0}blockquote{margin:1rem 0;padding-left:1rem;border-left:3px solid #bbb}footer{font:0.82rem/1.5 system-ui,sans-serif;margin-top:3rem;padding-top:1rem;border-top:1px solid #ddd}.table-container{overflow-x:auto}@media(max-width:650px){body{padding:1rem;font-size:1rem}h1{font-size:1.65rem}table{font-size:0.85rem}}@media print{body{max-width:none;padding:0;font-size:10.5pt}nav{display:none}pre{white-space:pre-wrap;overflow-wrap:anywhere}table{display:table;width:100%;font-size:8.7pt}th,td{padding:0.35em 0.5em}thead{display:table-header-group}tr{break-inside:avoid}math[display="block"]{overflow:visible}a{color:inherit}footer{font-size:8pt}}'''

def need(v,message):
    if not v:raise ValueError(message)
def digest(data):return sha256(data).hexdigest()
def js(v):return json.dumps(v,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
def file_inventory(root):return {p.relative_to(root).as_posix():{'bytes':p.stat().st_size,'sha256':digest(p.read_bytes())} for p in sorted(root.rglob('*')) if p.is_file()}
def portable_name(name):
    need('\\' not in name and ':' not in name and not name.startswith('/') and '..' not in Path(name).parts,'Unsafe source path: '+name)
    need(all(ord(c)>=32 for c in name),'Control character in source path')
    need(re.fullmatch(r'[A-Za-z0-9_./-]+',name) is not None,'Non-portable documentation filename: '+name)
def run_pandoc(exe,source,to):
    p=subprocess.run([exe,'--from=gfm+tex_math_dollars+raw_html','--to='+to,'--mathml','--wrap=none'],input=source,text=True,capture_output=True,env={**os.environ,'SOURCE_DATE_EPOCH':'1793664000'})
    need(p.returncode==0,'Pandoc failure: '+p.stderr)
    need(not p.stderr.strip(),'Pandoc reported a conversion warning: '+p.stderr)
    return p.stdout
def render_source(s):
    # GitHub's fenced math is made equivalent to display mathematics for Pandoc.
    return re.sub(r'^```math\s*\n(.*?)^```\s*$',lambda m:'$$\n'+m.group(1).rstrip()+'\n$$',s,flags=re.M|re.S)
def math_nodes(v):
    if isinstance(v,dict):
        if v.get('t')=='Math':yield {'tex':v['c'][1],'display':v['c'][0]['t']=='DisplayMath'}
        for x in v.values():yield from math_nodes(x)
    elif isinstance(v,list):
        for x in v:yield from math_nodes(x)
def typeset_svg(expression,output,cache):
    tex=expression['tex'];need(len(tex)<30000,'Mathematical expression exceeds bounded compiler limit')
    need(not re.search(r'\\(?:input|include|write|read|openout|openin|catcode|csname|usepackage|documentclass|def|let|newcommand|loop|repeat|special|immediate|directlua|pdfobj|pdffiledump|ShellEscape)\b',tex,re.I),'Unsafe TeX command in mathematical expression')
    for environment in re.findall(r'\\(?:begin|end)\{([^}]+)\}',tex):need(environment in {'aligned','alignedat','gathered','split','cases','matrix','pmatrix','bmatrix','Bmatrix','vmatrix','Vmatrix','smallmatrix'},'Unsupported mathematical environment: '+environment)
    key=digest(json.dumps(expression,sort_keys=True).encode())
    if key in cache:return cache[key]
    directory=output/'html/_math';directory.mkdir(parents=True,exist_ok=True);target=directory/(key+'.svg')
    with tempfile.TemporaryDirectory(prefix='radar math render with spaces ') as temporary:
        work=Path(temporary);source=work/'expression.tex'
        source.write_text('\\documentclass[12pt,border=1.5pt]{standalone}\n\\usepackage{amsmath,amssymb}\n\\pdfinfoomitdate=1\n\\pdftrailerid{}\n\\begin{document}\n$'+('\\displaystyle ' if expression['display'] else '\\textstyle ')+tex+'$\n\\end{document}\n',encoding='utf-8')
        process=subprocess.run(['pdflatex','-no-shell-escape','-halt-on-error','-interaction=batchmode','-jobname=math','expression.tex'],cwd=work,capture_output=True,text=True,timeout=30,env={**os.environ,'SOURCE_DATE_EPOCH':'1793664000','FORCE_SOURCE_DATE':'1','openin_any':'p','openout_any':'p'})
        need(process.returncode==0 and (work/'math.pdf').is_file(),'Bounded TeX typesetting failed: '+tex+' '+process.stdout[-1200:]+process.stderr[-1200:])
        process=subprocess.run(['pdftocairo','-svg',str(work/'math.pdf'),str(target)],capture_output=True,text=True,timeout=30)
        need(process.returncode==0 and target.is_file(),'SVG export failed: '+process.stderr)
    svg=target.read_text(encoding='utf-8');need('<svg' in svg and '<path' in svg,'Typeset SVG contains no vector path')
    need(not re.search(r'(?:href|src)=["\'](?:https?:|file:|//)',svg),'SVG has an external loaded reference')
    width=re.search(r'\bwidth="([0-9.]+)(?:pt)?"',svg);height=re.search(r'\bheight="([0-9.]+)(?:pt)?"',svg);need(width and height,'SVG page dimensions missing')
    result={'asset':target.relative_to(output).as_posix(),'sha256':digest(target.read_bytes()),'tex':tex,'display':expression['display'],'width_pt':float(width[1]),'height_pt':float(height[1])};cache[key]=result;return result
def add_svg_math(body,expressions,output,cache,from_md):
    iterator=iter(expressions)
    def replace(m):
        expression=next(iterator);asset=typeset_svg(expression,output,cache);relative=posixpath.relpath(asset['asset'],posixpath.dirname(html_path(from_md)));label='LaTeX: '+expression['tex'];css='display-math' if expression['display'] else 'inline-math'
        mathml=Path(asset['asset']).with_suffix('.mml');(output/mathml).write_text('<?xml version="1.0" encoding="UTF-8"?>\n'+m.group(0)+'\n',encoding='utf-8');asset['mathml_asset']=mathml.as_posix();asset['mathml_sha256']=digest((output/mathml).read_bytes())
        return '<span class="typeset-math '+css+'"><img class="math-svg" src="'+relative+'" alt="'+escape(label,quote=True)+'" data-mathml-source="'+posixpath.relpath(mathml.as_posix(),posixpath.dirname(html_path(from_md)))+'" width="'+str(math.ceil(asset['width_pt']*4/3))+'" height="'+str(math.ceil(asset['height_pt']*4/3))+'" style="width:'+format(asset['width_pt']/12,'.6f')+'em;height:auto"></span>'
    result=re.sub(r'<math\b[^>]*>.*?</math>',replace,body,flags=re.S)
    need(next(iterator,None) is None,'MathML replacement count differs');return result
class InspectHTML(HTMLParser):
    def __init__(self):super().__init__(convert_charrefs=True);self.ids=[];self.refs=[];self.loads=[];self.math=0;self.annotations=[];self.in_tex=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='a' and 'href' in a:self.refs.append(a['href'])
        for key in ['src','poster']:
            if key in a:self.loads.append(a[key])
        if tag=='link' and 'href' in a:self.loads.append(a['href'])
        need(tag not in {'script','iframe','object','embed'},'Executable or embedded remote surface in offline HTML: '+tag)
        if tag=='math':self.math+=1
        if tag=='annotation' and a.get('encoding')=='application/x-tex':self.in_tex=True;self.annotations.append('')
    def handle_endtag(self,tag):
        if tag=='annotation':self.in_tex=False
    def handle_data(self,data):
        if self.in_tex:self.annotations[-1]+=data
def html_path(md):return 'html/index.html' if md=='README.md' else 'html/'+md[:-3]+'.html'
def resolve_source(ref,from_md,root):
    u=urlsplit(unescape(ref));need(u.scheme.lower() not in {'javascript','vbscript','data'},'Unsafe reference: '+ref)
    if u.scheme or u.netloc:return None
    target=posixpath.normpath(posixpath.join(posixpath.dirname(from_md),unquote(u.path))) if u.path else from_md
    need(target!='..' and not target.startswith('../'),'Reference escapes documentation: '+ref+' in '+from_md)
    need((root/target).is_file(),'Missing documentation target: '+ref+' in '+from_md)
    return target,u
def rewrite_references(body,from_md,root,known_md):
    def substitute(m):
        attr,raw=m.group(1),m.group(2);resolved=resolve_source(raw,from_md,root)
        if resolved is None:return m.group(0)
        target,u=resolved
        dest=html_path(target) if target in known_md else target
        relative=posixpath.relpath(dest,posixpath.dirname(html_path(from_md)))
        if target==from_md and not u.path:relative=''
        value=urlunsplit(('', '',quote(relative,safe='/._-'),u.query,u.fragment))
        return attr+'="'+escape(value,quote=True)+'"'
    return re.sub(r'\b(href|src|poster)="([^"]*)"',substitute,body)
def title_of(md):
    for line in md.splitlines():
        if line.startswith('# '):return line[2:].strip()
    return 'Technical documentation'
def retain_explicit_anchors(body,source):
    explicit=re.findall(r'<a\b[^>]*\bid=["\']([^"\']+)["\']',source,re.I)
    need(len(explicit)==len(set(explicit)),'Duplicate explicit Markdown anchor')
    occupied=set(re.findall(r'\bid="([^"]+)"',body));renamed=[]
    def replace(m):
        if m[2] not in explicit:return m.group(0)
        new=m[2]+'-heading';index=2
        while new in occupied:new=m[2]+'-heading-'+str(index);index+=1
        occupied.add(new);renamed.append({'automatic_heading_id':m[2],'html_heading_id':new,'explicit_anchor_retained':m[2]})
        return m[1]+' id="'+new+'"'
    return re.sub(r'(<h[1-6]) id="([^"]+)"',replace,body),renamed
def index_text(md_files,root):
    rows=[]
    for name in md_files:
        if name=='README.md':continue
        title=title_of((root/name).read_text(encoding='utf-8'));rows.append('| ['+title.replace('|','\\|')+']('+name+') | `'+name+'` |')
    return '''# Technical documentation for sparse interval certificates

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
'''+ '\n'.join(rows)+'''

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
'''
def assemble(sources,output,pandoc):
    need(not output.exists(),'Output already exists')
    for src in sources:need(src.is_dir(),'Missing source directory: '+str(src));need(src.resolve()!=output.resolve() and src.resolve() not in output.resolve().parents,'Output must not be inside a source directory')
    sources=[x.resolve() for x in sources];before={str(src):file_inventory(src) for src in sources};output.mkdir(parents=True)
    copied={}
    for src in sources:
        for p in sorted(src.rglob('*')):
            if not p.is_file():continue
            need(not p.is_symlink(),'Linked source refused: '+str(p));name=p.relative_to(src).as_posix()
            if Path(name).parts[0] in IGNORED_ROOTS or name in IGNORED_FILES:continue
            portable_name(name);data=p.read_bytes()
            if name in copied:need(copied[name]==data,'Conflicting document or asset path: '+name);continue
            copied[name]=data;target=output/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
    md_files=sorted(n for n in copied if n.endswith('.md'))
    if 'README.md' not in md_files:
        (output/'README.md').write_text(index_text(md_files,output),encoding='utf-8');md_files=sorted(md_files+['README.md'])
    build=output/'_build';build.mkdir();shutil.copyfile(Path(__file__),build/'build_docs.py')
    buildguide='''# Rebuild the offline documentation\n\nCanonical Markdown and data are read-only inputs. Python 3.11+ and Pandoc are required. This assembly exercised Pandoc 3.1.3. Equations additionally use installed pdfLaTeX with standalone/AMS packages and Poppler pdftocairo to produce vector SVG images. Reading the supplied HTML requires none of those build tools. The builder uses only the Python standard library. No route installs dependencies, accesses the network, runs GitHub Actions, executes scientific experiments or publishes files.\n\nFrom the directory containing docs, choose a new destination:\n\n```text\npython docs/_build/build_docs.py --source docs --output "rebuilt docs"\n```\n\nThe result preserves every canonical Markdown/data byte, regenerates the HTML tree with visible SVG mathematics and retained native MathML, checks relative targets and anchors, compares mathematical TeX annotations with Pandoc's parsed mathematics and closes a SHA-256 inventory. Source snapshots are compared after execution.\n\nGitHub renders the canonical Markdown through its own renderer. The offline HTML uses local SVG images with exact LaTeX alternative labels. Native MathML and TeX annotations are retained in exact XML sidecars, rather than depending on browser MathML support for the visible rendering. This build does not fetch MathJax, KaTeX or a CDN script. TeX is compiled with shell escape disabled, bounded runtime and isolated temporary paths. Installed Computer Modern/AMS fonts and tools retain their own notices; this companion does not license those tools or fonts as new author material. Typeset formula inspection and office conversion remain distinct from a native-browser test; consult the actual assembly QA record for the renderer used.\n\nThe sources/commands in historical scientific components retain their own pinned environments and interpretation. This documentation builder does not replace them.\n'''
    (build/'README_BUILD.md').write_text(buildguide,encoding='utf-8')
    md_files=sorted(md_files+['_build/README_BUILD.md'])
    for name in md_files:
        destination=output/html_path(name);destination.parent.mkdir(parents=True,exist_ok=True);destination.write_text('',encoding='utf-8')
    version=subprocess.run([pandoc,'--version'],capture_output=True,text=True,check=True).stdout.splitlines()[0]
    rendered={};records=[];math_cache={}
    known_md=set(md_files)
    for name in md_files:
        source=(output/name).read_text(encoding='utf-8');converted=render_source(source)
        ast=json.loads(run_pandoc(pandoc,converted,'json'));math=list(math_nodes(ast));body=run_pandoc(pandoc,converted,'html5')
        body,heading_adjustments=retain_explicit_anchors(body,source)
        original=InspectHTML();original.feed(body)
        need(len(original.ids)==len(set(original.ids)),'Duplicate HTML anchor in '+name)
        need(original.math==len(math) and original.annotations==[x['tex'] for x in math],'MathML/TeX conservation differs in '+name)
        rendered[name]=original
        fixed=rewrite_references(body,name,output,known_md)
        fixed=add_svg_math(fixed,math,output,math_cache,name)
        target=html_path(name);back=posixpath.relpath('html/index.html',posixpath.dirname(target));src=posixpath.relpath(name,posixpath.dirname(target));scope=posixpath.relpath('html/distribution/scope-and-assets.html',posixpath.dirname(target))+'#companion-identity'
        page='<!doctype html>\n<html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="generator" content="RADAR D3 offline documentation"><title>'+escape(title_of(source))+'</title><style>'+CSS+'</style></head><body><nav aria-label="Documentation navigation"><a href="'+escape(back)+'">Documentation index</a> · <a href="'+escape(src)+'">Canonical Markdown</a> · <a href="'+escape(scope)+'">Companion identity</a></nav><main>'+fixed+'</main><footer>Antonio Clim · Journal of Global Optimization preparation · D3 technical companion · Prepared for distribution 1.2.0 · Version DOI 10.5281/zenodo.23921914 reserved at build; service publication status is verified separately. Generated from canonical Markdown.</footer></body></html>\n'
        dest=output/target;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(page,encoding='utf-8')
        records.append({'markdown':name,'markdown_sha256':digest((output/name).read_bytes()),'html':target,'html_sha256':digest(dest.read_bytes()),'anchors':original.ids,'automatic_heading_id_adjustments':heading_adjustments,'math_expressions':len(math)})
    source_links=0
    for name,info in rendered.items():
        for ref in info.refs+info.loads:
            resolved=resolve_source(ref,name,output)
            if resolved is None:continue
            target,u=resolved
            if u.fragment and target in known_md:need(unquote(u.fragment) in rendered[target].ids,'Missing Markdown/HTML anchor: '+ref+' in '+name)
            source_links+=1
    html_links=0;external_links=0
    for record in records:
        p=output/record['html'];info=InspectHTML();info.feed(p.read_text(encoding='utf-8'))
        need(not info.loads or all(not urlsplit(x).scheme and not urlsplit(x).netloc for x in info.loads),'Offline page has network-dependent loaded asset')
        for ref in info.refs+info.loads:
            u=urlsplit(ref)
            if u.scheme or u.netloc:external_links+=1;continue
            target=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve()
            need(target.is_relative_to(output.resolve()) and target.is_file(),'Broken or escaping final HTML link: '+ref+' in '+record['html'])
            if u.fragment and target.suffix=='.html':
                ti=InspectHTML();ti.feed(target.read_text(encoding='utf-8'));need(unquote(u.fragment) in ti.ids,'Broken final HTML fragment: '+ref)
            html_links+=1
    need(all(file_inventory(src)==before[str(src)] for src in sources),'Source bytes/set changed during build')
    texversion=subprocess.run(['pdflatex','--version'],capture_output=True,text=True,check=True).stdout.splitlines()[0] if math_cache else None
    poppler=subprocess.run(['pdftocairo','-v'],capture_output=True,text=True,check=True) if math_cache else None
    receipt={'schema':'RADAR_D3_DOI_BOUND_DOCUMENTATION_BUILD_V1','assembly_date':FIXED_DATE,'status':'PASS_DOCUMENTATION_BUILD_AND_STATIC_OFFLINE_CLOSURE','canonical_source':'Markdown and accompanying exact data files','pandoc':version,'pdflatex':texversion,'pdftocairo':(poppler.stderr or poppler.stdout).splitlines()[0] if poppler else None,'python_minimum':'3.11','native_mathml_sidecars_retained':True,'visible_math_rendition':'locally typeset vector SVG with exact accessible TeX labels','math_svg_assets':list(math_cache.values()),'network_dependent_loaded_assets':0,'source_tree_bytes_and_sets_unchanged':True,'markdown_pages':len(records),'source_local_targets_checked':source_links,'html_local_targets_checked':html_links,'external_hyperlinks_not_requested':external_links,'math_expressions':sum(x['math_expressions'] for x in records),'pages':records,'native_browser_visual_test':'NOT_EXECUTED by this builder; actual formula/office QA is separate','scientific_experiments_executed':False,'planned_distribution_version':'1.2.0','planned_GitHub_tag':'v1.2.0','new_Zenodo_DOI_status':'RESERVED_IN_AUTHOR_SUPPLIED_DRAFT_EXPORT_AT_BUILD','new_Zenodo_DOI':'10.5281/zenodo.23921914','Zenodo_version_record':'https://zenodo.org/records/23921914','release_title':'Sparse interval certificates for parametric biobjective optimisation — technical documentation and scientific companion','distribution_status_at_build':'prepared_for_publication','reservation_evidence':'Author-supplied Zenodo draft JSON export; identity consistency checked, not live authenticated service verification','source_draft_export_sha256':'4b23627c422d0b9a9edc296f2e15a161b3a19504da9ecf4753277b85718ee794','live_authenticated_service_verification':False,'publication_performed':False}
    (output/'DOCUMENTATION_BUILD_RECEIPT.json').write_text(js(receipt),encoding='utf-8')
    files=file_inventory(output);(output/'CONTENTS_SHA256.json').write_text(js({'schema':'RADAR_DOCUMENTATION_CLOSED_INVENTORY_V1','files':[{'path':n,**v} for n,v in files.items()]}),encoding='utf-8')
    return receipt
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source',type=Path,action='append',required=True,help='Repeat for collision-checked source fragments');p.add_argument('--output',type=Path,required=True);p.add_argument('--pandoc',default='pandoc');a=p.parse_args();r=assemble(a.source,a.output,a.pandoc);print(js({k:r[k] for k in ['status','markdown_pages','math_expressions','source_local_targets_checked','html_local_targets_checked','network_dependent_loaded_assets']}),end='')
if __name__=='__main__':main()
