#
# spec file for package xr-hardware
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           xr-hardware
Version:        1.1.0+4
Release:        0
Summary:        Hardware descriptions for XR devices
License:        BSL-1.0
URL:            https://gitlab.freedesktop.org/monado/utilities/xr-hardware
Source:         https://gitlab.freedesktop.org/monado/utilities/xr-hardware/-/archive/%{version}/%{name}-%{version}.tar.bz2
BuildArch:      noarch

%description
A simple set of scripts to generate udev rules for user access to XR (VR and AR)
hardware devices.

%prep
%setup -q -n %{name}-%{version}

%build

%install
make install_package DESTDIR="%{?buildroot}" PREFIX="%{_usr}"

%files
%license LICENSE.txt
%doc README.md CHANGELOG.md
%{_udevrulesdir}/70-xrhardware.rules

%changelog
