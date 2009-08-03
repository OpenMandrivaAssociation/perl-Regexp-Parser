%define upstream_name    Regexp-Parser
%define upstream_version 0.20

%define _requires_exceptions perl(Regexp::Parser::Diagnostics)\\|perl(Regexp::Parser::Handlers)\\|perl(Regexp::Parser::Objects)

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Regexp::Parser - base class for parsing regexes
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Regexp/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%dir %{perl_vendorlib}/Regexp/Parser
%dir %{perl_vendorlib}/Perl6/Rule
%{perl_vendorlib}/Regexp/Parser/*
%{perl_vendorlib}/Regexp/Parser.pm
%{perl_vendorlib}/Perl6/Rule/Parser.pm
%{_mandir}/*/*
