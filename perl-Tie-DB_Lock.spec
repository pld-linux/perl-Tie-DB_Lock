%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	DB_Lock
Summary:	Tie::DB_Lock - ties hashes to databases using shared and exclusive locks
Summary(pl):	Modu� Tie::DB_Lock - wi���cy hasze z bazami danych przy u�yciu blokad
Name:		perl-Tie-DB_Lock
Version:	0.07
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1f1c9d69e6064c53a5df9fe4072f62e5
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a front-end for the DB_File package. It ties hashes to
databases using shared and exlusive locks.

%description -l pl
Ten pakiet jest frontendem do DB_File. Wi��e hasze z bazami danych
przy u�yciu blokad wsp�dzielonych i wy��cznych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Tie/DB_Lock.pm
%{_mandir}/man3/*
