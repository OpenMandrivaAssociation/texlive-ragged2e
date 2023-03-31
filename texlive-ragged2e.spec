Name:		texlive-ragged2e
Version:	65008
Release:	2
Summary:	Alternative versions of "ragged"-type commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ragged2e
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ragged2e.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ragged2e.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ragged2e.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines new commands \Centering, \RaggedLeft, and
\RaggedRight and new environments Center, FlushLeft, and
FlushRight, which set ragged text and are easily configurable
to allow hyphenation (the corresponding commands in LaTeX, all
of whose names are lower-case, prevent hyphenation altogether).

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/ragged2e
%{_texmfdistdir}/tex/latex/ragged2e
%doc %{_texmfdistdir}/doc/latex/ragged2e

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
