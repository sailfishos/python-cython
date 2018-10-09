%global srcname Cython
%global upname cython

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
Release:        1%{?dist}
Summary:        Language for writing Python extension modules

License:        ASL 2.0
URL:            http://www.cython.org
Source:         https://github.com/cython/cython/archive/%{upver}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc

%global _description \
This is a development version of Pyrex, a language\
for writing Python extension modules.

%description %{_description}

%package -n python2-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{srcname}}
Provides:       cython = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       cython%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      cython < %{?epoch:%{epoch}:}%{version}-%{release}
BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description -n python2-%{srcname} %{_description}

Python 2 version.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Conflicts:      python2-%{srcname} < 0.28.4-2
BuildRequires:  python3-devel

%description -n python3-%{srcname} %{_description}

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

%files -n python2-%{srcname}
%license LICENSE.txt
%doc *.txt Demos Doc Tools
%{python_sitearch}/%{srcname}-*.egg-info/
%{python_sitearch}/%{srcname}/
%{python_sitearch}/pyximport/
%{python_sitearch}/%{upname}.py*

%files -n python3-%{srcname}
%license LICENSE.txt
%doc *.txt Demos Doc Tools
%{_bindir}/cython
%{_bindir}/cygdb
%{_bindir}/cythonize
%{python3_sitearch}/%{srcname}-*.egg-info/
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/pyximport/
%{python3_sitearch}/%{upname}.py
%{python3_sitearch}/__pycache__/%{upname}.*

