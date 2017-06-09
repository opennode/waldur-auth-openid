Name: nodeconductor-auth-openid
Summary: Waldur OpenID plugin
Group: Development/Libraries
Version: 0.8.1
Release: 1.el7
License: MIT
Url: http://waldur.com
Source0: %{name}-%{version}.tar.gz

Requires: nodeconductor > 0.138.0
Requires: python-django-openid-auth >= 0.14-2

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: python-setuptools

%description
Waldur plugin bringing OpenID-based authentication support.

%prep
%setup -q -n %{name}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --single-version-externally-managed -O1 --root=%{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Fri Jun 9 2017 Jenkins <jenkins@opennodecloud.com> - 0.8.1-1.el7
- New upstream release

* Fri Jun 9 2017 Jenkins <jenkins@opennodecloud.com> - 0.8.0-1.el7
- New upstream release

* Wed May 31 2017 Jenkins <jenkins@opennodecloud.com> - 0.7.0-1.el7
- New upstream release

* Sun Apr 23 2017 Jenkins <jenkins@opennodecloud.com> - 0.6.0-1.el7
- New upstream release

* Wed Apr 12 2017 Jenkins <jenkins@opennodecloud.com> - 0.5.0-1.el7
- New upstream release

* Wed Apr 5 2017 Jenkins <jenkins@opennodecloud.com> - 0.4.3-1.el7
- New upstream release

* Tue Apr 4 2017 Jenkins <jenkins@opennodecloud.com> - 0.4.2-1.el7
- New upstream release

* Wed Mar 15 2017 Jenkins <jenkins@opennodecloud.com> - 0.4.1-1.el7
- New upstream release

* Wed Mar 15 2017 Jenkins <jenkins@opennodecloud.com> - 0.4.0-1.el7
- New upstream release

* Tue Mar 14 2017 Jenkins <jenkins@opennodecloud.com> - 0.3.1-1.el7
- New upstream release

* Thu Mar 2 2017 Jenkins <jenkins@opennodecloud.com> - 0.3.0-1.el7
- New upstream release

* Wed Feb 8 2017 Jenkins <jenkins@opennodecloud.com> - 0.2.4-1.el7
- New upstream release

* Wed Jan 25 2017 Jenkins <jenkins@opennodecloud.com> - 0.2.3-1.el7
- New upstream release

* Wed Dec 28 2016 Jenkins <jenkins@opennodecloud.com> - 0.2.2-1.el7
- New upstream release

* Wed Dec 28 2016 Jenkins <jenkins@opennodecloud.com> - 0.2.1-1.el7
- New upstream release

* Wed Dec 28 2016 Jenkins <jenkins@opennodecloud.com> - 0.2.0-1.el7
- New upstream release

* Tue May 31 2016 Jenkins <jenkins@opennodecloud.com> - 0.1.0-1.el7
- New upstream release

* Tue May 3 2016 Juri Hudolejev <juri@opennodecloud.com> - 0.1.0-1.el7
- Initial version of the package
