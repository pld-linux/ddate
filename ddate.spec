Summary:	Convert Gregorian dates to Discordian dates
Summary(pl.UTF-8):	Tłumaczenie dat gregoriańskich na diskordiańskie
Name:		ddate
Version:	0.2.1
Release:	1
License:	Public Domain
Group:		Applications
Source0:	https://github.com/bo0ts/ddate/archive/v%{version}.tar.gz?/%{name}-%{version}.tar.gz
# Source0-md5:	4ca90de7a92ee3038de6d76e2b618b15
# temporarily use util-linux mans tarball
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/util-linux-non-english-man-pages.tar.bz2
# Source1-md5:	3c940c7e7fe699eaa2ddb1bffb3de2fe
URL:		https://github.com/bo0ts/ddate/
BuildRequires:	cmake >= 2.8
BuildRequires:	rpmbuild(macros) >= 1.605
Conflicts:	util-linux < 2.23
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ddate is a utility to convert Gregorian dates to Discordian dates.

%description -l pl.UTF-8
ddate to narzędzie do tłumaczenia dat gregoriańskich na
diskordiańskie.

%prep
%setup -q -a1

%build
%cmake .
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/man1 $RPM_BUILD_ROOT%{_mandir}
for f in man/*/man1/ddate.1 ; do
	install -Dp $f $RPM_BUILD_ROOT%{_mandir}/${f#man/}
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.org
%attr(755,root,root) %{_bindir}/ddate
%{_mandir}/man1/ddate.1*
%lang(es) %{_mandir}/es/man1/ddate.1*
%lang(ja) %{_mandir}/ja/man1/ddate.1*
%lang(ko) %{_mandir}/ko/man1/ddate.1*
