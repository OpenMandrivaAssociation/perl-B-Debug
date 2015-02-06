%define upstream_name    B-Debug
%define upstream_version 1.16

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    4

Summary:    Walk Perl syntax tree, printing debug info about ops
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/B/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(B)
BuildRequires: perl(Test::More)
BuildRequires: perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
See _ext/B/README_ and the newer the B::Concise manpage, the B::Terse
manpage.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*



%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.160.0-2mdv2011.0
+ Revision: 680509
- mass rebuild

* Mon Nov 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.160.0-1mdv2011.0
+ Revision: 595074
- update to new version 1.16

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.120.0-2mdv2011.0
+ Revision: 555683
- rebuild

* Thu Feb 11 2010 Jérôme Quelin <jquelin@mandriva.org> 1.120.0-1mdv2010.1
+ Revision: 504069
- update to 1.12

* Sun Jul 26 2009 Jérôme Quelin <jquelin@mandriva.org> 1.110.0-1mdv2010.0
+ Revision: 400258
- remove noarch
- using %%perl_convert_version
- fixed license field

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 1.11-1mdv2010.0
+ Revision: 374337
- import perl-B-Debug


* Mon May 11 2009 cpan2dist 1.11-1mdv
- initial mdv release, generated with cpan2dist

