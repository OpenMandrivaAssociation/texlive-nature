%global tl_name nature
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Prepare papers for the journal Nature
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nature
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nature.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nature.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Nature does not accept papers in LaTeX, but it does accept PDF. This
class and BibTeX style provide what seems to be necessary to produce
papers in a format acceptable to the publisher.

