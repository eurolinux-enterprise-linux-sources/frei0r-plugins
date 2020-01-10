Name:           frei0r-plugins
Version:        1.3
Release:        11%{?dist}
Summary:        Frei0r - a minimalist plugin API for video effects

Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://www.piksel.org/frei0r
Source0:        http://www.piksel.no/frei0r/releases/frei0r-plugins-%{version}.tar.gz

BuildRequires:  gavl-devel >= 0.2.3
BuildRequires:  opencv-devel >= 1.0.0
     

%description
It is a minimalist plugin API for video sources and filters. The behavior of
the effects can be controlled from the host by simple parameters. The intent is
to solve the recurring re-implementation or adaptation issue of standard effect

%package	opencv
Summary:	Frei0r plugins using OpenCV
Group:		System Environment/License
Requires:	%{name} = %{version}-%{release}

%description opencv
Frei0r plugins that use the OpenCV computer vision framework.

%package -n     frei0r-devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description -n frei0r-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n frei0r-%{version}


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

#Remove installed doc
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}



%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README TODO
%dir %{_libdir}/frei0r-1
%exclude %{_libdir}/frei0r-1/facebl0r.so
%exclude %{_libdir}/frei0r-1/facedetect.so
%{_libdir}/frei0r-1/*.so

%files opencv
%defattr(-,root,root,-)
%{_libdir}/frei0r-1/facebl0r.so
%{_libdir}/frei0r-1/facedetect.so

%files -n frei0r-devel
%defattr(-,root,root,-)
%{_includedir}/frei0r.h
%{_libdir}/pkgconfig/frei0r.pc

%changelog
* Wed Jul 17 2013 Matthias Clasen <mclasen@redhat.com> 1.3-11
- Fix source url

* Mon May 06 2013 Adam Jackson <ajax@redhat.com> 1.3-10
- Move OpenCV plugins to a subpackage

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 10 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.3-8
- Rebuilt for opencv built without nonfree/gpu modules
- Improve description

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.3-6
- Rebuilt for OpenCV 2.4.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 10 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.3-4
- Fix unowned directory - rhbz#744889

* Sun Aug 21 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.3-3
- Rebuild for OpenCV 2.3.1

* Fri May 27 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.3-1
- Update to 1.3

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 06 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.2.1-2
- Rebuild for OpenCV 2.2

* Fri Nov 26 2010 Nicolas Chauvet <kwizart@gmail.com> - 1.2.1-1
- Update to 1.2.1

* Sat Jun 26 2010 Nicolas Chauvet <kwizart@gmail.com> - 1.1.22-5
- Rebuilt for opencv

* Sat Feb 27 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 1.1.22-4
- Rebuild for opencv SO version change

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 22 2009 kwizart < kwizart at gmail.com > - 1.1.22-2
- Rebuild for opencv

* Tue Mar 24 2009 kwizart < kwizart at gmail.com > - 1.1.22-1
- Update to 1.1.22
- Prevent timestamp change when installing

* Tue Jul 22 2008 kwizart < kwizart at gmail.com > - 1.1.21-2
- Add gcc43 patches

* Sat Jun  7 2008 kwizart < kwizart at gmail.com > - 1.1.21-1
- Initial spec file for Fedora.

