#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : isodate
Version  : 0.6.0
Release  : 4
URL      : https://github.com/gweis/isodate/archive/0.6.0.tar.gz
Source0  : https://github.com/gweis/isodate/archive/0.6.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: isodate-legacypython
Requires: isodate-python3
Requires: isodate-python
Requires: six
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
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

%package legacypython
Summary: legacypython components for the isodate package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the isodate package.


%package python
Summary: python components for the isodate package.
Group: Default
Requires: isodate-python3

%description python
python components for the isodate package.


%package python3
Summary: python3 components for the isodate package.
Group: Default
Requires: python3-core

%description python3
python3 components for the isodate package.


%prep
%setup -q -n isodate-0.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523040281
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
export SOURCE_DATE_EPOCH=1523040281
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
