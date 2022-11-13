Name:		texlive-nature
Version:	21819
Release:	1
Summary:	Prepare papers for the journal Nature
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nature
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nature.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nature.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Nature does not accept papers in LaTeX, but it does accept PDF.
This class and BibTeX style provide what seems to be necessary
to produce papers in a format acceptable to the publisher.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/nature/naturemag.bst
%{_texmfdistdir}/tex/latex/nature/nature.cls
%doc %{_texmfdistdir}/doc/latex/nature/README
%doc %{_texmfdistdir}/doc/latex/nature/nature-template.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
