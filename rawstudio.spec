Name:		rawstudio
Version:	1.1
Release:	%mkrel 1
Summary:	Graphical tool to convert raw images of digital cameras
Group:		Graphics
URL:		http://rawstudio.org/
Source0:	http://rawstudio.org/files/release/%{name}-%{version}.tar.gz
License:	GPLv2
BuildRequires:	gtk+2-devel libjpeg-devel libGConf2-devel
BuildRequires:	libtiff-devel zlib-devel lcms-devel ImageMagick
BuildRequires:	libexiv-devel
BuildRequires:  desktop-file-utils
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
rm -rf $RPM_BUILD_DIR/%{name}-%{version}

%setup -q 

%build
%configure

%make

%install

rm -fr %buildroot

%makeinstall_std
%find_lang %{name}

# Icon in desktop file should not have an extension
sed -i -e "s/Icon=\(.*\)\.png$/Icon=\1/" $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


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
