Name:           oofmt
Version:        0.2.0
Release:        1%{?dist}
Summary:        Sovereign optimal paragraph reformer and text reflower in pure openOODA.
License:        Apache-2.0
URL:            https://github.com/openOODA-tools/oofmt
Source0:        oofmt-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oofmt is a sovereign, capability-bounded optimal paragraph reformer, gutter aligner,
and text reflow coordinator written in 100% pure native openOODA with zero ambient authority,
POSIX flags, and streaming Model Context Protocol (MCP) support.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oofmt
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oofmt-uninstall

%files
/usr/bin/oofmt
/usr/bin/oofmt-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Sovereign paragraph reflow engine with streaming MCP and tri-distribution packaging
