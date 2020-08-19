Summary:	NIS(YP) NSS glibc module
Summary(es.UTF-8):	Módulo NIS(YP) NSS de glibc
Summary(pl.UTF-8):	Moduł NIS(YP) NSS glibc
Name:		nss_nis
Version:	3.1
Release:	1
Epoch:		6
License:	LGPL v2.1+
Group:		Base
#Source0Download: https://github.com/thkukuk/libnss_nis/releases
Source0:	https://github.com/thkukuk/libnss_nis/releases/download/v%{version}/libnss_nis-%{version}.tar.xz
# Source0-md5:	2a96c9df26f19f7d61710621700a9996
URL:		https://github.com/thkukuk/libnss_nis
BuildRequires:	libnsl-devel
BuildRequires:	libtirpc-devel
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
glibc NSS (Name Service Switch) module for NIS(YP) databases access.

%description -l es.UTF-8
Módulo NSS de glibc para acceder las bases de datos NIS(YP).

%description -l pl.UTF-8
Moduł glibc NSS (Name Service Switch) dostępu do baz danych NIS(YP).

%prep
%setup -q -n libnss_nis-%{version}

%build
%configure \
	--libdir=/%{_lib} \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT/%{_lib}/libnss_nis.{la,so}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) /%{_lib}/libnss_nis.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libnss_nis.so.2
