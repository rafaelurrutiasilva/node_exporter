%define version 20210912
%define release 1

%define name        PhotonOS-Prometheus-node_exporter
%define summary     Prometheus exporter for machine metrics

%define packager    	R Urrutia <Rafael.Urrutia.S@gmail.com


Summary:        %{summary}
Name:           %{name}
Version:        %{version}
Release:        %{release}
Packager:       %{packager}
License:	sysmanXse
Group:		System Environment/Daemons
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires(pre):  /usr/sbin/useradd
Requires:	systemd

%description
rometheus exporter for machine metrics, written in Go with pluggable metric collectors.

%prep
rm -rf $RPM_BUILD_ROOT

getent group prometheus >/dev/null || groupadd -r prometheus
getent passwd prometheus >/dev/null || useradd -r -g prometheus -s /sbin/nologin \
    -d $RPM_BUILD_ROOT/var/lib/prometheus/ -c "prometheus Daemons" prometheus
exit 0


%build

%install
mkdir -p $RPM_BUILD_ROOT/var/lib/prometheus
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/etc/default/node_exporter

cp $RPM_SOURCE_DIR/node_exporter	$RPM_BUILD_ROOT/usr/bin/.


%post

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(0755,root,root,-)
/var/lib/prometheus
/usr/bin/node_exporter

%defattr(0755,prometheus,prometheus,-)
/etc/default/node_exporter

%changelog
* Sun Sep 12 2021 R Urrutia
- Create first version
