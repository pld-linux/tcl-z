Summary:	ZLIB compression and decompression for TCL
Name:		tcl-z
Version:	1.0
Release:	0.1
License:	distributable
Group:		Development/Languages/Tcl
Source0:	http://sgolovan.nes.ru/jabber/ztcl/ztcl/ztcl_%{version}b4_src.tar.gz
# Source0-md5:	32c2ae026ca12a370b56f7f1155ae90c
BuildRequires:	tcl-devel >= 8.4.3
Requires:	tcl-ztcl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ZTCL is an extension library for TCL written in the C language. It
implements an interface to the ZLIB compression and decompression
library, the one used by GZIP.

%prep
%setup -q -n ztcl_%{version}b4

%build
%configure \
	--enable-threads \
	--enable-shared \
	--enable-64bit
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{_libdir}/ztcl*
%attr(755,root,root) %{_libdir}/ztcl*/libztcl*.so
%{_libdir}/ztcl*/*.tcl
%{_mandir}/man*/ztcl*
