%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	DB_Lock
Summary:	Tie::DB_Lock perl module
Summary(pl):	Modu� perla Tie::DB_Lock
Name:		perl-Tie-DB_Lock
Version:	0.05
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie::DB_Lock perl module.

%description -l pl
Modu� perla Tie::DB_Lock.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Tie/DB_Lock.pm
%{_mandir}/man3/*
