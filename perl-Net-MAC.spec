%define upstream_name Net-MAC
Summary:	Perl extension for representing and manipulating MAC addresses
Name:		perl-%{upstream_name}
Version:	2.103622
Release:	6
License:	LGPL
Group:		Development/Perl
URL:		https://github.com/ollyg/Net-MAC/wiki
Source: 	https://cpan.metacpan.org/authors/id/O/OL/OLIVER/Net-MAC-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-devel

%description
Perl extension for representing and manipulating MAC addresses.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc Changes MANIFEST META.yml README
%{_mandir}/man3/Net::MAC.3pm*
%{perl_vendorlib}/Net/MAC.pm



%changelog
* Tue Sep 27 2011 Leonardo Coelho <leonardoc@mandriva.com> 2.103622-1mdv2012.0
+ Revision: 701555
- first mandriva version
- Created package structure for 'perl-Net-MAC'.

