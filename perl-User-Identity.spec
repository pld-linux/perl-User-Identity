#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	User
%define	pnam	Identity
Summary:	Mail::Identity - an e-mail role
#Summary(pl.UTF-8):
Name:		perl-User-Identity
Version:	0.99
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/MA/MARKOV/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c5c61e5c05b20bafcb293b2b2fdddc4b
URL:		http://search.cpan.org/dist/User-Identity/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Pod >= 1
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Mail::Identity object contains the description of role played by a
human when sending e-mail. Most people have more than one role these
days: for instance, a private and a company role with different e-mail
addresses.

An Mail::Identity object combines an e-mail address, user description
("phrase"), a signature, pgp-key, and so on. All fields are optional,
and some fields are smart. One such set of data represents one role.
Mail::Identity is therefore the smart cousine of the Mail::Address
object.

# %description -l pl.UTF-8 # TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/User
%{perl_vendorlib}/User/*.pm
%{perl_vendorlib}/User/Identity
%{perl_vendorlib}/Mail/Identity.pm
%{_mandir}/man3/*
