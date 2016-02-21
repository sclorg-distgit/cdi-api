%global pkg_name cdi-api
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global namedreltag .SP4
%global namedversion %{version}%{?namedreltag}

Name:             %{?scl_prefix}%{pkg_name}
Version:          1.0
Release:          11%{namedreltag}.12%{?dist}
Summary:          CDI API
License:          ASL 2.0
URL:              http://seamframework.org/Weld

# svn export http://anonsvn.jboss.org/repos/weld/cdi-api/tags/1.0-SP4/ cdi-api-1.0.SP4
# tar cafJ cdi-api-1.0.SP4.tar.xz cdi-api-1.0.SP4
Source0:          cdi-api-%{namedversion}.tar.xz

BuildArch:        noarch

BuildRequires:    %{?scl_prefix_java_common}javapackages-tools
BuildRequires:    %{?scl_prefix_java_common}maven-local
BuildRequires:    %{?scl_prefix}maven-compiler-plugin
BuildRequires:    %{?scl_prefix}maven-install-plugin
BuildRequires:    %{?scl_prefix}maven-jar-plugin
BuildRequires:    %{?scl_prefix}maven-javadoc-plugin
BuildRequires:    %{?scl_prefix}maven-surefire-provider-testng
BuildRequires:    %{?scl_prefix}maven-enforcer-plugin
BuildRequires:    %{?scl_prefix}testng
BuildRequires:    %{?scl_prefix}jboss-el-2.2-api
BuildRequires:    %{?scl_prefix}jboss-interceptors-1.1-api
BuildRequires:    %{?scl_prefix}jboss-ejb-3.1-api
BuildRequires:    %{?scl_prefix_java_common}geronimo-annotation
BuildRequires:    %{?scl_prefix}geronimo-parent-poms
BuildRequires:    %{?scl_prefix}weld-parent
BuildRequires:    %{?scl_prefix}maven-plugin-build-helper

%description
APIs for JSR-299: Contexts and Dependency Injection for Java EE

%package javadoc
Summary:          Javadocs for %{pkg_name}

%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%setup -q -n cdi-api-%{namedversion}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_file : %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 1.0-11.SP4.12
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1.0-11.SP4.11
- maven33 rebuild

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.0-11.SP4.10
- Mass rebuild 2015-01-13

* Mon Jan 12 2015 Michael Simacek <msimacek@redhat.com> - 1.0-11.SP4.9
- Rebuild to regenerate requires from java-common

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.0-11.SP4.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-11.SP4.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-11.SP4.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-11.SP4.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-11.SP4.4
- Remove requires on java

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-11.SP4.3
- SCL-ize build-requires
- Migrate from mvn-rpmbuild to %%mvn_build

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-11.SP4.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-11.SP4.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0-11.SP4
- Mass rebuild 2013-12-27

* Wed Nov 13 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-10.SP4
- Add BR: build-helper-maven-plugin

* Sat Mar 02 2013 Mat Booth <fedora@matbooth.co.uk> - 1.0-9.SP4
- Add missing BR, fixes FTBFS rhbz #913916

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8.SP4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0-7.SP4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Dec 04 2012 Marek Goldmann <mgoldman@redhat.com> - 1.0-6.SP4
- Added missing BR

* Tue Dec 04 2012 Marek Goldmann <mgoldman@redhat.com> - 1.0-5.SP4
- Added missing BR/R
- Simplified the spec file
- Removed unnecessary patch

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4.SP4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 25 2012 Asaf Shakarchi <asaf@redhat.com> 1.0-3.SP4
- Fixed changelog versions.

* Wed Mar 16 2012 Asaf Shakarchi <asaf@redhat.com> 1.0-2.SP4
- Added required dependencies, modified patches and cleaned spec.

* Mon Feb 20 2012 Marek Goldmann <mgoldman@redhat.com> 1.0-1.SP4
- Initial packaging

