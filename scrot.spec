Summary:	Screen-shot capture using Imlib 2
Summary(pl):	Zrzucanie ekranów przy u¿yciu Imlib2
Name:		scrot
Version:	0.7
Release:	1
License:	BSD
Group:		X11/Applications/Graphics
Source0:	http://linuxbrit.co.uk/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	ea6a26678b677f885d98ccbc0ec01a41
Patch0:		%{name}-ac.patch
URL:		http://linuxbrit.co.uk/scrot/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	giblib-devel >= 1.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A nice and straightforward screen capture utility implementing the
dynamic loaders of imlib2.

%description -l pl
Mi³e i ³atwe w u¿yciu narzêdzie do pobierania zrzutów ekranu
wykorzystuj±ce dynamiczne do³±czanie z imlib2.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README AUTHORS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/%{name}.1*
