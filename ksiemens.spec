# This spec file was generated using Kpp
# If you find any problems with this spec file please report
# the error to ian geiser <geiseri@msoe.edu>
Summary:	KSiemens is a KDE application that manages Siemens S25/35 mobile phones
Name:		ksiemens
Version:	0.1
Release:	1
License:	GPL
Url:		http://www.sourceforge.net/projects/ksiemens
Group:		Applications/KDE
Source:		ksiemens-0.1.tar.gz
BuildRoot:	/tmp/ksiemens-buildroot
Prefix:		/opt/kde2.1

%description


%prep
%setup
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" ./configure \
                --with-qt-dir=/usr/lib/qt2 --prefix=/opt/kde2.1 \
                $LOCALFLAGS
%build
# Setup for parallel builds
numprocs=`egrep -c ^cpu[0-9]+ /proc/stat || :`
if [ "$numprocs" = "0" ]; then
  numprocs=1
fi

make -j$numprocs

%install
make install-strip DESTDIR=$RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > $RPM_BUILD_DIR/file.list.ksiemens
find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.ksiemens
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.ksiemens

%clean
rm -rf $RPM_BUILD_ROOT/*
rm -rf $RPM_BUILD_DIR/ksiemens
rm -rf ../file.list.ksiemens


%files -f ../file.list.ksiemens
