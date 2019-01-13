%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		zeroconf-ioslave
Summary:	zeroconf ioslave
Summary(pl.UTF-8):	zeroconf ioslave
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	41d470c2e5555191086efea24ecd4d1f
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.37.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.37.0
BuildRequires:	kf5-kdnssd-devel >= 5.37.0
BuildRequires:	kf5-ki18n-devel >= 5.37.0
BuildRequires:	kf5-kio-devel >= 5.37.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= 5.9.0
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zeroconf ioslave.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt5/plugins/kded_dnssdwatcher.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kio/zeroconf.so
%{_datadir}/dbus-1/interfaces/org.kde.kdnssd.xml
%{_datadir}/kservices5/kded/dnssdwatcher.desktop
%{_datadir}/remoteview/zeroconf.desktop
