Summary:	Screen-shot capture using Imlib 2
Summary(pl):	Zrzucanie ekran�w przy u�yciu Imlib2
Name:		scrot
Version:	0.8
Release:	1
License:	BSD
Group:		X11/Applications/Graphics
Source0:	http://linuxbrit.co.uk/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	ccae904d225609571bdd3b03445c1e88
Patch0:		%{name}-ac.patch
URL:		http://linuxbrit.co.uk/scrot/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	giblib-devel >= 1.2.3
BuildRequires:	imlib2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A nice and straightforward screen capture utility implementing the
dynamic loaders of imlib2.

%description -l pl
Mi�e i �atwe w u�yciu narz�dzie do pobierania zrzut�w ekranu
wykorzystuj�ce dynamiczne do��czanie z imlib2.

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
