Name:		rawstudio
Version:	2.0
Release:	4
Summary:	Graphical tool to convert raw images of digital cameras
Group:		Graphics
URL:		http://rawstudio.org/
Source0:	http://rawstudio.org/files/release/%{name}-%{version}.tar.gz
Patch0:		rawstudio-2.0-rosa-linkage.patch
Patch1:		rawstudio-2.0-rosa-libpng.patch
BuildRequires:	pkgconfig(libgphoto2)
License:	GPLv2
BuildRequires:	gtk+2-devel libjpeg-devel GConf2
BuildRequires:	pkgconfig(libtiff-4) zlib-devel lcms-devel imagemagick
BuildRequires:	libexiv-devel flickcurl-devel
BuildRequires:	sqlite3-devel libxml2-devel fftw3-devel
BuildRequires:	pkgconfig(libgphoto2)
BuildRequires:	pkgconfig(lensfun)
BuildRequires:	pkgconfig(gconf-2.0)

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
# required for patch0
autoreconf -fi

%configure2_5x --disable-static
%make

%install
rm -fr %buildroot

%makeinstall_std
%find_lang %{name}

install -d %buildroot%{_datadir}/icons/{large,mini}

convert pixmaps/rawstudio.png -resize 32x32 %buildroot%{_iconsdir}/%{name}.png
convert pixmaps/rawstudio.png -resize 16x16 %buildroot%{_miconsdir}/%{name}.png
cp pixmaps/rawstudio.png %buildroot%{_liconsdir}/%{name}.png

rm -fr %buildroot%_includedir %buildroot%_libdir/{*.so,*.la,pkgconfig}

%files -f %{name}.lang
%docdir %{_docdir}/%{name}-%{version}
%doc README
%_bindir/*
%_libdir/*.so.*
%_datadir/%name
%_datadir/rawspeed
%_datadir/applications/*
%_datadir/pixmaps/*
%_iconsdir/*.png
%_liconsdir/*.png
%_miconsdir/*.png


%changelog
* Fri Apr 08 2011 Funda Wang <fwang@mandriva.org> 2.0-1mdv2011.0
+ Revision: 651970
- New version 2.0

* Wed Dec 01 2010 Funda Wang <fwang@mandriva.org> 1.2-6mdv2011.0
+ Revision: 604408
- rebuild for new exiv2

* Tue Aug 03 2010 Funda Wang <fwang@mandriva.org> 1.2-5mdv2011.0
+ Revision: 565569
- rebuild for new exiv2

* Sat Jan 16 2010 Funda Wang <fwang@mandriva.org> 1.2-4mdv2010.1
+ Revision: 492264
- rebuild for libjpeg v8

* Wed Dec 30 2009 Frederik Himpe <fhimpe@mandriva.org> 1.2-3mdv2010.1
+ Revision: 484209
- Rebuild for new libexiv2

* Sun Aug 23 2009 Funda Wang <fwang@mandriva.org> 1.2-2mdv2010.0
+ Revision: 420217
- fix build with newer glibc
- rebuild for new libjpeg v7

* Wed May 06 2009 Frederik Himpe <fhimpe@mandriva.org> 1.2-1mdv2010.0
+ Revision: 372739
- Update to new version 1.2
- Update -Werror=format-security patch

* Sun Jan 04 2009 Funda Wang <fwang@mandriva.org> 1.1-2mdv2009.1
+ Revision: 324541
- fix str fmt

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Fri Oct 10 2008 Frederik Himpe <fhimpe@mandriva.org> 1.1-1mdv2009.1
+ Revision: 291637
- Add BuildRequires libexiv-devel
- update to new version 1.1

* Thu Aug 07 2008 Frederik Himpe <fhimpe@mandriva.org> 1.0-1mdv2009.0
+ Revision: 266849
- Update to new version 1.0
- Add translations and a few other files

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.7-4mdv2009.0
+ Revision: 260074
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.7-3mdv2009.0
+ Revision: 247898
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Feb 25 2008 Frederik Himpe <fhimpe@mandriva.org> 0.7-1mdv2008.1
+ Revision: 175066
- New upstream version
- New license policy
- Remove extension from Icon line in desktop file

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 22 2007 Frederic Crozat <fcrozat@mandriva.com> 0.6-1mdv2008.0
+ Revision: 69136
- Fix BR for x86-64
- Import rawstudio

