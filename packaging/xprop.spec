%bcond_with x

Name:           xprop
Version:        1.2.2
Release:        1
License:        MIT
Summary:        Property displayer for X
Url:            http://xorg.freedesktop.org/
Group:          Graphics/Utilities
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1001: 	xprop.manifest
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17

%if !%{with x}
ExclusiveArch:
%endif

%description
xprop displays window and font properties of an X server.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%autogen
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license  COPYING
%{_bindir}/xprop
%{_mandir}/man1/xprop.1%{?ext_man}

%changelog
