Name:		rawstudio
Version:	1.2
Release:	%mkrel 2
Summary:	Graphical tool to convert raw images of digital cameras
Group:		Graphics
URL:		http://rawstudio.org/
Source0:	http://rawstudio.org/files/release/%{name}-%{version}.tar.gz
Patch0:		rawstudio-1.2-fix-str-fmt.patch
Patch1:		rawstudio-1.2-glibc-2.10.patch
License:	GPLv2
BuildRequires:	gtk+2-devel libjpeg-devel libGConf2-devel
BuildRequires:	libtiff-devel zlib-devel lcms-devel imagemagick
BuildRequires:	libexiv-devel
Buildroot:	%_tmppath/%name-%version-%release-root

%description
Rawstudio is an open source raw-image converter written in GTK+.

Features:
* Reads all dcraw supported formats
* Internal 16bit rgb
* Various post-shot controls (white balance, saturation and exposure
  compensation among others)
* Realtime histogram
* Optimized for MMX, 3dnow! and SSE (detected runtime)
* Easy sorting of images
* Fullscreen mode for better overview

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure2_5x
%make

%install
rm -fr %buildroot

%makeinstall_std
%find_lang %{name}

install -d %buildroot%{_datadir}/icons/{large,mini}

convert pixmaps/rawstudio.png -resize 32x32 %buildroot%{_iconsdir}/%{name}.png
convert pixmaps/rawstudio.png -resize 16x16 %buildroot%{_miconsdir}/%{name}.png
cp pixmaps/rawstudio.png %buildroot%{_liconsdir}/%{name}.png

%clean
rm -fr %buildroot

%if %mdkversion < 200900
%post
%update_desktop_database
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_desktop_database
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%docdir %{_docdir}/%{name}-%{version}
%doc README
%_bindir/*
%_datadir/applications/*
%_datadir/pixmaps/*
%_iconsdir/*.png
%_liconsdir/*.png
%_miconsdir/*.png
%_datadir/%name/rawstudio.gtkrc
%_datadir/%name/ui.xml
