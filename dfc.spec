#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dfc
Version  : 3.0.5
Release  : 1
URL      : http://projects.gw-computing.net/attachments/download/467/dfc-3.0.5.tar.gz
Source0  : http://projects.gw-computing.net/attachments/download/467/dfc-3.0.5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: dfc-bin
Requires: dfc-config
Requires: dfc-doc
Requires: dfc-locales
Requires: dfc-data
BuildRequires : cmake

%description
dfc is a simple tool that displays file system space usage using graph and color.

%package bin
Summary: bin components for the dfc package.
Group: Binaries
Requires: dfc-data
Requires: dfc-config

%description bin
bin components for the dfc package.


%package config
Summary: config components for the dfc package.
Group: Default

%description config
config components for the dfc package.


%package data
Summary: data components for the dfc package.
Group: Data

%description data
data components for the dfc package.


%package doc
Summary: doc components for the dfc package.
Group: Documentation

%description doc
doc components for the dfc package.


%package locales
Summary: locales components for the dfc package.
Group: Default

%description locales
locales components for the dfc package.


%prep
%setup -q -n dfc-3.0.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1496184097
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=%{_libdir} -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib
make VERBOSE=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1496184097
rm -rf %{buildroot}
pushd clr-build
%make_install
popd
%find_lang dfc

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dfc

%files config
%defattr(-,root,root,-)
%config /usr/etc/xdg/dfc/dfcrc
%config /usr/etc/xdg/dfc/fr/dfcrc

%files data
%defattr(-,root,root,-)
/usr/share/man/fr/man1/dfc.1

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/dfc/*
%doc /usr/share/man/man1/*

%files locales -f dfc.lang
%defattr(-,root,root,-)

