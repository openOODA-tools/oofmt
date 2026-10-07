Name:           oofmt
Version:        0.1.0
Release:        1%{?dist}
Summary:        Simple optimal text paragraph reformer keeping uniform margins and clean gutters.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oofmt
Source0:        oofmt-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oofmt is a sovereign, capability-bounded PARAGRAPH REFORM written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oofmt
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oofmt-uninstall

%files
/usr/bin/oofmt
/usr/bin/oofmt-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
