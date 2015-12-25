#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Coro
%define		pnam	Coro
Summary:	Coro - do events the coro-way
Summary(pl.UTF-8):	Coro - obsługa zdarzeń na sposób coro
Name:		perl-Coro
Version:	6.41
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/ML/MLEHMANN/%{pnam}-%{version}.tar.gz
# Source0-md5:	882b3606487db94b35ac309bc7025009
Patch0:		kill-blocked-test.patch
URL:		http://search.cpan.org/dist/Coro/
BuildRequires:	perl-AnyEvent >= 2:5.0
BuildRequires:	perl-EV >= 1:4.0
BuildRequires:	perl-Event >= 1.08
BuildRequires:	perl-devel >= 1:5.8.2
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	perl-AnyEvent-Impl-EV
BuildRequires:	perl-AnyEvent-Impl-Event
BuildRequires:	perl-Guard >= 0.5
BuildRequires:	perl-Storable >= 2.15
BuildRequires:	perl-Time-HiRes
BuildRequires:	perl-common-sense
%endif
Requires:	perl-AnyEvent >= 2:5.0
Requires:	perl-BDB >= 1.5
Requires:	perl-EV >= 1:4.0
Requires:	perl-Guard >= 0.5
Requires:	perl-Storable >= 2.15
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module enables you to create programs using the powerful Event
model (and module), while retaining the linear style known from simple
or threaded programs.

%description -l pl.UTF-8
Ten moduł pozwala na tworzenie programów przy użyciu potężnego modelu
(i modułu) Event z zachowaniem liniowego stylu znanego z prostych lub
wątkowych programów.

%prep
%setup -q -n %{pnam}-%{version}
%patch0 -p1

%{__sed} -i "s^/opt/bin/perl^%{_bindir}/perl^" Coro/jit*pl

%build
echo "y" | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} -j1 test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING Changes INSTALL README README.linux-glibc
%{perl_vendorarch}/Coro.pm
%{perl_vendorarch}/Coro
%dir %{perl_vendorarch}/auto/Coro
%dir %{perl_vendorarch}/auto/Coro/EV
%attr(755,root,root) %{perl_vendorarch}/auto/Coro/EV/EV.so
%dir %{perl_vendorarch}/auto/Coro/Event
%attr(755,root,root) %{perl_vendorarch}/auto/Coro/Event/Event.so
%dir %{perl_vendorarch}/auto/Coro/State
%attr(755,root,root) %{perl_vendorarch}/auto/Coro/State/State.so
%{_mandir}/man3/Coro*.3pm*
