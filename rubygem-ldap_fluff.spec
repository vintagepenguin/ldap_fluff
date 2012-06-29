%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname ldap_fluff 
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: LDAP integration for Active Directory, Free IPA and posix  
Name: rubygem-%{gemname}
Version: 0.0.6
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://www.redhat.com
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
Requires: rubygem-net-ldap
BuildRequires: rubygems
BuildRequires: rubygem-rake
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

# We often develop on Fedora but deploy to RHEL
%global _binary_filedigest_algorithm 1
%global _source_filedigest_algorithm 1
%global _binary_payload w9.gzdio
%global _source_payload w9.gzdio

%description
Provides multiple implementations of LDAP queries for various backends 


%prep
%setup -q

%build
rake ldap_fluff:gem
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc ./pkg/%{gemname}-%{version}.gem

mkdir -p %{buildroot}/etc
cp %{buildroot}%{gemdir}/gems/%{gemname}-%{version}/etc/ldap_fluff.yml %{buildroot}/etc

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec
%config(noreplace) /etc/ldap_fluff.yml


%changelog
* Fri Jun 29 2012 Jordan OMara <jomara@redhat.com> 0.0.6-1
- Adding some heavy recursive tests (jomara@redhat.com)
- Updating README to fix formatting (jsomara@gmail.com)
- Adding anon_queries to AD config; Fixing AD recursive group walk
  (jomara@redhat.com)
- Fixing a posix merge_filter bug. NEEDS SOME TESTS (jomara@redhat.com)
- Fixing a few minor bugs (jomara@redhat.com)

* Tue Jun 26 2012 Jordan OMara <jomara@redhat.com> 0.0.5-1
- Forgot to remove obsolete files from lib (jomara@redhat.com)

* Tue Jun 26 2012 Jordan OMara <jomara@redhat.com> 0.0.4-1
- rdoc/task -> rake/rdoctask for older rpm support (jomara@redhat.com)
- Updating readme (jomara@redhat.com)

* Tue Jun 26 2012 Jordan OMara <jomara@redhat.com> 0.0.3-1
- Automatic commit of package [rubygem-ldap_fluff] release [0.0.2-1].
  (jomara@redhat.com)

* Tue Jun 26 2012 Jordan OMara <jomara@redhat.com> 0.0.2-1
- new package built with tito

