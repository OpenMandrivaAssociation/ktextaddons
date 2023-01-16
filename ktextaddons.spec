%define major 1
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

%define libtextautocorrection %{mklibname KF5TextAutoCorrection}
%define libtextedittexttospeech %{mklibname KF5TextEditTextToSpeech}
%define libtextgrammarcheck %{mklibname KF5TextGrammarCheck}
%define libtexttranslator %{mklibname KF5TextTranslator}
%define devtextautocorrection %{mklibname -d KF5TextAutoCorrection}
%define devtextedittexttospeech %{mklibname -d KF5TextEditTextToSpeech}
%define devtextgrammarcheck %{mklibname -d KF5TextGrammarCheck}
%define devtexttranslator %{mklibname -d KF5TextTranslator}

Name:		ktextaddons
Version:	1.0
Release:	1
Source0:	http://download.kde.org/%{stable}/ktextaddons/%{name}-%{version}.tar.xz
Summary:	KDE library dealing with text (autocorrection, TTS, grammar, translation, etc.)
URL:		https://invent.kde.org/libraries/ktextaddons
License:	LGPL v2.1
Group:		System/Libraries
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	cmake(Qt5Keychain)
# For QCH format docs
BuildRequires:	doxygen
BuildRequires:	qt5-assistant
Requires:	%{libtextautocorrection} = %{EVRD}
Requires:	%{libtextedittexttospeech} = %{EVRD}
Requires:	%{libtextgrammarcheck} = %{EVRD}
Requires:	%{libtexttranslator} = %{EVRD}

%description
KDE library dealing with text (autocorrection, TTS, grammar checking,
translation, etc.)

%package -n %{libtextautocorrection}
Summary: KDE library for text autocorrection
Group: System/Libraries

%description -n %{libtextautocorrection}
KDE library for text autocorrection

%package -n %{devtextautocorrection}
Summary: Development files for the KDE Text Autocorrection library
Group: Development/C++
Requires: %{libtextautocorrection} = %{EVRD}

%description -n %{devtextautocorrection}
Development files for the KDE Text Autocorrection library

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

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devtextautocorrection} = %{EVRD}
Suggests: %{devtextedittexttospeech} = %{EVRD}
Suggests: %{devtextgrammarcheck} = %{EVRD}
Suggests: %{devtexttranslator} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files -n %{libtextautocorrection}
%{_libdir}/libKF5TextAutoCorrection.so.%{major}*

%files -n %{devtextautocorrection}
%{_libdir}/libKF5TextAutoCorrection.so
%{_libdir}/cmake/KF5TextAutoCorrection
%{_libdir}/qt5/mkspecs/modules/qt_TextAutoCorrection.pri
%{_includedir}/KF5/TextAutoCorrection

%files -n %{libtextedittexttospeech}
%{_libdir}/libKF5TextEditTextToSpeech.so.%{major}*

%files -n %{devtextedittexttospeech}
%{_libdir}/libKF5TextEditTextToSpeech.so
%{_libdir}/cmake/KF5TextEditTextToSpeech
%{_libdir}/qt5/mkspecs/modules/qt_TextEditTextToSpeech.pri
%{_includedir}/KF5/TextEditTextToSpeech

%files -n %{libtextgrammarcheck}
%{_libdir}/libKF5TextGrammarCheck.so.%{major}*

%files -n %{devtextgrammarcheck}
%{_libdir}/libKF5TextGrammarCheck.so
%{_libdir}/cmake/KF5TextGrammarCheck
%{_libdir}/qt5/mkspecs/modules/qt_TextGrammarCheck.pri
%{_includedir}/KF5/TextGrammarCheck

%files -n %{libtexttranslator}
%{_libdir}/libKF5TextTranslator.so.5*
%{_libdir}/libKF5TextTranslator.so.%{major}*
%dir %{_libdir}/qt5/plugins/kf5/translator
%{_libdir}/qt5/plugins/kf5/translator/translator_*.so

%files -n %{devtexttranslator}
%{_libdir}/libKF5TextTranslator.so
%{_libdir}/cmake/KF5TextTranslator
%{_libdir}/qt5/mkspecs/modules/qt_TextTranslator.pri
%{_includedir}/KF5/TextTranslator

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
