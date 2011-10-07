# NOTE:		perl-AnyEvent requires perl(Core::{Event,Signal})
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
Version:	6.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/ML/MLEHMANN/%{pnam}-%{version}.tar.gz
# Source0-md5:	2ee54f58bced7471f77149e97c73a94f
Patch0:		kill-blocked-test.patch
URL:		http://search.cpan.org/dist/Coro/
BuildRequires:	perl-AnyEvent >= 2:5.0
BuildRequires:	perl-EV >= 1:3.3
BuildRequires:	perl-Event >= 1.08
BuildRequires:	perl-devel >= 1:5.8.2
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	perl-Guard >= 0.5
BuildRequires:	perl-Storable >= 2.15
BuildRequires:	perl-Time-HiRes
BuildRequires:	perl-common-sense
%endif
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
%doc Changes INSTALL README README.linux-glibc
%{perl_vendorarch}/Coro.pm
%{perl_vendorarch}/Coro
%dir %{perl_vendorarch}/auto/Coro
%dir %{perl_vendorarch}/auto/Coro/EV
%{perl_vendorarch}/auto/Coro/EV/EV.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Coro/EV/EV.so
%dir %{perl_vendorarch}/auto/Coro/Event
%{perl_vendorarch}/auto/Coro/Event/Event.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Coro/Event/Event.so
%dir %{perl_vendorarch}/auto/Coro/State
%{perl_vendorarch}/auto/Coro/State/State.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Coro/State/State.so
%{_mandir}/man3/Coro*.3pm*
