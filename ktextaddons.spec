%define major 1
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

%define libtextautocorrection %{mklibname KF5TextAutoCorrection}
%define libtextautocorrectioncore %{mklibname KF5TextAutoCorrectionCore}
%define libtextautocorrectionwidgets %{mklibname KF5TextAutoCorrectionWidgets}
%define libtextedittexttospeech %{mklibname KF5TextEditTextToSpeech}
%define libtextgrammarcheck %{mklibname KF5TextGrammarCheck}
%define libtexttranslator %{mklibname KF5TextTranslator}
%define libtextemoticons %{mklibname KF5TextEmoticonsCore}
%define libtextemoticonswidgets %{mklibname KF5TextEmoticonsWidgets}
%define libtextaddonswidgets %{mklibname KF5TextAddonsWidgets}
%define devtextautocorrection %{mklibname -d KF5TextAutoCorrection}
%define devtextautocorrectioncore %{mklibname -d KF5TextAutoCorrectionCore}
%define devtextautocorrectionwidgets %{mklibname -d KF5TextAutoCorrectionWidgets}
%define devtextedittexttospeech %{mklibname -d KF5TextEditTextToSpeech}
%define devtextgrammarcheck %{mklibname -d KF5TextGrammarCheck}
%define devtexttranslator %{mklibname -d KF5TextTranslator}
%define devtextemoticons %{mklibname -d KF5TextEmoticonsCore}
%define devtextemoticonswidgets %{mklibname -d KF5TextEmoticonsWidgets}
%define devtextaddonswidgets %{mklibname -d KF5TextAddonsWidgets}

Name:		ktextaddons
Version:	1.3.2
Release:	1
#Source0:	http://download.kde.org/%{stable}/ktextaddons/%{name}-%{version}.tar.xz
Source0:	https://invent.kde.org/libraries/ktextaddons/-/archive/%{version}/ktextaddons-v%{version}.tar.bz2
Summary:	KDE library dealing with text (autocorrection, TTS, grammar, translation, etc.)
URL:		https://invent.kde.org/libraries/ktextaddons
License:	LGPL v2.1
Group:		System/Libraries
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5TextToSpeech)
BuildRequires:	cmake(Qt5Keychain)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(Qt5UiPlugin)
# For QCH format docs
BuildRequires:	doxygen
BuildRequires:	qt5-assistant
Requires:	%{libtextautocorrectioncore} = %{EVRD}
Requires:	%{libtextautocorrectionwidgets} = %{EVRD}
Requires:	%{libtextedittexttospeech} = %{EVRD}
Requires:	%{libtextgrammarcheck} = %{EVRD}
Requires:	%{libtexttranslator} = %{EVRD}
Requires:	%{libtextemoticons} = %{EVRD}
Requires:	%{libtextemoticonswidgets} = %{EVRD}
Requires:	%{libtextaddonswidgets} = %{EVRD}

%description
KDE library dealing with text (autocorrection, TTS, grammar checking,
translation, etc.)

%package -n %{libtextautocorrectioncore}
Summary: KDE library for text autocorrection (non-GUI)
Group: System/Libraries
Obsoletes: %{libtextautocorrection} < %{EVRD}

%description -n %{libtextautocorrectioncore}
KDE library for text autocorrection (non-GUI)

%package -n %{devtextautocorrectioncore}
Summary: Development files for the KDE Text Autocorrection library (non-GUI)
Group: Development/C++
Requires: %{libtextautocorrectioncore} = %{EVRD}

%description -n %{devtextautocorrectioncore}
Development files for the KDE Text Autocorrection library (non-GUI)

%package -n %{libtextautocorrectionwidgets}
Summary: KDE library for text autocorrection (GUI)
Group: System/Libraries
Requires: %{libtextautocorrectioncore} = %{EVRD}
Obsoletes: %{devtextautocorrection} < %{EVRD}

%description -n %{libtextautocorrectionwidgets}
KDE library for text autocorrection (GUI)

%package -n %{devtextautocorrectionwidgets}
Summary: Development files for the KDE Text Autocorrection library (GUI)
Group: Development/C++
Requires: %{libtextautocorrectionwidgets} = %{EVRD}

%description -n %{devtextautocorrectionwidgets}
Development files for the KDE Text Autocorrection library (GUI)

%package -n %{libtextedittexttospeech}
Summary: KDE library for Text-To-Speech processing
Group: System/Libraries

%description -n %{libtextedittexttospeech}
KDE library for Text-To-Speech processing

%package -n %{devtextedittexttospeech}
Summary: Development files for the KDE Text-To-Speech library
Group: Development/C++
Requires: %{libtextedittexttospeech} = %{EVRD}

%description -n %{devtextedittexttospeech}
Development files for the KDE Text-To-Speech library

%package -n %{libtextgrammarcheck}
Summary: KDE library for grammar checking
Group: System/Libraries

%description -n %{libtextgrammarcheck}
KDE library for grammar checking

%package -n %{devtextgrammarcheck}
Summary: Development files for the KDE Grammar Check library
Group: Development/C++
Requires: %{libtextgrammarcheck} = %{EVRD}

%description -n %{devtextgrammarcheck}
Development files for the KDE Grammar Check library

%package -n %{libtexttranslator}
Summary: KDE library for translating text online
Group: System/Libraries

%description -n %{libtexttranslator}
KDE library for translating text online

%package -n %{devtexttranslator}
Summary: Development files for the KDE Text Translation library
Group: Development/C++
Requires: %{libtexttranslator} = %{EVRD}

%description -n %{devtexttranslator}
Development files for the KDE Text Translation library

%package -n %{libtextemoticons}
Summary: KDE library for emoticon handling
Group: System/Libraries

%description -n %{libtextemoticons}
KDE library for emoticon handling

%package -n %{devtextemoticons}
Summary: Development files for the KDE Emoticons library
Group: Development/C++
Requires: %{libtextemoticons} = %{EVRD}

%description -n %{devtextemoticons}
Development files for the KDE Emoticons library

%package -n %{libtextemoticonswidgets}
Summary: KDE library for emoticon widgets
Group: System/Libraries

%description -n %{libtextemoticonswidgets}
KDE library for emoticon widgets

%package -n %{devtextemoticonswidgets}
Summary: Development files for KDE Emoticons widgets
Group: Development/C++
Requires: %{libtextemoticonswidgets} = %{EVRD}

%description -n %{devtextemoticonswidgets}
Development files for KDE Emoticons widgets

%package -n %{libtextaddonswidgets}
Summary: KDE library for text addon widgets
Group: System/Libraries

%description -n %{libtextaddonswidgets}
KDE library for text addon widgets

%package -n %{devtextaddonswidgets}
Summary: Development files for KDE Text Addon Widgets
Group: Development/C++
Requires: %{libtextaddonswidgets} = %{EVRD}

%description -n %{devtextaddonswidgets}
Development files for the KDE Text Addon Widgets

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devtextautocorrectioncore} = %{EVRD}
Suggests: %{devtextautocorrectionwidgets} = %{EVRD}
Suggests: %{devtextedittexttospeech} = %{EVRD}
Suggests: %{devtextgrammarcheck} = %{EVRD}
Suggests: %{devtexttranslator} = %{EVRD}
Suggests: %{devtextemoticons} = %{EVRD}
Suggests: %{devtextemoticonswidgets} = %{EVRD}
Suggests: %{devtextaddonswidgets} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang libtextautocorrection
%find_lang libtextedittexttospeech
%find_lang libtextemoticons
%find_lang libtextgrammarcheck
%find_lang libtexttranslator
%find_lang libtextgrammarcheck

%files -n %{libtextautocorrectioncore}
%{_libdir}/libKF5TextAutoCorrectionCore.so.%{major}*

%files -n %{devtextautocorrectioncore}
%{_libdir}/libKF5TextAutoCorrectionCore.so
%{_libdir}/cmake/KF5TextAutoCorrectionCore
%{_libdir}/qt5/mkspecs/modules/qt_TextAutoCorrectionCore.pri
%{_includedir}/KF5/TextAutoCorrectionCore

%files -n %{libtextautocorrectionwidgets} -f libtextautocorrection.lang
%{_libdir}/libKF5TextAutoCorrectionWidgets.so.%{major}*

%files -n %{devtextautocorrectionwidgets}
%{_libdir}/libKF5TextAutoCorrectionWidgets.so
%{_libdir}/cmake/KF5TextAutoCorrectionWidgets
%{_libdir}/qt5/mkspecs/modules/qt_TextAutoCorrectionWidgets.pri
%{_includedir}/KF5/TextAutoCorrectionWidgets

%files -n %{libtextedittexttospeech} -f libtextedittexttospeech.lang
%{_libdir}/libKF5TextEditTextToSpeech.so.%{major}*

%files -n %{devtextedittexttospeech}
%{_libdir}/libKF5TextEditTextToSpeech.so
%{_libdir}/cmake/KF5TextEditTextToSpeech
%{_libdir}/qt5/mkspecs/modules/qt_TextEditTextToSpeech.pri
%{_includedir}/KF5/TextEditTextToSpeech

%files -n %{libtextgrammarcheck} -f libtextgrammarcheck.lang
%{_libdir}/libKF5TextGrammarCheck.so.%{major}*

%files -n %{devtextgrammarcheck}
%{_libdir}/libKF5TextGrammarCheck.so
%{_libdir}/cmake/KF5TextGrammarCheck
%{_libdir}/qt5/mkspecs/modules/qt_TextGrammarCheck.pri
%{_includedir}/KF5/TextGrammarCheck

%files -n %{libtexttranslator} -f libtexttranslator.lang
%{_libdir}/libKF5TextTranslator.so.%{major}*
%dir %{_libdir}/qt5/plugins/kf5/translator
%{_libdir}/qt5/plugins/kf5/translator/translator_*.so

%files -n %{devtexttranslator}
%{_libdir}/libKF5TextTranslator.so
%{_libdir}/cmake/KF5TextTranslator
%{_libdir}/qt5/mkspecs/modules/qt_TextTranslator.pri
%{_includedir}/KF5/TextTranslator
%{_libdir}/qt5/plugins/designer/texttranslatorwidgets5.so

%files -n %{libtextaddonswidgets}
%{_libdir}/libKF5TextAddonsWidgets.so*

%files -n %{devtextaddonswidgets}
%{_includedir}/KF5/TextAddonsWidgets
%{_libdir}/cmake/KF5TextAddonsWidgets
%{_libdir}/qt5/mkspecs/modules/qt_textaddonswidgets.pri

%files -n %{libtextemoticons} -f libtextemoticons.lang
%{_libdir}/libKF5TextEmoticonsCore.so*

%files -n %{devtextemoticons}
%{_includedir}/KF5/TextEmoticonsCore
%{_libdir}/cmake/KF5TextEmoticonsCore
%{_libdir}/qt5/mkspecs/modules/qt_textemoticonscore.pri

%files -n %{libtextemoticonswidgets}
%{_libdir}/libKF5TextEmoticonsWidgets.so*

%files -n %{devtextemoticonswidgets}
%{_includedir}/KF5/TextEmoticonsWidgets
%{_libdir}/cmake/KF5TextEmoticonsWidgets
%{_libdir}/qt5/mkspecs/modules/qt_textemoticonswidgets.pri

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
