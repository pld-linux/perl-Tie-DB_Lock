%include	/usr/lib/rpm/macros.perl
Summary:	Tie-DB_Lock perl module
Summary(pl):	Modu� perla Tie-DB_Lock
Name:		perl-Tie-DB_Lock
Version:	0.05
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Tie/Tie-DB_Lock-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie-DB_Lock perl module.

%description -l pl
Modu� perla Tie-DB_Lock.

%prep
%setup -q -n Tie-DB_Lock-%{version}

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
