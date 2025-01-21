#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Devel-OverloadInfo
Version  : 0.007
Release  : 26
URL      : https://cpan.metacpan.org/authors/id/I/IL/ILMARI/Devel-OverloadInfo-0.007.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IL/ILMARI/Devel-OverloadInfo-0.007.tar.gz
Summary  : 'introspect overloaded operators'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Devel-OverloadInfo-license = %{version}-%{release}
Requires: perl-Devel-OverloadInfo-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(MRO::Compat)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Try::Tiny)

%description
This archive contains the distribution Devel-OverloadInfo,
version 0.007:
introspect overloaded operators

%package dev
Summary: dev components for the perl-Devel-OverloadInfo package.
Group: Development
Provides: perl-Devel-OverloadInfo-devel = %{version}-%{release}
Requires: perl-Devel-OverloadInfo = %{version}-%{release}

%description dev
dev components for the perl-Devel-OverloadInfo package.


%package license
Summary: license components for the perl-Devel-OverloadInfo package.
Group: Default

%description license
license components for the perl-Devel-OverloadInfo package.


%package perl
Summary: perl components for the perl-Devel-OverloadInfo package.
Group: Default
Requires: perl-Devel-OverloadInfo = %{version}-%{release}

%description perl
perl components for the perl-Devel-OverloadInfo package.


%prep
%setup -q -n Devel-OverloadInfo-0.007
cd %{_builddir}/Devel-OverloadInfo-0.007

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Devel-OverloadInfo
cp %{_builddir}/Devel-OverloadInfo-0.007/LICENSE %{buildroot}/usr/share/package-licenses/perl-Devel-OverloadInfo/252145e58792a64dedd5e05316ddbde817434361
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Devel::OverloadInfo.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Devel-OverloadInfo/252145e58792a64dedd5e05316ddbde817434361

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
