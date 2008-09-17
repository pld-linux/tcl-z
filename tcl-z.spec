Summary:	ZLIB compression and decompression for TCL
Name:		tcl-z
Version:	1.0
Release:	0.1
License:	distributable
Group:		Development/Languages/Tcl
Source0:	http://sgolovan.nes.ru/jabber/ztcl/ztcl/ztcl_%{version}b4_src.tar.gz
# Source0-md5:	32c2ae026ca12a370b56f7f1155ae90c
BuildRequires:	tcl-devel >= 8.4.3
BuildRequires:	tcl-more-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ZTCL is an extension library for TCL written in the C language. It
implements an interface to the ZLIB compression and decompression
library, the one used by GZIP.

%package devel
Summary:	Header files and develpment documentation for tcl-z
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumetacja do tcl-z
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and develpment documentation for tcl-z.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumetacja do tcl-z.

%prep
%setup -q -n ztcl_%{version}b4

sed -i -e 's#/home/devel/src/C/tcl/ztcl/main--1.0/##g' Makefile*

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
	INSTALL_ROOT="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel     -p      /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun devel   -p      /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc README
%dir %{_libdir}/ztcl*
%attr(755,root,root) %{_libdir}/libztcl[0-9].[0-9].[0-9].so
%{_libdir}/ztcl*/*.tcl
%{_infodir}/ztcl.info*

%files devel
%defattr(644,root,root,755)
%{_aclocaldir}/*.m4
%{_includedir}/*.h
%attr(755,root,root) %{_libdir}/libztcl[0-9].[0-9].so
%attr(755,root,root) %{_libdir}/libztcl[0-9].so
%{_libdir}/libztcl*.a
