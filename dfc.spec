#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dfc
Version  : 3.1.1
Release  : 10
URL      : https://projects.gw-computing.net/attachments/download/615/dfc-3.1.1.tar.gz
Source0  : https://projects.gw-computing.net/attachments/download/615/dfc-3.1.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: dfc-bin = %{version}-%{release}
Requires: dfc-data = %{version}-%{release}
Requires: dfc-license = %{version}-%{release}
Requires: dfc-locales = %{version}-%{release}
Requires: dfc-man = %{version}-%{release}
BuildRequires : buildreq-cmake

%description
`dfc` is a tool to report file system space usage information. When the output
is a terminal, it uses color and graphs by default. It has a lot of features
such as HTML, JSON and CSV export, multiple filtering options, the ability to
show mount options and so on.

%package bin
Summary: bin components for the dfc package.
Group: Binaries
Requires: dfc-data = %{version}-%{release}
Requires: dfc-license = %{version}-%{release}

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
Requires: dfc-man = %{version}-%{release}

%description doc
doc components for the dfc package.


%package license
Summary: license components for the dfc package.
Group: Default

%description license
license components for the dfc package.


%package locales
Summary: locales components for the dfc package.
Group: Default

%description locales
locales components for the dfc package.


%package man
Summary: man components for the dfc package.
Group: Default

%description man
man components for the dfc package.


%prep
%setup -q -n dfc-3.1.1
cd %{_builddir}/dfc-3.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604539909
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake .. -DXDG_CONFIG_DIR=/usr/share/xdg
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1604539909
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dfc
cp %{_builddir}/dfc-3.1.1/LICENSE %{buildroot}/usr/share/package-licenses/dfc/4b97208f35537134f453d5fa649a86dc097494ce
cp %{_builddir}/dfc-3.1.1/cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/dfc/ff3ed70db4739b3c6747c7f624fe2bad70802987
pushd clr-build
%make_install
popd
%find_lang dfc
## Remove excluded files
rm -f %{buildroot}/usr/share/xdg/dfc/fr/dfcrc
rm -f %{buildroot}/usr/share/xdg/dfc/nl/dfcrc
rm -f %{buildroot}/usr/share/man/fr/man1/dfc.1
rm -f %{buildroot}/usr/share/man/nl/man1/dfc.1

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dfc

%files data
%defattr(-,root,root,-)
/usr/share/xdg/dfc/dfcrc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/dfc/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dfc/4b97208f35537134f453d5fa649a86dc097494ce
/usr/share/package-licenses/dfc/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/dfc.1

%files locales -f dfc.lang
%defattr(-,root,root,-)

