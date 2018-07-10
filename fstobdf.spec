Summary:	Generate BDF font from X font server
Name:		fstobdf
Version:	1.0.6
Release:	3
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org/
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(libfs)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xorg-macros)

%description
The fstobdf program reads a font from a font server and generate BDF font.

%prep
%setup -q

%build
%configure	\
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/fstobdf
%{_mandir}/man1/fstobdf.*

