%define major 1
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

%define libtextautocorrection %{mklibname KF5TextAutoCorrection}
%define libtextautocorrectioncore %{mklibname KF5TextAutoCorrectionCore}
%define libtextautocorrectionwidgets %{mklibname KF5TextAutoCorrectionWidgets}
%define libtextedittexttospeech %{mklibname KF5TextEditTextToSpeech}
%define libtextgrammarcheck %{mklibname KF5TextGrammarCheck}
%define libtexttranslator %{mklibname KF5TextTranslator}
%define libtexttranslatord %{mklibname KF5TextTranslatorDesigner}
%define libtextemoticons %{mklibname KF5TextEmoticonsCore}
%define libtextemoticonswidgets %{mklibname KF5TextEmoticonsWidgets}
%define libtextaddonswidgets %{mklibname KF5TextAddonsWidgets}
%define libtextcustomeditor %{mklibname KF5TextCustomEditor}
%define libtextcustomeditord %{mklibname KF5TextCustomEditorDesigner}
%define libtextutils %{mklibname KF5TextUtils}
%define devtextautocorrection %{mklibname -d KF5TextAutoCorrection}
%define devtextautocorrectioncore %{mklibname -d KF5TextAutoCorrectionCore}
%define devtextautocorrectionwidgets %{mklibname -d KF5TextAutoCorrectionWidgets}
%define devtextedittexttospeech %{mklibname -d KF5TextEditTextToSpeech}
%define devtextgrammarcheck %{mklibname -d KF5TextGrammarCheck}
%define devtexttranslator %{mklibname -d KF5TextTranslator}
%define devtextemoticons %{mklibname -d KF5TextEmoticonsCore}
%define devtextemoticonswidgets %{mklibname -d KF5TextEmoticonsWidgets}
%define devtextaddonswidgets %{mklibname -d KF5TextAddonsWidgets}
%define devtextcustomeditor %{mklibname -d KF5TextCustomEditor}
%define devtextutils %{mklibname -d KF5TextUtils}

%define lib6textautocorrection %{mklibname KF6TextAutoCorrection}
%define lib6textautocorrectioncore %{mklibname KF6TextAutoCorrectionCore}
%define lib6textautocorrectionwidgets %{mklibname KF6TextAutoCorrectionWidgets}
%define lib6textedittexttospeech %{mklibname KF6TextEditTextToSpeech}
%define lib6textgrammarcheck %{mklibname KF6TextGrammarCheck}
%define lib6texttranslator %{mklibname KF6TextTranslator}
%define lib6texttranslatord %{mklibname KF6TextTranslatorDesigner}
%define lib6textemoticons %{mklibname KF6TextEmoticonsCore}
%define lib6textemoticonswidgets %{mklibname KF6TextEmoticonsWidgets}
%define lib6textcustomeditor %{mklibname KF6TextCustomEditor}
%define lib6textcustomeditord %{mklibname KF6TextCustomEditorDesigner}
%define lib6textaddonswidgets %{mklibname KF6TextAddonsWidgets}
%define lib6textutils %{mklibname KF6TextUtils}
%define dev6textautocorrection %{mklibname -d KF6TextAutoCorrection}
%define dev6textautocorrectioncore %{mklibname -d KF6TextAutoCorrectionCore}
%define dev6textautocorrectionwidgets %{mklibname -d KF6TextAutoCorrectionWidgets}
%define dev6textedittexttospeech %{mklibname -d KF6TextEditTextToSpeech}
%define dev6textgrammarcheck %{mklibname -d KF6TextGrammarCheck}
%define dev6texttranslator %{mklibname -d KF6TextTranslator}
%define dev6textemoticons %{mklibname -d KF6TextEmoticonsCore}
%define dev6textemoticonswidgets %{mklibname -d KF6TextEmoticonsWidgets}
%define dev6textaddonswidgets %{mklibname -d KF6TextAddonsWidgets}
%define dev6textcustomeditor %{mklibname -d KF6TextCustomEditor}
%define dev6textutils %{mklibname -d KF6TextUtils}

%bcond_without qt5
%bcond_without qt6

Name:		ktextaddons
Version:	1.5.4
Release:	7
#Source0:	http://download.kde.org/%{stable}/ktextaddons/%{name}-%{version}.tar.xz
Source0:	https://invent.kde.org/libraries/ktextaddons/-/archive/v%{version}/ktextaddons-v%{version}.tar.bz2
Summary:	KDE library dealing with text (autocorrection, TTS, grammar, translation, etc.)
URL:		https://invent.kde.org/libraries/ktextaddons
License:	LGPL v2.1
Group:		System/Libraries
BuildRequires:	cmake(ECM)

%if %{with qt5}
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Designer)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5TextToSpeech)
BuildRequires:	cmake(Qt5Keychain)
BuildRequires:  cmake(KF5Sonnet)
BuildRequires:  cmake(KF5SonnetUi)
BuildRequires:  cmake(KF5KIO)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:	cmake(Qt5UiPlugin)
BuildRequires:	qt5-assistant
%endif
%if %{with qt6}
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Designer)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6TextToSpeech)
BuildRequires:	cmake(Qt6Keychain)
BuildRequires:	cmake(KF6Sonnet)
BuildRequires:  cmake(KF6KIO)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:	cmake(Qt6UiPlugin)
%endif
# For QCH format docs
BuildRequires:	doxygen
Requires:	%{libtextautocorrectioncore} = %{EVRD}
Requires:	%{libtextautocorrectionwidgets} = %{EVRD}
Requires:	%{libtextedittexttospeech} = %{EVRD}
Requires:	%{libtextgrammarcheck} = %{EVRD}
Requires:	%{libtexttranslator} = %{EVRD}
Requires:	%{libtextemoticons} = %{EVRD}
Requires:	%{libtextemoticonswidgets} = %{EVRD}
Requires:	%{libtextaddonswidgets} = %{EVRD}

%patchlist
ktextaddons-1.5.4-qt-6.9.patch

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

%package -n %{libtexttranslatord}
Summary: Qt Designer plugin for the KDE library for translating text online
Group: System/Libraries

%description -n %{libtexttranslatord}
Qt Designer plugin for the KDE library for translating text online

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

%package -n %{libtextcustomeditor}
Summary: KDE custom text editor widget
Group: System/Libraries

%description -n %{libtextcustomeditor}
KDE custom text editor widget

%package -n %{libtextcustomeditord}
Summary: Qt Designer plugin for the KDE custom text editor widget
Group: Development/Tools
Requires: %{libtextcustomeditor} = %{EVRD}

%description -n %{libtextcustomeditord}
Qt Designer plugin for the KDE custom text editor widget

%package -n %{devtextcustomeditor}
Summary: Development files for KDE custom text editor
Group: Development/C++
Requires: %{libtextcustomeditor} = %{EVRD}

%description -n %{devtextcustomeditor}
Development files for the KDE custom text editor

%package -n %{libtextutils}
Summary: KDE text utility library
Group: System/Libraries

%description -n %{libtextutils}
KDE text utility library

%package -n %{devtextutils}
Summary: Development files for the KDE text utility library
Group: Development/C++
Requires: %{libtextutils} = %{EVRD}

%description -n %{devtextutils}
Development files for the KDE text utility library

%package -n %{lib6textautocorrectioncore}
Summary: KDE library for text autocorrection (non-GUI)
Group: System/Libraries

%description -n %{lib6textautocorrectioncore}
KDE library for text autocorrection (non-GUI)

%package -n %{dev6textautocorrectioncore}
Summary: Development files for the KDE Text Autocorrection library (non-GUI)
Group: Development/C++
Requires: %{lib6textautocorrectioncore} = %{EVRD}

%description -n %{dev6textautocorrectioncore}
Development files for the KDE Text Autocorrection library (non-GUI)

%package -n %{lib6textautocorrectionwidgets}
Summary: KDE library for text autocorrection (GUI)
Group: System/Libraries
Requires: %{lib6textautocorrectioncore} = %{EVRD}

%description -n %{lib6textautocorrectionwidgets}
KDE library for text autocorrection (GUI)

%package -n %{dev6textautocorrectionwidgets}
Summary: Development files for the KDE Text Autocorrection library (GUI)
Group: Development/C++
Requires: %{lib6textautocorrectionwidgets} = %{EVRD}

%description -n %{dev6textautocorrectionwidgets}
Development files for the KDE Text Autocorrection library (GUI)

%package -n %{lib6textedittexttospeech}
Summary: KDE library for Text-To-Speech processing
Group: System/Libraries

%description -n %{lib6textedittexttospeech}
KDE library for Text-To-Speech processing

%package -n %{dev6textedittexttospeech}
Summary: Development files for the KDE Text-To-Speech library
Group: Development/C++
Requires: %{lib6textedittexttospeech} = %{EVRD}

%description -n %{dev6textedittexttospeech}
Development files for the KDE Text-To-Speech library

%package -n %{lib6textgrammarcheck}
Summary: KDE library for grammar checking
Group: System/Libraries

%description -n %{lib6textgrammarcheck}
KDE library for grammar checking

%package -n %{dev6textgrammarcheck}
Summary: Development files for the KDE Grammar Check library
Group: Development/C++
Requires: %{lib6textgrammarcheck} = %{EVRD}

%description -n %{dev6textgrammarcheck}
Development files for the KDE Grammar Check library

%package -n %{lib6texttranslator}
Summary: KDE library for translating text online
Group: System/Libraries

%description -n %{lib6texttranslator}
KDE library for translating text online

%package -n %{lib6texttranslatord}
Summary: Qt Designer plugin for the KDE library for translating text online
Group: System/Libraries

%description -n %{lib6texttranslatord}
Qt Designer plugin for the KDE library for translating text online

%package -n %{dev6texttranslator}
Summary: Development files for the KDE Text Translation library
Group: Development/C++
Requires: %{lib6texttranslator} = %{EVRD}

%description -n %{dev6texttranslator}
Development files for the KDE Text Translation library

%package -n %{lib6textemoticons}
Summary: KDE library for emoticon handling
Group: System/Libraries

%description -n %{lib6textemoticons}
KDE library for emoticon handling

%package -n %{dev6textemoticons}
Summary: Development files for the KDE Emoticons library
Group: Development/C++
Requires: %{lib6textemoticons} = %{EVRD}

%description -n %{dev6textemoticons}
Development files for the KDE Emoticons library

%package -n %{lib6textemoticonswidgets}
Summary: KDE library for emoticon widgets
Group: System/Libraries

%description -n %{lib6textemoticonswidgets}
KDE library for emoticon widgets

%package -n %{dev6textemoticonswidgets}
Summary: Development files for KDE Emoticons widgets
Group: Development/C++
Requires: %{lib6textemoticonswidgets} = %{EVRD}

%description -n %{dev6textemoticonswidgets}
Development files for KDE Emoticons widgets

%package -n %{lib6textaddonswidgets}
Summary: KDE library for text addon widgets
Group: System/Libraries

%description -n %{lib6textaddonswidgets}
KDE library for text addon widgets

%package -n %{dev6textaddonswidgets}
Summary: Development files for KDE Text Addon Widgets
Group: Development/C++
Requires: %{lib6textaddonswidgets} = %{EVRD}

%description -n %{dev6textaddonswidgets}
Development files for the KDE Text Addon Widgets

%package -n %{lib6textcustomeditor}
Summary: KDE custom text editor widget
Group: System/Libraries

%description -n %{lib6textcustomeditor}
KDE custom text editor widget

%package -n %{lib6textcustomeditord}
Summary: Qt Designer plugin for the KDE custom text editor widget
Group: Development/Tools
Requires: %{lib6textcustomeditor} = %{EVRD}

%description -n %{lib6textcustomeditord}
Qt Designer plugin for the KDE custom text editor widget

%package -n %{dev6textcustomeditor}
Summary: Development files for KDE custom text editor
Group: Development/C++
Requires: %{lib6textcustomeditor} = %{EVRD}

%description -n %{dev6textcustomeditor}
Development files for the KDE custom text editor

%package -n %{lib6textutils}
Summary: KDE text utility library
Group: System/Libraries

%description -n %{lib6textutils}
KDE text utility library

%package -n %{dev6textutils}
Summary: Development files for the KDE text utility library
Group: Development/C++
Requires: %{lib6textutils} = %{EVRD}

%description -n %{dev6textutils}
Development files for the KDE text utility library

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
%autosetup -n %{name}-v%{version} -p1
%if %{with qt5}
%cmake_kde5
cd ..
%endif

%if %{with qt6}
export CMAKE_BUILD_DIR=build6
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja
%endif

%build
%if %{with qt5}
%ninja_build -C build
%endif

%if %{with qt6}
%ninja_build -C build6
%endif

%install
%if %{with qt5}
%ninja_install -C build
%endif

%if %{with qt6}
%ninja_install -C build6
%endif

%find_lang libtextautocorrection
%find_lang libtextedittexttospeech
%find_lang libtextemoticons
%find_lang libtextgrammarcheck
%find_lang libtexttranslator
%find_lang libtextgrammarcheck
%find_lang libtextcustomeditor
%find_lang libtextaddonswidgets

%if %{with qt5}
%files -n %{libtextautocorrectioncore}
%{_libdir}/libKF5TextAutoCorrectionCore.so.%{major}*

%files -n %{devtextautocorrectioncore}
%{_libdir}/libKF5TextAutoCorrectionCore.so
%{_libdir}/cmake/KF5TextAutoCorrectionCore
%{_includedir}/KF5/TextAutoCorrectionCore

%files -n %{libtextautocorrectionwidgets} -f libtextautocorrection.lang
%{_libdir}/libKF5TextAutoCorrectionWidgets.so.%{major}*

%files -n %{devtextautocorrectionwidgets}
%{_libdir}/libKF5TextAutoCorrectionWidgets.so
%{_libdir}/cmake/KF5TextAutoCorrectionWidgets
%{_includedir}/KF5/TextAutoCorrectionWidgets

%files -n %{libtextedittexttospeech} -f libtextedittexttospeech.lang
%{_libdir}/libKF5TextEditTextToSpeech.so.%{major}*

%files -n %{devtextedittexttospeech}
%{_libdir}/libKF5TextEditTextToSpeech.so
%{_libdir}/cmake/KF5TextEditTextToSpeech
%{_includedir}/KF5/TextEditTextToSpeech

%files -n %{libtextgrammarcheck} -f libtextgrammarcheck.lang
%{_libdir}/libKF5TextGrammarCheck.so.%{major}*

%files -n %{devtextgrammarcheck}
%{_libdir}/libKF5TextGrammarCheck.so
%{_libdir}/cmake/KF5TextGrammarCheck
%{_includedir}/KF5/TextGrammarCheck

%files -n %{libtexttranslator} -f libtexttranslator.lang
%{_libdir}/libKF5TextTranslator.so.%{major}*
%dir %{_libdir}/qt5/plugins/kf5/translator
%{_libdir}/qt5/plugins/kf5/translator/translator_*.so

%files -n %{libtexttranslatord}
%{_libdir}/qt5/plugins/designer/texttranslatorwidgets5.so

%files -n %{devtexttranslator}
%{_libdir}/libKF5TextTranslator.so
%{_libdir}/cmake/KF5TextTranslator
%{_includedir}/KF5/TextTranslator

%files -n %{libtextaddonswidgets} -f libtextaddonswidgets.lang
%{_libdir}/libKF5TextAddonsWidgets.so*
%{_datadir}/qlogging-categories5/ktextaddons.categories
%{_datadir}/qlogging-categories5/ktextaddons.renamecategories

%files -n %{devtextaddonswidgets}
%{_includedir}/KF5/TextAddonsWidgets
%{_libdir}/cmake/KF5TextAddonsWidgets

%files -n %{libtextemoticons} -f libtextemoticons.lang
%{_libdir}/libKF5TextEmoticonsCore.so*

%files -n %{devtextemoticons}
%{_includedir}/KF5/TextEmoticonsCore
%{_libdir}/cmake/KF5TextEmoticonsCore

%files -n %{libtextemoticonswidgets}
%{_libdir}/libKF5TextEmoticonsWidgets.so*

%files -n %{devtextemoticonswidgets}
%{_includedir}/KF5/TextEmoticonsWidgets
%{_libdir}/cmake/KF5TextEmoticonsWidgets

%files -n %{libtextcustomeditor} -f libtextcustomeditor.lang
%{_libdir}/libKF5TextCustomEditor.so*

%files -n %{libtextcustomeditord}
%{_libdir}/qt5/plugins/designer/textcustomeditor.so

%files -n %{devtextcustomeditor}
%{_includedir}/KF5/TextCustomEditor
%{_libdir}/cmake/KF5TextCustomEditor

%files -n %{libtextutils}
%{_libdir}/libKF5TextUtils.so*

%files -n %{devtextutils}
%{_includedir}/KF5/TextUtils
%{_libdir}/cmake/KF5TextUtils
%endif

%if %{with qt6}
%files -n %{lib6textautocorrectioncore}
%{_libdir}/libKF6TextAutoCorrectionCore.so.%{major}*

%files -n %{dev6textautocorrectioncore}
%{_libdir}/libKF6TextAutoCorrectionCore.so
%{_libdir}/cmake/KF6TextAutoCorrectionCore
%{_includedir}/KF6/TextAutoCorrectionCore

%files -n %{lib6textautocorrectionwidgets} -f libtextautocorrection.lang
%{_libdir}/libKF6TextAutoCorrectionWidgets.so.%{major}*

%files -n %{dev6textautocorrectionwidgets}
%{_libdir}/libKF6TextAutoCorrectionWidgets.so
%{_libdir}/cmake/KF6TextAutoCorrectionWidgets
%{_includedir}/KF6/TextAutoCorrectionWidgets

%files -n %{lib6textedittexttospeech} -f libtextedittexttospeech.lang
%{_libdir}/libKF6TextEditTextToSpeech.so.%{major}*

%files -n %{dev6textedittexttospeech}
%{_libdir}/libKF6TextEditTextToSpeech.so
%{_libdir}/cmake/KF6TextEditTextToSpeech
%{_includedir}/KF6/TextEditTextToSpeech

%files -n %{lib6textgrammarcheck} -f libtextgrammarcheck.lang
%{_libdir}/libKF6TextGrammarCheck.so.%{major}*

%files -n %{dev6textgrammarcheck}
%{_libdir}/libKF6TextGrammarCheck.so
%{_libdir}/cmake/KF6TextGrammarCheck
%{_includedir}/KF6/TextGrammarCheck

%files -n %{lib6texttranslator} -f libtexttranslator.lang
%{_libdir}/libKF6TextTranslator.so.%{major}*
%dir %{_libdir}/qt6/plugins/kf6/translator
%{_libdir}/qt6/plugins/kf6/translator/translator_*.so

%files -n %{lib6texttranslatord}
%{_libdir}/qt6/plugins/designer/texttranslatorwidgets6.so

%files -n %{dev6texttranslator}
%{_libdir}/libKF6TextTranslator.so
%{_libdir}/cmake/KF6TextTranslator
%{_includedir}/KF6/TextTranslator

%files -n %{lib6textaddonswidgets} -f libtextaddonswidgets.lang
%{_libdir}/libKF6TextAddonsWidgets.so*
%{_datadir}/qlogging-categories6/ktextaddons.categories
%{_datadir}/qlogging-categories6/ktextaddons.renamecategories

%files -n %{dev6textaddonswidgets}
%{_includedir}/KF6/TextAddonsWidgets
%{_libdir}/cmake/KF6TextAddonsWidgets

%files -n %{lib6textemoticons} -f libtextemoticons.lang
%{_libdir}/libKF6TextEmoticonsCore.so*

%files -n %{dev6textemoticons}
%{_includedir}/KF6/TextEmoticonsCore
%{_libdir}/cmake/KF6TextEmoticonsCore

%files -n %{lib6textemoticonswidgets}
%{_libdir}/libKF6TextEmoticonsWidgets.so*

%files -n %{dev6textemoticonswidgets}
%{_includedir}/KF6/TextEmoticonsWidgets
%{_libdir}/cmake/KF6TextEmoticonsWidgets

%files -n %{lib6textcustomeditor} -f libtextcustomeditor.lang
%{_libdir}/libKF6TextCustomEditor.so*

%files -n %{lib6textcustomeditord}
%{_qtdir}/plugins/designer/textcustomeditor.so

%files -n %{dev6textcustomeditor}
%{_includedir}/KF6/TextCustomEditor
%{_libdir}/cmake/KF6TextCustomEditor

%files -n %{lib6textutils}
%{_libdir}/libKF6TextUtils.so*

%files -n %{dev6textutils}
%{_includedir}/KF6/TextUtils
%{_libdir}/cmake/KF6TextUtils
%endif

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
