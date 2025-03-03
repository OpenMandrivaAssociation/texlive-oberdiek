Name:		texlive-oberdiek
Version:	71916
Release:	1
Summary:	A bundle of packages submitted by Heiko Oberdiek
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/oberdiek
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oberdiek.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oberdiek.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oberdiek.source.r%{version}.tar.xz
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
%{_texmfdistdir}/bibtex/bib/oberdiek
%{_texmfdistdir}/tex/generic/oberdiek
%{_texmfdistdir}/tex/latex/oberdiek
%doc %{_texmfdistdir}/doc/latex/oberdiek
#- source
%doc %{_texmfdistdir}/source/latex/oberdiek

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
