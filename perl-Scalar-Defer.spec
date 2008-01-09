#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Scalar
%define	pnam	Defer
Summary:	Scalar::Defer - Lazy evaluation in Perl
#Summary(pl):	
Name:		perl-Scalar-Defer
Version:	0.14
Release:	1
License:	Mit
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/A/AU/AUDREYT/Scalar-Defer-0.14.tar.gz
# Source0-md5:	6fef0daeaabb7271480ccd04f91b56eb
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Class::InsideOut)
BuildRequires:	perl(Exporter::Lite)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module exports two functions, defer and lazy, for constructing
values that are evaluated on demand. It also exports a force function
to force evaluation of a deferred value.

Takes a block or a code reference, and returns a deferred value.
Each time that value is demanded, the block is evaluated again to
yield a fresh result.

Like defer, except the value is computed at most once. Subsequent
evaluation will simply use the cached result.

# %description -l pl
# TODO

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
#%%{perl_vendorlib}/Scalar/Defer
%{_mandir}/man3/*
