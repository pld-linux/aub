Summary:	Assemble Usenet Binaries
Summary(pl):	Narzêdzie do ¶ci±gania binariów z usenetu
Name:		aub
Version:	2.1.2
Release:	1
License:	GPL
Group:		Applications/News
Source0:	http://yukidoke.org/~mako/projects/aub/download/aub-2.1.2.tar.gz
URL:		http://yukidoke.org/~mako/projects/aub/
BuildRequires:	rpm-perlprov
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aub is a time-tested Perl program to download articles from newsgroups
and decode them automatically. It is simple, well documented, and easy
to use and configure. It handles multi-part postings, and both
uuencoded and base64 encodings.

%description -l pl
aub jest programem w Perlu do ¶ci±gania artyku³ów z grup usenetowych i
ich automatycznego dekodowania. Jest prosty, dobrze udokumentowany,
³atwy w u¿yciu i konfiguracji. Obs³uguje przesy³ki wieloczê¶ciowe,
zakodowane uuencode lub base64.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install aub $RPM_BUILD_ROOT%{_bindir}
install aub.1 aubconf.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aub
%{_mandir}/man1/*.1.gz
