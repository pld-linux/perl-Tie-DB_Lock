%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	DB_Lock
Summary:	Tie::DB_Lock - ties hashes to databases using shared and exclusive locks
Summary(pl):	Modu³ Tie::DB_Lock - wi±¿±cy hasze z bazami danych przy u¿yciu blokad
Name:		perl-Tie-DB_Lock
Version:	0.07
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a front-end for the DB_File package. It ties hashes to
databases using shared and exlusive locks.

%description -l pl
Ten pakiet jest frontendem do DB_File. Wi±¿e hasze z bazami danych
przy u¿yciu blokad wspó³dzielonych i wy³±cznych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Tie/DB_Lock.pm
%{_mandir}/man3/*
