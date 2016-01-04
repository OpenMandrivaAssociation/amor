%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Amusing Misuse Of Resources put's comic figures above your windows
Name:		amor
Version:	15.08.3
Release:	2
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel
Conflicts:	kdetoys4-devel < 1:4.11.0

%description
Amusing Misuse Of Resources put's comic figures above your windows.

%files
%{_kde_bindir}/amor
%{_kde_applicationsdir}/amor.desktop
%{_kde_appsdir}/amor
%{_kde_iconsdir}/hicolor/*/apps/amor.png
%{_kde_docdir}/*/*/amor
%{_kde_mandir}/man6/amor.6.*
%{_datadir}/dbus-1/interfaces/org.kde.amor.xml

#-------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 -DCMAKE_MINIMUM_REQUIRED_VERSION=2.6
%make

%install
%makeinstall_std -C build
