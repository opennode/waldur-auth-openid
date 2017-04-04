Name: nodeconductor-auth-openid
Summary: NodeConductor OpenID plugin
Group: Development/Libraries
Version: 0.4.2
Release: 1.el7
License: MIT
Url: http://nodeconductor.com
Source0: %{name}-%{version}.tar.gz

Requires: nodeconductor > 0.108.3
Requires: python-django-openid-auth >= 0.13

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: python-setuptools

%description
NodeConductor plugin bringing OpenID-based authentication support.

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
