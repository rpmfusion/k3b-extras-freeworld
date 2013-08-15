
Name:    k3b-extras-freeworld
Summary: Additional codec plugins for the k3b CD/DVD burning application
Epoch:   1
Version: 2.0.2
Release: 12%{?dist}

Group:   Applications/Archiving
License: GPLv2+
URL:     http://www.k3b.org/
Source0: http://downloads.sourceforge.net/sourceforge/k3b/k3b-%{version}%{?pre}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
# TODO: bugzilla/document
ExcludeArch: s390 s390x

# upstream patches
Patch244: 0244-Fixed-compilation-with-new-FFMPEG.patch
Patch290: 0290-fix-for-newer-kde-4.7-FindFFMPEG.cmake.patch
Patch312: 0312-Fix-K3B-to-build-with-recent-FFMPEG-versions.patch

BuildRequires: cmake
BuildRequires: flac-devel
BuildRequires: gettext
BuildRequires: kdelibs4-devel
BuildRequires: kdemultimedia-devel
BuildRequires: libdvdread-devel
BuildRequires: libmpcdec-devel
BuildRequires: libmusicbrainz-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: libvorbis-devel
# needed by k3bsetup
#BuildRequires: polkit-qt-devel
BuildRequires: taglib-devel

BuildRequires:  ffmpeg-devel
BuildRequires:  lame-devel
BuildRequires:  libdvdread-devel
BuildRequires:  libmad-devel

Requires:       k3b >= %{epoch}:%{version}


%description
Additional decoder/encoder plugins for k3b, a feature-rich and easy to
handle CD/DVD burning application.



%prep
%setup -q -n k3b-%{version}

%patch244 -p1 -b .0244
%patch290 -p1 -b .0290
%patch312 -p1 -b .0313


%build

mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} \
  ..
popd

#make %{?_smp_mflags} -C %{_target_platform}/libk3bdevice
#make %{?_smp_mflags} -C %{_target_platform}/libk3b
make %{?_smp_mflags} -C %{_target_platform}/plugins/decoder/ffmpeg
make %{?_smp_mflags} -C %{_target_platform}/plugins/decoder/mp3
make %{?_smp_mflags} -C %{_target_platform}/plugins/encoder/lame



%install
rm -rf %{buildroot}

make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/plugins/decoder/ffmpeg
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/plugins/decoder/mp3
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/plugins/encoder/lame


%clean
rm -rf %{buildroot}


%files 
%defattr(-,root,root,-)
%{_kde4_libdir}/kde4/k3bffmpegdecoder.so
%{_kde4_libdir}/kde4/k3blameencoder.so
%{_kde4_libdir}/kde4/k3bmaddecoder.so
%{_kde4_libdir}/kde4/kcm_k3blameencoder.so
%{_kde4_datadir}/kde4/services/k3bffmpegdecoder.desktop
%{_kde4_datadir}/kde4/services/k3blameencoder.desktop
%{_kde4_datadir}/kde4/services/k3bmaddecoder.desktop
%{_kde4_datadir}/kde4/services/kcm_k3blameencoder.desktop


%changelog
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

* Sat Sep 17 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1:2.0.2-1
- update to 2.0.2
- Requires: k3b >= %{epoch}:%{version} rather than just %{version}

* Wed Oct 13 2010 Rex Dieter <rdieter@fedoraproject.org> - 1:2.0.1-2
- rebuild (gcc)

* Mon Sep 13 2010 Rex Dieter <rdieter@fedoraproject.org> - 1:2.0.1-1
- k3b-2.0.1

* Sat Jul 10 2010 Rex Dieter <rdieter@fedoraproject.org> - 1:2.0.0-1
- k3b-2.0.0

* Sun May 23 2010 Rex Dieter <rdieter@fedoraproject.org> - 1:1.92.0-1
- k3b-1.92.0 (rc3)

* Sat May 15 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1:1.91.0-1
- k3b-1.91.0 (rc2)
- fix build with Qt 4.7 (upstream patch by cfeck)
- fix build with FFmpeg 0.6 snapshots (define __STDC_CONSTANT_MACROS)

* Fri Mar 05 2010 Rex Dieter <rdieter@fedoraproject.org> - 1:1.90.0-1
- k3b-1.90.0 (rc1)

* Mon Feb 01 2010 Rex Dieter <rdieter@fedoraproject.org> - 1:1.70.0-1
- k3b-1.70.0 (beta1)

* Fri Dec 18 2009 Rex Dieter <rdieter@fedoraproject.org> - 1:1.69.0-1
- k3b-1.69.0 (alpha4)

* Thu Oct 01 2009 Rex Dieter <rdieter@fedoraproject.org> - 1:1.0.5-7
- Epoch: 1 (F-12 revert to k3b-1.0.5)

* Wed Jun 17 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.66.0-0.1.alpha2
- k3b-1.66.0

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.0.5-6
- rebuild for new F11 features

* Mon Dec 15 2008 Dominik Mierzejewski <rpm@greysector.net> - 1.0.5-5
- fix build with current ffmpeg

* Wed Sep 17 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.0.5-4
- better pkgconfig-based ffmpeg patch
- optimize configure
- License: GPLv2+

* Tue Sep 16 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.0.5-3
- re-enable ffmpeg support

* Mon Sep 15 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.0.5-2
- omit ffmpeg support (for now)

* Mon Sep 15 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.0.5-1
- k3b-extras-freeworld for rpmfusion

* Thu Jan 31 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.0.4-2
- BR: kdelibs3-devel

* Mon Nov 26 2007 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.0.4-1
- Update to 1.0.4 (no relevant changes, however).

* Sat Nov 24 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 1.0.3-2
- rebuilt

* Tue Jul 24 2007 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.0.3-1
- Update to 1.0.3 (fix for mp3 without tags).

* Mon Jun 25 2007 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.0.2-1
- Update to 1.0.2.

* Wed May 30 2007 Rex Dieter <rexdieter[AT]users.sf.net>
- drop extraneous BR's

* Fri Apr 27 2007 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.0.1-1
- Update to 1.0.1 (LAME encoder plugin fix).

* Sat Mar 17 2007 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.0-1
- Upgrade to 1.0 final.

* Sun Feb 18 2007 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.0-0.2.rc6
- Upgrade to 1.0rc6 (which has appeared in Rawhide).

* Tue Feb  6 2007 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.12.17-3
- Rebuild for new ffmpeg.

* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.12.17-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Sun Sep 24 2006 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.12.17-1
- Update to 0.12.17.

* Fri Mar 31 2006 Michael Schwendt <mschwendt[AT]users.sf.net> 0.12.14-2
- Don't build libsndfile plugin anymore, since it moves to k3b-extras.

* Wed Mar 15 2006 Michael Schwendt <mschwendt[AT]users.sf.net> 0.12.14-1
- Update to 0.12.14.
- The oh-so-clever build speed-up trick cannot be used anymore,
  since libtool archives have been dropped from FC k3b package.

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Sat Dec 31 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 0.12.10-0.lvn.1
- Update to 0.12.10.
- Rename package to k3b-extras-nonfree.

* Sun Jul 17 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 0.12.2-0.lvn.1
- Update to 0.12.2 (for FC Development).
- Rename package to k3b-extras.
- Add plugins: ffmpeg decoder, libsndfile decoder, lame encoder.
- Use BR k3b to speed up build.
- Drop explicit Epoch 0.

* Fri May 20 2005 Thorsten Leemhuis <fedora[AT]leemhuis.info> 0:0.11.24-0.lvn.2
- Use configure-parm "--with-qt-libraries=$QTDIR/lib" to fix FC4-x86_64 build

* Wed May 11 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 0:0.11.24-0.lvn.1
- Update to 0.11.24 (advertised as handling mp3 errors better).
- Remove GCC version check which blacklists FC4's GCC (d'oh!).
- Explicity disable external libsamplerate, which is in FE and
  hence FC's k3b doesn't use it either.
- Merge statfs patch from FC's k3b package.

* Thu Mar 24 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 0:0.11.22-0.lvn.1
- Update to 0.11.22 (MAD decoder update).
- Use new switches to disable OggVorbis and FLAC explicitly.

* Wed Jan 26 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 0:0.11.19-0.lvn.1
- Update to 0.11.19 (for another mp3 detection fix).

* Tue Aug 10 2004 Michael Schwendt <mschwendt[AT]users.sf.net> 0:0.11.14-0.lvn.1
- Update to 0.11.14 (which obsoletes patches again).

* Tue Aug 10 2004 Michael Schwendt <mschwendt[AT]users.sf.net> 0:0.11.13-0.lvn.1
- Add patch from CVS to fix mp3 decoder.

* Sat Aug  7 2004 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.11.13-0.lvn.1
- Updated to 0.11.13 (includes new mp3 backport).
- Patch for k3bdiskinfo.cpp is obsolete.
- Now k3bdevice.cpp needs patch for Qt 3.1.
- Remove a few more unneeded BR.

* Thu May 27 2004 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.11.10-0.lvn.1
- Update to 0.11.10 (includes mp3 fixes).
- Fix k3bdiskinfo.cpp for Qt 3.1.
- Remove redundant BR qt-devel.
- Disable RPATH (seems to work now).
- Rename package to k3b-mp3, build just the plugin and all depending targets.
- Delete old changelog entries which are no longer relevant to this package.

* Mon Mar 29 2004 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.11.9-0.fdr.1
- Update to 0.11.9.

* Mon Mar 29 2004 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.11.8-0.fdr.1
- Update to 0.11.8.

* Sun Mar 28 2004 Michael Schwendt <mschwendt[AT]users.sf.net>
- Rewrite the conditional code sections, although they work fine in
  normal build environments and the fedora.us build system. But 'mach'
  makes some weird assumptions about build requirements in spec files
  and causes unexpected results.

