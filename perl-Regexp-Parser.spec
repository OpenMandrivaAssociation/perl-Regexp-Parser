%define upstream_name    Regexp-Parser
%define upstream_version 0.21

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Regexp::Parser::Diagnostics\\)|perl\\(Regexp::Parser::Handlers\\)|perl\\(Regexp::Parser::Objects\\)'
%else
%define _requires_exceptions perl(Regexp::Parser::Diagnostics)\\|perl(Regexp::Parser::Handlers)\\|perl(Regexp::Parser::Objects)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Regexp::Parser - base class for parsing regexes
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Regexp/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module parses regular expressions (regexes). Its default
"grammar" is Perl 5.8.4's regex set. Grammar is quoted because the
module does not so much define a grammar as let each matched node
state what it expects to match next, but there is not currently a
way of extracting a complete grammar. This may change in future
versions.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%dir %{perl_vendorlib}/Regexp/Parser
%dir %{perl_vendorlib}/Perl6/Rule
%{perl_vendorlib}/Regexp/Parser/*
%{perl_vendorlib}/Regexp/Parser.pm
%{perl_vendorlib}/Perl6/Rule/Parser.pm
%{_mandir}/*/*


%changelog
* Tue May 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.210.0-1mdv2011.0
+ Revision: 682145
- update to new version 0.21

* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.200.0-1mdv2010.0
+ Revision: 408043
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.20-7mdv2009.0
+ Revision: 258326
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.20-6mdv2009.0
+ Revision: 246404
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.20-4mdv2008.1
+ Revision: 136347
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 0.20-4mdv2008.0
+ Revision: 25099
- rebuild


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.20-3mdk
- Fix According to perl Policy
	- Source URL
- use mkrel

* Wed Jul 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.20-2mdk
- 0.20

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 0.10-2mdk
- BuildArch: noarch
- rule out some requires

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 0.10-1mdk
- initial Mandriva package

