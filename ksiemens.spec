Summary:	KSiemens is a KDE application that manages Siemens S25/35 mobile phones
Summary(pl):	KSiemens jest aplikacj± KDE, s³u¿±c± do zarz±dania telefonami Siemens S25/35
Name:		ksiemens
Version:	0.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://prdownloads.sourceforge.net/ksiemens/%{name}-%{version}.tar.gz
URL:		http://www.sourceforge.net/projects/ksiemens/
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
KSiemens is a KDE application that manages Siemens S25/35 mobile
phones.

%description -l pl
KSiemens jest aplikacj± dla KDE, s³u¿±c± do zarz±dzania telefonami
komórkowymi Siemens S25/35.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti"

%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_applnkdir}/{Applications,Utilities}

%find_lang %{name} --with-kde --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/ksiemens
%{_applnkdir}/Utilities/ksiemens.desktop
