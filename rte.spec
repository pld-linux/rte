Summary:	Real Time Software Video/Audio Encoder library
Name:		rte
Version:	0.3
Release:	1
License:	GPL
Group:		Applications/Multimedia
Group(de):	Applikationen/Multimedia
Group(pl):	Aplikacje/Multimedia
URL:		http://zapping.sf.net/
Source0:	http://prdownloads.sourceforge.net/zapping/%{name}-%{version}.tar.bz2
BuildRequires:	nasm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_rte_version	0.3
%define		_mp1e_version	1.9

%description
Real Time Software Video/Audio Encoder library.

%package devel
Summary:	rte library development files
Group:		Applications/Multimedia
Group(de):	Applikationen/Multimedia
Group(pl):	Aplikacje/Multimedia
Requires:	rte

%description devel
rte library development files

%package static
Summary:	rte static library
Group:		Applications/Multimedia
Group(de):	Applikationen/Multimedia
Group(pl):	Aplikacje/Multimedia
Requires:	rte-devel

%description static
rte static library

%package -n mp1e
Summary:	Realtime MPEG-1 audio/video encoder
Group:		Applications/Multimedia
Group(de):	Applikationen/Multimedia
Group(pl):	Aplikacje/Multimedia
Version:	%{_mp1e_version}
Requires:	rte

%description -n mp1e
Realtime MPEG-1 audio/video encoder


%prep
%setup  -q
#%patch0 -p1

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} \
	DESTDIR=$RPM_BUILD_ROOT \
	bindir=%{_bindir} \
	man1dir=%{_mandir}/man1 \
	install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librte.??
%attr(755,root,root) %{_libdir}/librte-%{_rte_version}.so
%doc *.gz

%files devel
%defattr(644,root,root,755)
%{_includedir}/rte.h

%files static
%defattr(644,root,root,755)
%{_libdir}/librte.a

%files -n mp1e
%defattr(644,root,root,755)
%{_bindir}/*
%{_mandir}/*
