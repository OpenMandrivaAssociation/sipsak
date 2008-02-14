Summary:	SIP swiss army knife
Name:		sipsak
Version:	0.9.6
Release:	%mkrel 1
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


