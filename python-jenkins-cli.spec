# Taken from http://copr-dist-git.fedorainfracloud.org/cgit/radomirbosak/python-jenkins-cli/python-jenkins-cli.git/commit/?id=312b32ce8c92e52d1f0aa340247fcb1377bca442
%global srcname jenkins-cli
%global sum A CLI for Jenkins CI

Name:           python-%{srcname}
Version:        0.2.0
Release:        2%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://pypi.python.org/pypi/jenkins-cli
Source0:        v0.2.0.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel python3-devel


%description
A CLI for Jenkins CI

%package -n python2-%{srcname}
Summary:        %{sum}

BuildRequires:  python2-devel
BuildRequires:  python2-pyfakefs
BuildRequires:  python2-mock
BuildRequires:  python2-unittest2
BuildRequires:  python2-jenkins
BuildRequires:  python-six
BuildRequires:  python2-pyxdg
Requires:       python2-jenkins
Requires:       python-six
Requires:       python2-pyxdg

%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
A CLI for Jenkins CI


%package -n python3-%{srcname}
Summary:        %{sum}

BuildRequires:  python3-devel
BuildRequires:  python3-pyfakefs
BuildRequires:  python3-mock
BuildRequires:  python3-unittest2
BuildRequires:  python3-jenkins
BuildRequires:  python3-six
BuildRequires:  python3-pyxdg
Requires:       python3-jenkins
Requires:       python3-six
Requires:       python3-pyxdg

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A CLI for Jenkins CI


%prep
%autosetup -n %{srcname}-python-%{version}

# Adjust python-jenkins and pyfakefs versions for Fedora 25
sed -i 's/python-jenkins==0.4.14/python-jenkins>=0.4.12/' requirements.txt setup.py
sed -i 's/pyfakefs==2.7.0/pyfakefs>=3.1/' requirements.txt setup.py

%build
%py2_build
%py3_build

%install
# Must do the python2 install first because the scripts in /usr/bin are
# overwritten with every setup.py install, and in general we want the
# python3 version to be the default.
# If, however, we're installing separate executables for python2 and python3,
# the order needs to be reversed so the unversioned executable is the python2 one.
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

# Note that there is no %%files section for the unversioned python module if we are building for several python runtimes
%files -n python2-%{srcname}
%license LICENSE
%doc README.rst
%{python2_sitelib}/*
%{_bindir}/jenkins
%{_datarootdir}/bash-completion/completions/jenkins

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*
%{_bindir}/jenkins
%{_datarootdir}/bash-completion/completions/jenkins

%changelog
