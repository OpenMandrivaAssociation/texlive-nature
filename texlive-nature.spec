# revision 21819
# category Package
# catalog-ctan /macros/latex/contrib/nature
# catalog-date 2008-09-15 13:49:48 +0200
# catalog-license noinfo
# catalog-version 1.0
Name:		texlive-nature
Version:	1.0
Release:	8
Summary:	Prepare papers for the journal Nature
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nature
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nature.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nature.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 754249
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719102
- texlive-nature
- texlive-nature
- texlive-nature
- texlive-nature

