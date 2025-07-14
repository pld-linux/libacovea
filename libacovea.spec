Summary:	ACOVEA (Analysis of Compiler Options via Evolutionary Algorithm)
Name:		libacovea
Version:	5.1.1
Release:	3
License:	GPL
Group:		Libraries
URL:		http://www.coyotegulch.com/products/acovea/index.html
Source0:	http://www.coyotegulch.com/distfiles/%{name}-%{version}.tar.gz
# Source0-md5:	e3bfa6b782205bad083ba58a8b882158
Patch0:		%{name}-evocosm-latest.patch
Patch1:		%{name}-libs.patch
BuildRequires:	expat-devel
BuildRequires:	libcoyotl-devel >= 3.1.0
BuildRequires:	libevocosm-devel >= 3.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ACOVEA (Analysis of Compiler Options via Evolutionary Algorithm)
implements a genetic algorithm to find the "best" options for
compiling programs with the GNU Compiler Collection (GCC) C and C++
compilers. "Best", in this context, is defined as those options that
produce the fastest executable program from a given source code.
Acovea is a C++ framework that can be extended to test other
programming languages and non-GCC compilers.

%package devel
Summary:	libacovea headers and documentation
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
libacovea libraries headers and documentation.

%package static
Summary:	libacovea static libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
libacovea static libraries.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/lib*.la
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/benchmarks
%{_datadir}/%{name}/benchmarks/*
%dir %{_datadir}/%{name}/config
%{_datadir}/%{name}/config/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
