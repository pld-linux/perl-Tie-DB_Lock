#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Tie
%define		pnam	DB_Lock
Summary:	Tie::DB_Lock Perl module - ties hashes to databases using shared and exclusive locks
Summary(pl.UTF-8):	Moduł Perla Tie::DB_Lock - związanie haszy z bazami danych przy użyciu blokad
Name:		perl-Tie-DB_Lock
Version:	0.07
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1f1c9d69e6064c53a5df9fe4072f62e5
URL:		http://search.cpan.org/dist/Tie-DB_Lock/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a front-end for the DB_File package. It ties hashes to
databases using shared and exlusive locks.

%description -l pl.UTF-8
Ten pakiet jest frontendem do DB_File. Wiąże hasze z bazami danych
przy użyciu blokad współdzielonych i wyłącznych.

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
%{perl_vendorlib}/Tie/DB_Lock.pm
%{_mandir}/man3/*
