Name: fstobdf
Version: 1.0.4
Release: %mkrel 3
Summary: Generate BDF font from X font server
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libfs-devel >= 1.0.0
BuildRequires: libx11-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The fstobdf program reads a font from a font server and generate BDF font.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/fstobdf
%{_mandir}/man1/fstobdf.*




%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-2mdv2011.0
+ Revision: 664393
- mass rebuild

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2011.0
+ Revision: 592589
- new release

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-4mdv2010.1
+ Revision: 522674
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.3-3mdv2010.0
+ Revision: 424482
- rebuild

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-2mdv2009.0
+ Revision: 264520
- rebuild early 2009.0 package (before pixel changes)

* Tue May 27 2008 Colin Guthrie <cguthrie@mandriva.org> 1.0.3-1mdv2009.0
+ Revision: 211799
- New version

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-5mdv2008.1
+ Revision: 150087
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 29 2007 Anne Nicolas <ennael@mandriva.org> 1.0.2-4mdv2008.0
+ Revision: 93860
- bump release for upload

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages extension

* Thu Jun 28 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.2-3mdv2008.0
+ Revision: 45342
- rebuild for 2008


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 20:17:57 (31598)
- X11R7.1

* Tue May 16 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-16 23:25:13 (27461)
- fix description

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

