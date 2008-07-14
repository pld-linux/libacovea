Summary:	ACOVEA (Analysis of Compiler Options via Evolutionary Algorithm)
Name:		libacovea
Version:	5.1.1
Release:	1
License:	GPL
Group:		System Environment/Libraries
BuildRequires:  libcoyotl-devel >= 3.1.0
BuildRequires:	libevocosm >= 3.1.0
URL:		http://www.coyotegulch.com/products/libcoyotl/index.html
Source:		%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
ACOVEA (Analysis of Compiler Options via Evolutionary Algorithm) implements a genetic algorithm to find the "best" options for compiling programs with the GNU Compiler Collection (GCC) C and C++ compilers. "Best", in this context, is defined as those options that produce the fastest executable program from a given source code. Acovea is a C++ framework that can be extended to test other programming languages and non-GCC compilers.

%package devel
Summary:        libacovea headers and documentation
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
libacovea libraries headers and documentation.

%package static
Summary:        libacovea static libraries
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description static
libacovea static libraries.

%prep
%setup

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 0755)
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
