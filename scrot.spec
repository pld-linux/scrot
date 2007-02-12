Summary:	Screen-shot capture using Imlib 2
Summary(pl.UTF-8):	Zrzucanie ekranów przy użyciu Imlib2
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

%description -l pl.UTF-8
Miłe i łatwe w użyciu narzędzie do pobierania zrzutów ekranu
wykorzystujące dynamiczne dołączanie z imlib2.

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_prefix}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README AUTHORS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/%{name}.1*
