Summary:	KSiemens is a KDE application that manages Siemens S25/35 mobile phones
Summary(pl):	KSiemens jest aplikacj± KDE, s³u¿±c± do zarz±dania telefonami Siemens S25/35
Name:		ksiemens
Version:	0.2
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Source0:	http://prdownloads.sourceforge.net/ksiemens/%{name}-%{version}.tar.gz
URL:		http://www.sourceforge.net/projects/ksiemens/
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
KSiemens is a KDE application that manages Siemens S25/35 mobile
phones.

%description -l pl
KSiemens jest aplikacj± dla KDE, s³u¿±c± do zarz±dzania telefonami
komórkowymi Siemens S25/35.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS"  \
./configure \
	--with-qt-dir=/usr/lib/qt2 \
	--prefix=%{_prefix} \
	$LOCALFLAGS

# Setup for parallel builds
numprocs=`egrep -c ^cpu[0-9]+ /proc/stat || :`
if [ "$numprocs" = "0" ]; then
  numprocs=1
fi

%{__make} -j$numprocs

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install-strip DESTDIR=$RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > $RPM_BUILD_DIR/file.list.ksiemens
find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.ksiemens
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.ksiemens

%clean
rm -rf $RPM_BUILD_ROOT/*
rm -rf $RPM_BUILD_DIR/ksiemens
rm -rf ../file.list.ksiemens

%files -f ../file.list.ksiemens
