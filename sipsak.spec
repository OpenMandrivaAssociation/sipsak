Summary:	SIP swiss army knife
Name:		sipsak
Version:	0.9.6
Release:	%mkrel 7
License:	GPL
Group:		Networking/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://sipsak.org/
Source0:	http://download.berlios.de/sipsak/%{name}-%{version}-1.tar.bz2
BuildRequires:	openssl-devel
BuildRequires:	ruli-devel

%description
sipsak is a small command line tool for developers and
administrators of Session Initiation Protocol (SIP) applications.
It can be used for some simple tests on SIP applications and
devices.

%prep

%setup -q

%build

%configure2_5x \
    --disable-gnutls \
    --enable-timeout=500

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS TODO
%{_bindir}/*
%{_mandir}/man1/*




%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.6-7mdv2011.0
+ Revision: 614892
- the mass rebuild of 2010.1 packages

* Mon Apr 12 2010 Funda Wang <fwang@mandriva.org> 0.9.6-6mdv2010.1
+ Revision: 533649
- rebuild for openssl 1.0

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 0.9.6-5mdv2010.0
+ Revision: 433837
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 0.9.6-4mdv2009.0
+ Revision: 260712
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.9.6-3mdv2009.0
+ Revision: 252478
- rebuild
- fix no-buildroot-tag

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.9.6-1mdv2008.1
+ Revision: 127292
- kill re-definition of %%buildroot on Pixel's request


* Fri Mar 02 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.6-1mdv2007.0
+ Revision: 131206
- Import sipsak

* Wed Feb 08 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.6-1mdk
- 0.9.6
- disable gnutls support
- fix deps

* Mon Apr 25 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.12-1mdk
- initial Mandriva package

