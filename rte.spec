#
%bcond_without	mp1e	# without MP1E backend
#
%ifnarch %{ix86}
%undefine	with_mp1e
%endif
Summary:	Real Time Software Video/Audio Encoder library
Summary(pl):	Programowa biblioteka kodera audio/wideo czasu rzeczywistego
Name:		rte
Version:	0.5.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/zapping/%{name}-%{version}.tar.bz2
# Source0-md5:	00ebfd8da3a8f5613265d1afc2bf6387
Patch0:		%{name}-mp1e-common.patch
URL:		http://zapping.sf.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
%{?with_mp1e:BuildRequires:	mp1e-devel >= 1.9.3}
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
%setup -q
%patch -p1

rm -f m4/{[!a]*,as}.m4
# needed by automake
install -d mp1e/{macros,vbi,devices,test}

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--without-divx4linux \
	%{!?with_mp1e:--without-mp1e} \
%ifnarch %{ix86}
	--without-ffmpeg
# included ffmpeg is modified (has "ticker" hacks), so cannot use system one
# and this version supports only x86 unlike system version...
%endif

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
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
