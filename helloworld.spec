# SPEC file overview:
# https://docs.fedoraproject.org/en-US/quick-docs/creating-rpm-packages/#con_rpm-spec-file-overview
# Fedora packaging guidelines:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/
%define debug_package %{nil}

Name:		helloworld
Version:	1
Release:	0%{?dist}
Summary:	say hi~
License:        AGPL-3.0

Source0:	helloworld.tar.gz

Patch0:		0001-change-1-to-2-at-a.c.patch
Patch1:         0001-change-2-to-3.patch
Patch2:         0001-you-can-build-it-and-say-helloworld.patch

BuildRequires:	gcc-c++
Requires:	gcc-c++

%description


%prep
%setup -q -n src

%patch0 -p2
%patch1 -p2
%patch2 -p2

%build
# make %{?_smp_mflags}
gcc a.cpp -lstdc++ -o helloworld

%install
mkdir -p %{buildroot}/bin
install -m 755 helloworld %{buildroot}/bin/


%files
/bin/helloworld
%doc
%license



%changelog
* Tue Feb 18 2020 changjie.fu <changjie.fu@cs2c.com.cn> - 1.0
- Say hi to world!
