%define		_rte_version	0.3.1
%define		_mp1e_version	1.9.1

Summary:	Real Time Software Video/Audio Encoder library
Summary(pl):	Programowa biblioteka kodera audio/wideo czasu rzeczywistego
Name:		rte
Version:	%{_rte_version}
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
URL:		http://zapping.sf.net/
Source0:	http://prdownloads.sourceforge.net/zapping/%{name}-%{version}.tar.bz2
BuildRequires:	esound-devel
BuildRequires:	XFree86-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	nasm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Real Time Software Video/Audio Encoder library.

%description -l pl
Programowa biblioteka kodera audio/wideo czasu rzeczywistego.

%package devel
Summary:	rte library development files
Summary(pl):	Pliki programistyczne biblioteki rte
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name} = %{version}

%description devel
rte library development files

%description devel -l pl
Pliki programistyczne biblioteki rte

%package static
Summary:	rte static library
Summary(pl):	Biblioteka statyczna rte
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name}-devel = %{version}

%description static
rte static library

%description static -l pl
Pliki programistyczne biblioteki rte.

%package -n mp1e
Summary:	Realtime MPEG-1 audio/video encoder
Summary(pl):	Koder audio/wideo MPEG-1 czasu rzeczywistego
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
Group(pt):	AplicaГУes/GrАficos
Version:	%{_mp1e_version}
Requires:	rte

%description -n mp1e
Realtime MPEG-1 audio/video encoder

%description -n mp1e -l pl
Koder audio/wideo MPEG-1 czasu rzeczywistego

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

%{__make} \
	DESTDIR=$RPM_BUILD_ROOT \
	bindir=%{_bindir} \
	man1dir=%{_mandir}/man1 \
	install

gzip -9nf AUTHORS NEWS README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
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
