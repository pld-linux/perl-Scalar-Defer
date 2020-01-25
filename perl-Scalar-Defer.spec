#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Scalar
%define	pnam	Defer
Summary:	Scalar::Defer - Lazy evaluation in Perl
Summary(pl.UTF-8):	Scalar::Defer - leniwe obliczenia w Perlu
Name:		perl-Scalar-Defer
Version:	0.23
Release:	1
License:	Mit
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Scalar/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	df4e9d0b8ca20274376a032d40703c57
URL:		http://search.cpan.org/dist/Scalar-Defer/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-InsideOut
BuildRequires:	perl-Exporter-Lite
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module exports two functions, defer and lazy, for constructing
values that are evaluated on demand. It also exports a force function
to force evaluation of a deferred value.

%description -l pl.UTF-8
Ten moduł eksportuje dwie funkcje: defer i lazy, służące do tworzenia
wartości obliczanych na żądanie. Eksportuje także funkcję force do
wymuszenia obliczenia opóźnionej wartości.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Scalar/*.pm
%{_mandir}/man3/*
