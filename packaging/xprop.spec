Name:           xprop
Version:        1.2.1
Release:        1
License:        MIT
Summary:        Property displayer for X
Url:            http://xorg.freedesktop.org/
Group:          Graphics/Utilities
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17

%description
xprop displays window and font properties of an X server.

%prep
%setup -q

%build
%autogen
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%license  COPYING 
%{_bindir}/xprop
%{_mandir}/man1/xprop.1%{?ext_man}

%changelog
