Summary:	Generate BDF font from X font server
Name:		fstobdf
Version:	1.0.7
Release:	1
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org/
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(libfs)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xorg-macros)

%description
The fstobdf program reads a font from a font server and generate BDF font.

%prep
%autosetup -p1

%build
%configure \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/fstobdf
%doc %{_mandir}/man1/fstobdf.*

