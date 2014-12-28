#
# Conditional build:
%bcond_without	mp1e	# without MP1E backend
#
%ifnarch %{ix86}
%undefine	with_mp1e
%endif
Summary:	Real Time Software Video/Audio Encoder library
Summary(pl.UTF-8):	Programowa biblioteka kodera audio/wideo czasu rzeczywistego
Name:		rte
Version:	0.5.6
Release:	2
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/zapping/%{name}-%{version}.tar.bz2
# Source0-md5:	6259cdff255af71c23a4576e7c5664a0
URL:		http://zapping.sourceforge.net/
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Real Time Software Video/Audio Encoder library.

%description -l pl.UTF-8
Programowa biblioteka kodera audio/wideo czasu rzeczywistego.

%package devel
Summary:	rte library development files
Summary(pl.UTF-8):	Pliki programistyczne biblioteki rte
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
rte library development files.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki rte.

%package static
Summary:	rte static library
Summary(pl.UTF-8):	Biblioteka statyczna rte
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
rte static library.

%description static -l pl.UTF-8
Statyczna biblioteka rte.

%prep
%setup -q
# keep only aclocal-include.m4
%{__rm} m4/{[!a]*,as}.m4
# needed by automake
install -d mp1e/{macros,vbi,devices,test}

# workaround for test at the end of configure (to not return 1)
touch mp1e/configure.in

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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/librte.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librte.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librte.so
%{_libdir}/librte.la
%{_includedir}/librte.h

%files static
%defattr(644,root,root,755)
%{_libdir}/librte.a
