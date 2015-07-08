%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define tarname oiopy

Name:           python-oiopy

%if %{?_with_test:0}%{!?_with_test:1}
Version:        0.4.0
Release:        1%{?dist}
%define         tarversion %{version}
Source0:        https://pypi.python.org/packages/source/o/oiopy/oiopy-%{tarversion}.tar.gz
%else
# Testing purpose only. Do not modify.
%define         date %(date +"%Y%m%d%H%M")
Version:        test%{date}.%{tag}
Release:        0%{?dist}
%define         tarversion %{tag}
Source0:        https://github.com/open-io/oiopy/archive/%{tarversion}.tar.gz
%endif

Summary:        Python API for OpenIO SDS
License:        LGPL v3
URL:            http://www.openio.io/

BuildArch:      noarch
BuildRequires:  python-setuptools
#BuildRequires:  python-pbr
Requires:       python-eventlet >= 0.15.2
Requires:       python-requests
#Requires:       python-pbr

Obsoletes:	python-openio-sds-client

%description
Python API for OpenIO SDS

%prep
%setup -q -n %{tarname}-%{tarversion}


%build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT

%files
%{python_sitelib}/*


%changelog
* Mon Jun 29 2015 0.4.0-1 Romain Acciari <romain.acciari@openio.io>
- Account support
* Thu Apr 23 2015 0.3-2 Romain Acciari <romain.acciari@openio.io>
- Package renamed
* Mon Apr 20 2015 0.3-1 Romain Acciari <romain.acciari@openio.io>
- Jka proxyd pool
* Fri Apr 10 2015 0.2-1 Romain Acciari <romain.acciari@openio.io>
- New release to fit with OpenIO SDS 0.3
* Fri Feb 13 2015 0.1-1 Julien Kasarherou <julien.kasarherou@openio.io>
- Initial release
