%global tl_name gtrcrd
%global tl_revision 32484

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Add chords to lyrics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gtrcrd
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gtrcrd.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gtrcrd.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the means to specify guitar chords to be played
with each part of the lyrics of a song. The syntax of the macros reduces
the chance of failing to provide a chord where one is needed, and the
structure of the macros ensures that the chord specification appears
immediately above the start of the lyric.

