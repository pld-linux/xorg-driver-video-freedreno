Summary:	X.org video driver for Adreno graphics
Summary(pl.UTF-8):	Sterownik obrazu X.org dla układów Adreno
Name:		xorg-driver-video-freedreno
Version:	1.1.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-freedreno-%{version}.tar.bz2
# Source0-md5:	085642246f217ecd9d03c8699526a653
URL:		http://xorg.freedesktop.org/
BuildRequires:	Mesa-libxatracker-devel >= 10.2
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	pkgconfig(libdrm_freedreno)
BuildRequires:	pkgconfig(xatracker) >= 2.2.0
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	udev-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.99.1
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.4
BuildRequires:	xorg-xserver-server-devel
%{?requires_xorg_xserver_videodrv}
Requires:	xorg-xserver-server
ExclusiveArch:	arm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Open-source X.org video driver for Adreno graphics.

%description -l pl.UTF-8
Sterownik graficzny X.org o otwartych źródłach dla układów graficznych
Adreno.

%prep
%setup -q -n xf86-video-freedreno-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/freedreno_drv.so
