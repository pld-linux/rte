%define		_rte_version	0.4
# when upgrading, update the following from rte-%{version}/mp1e/configure.in
%define		_mp1e_version	1.9.2

Summary:	Real Time Software Video/Audio Encoder library
Summary(pl):	Programowa biblioteka kodera audio/wideo czasu rzeczywistego
Name:		rte
Version:	%{_rte_version}
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://prdownloads.sourceforge.net/zapping/%{name}-%{version}.tar.bz2
URL:		http://zapping.sf.net/
BuildRequires:	esound-devel
BuildRequires:	XFree86-devel
%ifnarch sparc spar64 ppc
BuildRequires:	alsa-lib-devel
BuildRequires:	nasm
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Real Time Software Video/Audio Encoder library.

%description -l pl
Programowa biblioteka kodera audio/wideo czasu rzeczywistego.

%package devel
Summary:	rte library development files
Summary(pl):	Pliki programistyczne biblioteki rte
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
rte library development files.

%description devel -l pl
Pliki programistyczne biblioteki rte.

%package static
Summary:	rte static library
Summary(pl):	Biblioteka statyczna rte
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
rte static library.

%description static -l pl
Pliki programistyczne biblioteki rte.

%package -n mp1e
Summary:	Realtime MPEG-1 audio/video encoder
Summary(pl):	Koder audio/wideo MPEG-1 czasu rzeczywistego
Group:		Applications/Graphics
Version:	%{_mp1e_version}
Requires:	rte

%description -n mp1e
Realtime MPEG-1 audio/video encoder.

%description -n mp1e -l pl
Koder audio/wideo MPEG-1 czasu rzeczywistego.

%prep
%setup  -q

%build
%configure2_13
cd mp1e
%configure2_13
cd ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	bindir=%{_bindir} \
	man1dir=%{_mandir}/man1

gzip -9nf AUTHORS NEWS README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librte-%{_rte_version}.so
%doc [ANR]*.gz

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librte.??
%{_includedir}/rte.h
%doc ChangeLog.gz

%files static
%defattr(644,root,root,755)
%{_libdir}/librte.a

%files -n mp1e
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
