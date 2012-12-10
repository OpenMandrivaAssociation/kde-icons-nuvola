
%define base_name	kde-icons
%define theme_name	nuvola
%define version		1.0
%define name		%{base_name}-%{theme_name}
%define rel             9
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
Requires:	kdebase3-progs
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


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-9mdv2011.0
+ Revision: 619901
- the mass rebuild of 2010.0 packages

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 1.0-8mdv2010.0
+ Revision: 438083
- rebuild

* Sun Mar 22 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 1.0-7mdv2009.1
+ Revision: 360337
- Fix Requires

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.0-6mdv2008.1
+ Revision: 140853
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Sep 17 2007 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 1.0-6mdv2008.0
+ Revision: 88898
- Fix Requires (Bug #33668)
- Import kde-icons-nuvola



* Tue Jul 11 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.0-5mdv2007.0
- Rebuild for new extension

* Thu Apr 06 2006 Sebastien Savarin <plouf@mandriva.org> 1.0-4mdk
- Rebuild
- use macros
- use %%mkrel

* Tue Mar 22 2005 Sebastien Savarin <plouf@mandrake.org> 1.0-3mdk
-rename icons kmenu.png > menuk-mdk.png kfm_home.png > home-mdk.png
 icons.png > desktop-mdk.png at build

* Fri Mar 18 2005 Nicolas Lécureuil <neoclust@mandrake.org> 1.0-2mdk
- Rebuild

* Mon Oct 25 2004 Laurent Culioli <laurent@mandrake.org> 1.0-1mdk
- 1.0

* Fri Aug 06 2004 Laurent Culioli <laurent@mandrake.org> 1.0-0.rc1.1mdk
- 1.0-rc1

* Sun May 02 2004 Laurent Culioli <laurent@mandrake.org> 1.0-0.beta.1mdk
- 1.0beta

* Fri Apr 16 2004 Laurent Culioli <laurent@mandrake.org> 0.2.5-2mdk
- make rpmlint happy with perms
- new naming scheme

* Wed Aug 27 2003 Laurent Culioli <laurent@pschit.net> 0.2.5-1mdk
- initial package
