Name:		rawstudio
Version:	0.6
Release:	%mkrel 1
Summary:	Graphical tool to convert raw images of digital cameras
Group:		Graphics
URL:		http://rawstudio.org/
Source0:	http://rawstudio.org/files/release/%{name}-%{version}.tar.gz
License:	GPL
BuildRequires:	gtk+2-devel libjpeg-devel libGConf2-devel
BuildRequires:	libtiff-devel zlib-devel lcms-devel ImageMagick
BuildRequires:  desktop-file-utils

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
rm -rf $RPM_BUILD_DIR/%{name}-%{version}

%setup -q 

%build
%configure2_5x 

%make

%install

rm -fr %buildroot

%makeinstall_std 

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


install -d %buildroot%{_datadir}/icons/{large,mini}

convert pixmaps/rawstudio.png -resize 32x32 %buildroot%{_iconsdir}/%{name}.png
convert pixmaps/rawstudio.png -resize 16x16 %buildroot%{_miconsdir}/%{name}.png
cp pixmaps/rawstudio.png %buildroot%{_liconsdir}/%{name}.png

%clean
rm -fr %buildroot

%post
%update_desktop_database
%update_menus

%postun
%clean_menus
%clean_desktop_database

%files 
%defattr(-,root,root)
%docdir %{_docdir}/%{name}-%{version}
%doc README
%_bindir/*
%_datadir/applications/*
%_datadir/pixmaps/*
%_iconsdir/*.png
%_liconsdir/*.png
%_miconsdir/*.png
