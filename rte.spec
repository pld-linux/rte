Summary:	Real Time Software Video/Audio Encoder library
Summary(pl):	Programowa biblioteka kodera audio/wideo czasu rzeczywistego
Name:		rte
Version:	0.5
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/zapping/%{name}-%{version}.tar.bz2
URL:		http://zapping.sf.net/
BuildRequires:	XFree86-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	libtool
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
Statyczna biblioteka rte.

%prep
%setup  -q

%build
%configure --without-divx4linux
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
