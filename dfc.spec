#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dfc
Version  : 3.1.1
Release  : 6
URL      : https://projects.gw-computing.net/attachments/download/615/dfc-3.1.1.tar.gz
Source0  : https://projects.gw-computing.net/attachments/download/615/dfc-3.1.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: dfc-bin
Requires: dfc-doc
Requires: dfc-locales
Requires: dfc-data
BuildRequires : cmake

%description
`dfc` is a tool to report file system space usage information. When the output
is a terminal, it uses color and graphs by default. It has a lot of features
such as HTML, JSON and CSV export, multiple filtering options, the ability to
show mount options and so on.

%package bin
Summary: bin components for the dfc package.
Group: Binaries
Requires: dfc-data

%description bin
bin components for the dfc package.


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
%setup -q -n dfc-3.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1520362679
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DXDG_CONFIG_DIR=/usr/share/xdg
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1520362679
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

%files data
%defattr(-,root,root,-)
%exclude /usr/share/man/fr/man1/dfc.1
%exclude /usr/share/man/nl/man1/dfc.1
%exclude /usr/share/xdg/dfc/fr/dfcrc
%exclude /usr/share/xdg/dfc/nl/dfcrc
/usr/share/xdg/dfc/dfcrc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/dfc/*
%doc /usr/share/man/man1/*

%files locales -f dfc.lang
%defattr(-,root,root,-)

