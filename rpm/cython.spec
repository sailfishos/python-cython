# based on work by The Fedora Project (2017)
# Copyright (c) 1998, 1999, 2000 Thai Open Source Software Center Ltd
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

%global srcname Cython

# To prepare for the future changes in RPM macro support
%if ! %{defined python3_sitearch}
%define python3_sitearch /%{_libdir}/python3.?/site-packages
%endif

%if ! %{defined python3_sitelib}
%define python3_sitelib %{python3_sitearch}
%endif

# https://github.com/cython/cython/issues/1982
%bcond_with tests

Name:           cython
%global upver 0.29rc2
Version:        0.29~rc2
Release:        1
Summary:        Language for writing Python extension modules

License:        ASL 2.0
URL:            http://www.cython.org
Source:         %{name}-%{version}.tar.gz

BuildRequires:  gcc

%global _description \
This is a development version of Pyrex, a language\
for writing Python extension modules.

%description %{_description}

%package -n python-%{name}
Summary:        %{summary}
Provides:       cython = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       cython = %{?epoch:%{epoch}:}%{version}-%{release}
BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description -n python-%{name} %{_description}

Python 2 version.

%package -n python3-%{name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Conflicts:      python-%{srcname} < 0.28.4-2
BuildRequires:  python3-devel

%description -n python3-%{name} %{_description}

Python 3 version.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
%{__python} setup.py build
%{__python3} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}
rm -rf %{buildroot}%{python_sitelib}/setuptools/tests
rm %{buildroot}%{_bindir}/*

%{__python3} setup.py install --skip-build --root %{buildroot}
rm -rf %{buildroot}%{python3_sitelib}/setuptools/tests

%check

%clean
rm -rf ${RPM_BUILD_ROOT}

%files -n python-%{name}
%license LICENSE.txt
%doc *.txt Demos Doc Tools
%{python_sitearch}/%{srcname}-*.egg-info/
%{python_sitearch}/%{srcname}/
%{python_sitearch}/pyximport/
%{python_sitearch}/%{name}.py*

%files -n python3-%{name}
%license LICENSE.txt
%doc *.txt Demos Doc Tools
%{_bindir}/cython
%{_bindir}/cygdb
%{_bindir}/cythonize
%{python3_sitearch}/%{srcname}-*.egg-info/
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/pyximport/
%{python3_sitearch}/%{name}.py
%{python3_sitearch}/__pycache__/%{name}.*

