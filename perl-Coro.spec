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
Version:	5.26
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/%{pnam}-%{version}.tar.gz
# Source0-md5:	96161bae337944c6bdd2b9b5fb811a6f
URL:		http://search.cpan.org/dist/Coro/
BuildRequires:	perl-AnyEvent >= 2:5.0
BuildRequires:	perl-EV >= 1:3.3
BuildRequires:	perl-Event >= 0.89
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Guard
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
%dir %{perl_vendorarch}/auto/Coro/Event
%dir %{perl_vendorarch}/auto/Coro/State
%{perl_vendorarch}/auto/Coro/EV/*.bs
%{perl_vendorarch}/auto/Coro/Event/*.bs
%{perl_vendorarch}/auto/Coro/State/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Coro/EV/*.so
%attr(755,root,root) %{perl_vendorarch}/auto/Coro/Event/*.so
%attr(755,root,root) %{perl_vendorarch}/auto/Coro/State/*.so
%{_mandir}/man3/*
