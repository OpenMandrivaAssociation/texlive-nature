Name:		texlive-nature
Version:	1.0
Release:	1
Summary:	Prepare papers for the journal Nature
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nature
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nature.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nature.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Nature does not accept papers in LaTeX, but it does accept PDF.
This class and BibTeX style provide what seems to be necessary
to produce papers in a format acceptable to the publisher.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/nature/naturemag.bst
%{_texmfdistdir}/tex/latex/nature/nature.cls
%doc %{_texmfdistdir}/doc/latex/nature/README
%doc %{_texmfdistdir}/doc/latex/nature/nature-template.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
