Name:		rawstudio
Version:	2.0
Release:	5
Summary:	Graphical tool to convert raw images of digital cameras
Group:		Graphics
URL:		http://rawstudio.org/
Source0:	http://rawstudio.org/files/release/%{name}-%{version}.tar.gz
Patch0:		rawstudio-2.0-rosa-linkage.patch
Patch1:		rawstudio-2.0-rosa-libpng.patch
BuildRequires:	pkgconfig(libgphoto2)
License:	GPLv2
BuildRequires:	pkgconfig(gtk+-2.0) jpeg-devel GConf2
BuildRequires:	pkgconfig(libtiff-4) zlib-devel lcms-devel imagemagick
BuildRequires:	pkgconfig(exiv2) flickcurl-devel
BuildRequires:	sqlite3-devel pkgconfig(libxml-2.0) fftw3-devel
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
%makeinstall_std
%find_lang %{name}

install -d %{buildroot}%{_datadir}/icons/{large,mini}

convert pixmaps/rawstudio.png -resize 32x32 %{buildroot}%{_iconsdir}/%{name}.png
convert pixmaps/rawstudio.png -resize 16x16 %{buildroot}%{_miconsdir}/%{name}.png
cp pixmaps/rawstudio.png %{buildroot}%{_liconsdir}/%{name}.png

rm -fr %{buildroot}%{_includedir} %{buildroot}%_libdir/{*.so,*.la,pkgconfig}

%files -f %{name}.lang
%docdir %{_docdir}/%{name}-%{version}
%doc README
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/%name
%{_datadir}/rawspeed
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_iconsdir}/*.png
%{_liconsdir}/*.png
%{_miconsdir}/*.png

