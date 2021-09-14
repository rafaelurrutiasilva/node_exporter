%define _unpackaged_files_terminate_build 0
%define debug_package %{nil}

%define _version 1.2.2

Name:		node-exporter
Version:        %{_version}
Release:        1%{?dist}

Summary:	Prometheus exporter for machine metrics, written in Go with pluggable metric collectors.
Group:		System Environment/Daemons
License:	See the LICENSE file at github.
URL:		https://github.com/prometheus/node_exporter

Source0:        https://github.com/prometheus/node_exporter/releases/download/v%{version}/node_exporter-%{version}.linux-amd64.tar.gz


BuildRoot:	%{_tmppath}/%{name}-%{version}-root

Requires(pre):  	/usr/sbin/useradd
Requires(post): 	systemd
Requires(preun): 	systemd
Requires(postun): 	systemd
AutoReqProv:    	No

%description
Prometheus exporter for machine metrics, written in Go with pluggable metric collectors.

%prep
%setup -q -n node_exporter-%{version}.linux-amd64

%build
echo

%install
#mkdir -vp $RPM_BUILD_ROOT/var/run/prometheus
#mkdir -vp $RPM_BUILD_ROOT/var/lib/prometheus
mkdir -vp $RPM_BUILD_ROOT/usr/sbin
#mkdir -vp $RPM_BUILD_ROOT/opt/prometheus

mkdir -vp $RPM_BUILD_ROOT/usr/lib/systemd/system
cp $RPM_SOURCE_DIR/contrib/node_exporter.service	$RPM_BUILD_ROOT/usr/lib/systemd/system/node_exporter.service

install -m 755 node_exporter $RPM_BUILD_ROOT/usr/sbin/node_exporter

%clean

%pre
getent group prometheus >/dev/null || groupadd -r prometheus
getent passwd prometheus >/dev/null || useradd -r -g prometheus -s /sbin/nologin \
    -d $RPM_BUILD_ROOT/var/lib/prometheus/ -c "prometheus Daemons" prometheus
exit 0

%post
#chgrp prometheus /var/run/prometheus
#chmod 774 /var/run/prometheus
#chown prometheus:prometheus /opt/prometheus
#chmod 744 /opt/prometheus

systemctl daemon-reload
systemctl start node_exporter
systemctl enable node_exporter


%files
%defattr(-,root,root,-)
/usr/sbin/node_exporter
#/var/run/prometheus
#/opt/prometheus
/usr/lib/systemd/system/node_exporter.service
