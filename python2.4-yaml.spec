%define real_name PyYAML

Name:           python2.4-yaml
Version:        3.09
Release:        %mkrel 1
Epoch:          0
Summary:        Python package implementing YAML parser and emitter
License:        MIT
Group:          Development/Python
URL:            http://pyyaml.org/
Source0:        http://pyyaml.org/download/pyyaml/PyYAML-%{version}.tar.gz
%py_requires -d
BuildRequires:	yaml-devel
BuildRequires:  python2.4-devel
Requires:       python2.4
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
PyYAML is a YAML parser and emitter for the Python programming
language. 

YAML is a data serialization format designed for human readability
and interaction with scripting languages.

%prep
%setup -q -n %{real_name}-%{version}

%build
export CFLAGS="%{optflags}"
python2.4 setup.py build

%install
%{__rm} -rf %{buildroot}
python2.4 setup.py install --root=%{buildroot} --prefix=%{_prefix}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README examples
%{_libdir}/python2.4/site-packages/yaml
%{_libdir}/python2.4/site-packages/*.so
