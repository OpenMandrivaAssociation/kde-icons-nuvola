
%define base_name	kde-icons
%define theme_name	nuvola
%define version		1.0
%define name		%{base_name}-%{theme_name}
%define rel             5
%define release		%mkrel %rel
%define summary          Nuvola icons for KDE Desktop


Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{summary}
License:	LGPL
Group:		Graphical desktop/KDE
Source:		http://files.icon-king.com/%{theme_name}-%{version}.tar.bz2
URL:		http://kde-look.org/content/show.php?content=5358
Requires:	kdebase
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot
Obsoletes:	kdemoreartwork-%{theme_name}
Provides:	kdemoreartwork-%{theme_name}

%description
Nuvola SVG evolution of SKY icon theme.
 
 NUVOLA is an SVG based icon theme.
 This mean that all icons where designed with a vector graphics software and 
 then exported to SVG.
 Icons of the KDE version of Nuvola are PNG images (unscalable).
 SVG files are available (not always updated) on my web site in the "svg"
 section.
 


%prep
rm -rf %buildroot
%setup -q -n %{theme_name}

%build


%install
install -d -m 755 %buildroot%_iconsdir/%{theme_name}
install -d -m 755 %buildroot%_iconsdir/%{theme_name}/16x16
install -d -m 755 %buildroot%_iconsdir/%{theme_name}/32x32
install -d -m 755 %buildroot%_iconsdir/%{theme_name}/48x48
install -d -m 755 %buildroot%_iconsdir/icons/%{theme_name}/64x64
install -d -m 755 %buildroot%_iconsdir/%{theme_name}/128x128
cp -fr * %buildroot%_iconsdir/%{theme_name}/
cp -f 16x16/apps/kmenu.png %buildroot%_iconsdir/%{theme_name}/16x16/apps/menuk-mdk.png
cp -f 16x16/apps/icons.png %buildroot%_iconsdir/%{theme_name}/16x16/apps/desktop-mdk.png
cp -f 16x16/apps/kfm_home.png %buildroot%_iconsdir/%{theme_name}/16x16/apps/home-mdk.png
cp -f 32x32/apps/kmenu.png %buildroot%_iconsdir/%{theme_name}/32x32/apps/menuk-mdk.png
cp -f 32x32/apps/icons.png %buildroot%_iconsdir/%{theme_name}/32x32/apps/desktop-mdk.png
cp -f 32x32/apps/kfm_home.png %buildroot%_iconsdir/%{theme_name}/32x32/apps/home-mdk.png
cp -f 48x48/apps/kmenu.png %buildroot%_iconsdir/%{theme_name}/48x48/apps/menuk-mdk.png
cp -f 48x48/apps/icons.png %buildroot%_iconsdir/%{theme_name}/48x48/apps/desktop-mdk.png
cp -f 48x48/apps/kfm_home.png %buildroot%_iconsdir/%{theme_name}/48x48/apps/home-mdk.png
cp -f 64x64/apps/kmenu.png %buildroot%_iconsdir/%{theme_name}/64x64/apps/menuk-mdk.png
cp -f 64x64/apps/icons.png %buildroot%_iconsdir/%{theme_name}/64x64/apps/desktop-mdk.png
cp -f 64x64/apps/kfm_home.png %buildroot%_iconsdir/%{theme_name}/64x64/apps/home-mdk.png
cp -f 128x128/apps/kmenu.png %buildroot%_iconsdir/%{theme_name}/128x128/apps/menuk-mdk.png
cp -f 128x128/apps/icons.png %buildroot%_iconsdir/%{theme_name}/128x128/apps/desktop-mdk.png
cp -f 128x128/apps/kfm_home.png %buildroot%_iconsdir/%{theme_name}/128x128/apps/home-mdk.png




%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc author license.txt readme.txt 
%{_iconsdir}/%{theme_name}/*
