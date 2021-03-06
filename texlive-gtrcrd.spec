# revision 32484
# category Package
# catalog-ctan /macros/latex/contrib/gtrcrd
# catalog-date 2013-12-25 08:30:41 +0100
# catalog-license lppl1.3
# catalog-version 1.1
Name:		texlive-gtrcrd
Version:	1.1
Release:	7
Summary:	Add chords to lyrics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gtrcrd
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gtrcrd.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gtrcrd.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the means to specify guitar chords to be
played with each part of the lyrics of a song. The syntax of
the macros reduces the chance of failing to provide a chord
where one is needed, and the structure of the macros ensures
that the chord specification appears immediately above the
start of the lyric.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gtrcrd/gtrcrd.sty
%doc %{_texmfdistdir}/doc/latex/gtrcrd/README
%doc %{_texmfdistdir}/doc/latex/gtrcrd/gtrcrd-doc.pdf
%doc %{_texmfdistdir}/doc/latex/gtrcrd/gtrcrd-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
