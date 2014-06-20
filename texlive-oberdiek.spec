# revision 33322
# category Package
# catalog-ctan /macros/latex/contrib/oberdiek
# catalog-date 2013-11-22 17:11:31 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-oberdiek
Version:	20131122
Release:	1
Summary:	A bundle of packages submitted by Heiko Oberdiek
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/oberdiek
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oberdiek.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oberdiek.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oberdiek.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle comprises packages to provide: accsupp: better
accessibility support for PDF files; aliascnt: 'alias
counters'; alphalph: multiple-alphabetic counting
(a...z,aa...zz,... -- up to the full extent of a TeX counter);
askinclude: replaces \includeonly by an interactive user
interface; atbegshi: a modern reimplementation of package
everyshi; atenddvi: provides \AtEndDvi command; attachfile2:
attach files to PDF files; atveryend: hooks the very end of a
document; auxhook: stick stuff at the start of the .aux file;
bigintcalc: expandable arithmetic operations with big integers
that can exceed TeX's number limits; bitset: defines and
implements the data type bit set, a vector of bits; bmpsize:
get bitmap size and resolution data; bookmark: alternative
bookmark (outline) organization for package hyperref;
catchfile: collects the contents of a file and puts it in a
macro; centernot: a horizontally-centred \not symbol; chemarr:
extensible chemists' reaction arrows; classlist: record
information about document class(es) used; colonequals: poor
man's mathematical relation symbols; dvipscol: dvips colour
stack management; embedfile: embed files in PDF documents;
engord: define counter-printing operations producing English
ordinals; eolgrab: collect arguments delimited by end of line;
epstopdf: conversion with epstopdf on the fly; etexcmds: adds a
prefix to eTeX's commands, to avoid conflicts with existing
macros; flags: setting and clearing flags in bit fields and
converting the bit field into a decimal number; gettitlestring:
clean up the string containing the title of a section, etc.;
grfext: macros for adding and reordering the list of graphics
file extensions recognised by the graphics package; grffile:
extend file name processing in the graphics bundle; hosub:
build collections of packages; holtxdoc: extra documentation
macros; hologo: bookmark-enabled logos; hopatch: safely apply
package patches; hycolor: implements the color option stuff
that is used by packages hyperref and bookmark; hypbmsec:
bookmarks in sectioning commands; hypcap: anjusting anchors of
captions; hypdestopt: optimising hyperref's pdftex driver
destinations; hypdoc: hyper-references in the LaTeX standard
doc package; hypgotoe: experimental package for links to
embedded files; hyphsubst: substitute hyphenation patterns;
ifdraft: switch for option draft; iflang: provides expandable
checks for the current language; ifluatex: looks for LuaTeX
regardless of its mode and provides the switch \ifluatex;
ifpdf: provides the \ifpdf switch; ifvtex: provides the \ifvtex
switch; infwarerr: provides a complete set of macros for
informations, warnings and error messages with support for
plain TeX; inputenx: enhanced handling of input encoding;
intcalc: provides expandable arithmetic operations with
integers; kvdefinekeys: define key-value keys in the same
manner as keyval; kvoptions: use package options in key value
format ; kvsetkeys: a variant of the \setkeys command;
letltxmacro: Let assignment for LaTeX macros; listingsutf8:
(partially) extends the listings package to UTF-8 encoding;
ltxcmds: exports some utility macros from the LaTeX kernel into
a separate namespace and also provides them for other formats
such as plain-TeX; luacolor: implements colour support based on
LuaTeX's node attributes; luatex: utilises new and extended
features and resources that LuaTeX provides; magicnum: allows
to access magic numbers by a hierarchical name system;
makerobust: make a command robust; pagegrid: prints a page grid
in the background; pagesel: select pages of a document for
output; pdfcolfoot: using pdftex's color stack for footnotes;
pdfcol: macros for setting and maintaining new color stacks;
pdfcolmk: PDFTeX COLour MarK -- fake a PDFTeX colour stack
using marks (not needed for PDFTeX 1.40.0 and later);
pdfcolparallel: fixes colour problems in package parallel;
pdfcolparcolumns: fixes colour problems in package parcolumns;
pdfcrypt: setting PDF encryption; pdfescape: pdfTeX's escape
features using TeX or e-TeX; pdflscape: landscape pages in PDF;
pdfrender: control PDF rendering modes; pdftexcmds: provide
PDFTeX primitives missing in LuaTeX; picture: dimens for
picture macros; pmboxdraw: poor man's box drawing characters;
protecteddef: define a command that protected against
expansion; refcount: using the numeric values of references;
rerunfilecheck: checksum based rerun checks on auxiliary files;
resizegather: automatically resize overly large equations;
rotchiffre: performs simple rotation cyphers; scrindex:
redefines environment 'theindex' of package 'index', if a class
from KOMA-Script is loaded; selinput: select the input encoding
by specifying pairs of input characters and their glyph names;
setouterhbox: set \hbox in outer horizontal mode; settobox:
getting box sizes; soulutf8: extends package soul and adds some
support for UTF-8; stackrel: extensions of the \stackrel
command; stampinclude: selects the files for \include by
inspecting the timestamp of the .aux file(s); stringenc:
provides \StringEncodingConvert for converting a string between
different encodings; tabularht: tabulars with height
specification; tabularkv: key value interface for tabular
parameters; telprint: print German telephone numbers;
thepdfnumber: canonical numbers for use in PDF files and
elsewhere; transparent: using a color stack for transparency
with pdftex; twoopt: commands with two optional arguments;
uniquecounter: provides unlimited unique counter; zref: a
proposed new reference system. Each of the packages is
represented by two files, a .dtx (documented source) and a PDF
file; the .ins file necessary for installation is extracted by
running the .dtx file with Plain TeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/oberdiek/oberdiek-bundle.bib
%{_texmfdistdir}/bibtex/bib/oberdiek/oberdiek-source.bib
%{_texmfdistdir}/scripts/oberdiek/luacolor-pre065.lua
%{_texmfdistdir}/scripts/oberdiek/luacolor.lua
%{_texmfdistdir}/scripts/oberdiek/magicnum.lua
%{_texmfdistdir}/scripts/oberdiek/oberdiek.luacolor-pre065.lua
%{_texmfdistdir}/scripts/oberdiek/oberdiek.luacolor.lua
%{_texmfdistdir}/scripts/oberdiek/oberdiek.luatex.lua
%{_texmfdistdir}/scripts/oberdiek/oberdiek.magicnum.lua
%{_texmfdistdir}/scripts/oberdiek/oberdiek.pdftexcmds.lua
%{_texmfdistdir}/scripts/oberdiek/pdfatfi.pl
%{_texmfdistdir}/scripts/oberdiek/pdftexcmds.lua
%{_texmfdistdir}/tex/generic/oberdiek/alphalph.sty
%{_texmfdistdir}/tex/generic/oberdiek/atbegshi.sty
%{_texmfdistdir}/tex/generic/oberdiek/bigintcalc.sty
%{_texmfdistdir}/tex/generic/oberdiek/bitset.sty
%{_texmfdistdir}/tex/generic/oberdiek/catchfile.sty
%{_texmfdistdir}/tex/generic/oberdiek/embedfile.sty
%{_texmfdistdir}/tex/generic/oberdiek/engord.sty
%{_texmfdistdir}/tex/generic/oberdiek/eolgrab.sty
%{_texmfdistdir}/tex/generic/oberdiek/etexcmds.sty
%{_texmfdistdir}/tex/generic/oberdiek/fibnum.sty
%{_texmfdistdir}/tex/generic/oberdiek/gettitlestring.sty
%{_texmfdistdir}/tex/generic/oberdiek/hobsub-generic.sty
%{_texmfdistdir}/tex/generic/oberdiek/hobsub-hyperref.sty
%{_texmfdistdir}/tex/generic/oberdiek/hobsub.sty
%{_texmfdistdir}/tex/generic/oberdiek/hologo.sty
%{_texmfdistdir}/tex/generic/oberdiek/hyphsubst.sty
%{_texmfdistdir}/tex/generic/oberdiek/iflang.sty
%{_texmfdistdir}/tex/generic/oberdiek/ifpdf.sty
%{_texmfdistdir}/tex/generic/oberdiek/ifvtex.sty
%{_texmfdistdir}/tex/generic/oberdiek/infwarerr.sty
%{_texmfdistdir}/tex/generic/oberdiek/intcalc.sty
%{_texmfdistdir}/tex/generic/oberdiek/kvdefinekeys.sty
%{_texmfdistdir}/tex/generic/oberdiek/kvsetkeys.sty
%{_texmfdistdir}/tex/generic/oberdiek/ltxcmds.sty
%{_texmfdistdir}/tex/generic/oberdiek/luatex-loader.sty
%{_texmfdistdir}/tex/generic/oberdiek/luatex.sty
%{_texmfdistdir}/tex/generic/oberdiek/magicnum.sty
%{_texmfdistdir}/tex/generic/oberdiek/mleftright.sty
%{_texmfdistdir}/tex/generic/oberdiek/pdfcol.sty
%{_texmfdistdir}/tex/generic/oberdiek/pdfcrypt.sty
%{_texmfdistdir}/tex/generic/oberdiek/pdfescape.sty
%{_texmfdistdir}/tex/generic/oberdiek/pdfrender.sty
%{_texmfdistdir}/tex/generic/oberdiek/pdftexcmds.sty
%{_texmfdistdir}/tex/generic/oberdiek/protecteddef.sty
%{_texmfdistdir}/tex/generic/oberdiek/rotchiffre.sty
%{_texmfdistdir}/tex/generic/oberdiek/se-ascii-print.def
%{_texmfdistdir}/tex/generic/oberdiek/se-ascii.def
%{_texmfdistdir}/tex/generic/oberdiek/se-clean7bit.def
%{_texmfdistdir}/tex/generic/oberdiek/se-cp1250.def
%{_texmfdistdir}/tex/generic/oberdiek/se-cp1251.def
%{_texmfdistdir}/tex/generic/oberdiek/se-cp1252.def
%{_texmfdistdir}/tex/generic/oberdiek/se-cp1257.def
%{_texmfdistdir}/tex/generic/oberdiek/se-cp437.def
%{_texmfdistdir}/tex/generic/oberdiek/se-cp850.def
%{_texmfdistdir}/tex/generic/oberdiek/se-cp852.def
%{_texmfdistdir}/tex/generic/oberdiek/se-cp855.def
%{_texmfdistdir}/tex/generic/oberdiek/se-cp858.def
%{_texmfdistdir}/tex/generic/oberdiek/se-cp865.def
%{_texmfdistdir}/tex/generic/oberdiek/se-cp866.def
%{_texmfdistdir}/tex/generic/oberdiek/se-dec-mcs.def
%{_texmfdistdir}/tex/generic/oberdiek/se-iso-8859-1.def
%{_texmfdistdir}/tex/generic/oberdiek/se-iso-8859-10.def
%{_texmfdistdir}/tex/generic/oberdiek/se-iso-8859-11.def
%{_texmfdistdir}/tex/generic/oberdiek/se-iso-8859-13.def
%{_texmfdistdir}/tex/generic/oberdiek/se-iso-8859-14.def
%{_texmfdistdir}/tex/generic/oberdiek/se-iso-8859-15.def
%{_texmfdistdir}/tex/generic/oberdiek/se-iso-8859-16.def
%{_texmfdistdir}/tex/generic/oberdiek/se-iso-8859-2.def
%{_texmfdistdir}/tex/generic/oberdiek/se-iso-8859-3.def
%{_texmfdistdir}/tex/generic/oberdiek/se-iso-8859-4.def
%{_texmfdistdir}/tex/generic/oberdiek/se-iso-8859-5.def
%{_texmfdistdir}/tex/generic/oberdiek/se-iso-8859-6.def
%{_texmfdistdir}/tex/generic/oberdiek/se-iso-8859-7.def
%{_texmfdistdir}/tex/generic/oberdiek/se-iso-8859-8.def
%{_texmfdistdir}/tex/generic/oberdiek/se-iso-8859-9.def
%{_texmfdistdir}/tex/generic/oberdiek/se-koi8-r.def
%{_texmfdistdir}/tex/generic/oberdiek/se-mac-centeuro.def
%{_texmfdistdir}/tex/generic/oberdiek/se-mac-cyrillic.def
%{_texmfdistdir}/tex/generic/oberdiek/se-mac-roman.def
%{_texmfdistdir}/tex/generic/oberdiek/se-nextstep.def
%{_texmfdistdir}/tex/generic/oberdiek/se-pdfdoc.def
%{_texmfdistdir}/tex/generic/oberdiek/se-utf16le.def
%{_texmfdistdir}/tex/generic/oberdiek/se-utf32be.def
%{_texmfdistdir}/tex/generic/oberdiek/se-utf32le.def
%{_texmfdistdir}/tex/generic/oberdiek/se-utf8.def
%{_texmfdistdir}/tex/generic/oberdiek/setouterhbox.sty
%{_texmfdistdir}/tex/generic/oberdiek/soulutf8.sty
%{_texmfdistdir}/tex/generic/oberdiek/stringenc.sty
%{_texmfdistdir}/tex/generic/oberdiek/telprint.sty
%{_texmfdistdir}/tex/generic/oberdiek/thepdfnumber.sty
%{_texmfdistdir}/tex/generic/oberdiek/uniquecounter.sty
%{_texmfdistdir}/tex/latex/oberdiek/accsupp-dvipdfm.def
%{_texmfdistdir}/tex/latex/oberdiek/accsupp-dvips.def
%{_texmfdistdir}/tex/latex/oberdiek/accsupp-pdftex.def
%{_texmfdistdir}/tex/latex/oberdiek/accsupp.sty
%{_texmfdistdir}/tex/latex/oberdiek/aliascnt.sty
%{_texmfdistdir}/tex/latex/oberdiek/askinclude.sty
%{_texmfdistdir}/tex/latex/oberdiek/atenddvi.sty
%{_texmfdistdir}/tex/latex/oberdiek/atfi-dvipdfmx.def
%{_texmfdistdir}/tex/latex/oberdiek/atfi-dvips.def
%{_texmfdistdir}/tex/latex/oberdiek/atfi-pdftex.def
%{_texmfdistdir}/tex/latex/oberdiek/attachfile2.sty
%{_texmfdistdir}/tex/latex/oberdiek/atveryend.sty
%{_texmfdistdir}/tex/latex/oberdiek/auxhook.sty
%{_texmfdistdir}/tex/latex/oberdiek/bkm-dvipdfm.def
%{_texmfdistdir}/tex/latex/oberdiek/bkm-dvips.def
%{_texmfdistdir}/tex/latex/oberdiek/bkm-dvipsone.def
%{_texmfdistdir}/tex/latex/oberdiek/bkm-pdftex.def
%{_texmfdistdir}/tex/latex/oberdiek/bkm-textures.def
%{_texmfdistdir}/tex/latex/oberdiek/bkm-vtex.def
%{_texmfdistdir}/tex/latex/oberdiek/bmpsize-base.sty
%{_texmfdistdir}/tex/latex/oberdiek/bmpsize-dvipdfm.def
%{_texmfdistdir}/tex/latex/oberdiek/bmpsize-dvipdfmx.def
%{_texmfdistdir}/tex/latex/oberdiek/bmpsize-dvips.def
%{_texmfdistdir}/tex/latex/oberdiek/bmpsize-test.tex
%{_texmfdistdir}/tex/latex/oberdiek/bmpsize.sty
%{_texmfdistdir}/tex/latex/oberdiek/bookmark.sty
%{_texmfdistdir}/tex/latex/oberdiek/centernot.sty
%{_texmfdistdir}/tex/latex/oberdiek/chemarr.sty
%{_texmfdistdir}/tex/latex/oberdiek/classlist.sty
%{_texmfdistdir}/tex/latex/oberdiek/colonequals.sty
%{_texmfdistdir}/tex/latex/oberdiek/dtx-attach.sty
%{_texmfdistdir}/tex/latex/oberdiek/dvipscol.sty
%{_texmfdistdir}/tex/latex/oberdiek/enparen.sty
%{_texmfdistdir}/tex/latex/oberdiek/epstopdf-base.sty
%{_texmfdistdir}/tex/latex/oberdiek/epstopdf.sty
%{_texmfdistdir}/tex/latex/oberdiek/flags.sty
%{_texmfdistdir}/tex/latex/oberdiek/grfext.sty
%{_texmfdistdir}/tex/latex/oberdiek/grffile.sty
%{_texmfdistdir}/tex/latex/oberdiek/holtxdoc.sty
%{_texmfdistdir}/tex/latex/oberdiek/hopatch.sty
%{_texmfdistdir}/tex/latex/oberdiek/hycolor.sty
%{_texmfdistdir}/tex/latex/oberdiek/hypbmsec.sty
%{_texmfdistdir}/tex/latex/oberdiek/hypcap.sty
%{_texmfdistdir}/tex/latex/oberdiek/hypdestopt.sty
%{_texmfdistdir}/tex/latex/oberdiek/hypdoc.sty
%{_texmfdistdir}/tex/latex/oberdiek/hypgotoe.sty
%{_texmfdistdir}/tex/latex/oberdiek/ifdraft.sty
%{_texmfdistdir}/tex/latex/oberdiek/inputenx.sty
%{_texmfdistdir}/tex/latex/oberdiek/ix-alias.def
%{_texmfdistdir}/tex/latex/oberdiek/ix-math.def
%{_texmfdistdir}/tex/latex/oberdiek/ix-name.def
%{_texmfdistdir}/tex/latex/oberdiek/ix-slot.def
%{_texmfdistdir}/tex/latex/oberdiek/ix-uc.def
%{_texmfdistdir}/tex/latex/oberdiek/ix-utf8enc.dfu
%{_texmfdistdir}/tex/latex/oberdiek/kvoptions-patch.sty
%{_texmfdistdir}/tex/latex/oberdiek/kvoptions.sty
%{_texmfdistdir}/tex/latex/oberdiek/letltxmacro.sty
%{_texmfdistdir}/tex/latex/oberdiek/listingsutf8.sty
%{_texmfdistdir}/tex/latex/oberdiek/luacolor.sty
%{_texmfdistdir}/tex/latex/oberdiek/makerobust.sty
%{_texmfdistdir}/tex/latex/oberdiek/pagegrid.sty
%{_texmfdistdir}/tex/latex/oberdiek/pagesel.sty
%{_texmfdistdir}/tex/latex/oberdiek/pdfcolfoot.sty
%{_texmfdistdir}/tex/latex/oberdiek/pdfcolmk.sty
%{_texmfdistdir}/tex/latex/oberdiek/pdfcolparallel.sty
%{_texmfdistdir}/tex/latex/oberdiek/pdfcolparcolumns.sty
%{_texmfdistdir}/tex/latex/oberdiek/pdflscape.sty
%{_texmfdistdir}/tex/latex/oberdiek/picture.sty
%{_texmfdistdir}/tex/latex/oberdiek/pmboxdraw.sty
%{_texmfdistdir}/tex/latex/oberdiek/pmboxdrawenc.dfu
%{_texmfdistdir}/tex/latex/oberdiek/refcount.sty
%{_texmfdistdir}/tex/latex/oberdiek/rerunfilecheck.sty
%{_texmfdistdir}/tex/latex/oberdiek/resizegather.sty
%{_texmfdistdir}/tex/latex/oberdiek/scrindex.sty
%{_texmfdistdir}/tex/latex/oberdiek/selinput.sty
%{_texmfdistdir}/tex/latex/oberdiek/settobox.sty
%{_texmfdistdir}/tex/latex/oberdiek/stackrel.sty
%{_texmfdistdir}/tex/latex/oberdiek/stampinclude.sty
%{_texmfdistdir}/tex/latex/oberdiek/tabularht.sty
%{_texmfdistdir}/tex/latex/oberdiek/tabularkv.sty
%{_texmfdistdir}/tex/latex/oberdiek/transparent.sty
%{_texmfdistdir}/tex/latex/oberdiek/twoopt.sty
%{_texmfdistdir}/tex/latex/oberdiek/x-ascii.def
%{_texmfdistdir}/tex/latex/oberdiek/x-atarist.def
%{_texmfdistdir}/tex/latex/oberdiek/x-cp1250.def
%{_texmfdistdir}/tex/latex/oberdiek/x-cp1251.def
%{_texmfdistdir}/tex/latex/oberdiek/x-cp1252.def
%{_texmfdistdir}/tex/latex/oberdiek/x-cp1255.def
%{_texmfdistdir}/tex/latex/oberdiek/x-cp1257.def
%{_texmfdistdir}/tex/latex/oberdiek/x-cp437.def
%{_texmfdistdir}/tex/latex/oberdiek/x-cp850.def
%{_texmfdistdir}/tex/latex/oberdiek/x-cp852.def
%{_texmfdistdir}/tex/latex/oberdiek/x-cp855.def
%{_texmfdistdir}/tex/latex/oberdiek/x-cp858.def
%{_texmfdistdir}/tex/latex/oberdiek/x-cp865.def
%{_texmfdistdir}/tex/latex/oberdiek/x-cp866.def
%{_texmfdistdir}/tex/latex/oberdiek/x-dec-mcs.def
%{_texmfdistdir}/tex/latex/oberdiek/x-iso-8859-1.def
%{_texmfdistdir}/tex/latex/oberdiek/x-iso-8859-10.def
%{_texmfdistdir}/tex/latex/oberdiek/x-iso-8859-13.def
%{_texmfdistdir}/tex/latex/oberdiek/x-iso-8859-14.def
%{_texmfdistdir}/tex/latex/oberdiek/x-iso-8859-15.def
%{_texmfdistdir}/tex/latex/oberdiek/x-iso-8859-16.def
%{_texmfdistdir}/tex/latex/oberdiek/x-iso-8859-2.def
%{_texmfdistdir}/tex/latex/oberdiek/x-iso-8859-3.def
%{_texmfdistdir}/tex/latex/oberdiek/x-iso-8859-4.def
%{_texmfdistdir}/tex/latex/oberdiek/x-iso-8859-5.def
%{_texmfdistdir}/tex/latex/oberdiek/x-iso-8859-8.def
%{_texmfdistdir}/tex/latex/oberdiek/x-iso-8859-9.def
%{_texmfdistdir}/tex/latex/oberdiek/x-koi8-r.def
%{_texmfdistdir}/tex/latex/oberdiek/x-mac-centeuro.def
%{_texmfdistdir}/tex/latex/oberdiek/x-mac-cyrillic.def
%{_texmfdistdir}/tex/latex/oberdiek/x-mac-roman.def
%{_texmfdistdir}/tex/latex/oberdiek/x-nextstep.def
%{_texmfdistdir}/tex/latex/oberdiek/x-verbatim.def
%{_texmfdistdir}/tex/latex/oberdiek/xcolor-patch.sty
%{_texmfdistdir}/tex/latex/oberdiek/zref-abspage.sty
%{_texmfdistdir}/tex/latex/oberdiek/zref-abspos.sty
%{_texmfdistdir}/tex/latex/oberdiek/zref-base.sty
%{_texmfdistdir}/tex/latex/oberdiek/zref-counter.sty
%{_texmfdistdir}/tex/latex/oberdiek/zref-dotfill.sty
%{_texmfdistdir}/tex/latex/oberdiek/zref-env.sty
%{_texmfdistdir}/tex/latex/oberdiek/zref-hyperref.sty
%{_texmfdistdir}/tex/latex/oberdiek/zref-lastpage.sty
%{_texmfdistdir}/tex/latex/oberdiek/zref-marks.sty
%{_texmfdistdir}/tex/latex/oberdiek/zref-nextpage.sty
%{_texmfdistdir}/tex/latex/oberdiek/zref-pageattr.sty
%{_texmfdistdir}/tex/latex/oberdiek/zref-pagelayout.sty
%{_texmfdistdir}/tex/latex/oberdiek/zref-perpage.sty
%{_texmfdistdir}/tex/latex/oberdiek/zref-runs.sty
%{_texmfdistdir}/tex/latex/oberdiek/zref-savepos.sty
%{_texmfdistdir}/tex/latex/oberdiek/zref-thepage.sty
%{_texmfdistdir}/tex/latex/oberdiek/zref-titleref.sty
%{_texmfdistdir}/tex/latex/oberdiek/zref-totpages.sty
%{_texmfdistdir}/tex/latex/oberdiek/zref-user.sty
%{_texmfdistdir}/tex/latex/oberdiek/zref-xr.sty
%{_texmfdistdir}/tex/latex/oberdiek/zref.sty
%doc %{_texmfdistdir}/doc/latex/oberdiek/accsupp-example1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/accsupp-example2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/accsupp.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/aliascnt.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/alphalph.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/askinclude.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/atbegshi-example1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/atbegshi-example2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/atbegshi.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/atenddvi.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/attachfile2.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/atveryend.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/auxhook.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/bigintcalc.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/bitset.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/bmpsize.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/bookmark-example.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/bookmark.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/catchfile.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/centernot.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/chemarr-example.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/chemarr.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/classlist.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/colonequals.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/dvipscol.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/embedfile-example-collection.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/embedfile-example-plain.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/embedfile.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/engord.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/enparen.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/eolgrab.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/epstopdf.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/etexcmds.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/example-mycolorsetup.sty
%doc %{_texmfdistdir}/doc/latex/oberdiek/example/eolgrab-example-env.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/example/eolgrab-example-ltx.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/example/eolgrab-example-sec.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/example/hologo-example.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/fibnum.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/flags.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/gettitlestring.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/grfext.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/grffile.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/hobsub.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/hologo.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/holtxdoc.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/hopatch.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/hycolor.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/hypbmsec.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/hypcap.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/hypdestopt.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/hypdoc.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/hypgotoe-example.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/hypgotoe.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/hyphsubst.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/ifdraft.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/iflang.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/ifpdf.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/ifvtex.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/infwarerr.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/inputenx-licrcmds.txt
%doc %{_texmfdistdir}/doc/latex/oberdiek/inputenx-utf8enc.txt
%doc %{_texmfdistdir}/doc/latex/oberdiek/inputenx.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/intcalc.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/kvdefinekeys.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/kvoptions.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/kvsetkeys-example.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/kvsetkeys.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/letltxmacro-showcases.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/letltxmacro.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/listingsutf8.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/ltxcmds.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/luacolor.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/luatex.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/magicnum.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/magicnum.txt
%doc %{_texmfdistdir}/doc/latex/oberdiek/makerobust-example.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/makerobust.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/mleftright.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/oberdiek.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/pagegrid.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/pagesel.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/pdfcol.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/pdfcolfoot.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/pdfcolmk.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/pdfcolparallel.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/pdfcolparcolumns.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/pdfcrypt.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/pdfescape.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/pdflscape.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/pdfrender.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/pdftexcmds.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/picture-example.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/picture.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/pmboxdraw.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/protecteddef.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/refcount.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/rerunfilecheck-example.cfg
%doc %{_texmfdistdir}/doc/latex/oberdiek/rerunfilecheck.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/resizegather.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/rotchiffre.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/scrindex-example1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/scrindex-example2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/scrindex.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/selinput.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/setouterhbox-example.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/setouterhbox.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/settobox-example.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/settobox.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/soulutf8.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/stackrel.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/stampinclude.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/stringenc.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/tabularht-example1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/tabularht-example2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/tabularht.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/tabularkv-example.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/tabularkv.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/telprint.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/ExtractRotate.java
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/accsupp-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/alphalph-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/alphalph-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/alphalph-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-a.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-b.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-c.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-test10.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-test11.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-test12.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-test13.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-test14.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-test15.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-test16.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-test17.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-test18.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-test19.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-test20.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-test21.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-test22.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-test23.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-test24.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-test4.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-test5.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-test6.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-test7.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-test8.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/askinclude-test9.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/atbegshi-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/atbegshi-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/atbegshi-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/atveryend-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/bigintcalc-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/bigintcalc-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/bigintcalc-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/bitset-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/bitset-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/bitset-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/catchfile-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/catchfile-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/catchfile-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/embedfile-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/embedfile-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/embedfile-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/embedfile-test4.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/engord-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/eolgrab-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/eolgrab-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/epstopdf-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/etexcmds-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/etexcmds-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/etexcmds-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/etexcmds-test4.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/fibnum-test-calc.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/fibnum-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/gettitlestring-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/gettitlestring-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/grfext-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/grfext-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/grffile-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/hobsub-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/hologo-test-list.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/hologo-test-spacefactor.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/hologo-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/hopatch-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/hopatch-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/hycolor-test-xcol1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/hycolor-test-xcol2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/hycolor-test-xcol3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/hycolor-test-xcol4.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/hycolor-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/hycolor-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/hycolor-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/hyphsubst-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/hyphsubst-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/iflang-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/iflang-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/iflang-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/iflang-test4.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/iflang-test5.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/ifpdf-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/ifvtex-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/infwarerr-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/infwarerr-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/infwarerr-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/intcalc-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/intcalc-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/intcalc-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/intcalc-test4.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/kvdefinekeys-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/kvoptions-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/kvoptions-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/kvoptions-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/kvoptions-test4.sty
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/kvoptions-test4.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/kvsetkeys-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/kvsetkeys-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/kvsetkeys-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/kvsetkeys-test4.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/letltxmacro-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/letltxmacro-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/listingsutf8-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/listingsutf8-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/listingsutf8-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/listingsutf8-test4.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/listingsutf8-test5.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/ltxcmds-test-carcdr.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/ltxcmds-test-gobble.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/ltxcmds-test-ifboxempty.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/ltxcmds-test-ifempty.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/ltxcmds-test-nextchar.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/ltxcmds-test-zapspace.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/ltxcmds-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/luacolor-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/luacolor-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/luacolor-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/luatex-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/luatex-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/luatex-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/luatex-test4.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/luatex-test5.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/magicnum-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/magicnum-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/magicnum-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/magicnum-test4.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/mleftright-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pagegrid-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdfcol-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdfcol-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdfcol-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdfcol-test4.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdfcolfoot-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdfcolparallel-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdfcolparcolumns-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdfescape-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdfescape-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdfescape-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdfescape-test4.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdfescape-test5.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdfescape-test6.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdflscape-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdflscape-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdflscape-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdflscape-test4.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdflscape-test5.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdflscape-test6.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdflscape-test6.txt
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdfrender-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdfrender-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdfrender-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdfrender-test4.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdfrender-test5.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdftexcmds-test-escape.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdftexcmds-test-shell.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdftexcmds-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pdftexcmds-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/pmboxdraw-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/protecteddef-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/protecteddef-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/refcount-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/refcount-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/refcount-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/refcount-test4.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/refcount-test5.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/rerunfilecheck-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/resizegather-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/rotchiffre-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/rotchiffre-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/selinput-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/selinput-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/selinput-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/selinput-test4.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/selinput-test5.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/setouterhbox-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/setouterhbox-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/soulutf8-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/soulutf8-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/soulutf8-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/soulutf8-test4.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/soulutf8-test5.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/stringenc-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/stringenc-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/telprint-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/thepdfnumber-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/thepdfnumber-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/thepdfnumber-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/uniquecounter-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/uniquecounter-test2.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/uniquecounter-test3.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/zref-test-base.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/zref-test-runs.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/zref-test-titleref-memoir.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/test/zref-test1.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/thepdfnumber.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/transparent-example.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/transparent.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/twoopt.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/uniquecounter-example.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/uniquecounter.pdf
%doc %{_texmfdistdir}/doc/latex/oberdiek/zref-example-lastpage.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/zref-example-nextpage.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/zref-example.tex
%doc %{_texmfdistdir}/doc/latex/oberdiek/zref.pdf
#- source
%doc %{_texmfdistdir}/source/latex/oberdiek/accsupp.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/aliascnt.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/alphalph.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/askinclude.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/atbegshi.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/atenddvi.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/attachfile2.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/atveryend.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/auxhook.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/bigintcalc.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/bitset.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/bmpsize.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/bookmark.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/accsupp.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/aliascnt.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/alphalph.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/askinclude.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/atbegshi.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/atenddvi.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/attachfile2.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/atveryend.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/auxhook.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/bigintcalc.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/bitset.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/bmpsize.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/bookmark.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/catchfile.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/centernot.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/chemarr.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/classlist.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/colonequals.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/dvipscol.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/embedfile.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/engord.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/eolgrab.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/epstopdf-pkg.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/etexcmds.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/flags.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/gettitlestring.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/grfext.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/grffile.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/hobsub.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/hologo.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/holtxdoc.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/hopatch.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/hycolor.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/hypbmsec.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/hypcap.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/hypdestopt.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/hypdoc.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/hypgotoe.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/hyphsubst.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/ifdraft.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/iflang.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/ifluatex.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/ifpdf.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/ifvtex.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/infwarerr.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/inputenx.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/intcalc.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/kvdefinekeys.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/kvoptions.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/kvsetkeys.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/letltxmacro.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/listingsutf8.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/ltxcmds.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/luacolor.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/luatex.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/magicnum.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/makerobust.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/mleftright.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/pagegrid.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/pagesel.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/pdfcol.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/pdfcolfoot.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/pdfcolmk.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/pdfcolparallel.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/pdfcolparcolumns.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/pdfcrypt.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/pdfescape.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/pdflscape.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/pdfrender.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/pdftexcmds.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/picture.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/pmboxdraw.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/protecteddef.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/refcount.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/rerunfilecheck.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/resizegather.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/rotchiffre.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/scrindex.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/selinput.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/setouterhbox.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/settobox.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/soulutf8.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/stackrel.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/stampinclude.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/stringenc.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/tabularht.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/tabularkv.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/telprint.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/transparent.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/twoopt.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/uniquecounter.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catalogue/zref.xml
%doc %{_texmfdistdir}/source/latex/oberdiek/catchfile.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/centernot.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/chemarr.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/classlist.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/colonequals.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/dvipscol.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/embedfile.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/engord.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/enparen.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/eolgrab.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/epstopdf.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/etexcmds.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/fibnum.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/flags.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/gettitlestring.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/grfext.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/grffile.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/hobsub.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/hologo-eroux.patch
%doc %{_texmfdistdir}/source/latex/oberdiek/hologo.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/holtxdoc.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/hopatch.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/hycolor.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/hypbmsec.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/hypcap.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/hypdestopt.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/hypdoc.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/hypgotoe.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/hyphsubst.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/ifdraft.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/iflang.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/ifpdf.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/ifvtex.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/infwarerr.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/inputenx.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/intcalc.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/kvdefinekeys.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/kvoptions.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/kvsetkeys.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/letltxmacro.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/listingsutf8.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/ltxcmds.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/luacolor.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/luatex.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/magicnum.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/makerobust.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/mleftright.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/oberdiek.ins
%doc %{_texmfdistdir}/source/latex/oberdiek/oberdiek.tex
%doc %{_texmfdistdir}/source/latex/oberdiek/pagegrid.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/pagesel.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/pdfcol.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/pdfcolfoot.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/pdfcolmk.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/pdfcolparallel.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/pdfcolparcolumns.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/pdfcrypt.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/pdfescape.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/pdflscape.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/pdfrender.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/pdftexcmds-eroux.patch
%doc %{_texmfdistdir}/source/latex/oberdiek/pdftexcmds.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/picture.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/pmboxdraw.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/protecteddef.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/readme-ctan.txt
%doc %{_texmfdistdir}/source/latex/oberdiek/refcount.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/rerunfilecheck.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/resizegather.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/rotchiffre.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/scrindex.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/selinput.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/setouterhbox.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/settobox.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/soulutf8.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/stackrel.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/stampinclude.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/stringenc.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/tabularht.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/tabularkv.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/telprint.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/thepdfnumber.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/transparent.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/twoopt.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/uniquecounter.dtx
%doc %{_texmfdistdir}/source/latex/oberdiek/zref.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex scripts tex doc source %{buildroot}%{_texmfdistdir}
