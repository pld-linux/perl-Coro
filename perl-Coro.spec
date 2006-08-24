#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Coro
%define		pnam	Coro
Summary:	Coro - do events the coro-way
Summary(pl):	Coro - obs³uga zdarzeñ na sposób coro
Name:		perl-Coro
Version:	1.9
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	63efa9fb31ded80f2c7d1fb900163824
URL:		http://search.cpan.org/dist/Coro/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module enables you to create programs using the powerful Event
model (and module), while retaining the linear style known from simple
or threaded programs.

%description -l pl
Ten modu³ pozwala na tworzenie programów przy u¿yciu potê¿nego modelu
(i modu³u) Event z zachowaniem liniowego stylu znanego z prostych lub
w±tkowych programów.

%prep
%setup -q -n %{pnam}-%{version}

%build
echo "y
l
16384" | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE ChangeLog README TODO
%{perl_vendorarch}/Coro.pm
%{perl_vendorarch}/Coro
%dir %{perl_vendorarch}/auto/Coro
%{perl_vendorarch}/auto/Coro/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Coro/*.so
%{_mandir}/man3/*
