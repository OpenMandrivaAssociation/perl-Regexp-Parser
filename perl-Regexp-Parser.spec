%define _requires_exceptions perl(Regexp::Parser::Diagnostics)\\|perl(Regexp::Parser::Handlers)\\|perl(Regexp::Parser::Objects)

%define real_name Regexp-Parser

Summary:	Regexp::Parser - base class for parsing regexes
Name:		perl-%{real_name}
Version:	0.20
Release: %mkrel 4
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Regexp/%{real_name}-%{version}.tar.bz2
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
%setup -q -n %{real_name}-%{version} 

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

