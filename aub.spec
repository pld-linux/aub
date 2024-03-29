Summary:	Assemble Usenet Binaries
Summary(pl.UTF-8):	Narzędzie do ściągania binariów z usenetu
Name:		aub
Version:	2.1.3
Release:	3
License:	GPL
Group:		Applications/News
Source0:	http://yukidoke.org/~mako/projects/aub/download/%{name}-%{version}.tar.gz
# Source0-md5:	ddbf57eb340199bca978569017061fcb
URL:		http://yukidoke.org/~mako/projects/aub/
BuildRequires:	perl-devel >= 1:5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aub is a time-tested Perl program to download articles from newsgroups
and decode them automatically. It is simple, well documented, and easy
to use and configure. It handles multi-part postings, and both
uuencoded and base64 encodings.

%description -l pl.UTF-8
aub jest programem w Perlu do ściągania artykułów z grup usenetowych i
ich automatycznego dekodowania. Jest prosty, dobrze udokumentowany,
łatwy w użyciu i konfiguracji. Obsługuje przesyłki wieloczęściowe,
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
%{_mandir}/man1/*.1*
