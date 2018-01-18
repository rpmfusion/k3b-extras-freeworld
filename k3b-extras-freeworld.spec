Name:    k3b-extras-freeworld
Summary: Provides ffmpeg decoder plugin for the k3b CD/DVD burning application
Epoch:   1
Version: 17.08.3
Release: 2%{?dist}

License: GPLv2+
URL:     http://www.k3b.org/
Source0: https://download.kde.org/stable/applications/%{version}/src/k3b-%{version}.tar.xz

# TODO: bugzilla/document
ExcludeArch: s390 s390x

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: cmake(Qt5Gui)
BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5FileMetaData)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5JobWidgets)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5NewStuff)
BuildRequires: cmake(KF5NotifyConfig)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5XmlGui)

BuildRequires: kf5-libkcddb-devel

BuildRequires: libmpcdec-devel
BuildRequires: pkgconfig(dvdread)
BuildRequires: pkgconfig(flac++)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(taglib)
BuildRequires: pkgconfig(vorbisenc) pkgconfig(vorbisfile)
BuildRequires: pkgconfig(libavcodec) pkgconfig(libavformat)

Requires: k3b >= %{epoch}:%{version}

%description
Provides ffmpeg decoder plugin for k3b, a feature-rich and easy to
handle CD/DVD burning application.


%prep
%autosetup -p1 -n k3b-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} .. \
  -DK3B_BUILD_FFMPEG_DECODER_PLUGIN:BOOL=ON
popd

%make_build -C %{_target_platform}/plugins/decoder/ffmpeg


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/plugins/decoder/ffmpeg


%files 
%{_kf5_qtplugindir}/k3bffmpegdecoder.so
%{_kf5_datadir}/kservices5/k3bffmpegdecoder.desktop


%changelog
* Thu Jan 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:17.08.3-2
- Rebuilt for ffmpeg-3.5 git

* Fri Dec 29 2017 Sérgio Basto <sergio@serjux.com> - 1:17.08.3-1
- Update k3b-extras-freeworld to 17.08.3

* Tue Oct 17 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:17.08.2-1
- Update to 17.08.2

* Wed Oct 11 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:17.08.1-1
- Update to 17.08.1

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1:17.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:17.04.2-1
- Update to 17.04.2

* Mon Jul 10 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:17.04.1-1
- Update to 17.04.1

* Sat Apr 29 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:2.0.3-6
- Rebuild for ffmpeg update

* Thu Mar 23 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:2.0.3-5
- Patch for gcc7

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1:2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jul 30 2016 Julian Sikorski <belegdol@fedoraproject.org> - 1:2.0.3-3
- Rebuilt for ffmpeg-3.1.1

* Wed Jun 22 2016 Leigh Scott <leigh123linux@googlemail.com> - 1:2.0.3-2
- Patch for gcc6
- Patch fot ffmpeg

* Thu Apr 14 2016 Sérgio Basto <sergio@serjux.com> - 1:2.0.3-1
- Update to 2.0.3 .
- Drop all 5 upstream patches .
- Add hack around cmake-related FTBFS .
- Use a new Source URL.

* Fri Apr 08 2016 Adrian Reber <adrian@lisas.de> - 1:2.0.2-22
- remove BR: pkgconfig(libmusicbrainz); package retired in F24

* Mon Oct 20 2014 Sérgio Basto <sergio@serjux.com> - 1:2.0.2-21
- Rebuilt for FFmpeg 2.4.3

* Wed Oct 01 2014 Sérgio Basto <sergio@serjux.com> - 1:2.0.2-20
- Rebuilt again for FFmpeg 2.3.x (with FFmpeg 2.3.x in buildroot)

* Sat Sep 27 2014 kwizart <kwizart@gmail.com> - 1:2.0.2-19
- Rebuilt for FFmpeg 2.3x

* Fri Sep 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 1:2.0.2-18
- Rebuilt for FFmpeg 2.4.x

* Thu Sep 25 2014 Rex Dieter <rdieter@fedoraproject.org> 1:2.0.2-17
- rebuild (ffmpeg-2.4)

* Thu Aug 07 2014 Sérgio Basto <sergio@serjux.com> - 1:2.0.2-16
- Rebuilt for ffmpeg-2.3

* Sat Mar 29 2014 Sérgio Basto <sergio@serjux.com> - 1:2.0.2-15
- Rebuilt for ffmpeg-2.2

* Fri Nov 01 2013 Rex Dieter <rdieter@fedoraproject.org> 1:2.0.2-14
- re-enable ffmpeg support (kde-bug#325486,kde-review#113295)

* Tue Oct 01 2013 Rex Dieter <rdieter@fedoraproject.org> 1:2.0.2-13
- cleanup/rebuild

* Thu Aug 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 1:2.0.2-12
- Rebuilt for FFmpeg 2.0.x

* Sun May 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 1:2.0.2-11
- Rebuilt for x264/FFmpeg

* Tue Apr 09 2013 Rex Dieter <rdieter@fedoraproject.org> 1:2.0.2-10
- rebuild (ffmpeg)

* Sat Nov 24 2012 Nicolas Chauvet <kwizart@gmail.com> - 1:2.0.2-9
- Rebuilt for FFmpeg 1.0

* Sat Oct 13 2012 Rex Dieter <rdieter@fedoraproject.org> 1:2.0.2-8
- more upstream ffmpeg-related fixes

* Tue Jun 26 2012 Nicolas Chauvet <kwizart@gmail.com> - 1:2.0.2-7
- Rebuilt for FFmpeg

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 1:2.0.2-6
- Rebuilt for c++ ABI breakage

* Tue Feb 28 2012 Nicolas Chauvet <kwizart@gmail.com> - 1:2.0.2-5
- Rebuilt for x264/FFmpeg

* Fri Feb 10 2012 Rex Dieter <rdieter@fedoraproject.org> 1:2.0.2-4
- fix for newer FindFFMPEG.cmake

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 1:2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 29 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1:2.0.2-2
- fix build with FFmpeg 0.8 (#1960)

