#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : isodate
Version  : 0.6.0
Release  : 36
URL      : https://github.com/gweis/isodate/archive/0.6.0.tar.gz
Source0  : https://github.com/gweis/isodate/archive/0.6.0.tar.gz
Summary  : An ISO 8601 date/time/duration parser and formatter
Group    : Development/Tools
License  : BSD-3-Clause
Requires: isodate-python = %{version}-%{release}
Requires: isodate-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
ISO 8601 date/time parser
=========================
.. image:: https://travis-ci.org/gweis/isodate.svg?branch=master
:target: https://travis-ci.org/gweis/isodate
:alt: Travis-CI
.. image:: https://coveralls.io/repos/gweis/isodate/badge.svg?branch=master
:target: https://coveralls.io/r/gweis/isodate?branch=master
:alt: Coveralls
.. image:: https://img.shields.io/pypi/v/isodate.svg
:target: https://pypi.python.org/pypi/isodate/
:alt: Latest Version
.. image:: https://img.shields.io/pypi/l/isodate.svg
:target: https://pypi.python.org/pypi/isodate/
:alt: License

%package python
Summary: python components for the isodate package.
Group: Default
Requires: isodate-python3 = %{version}-%{release}

%description python
python components for the isodate package.


%package python3
Summary: python3 components for the isodate package.
Group: Default
Requires: python3-core
Provides: pypi(isodate)
Requires: pypi(six)

%description python3
python3 components for the isodate package.


%prep
%setup -q -n isodate-0.6.0
cd %{_builddir}/isodate-0.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603393741
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
