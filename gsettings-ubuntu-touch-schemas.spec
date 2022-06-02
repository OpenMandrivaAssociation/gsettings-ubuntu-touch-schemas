%define _name   gsettings-ubuntu-touch-schemas
%define _version 0.0.7+21.10.20210712
Name:           gsettings-ubuntu-schemas
Version:        0.0.7
Release:        1
Summary:        GSettings desktop-wide schemas from Ubuntu
License:        LGPL-2.1-only
Group:          System/GUI/Other
URL:            https://launchpad.net/gsettings-ubuntu-touch-schemas
Source:         https://launchpad.net/ubuntu/+archive/primary/+files/%{_name}_%{_version}.orig.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  polkit
BuildRequires:  pkgconfig(glib-2.0)
BuildArch:      noarch

%description
gsettings-ubuntu-schemas contains a collection of GSettings schemas
for settings shared by various components of an Ubuntu environment.

%package -n accountsservice-ubuntu-schemas
Summary:        AccountsService schemas from Ubuntu
Group:          System/GUI/Other
Requires:       accountsservice

%description -n accountsservice-ubuntu-schemas
accountsservice-ubuntu-schemas contains a collection of
AccountsService vendor extension schemas used by various components
of an Ubuntu environment.

%package devel
Summary:        Development files for Ubuntu GSettings schemas
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
gsettings-ubuntu-schemas contains a collection of GSettings schemas
for settings shared by various components of an Ubuntu environment.

This package contains the development files for gsettings-ubuntu-schemas.

%prep
%setup -q -c

%build
intltoolize
autoreconf -vfi
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc README
%{_datadir}/glib-2.0/schemas/com.canonical.*.gschema.xml
%{_datadir}/glib-2.0/schemas/com.ubuntu.*.gschema.xml

%files -n accountsservice-ubuntu-schemas
%license COPYING
%doc README
%dir %{_datadir}/accountsservice/
%dir %{_datadir}/accountsservice/interfaces/
%{_datadir}/accountsservice/interfaces/com.ubuntu.*.xml
%dir %{_datadir}/dbus-1/
%dir %{_datadir}/dbus-1/interfaces/
%{_datadir}/dbus-1/interfaces/com.ubuntu.*.xml
%{_datadir}/polkit-1/actions/com.ubuntu.AccountsService.policy
%dir %{_localstatedir}/lib/polkit-1/
%dir %{_localstatedir}/lib/polkit-1/localauthority/
%dir %{_localstatedir}/lib/polkit-1/localauthority/10-vendor.d/
%{_localstatedir}/lib/polkit-1/localauthority/10-vendor.d/50-com.ubuntu.AccountsService.pkla

%files devel
%{_datadir}/pkgconfig/gsettings-unity-schemas.pc
