%define upstream_name Net-MAC
%define upstream_version 2.103622

Summary:	Perl extension for representing and manipulating MAC addresses
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
License:	LGPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/Net-MAC/
Source: 	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Perl extension for representing and manipulating MAC addresses.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

