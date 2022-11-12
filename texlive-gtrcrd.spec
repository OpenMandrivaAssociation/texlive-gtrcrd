Name:		texlive-gtrcrd
Version:	32484
Release:	1
Summary:	Add chords to lyrics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gtrcrd
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gtrcrd.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gtrcrd.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
