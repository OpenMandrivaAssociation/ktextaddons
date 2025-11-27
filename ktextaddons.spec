%define major 1
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

%define lib5textautocorrection %{mklibname KF5TextAutoCorrection}
%define lib5textautocorrectioncore %{mklibname KF5TextAutoCorrectionCore}
%define lib5textautocorrectionwidgets %{mklibname KF5TextAutoCorrectionWidgets}
%define lib5textedittexttospeech %{mklibname KF5TextEditTextToSpeech}
%define lib5textgrammarcheck %{mklibname KF5TextGrammarCheck}
%define lib5texttranslator %{mklibname KF5TextTranslator}
%define lib5texttranslatord %{mklibname KF5TextTranslatorDesigner}
%define lib5textemoticons %{mklibname KF5TextEmoticonsCore}
%define lib5textemoticonswidgets %{mklibname KF5TextEmoticonsWidgets}
%define lib5textaddonswidgets %{mklibname KF5TextAddonsWidgets}
%define lib5textcustomeditor %{mklibname KF5TextCustomEditor}
%define lib5textcustomeditord %{mklibname KF5TextCustomEditorDesigner}
%define lib5textutils %{mklibname KF5TextUtils}
%define dev5textautocorrection %{mklibname -d KF5TextAutoCorrection}
%define dev5textautocorrectioncore %{mklibname -d KF5TextAutoCorrectionCore}
%define dev5textautocorrectionwidgets %{mklibname -d KF5TextAutoCorrectionWidgets}
%define dev5textedittexttospeech %{mklibname -d KF5TextEditTextToSpeech}
%define dev5textgrammarcheck %{mklibname -d KF5TextGrammarCheck}
%define dev5texttranslator %{mklibname -d KF5TextTranslator}
%define dev5textemoticons %{mklibname -d KF5TextEmoticonsCore}
%define dev5textemoticonswidgets %{mklibname -d KF5TextEmoticonsWidgets}
%define dev5textaddonswidgets %{mklibname -d KF5TextAddonsWidgets}
%define dev5textcustomeditor %{mklibname -d KF5TextCustomEditor}
%define dev5textutils %{mklibname -d KF5TextUtils}

%define libtextautocorrection %{mklibname KF6TextAutoCorrection}
%define libtextautocorrectioncore %{mklibname KF6TextAutoCorrectionCore}
%define libtextautocorrectionwidgets %{mklibname KF6TextAutoCorrectionWidgets}
%define libtextedittexttospeech %{mklibname KF6TextEditTextToSpeech}
%define libtextgrammarcheck %{mklibname KF6TextGrammarCheck}
%define libtexttranslator %{mklibname KF6TextTranslator}
%define libtexttranslatord %{mklibname KF6TextTranslatorDesigner}
%define libtextemoticons %{mklibname KF6TextEmoticonsCore}
%define libtextemoticonswidgets %{mklibname KF6TextEmoticonsWidgets}
%define libtextcustomeditor %{mklibname KF6TextCustomEditor}
%define libtextcustomeditord %{mklibname KF6TextCustomEditorDesigner}
%define libtextaddonswidgets %{mklibname KF6TextAddonsWidgets}
%define libtextutils %{mklibname KF6TextUtils}
%define libtextautogeneratetext %{mklibname KF6TextAutoGenerateText}
%define libtextspeechtotext %{mklibname KF6TextSpeechToText}
%define devtextautocorrection %{mklibname -d KF6TextAutoCorrection}
%define devtextautocorrectioncore %{mklibname -d KF6TextAutoCorrectionCore}
%define devtextautocorrectionwidgets %{mklibname -d KF6TextAutoCorrectionWidgets}
%define devtextedittexttospeech %{mklibname -d KF6TextEditTextToSpeech}
%define devtextgrammarcheck %{mklibname -d KF6TextGrammarCheck}
%define devtexttranslator %{mklibname -d KF6TextTranslator}
%define devtextemoticons %{mklibname -d KF6TextEmoticonsCore}
%define devtextemoticonswidgets %{mklibname -d KF6TextEmoticonsWidgets}
%define devtextaddonswidgets %{mklibname -d KF6TextAddonsWidgets}
%define devtextcustomeditor %{mklibname -d KF6TextCustomEditor}
%define devtextutils %{mklibname -d KF6TextUtils}
%define devtextautogeneratetext %{mklibname -d KF6TextAutoGenerateText}
%define devtextspeechtotext %{mklibname -d KF6TextSpeechToText}

Name:		ktextaddons
Version:	1.7.1
Release:	2
#Source0:	http://download.kde.org/%{stable}/ktextaddons/%{name}-%{version}.tar.xz
Source0:	https://invent.kde.org/libraries/ktextaddons/-/archive/v%{version}/ktextaddons-v%{version}.tar.bz2
Summary:	KDE library dealing with text (autocorrection, TTS, grammar, translation, etc.)
URL:		https://invent.kde.org/libraries/ktextaddons
License:	LGPL v2.1
Group:		System/Libraries
BuildRequires:	cmake(ECM)

BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Designer)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6MultimediaWidgets)
BuildRequires:	cmake(Qt6Sql)
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
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(Qt6UiPlugin)
# For QCH format docs
BuildRequires:	doxygen
Requires:	%{libtextautocorrectioncore} = %{EVRD}
Requires:	%{libtextautocorrectionwidgets} = %{EVRD}
Requires:	%{libtextedittexttospeech} = %{EVRD}
Requires:	%{libtextgrammarcheck} = %{EVRD}
Requires:	%{libtexttranslator} = %{EVRD}
Requires:	%{libtextemoticons} = %{EVRD}
Requires:	%{libtextemoticonswidgets} = %{EVRD}
Requires:	%{libtextutils} = %{EVRD}
Requires:	%{libtextaddonswidgets} = %{EVRD}
Requires:	%{libtextautogeneratetext} = %{EVRD}
Requires:	%{libtextspeechtotext} = %{EVRD}
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KDE library dealing with text (autocorrection, TTS, grammar checking,
translation, etc.)

%package -n %{libtextautocorrectioncore}
Summary: KDE library for text autocorrection (non-GUI)
Group: System/Libraries
# Qt 5.x is no longer supported, got to get rid of the
# old package somewhere
Obsoletes: %{lib5textautocorrectioncore} < %{EVRD}

%description -n %{libtextautocorrectioncore}
KDE library for text autocorrection (non-GUI)

%package -n %{devtextautocorrectioncore}
Summary: Development files for the KDE Text Autocorrection library (non-GUI)
Group: Development/C++
Requires: %{libtextautocorrectioncore} = %{EVRD}
# Qt 5.x is no longer supported, got to get rid of the
# old package somewhere
Obsoletes: %{dev5textautocorrectioncore} < %{EVRD}

%description -n %{devtextautocorrectioncore}
Development files for the KDE Text Autocorrection library (non-GUI)

%package -n %{libtextautocorrectionwidgets}
Summary: KDE library for text autocorrection (GUI)
Group: System/Libraries
Requires: %{libtextautocorrectioncore} = %{EVRD}
# Qt 5.x is no longer supported, got to get rid of the
# old package somewhere
Obsoletes: %{lib5textautocorrectionwidgets} < %{EVRD}

%description -n %{libtextautocorrectionwidgets}
KDE library for text autocorrection (GUI)

%package -n %{devtextautocorrectionwidgets}
Summary: Development files for the KDE Text Autocorrection library (GUI)
Group: Development/C++
Requires: %{libtextautocorrectionwidgets} = %{EVRD}
# Qt 5.x is no longer supported, got to get rid of the
# old package somewhere
Obsoletes: %{dev5textautocorrectionwidgets} < %{EVRD}

%description -n %{devtextautocorrectionwidgets}
Development files for the KDE Text Autocorrection library (GUI)

%package -n %{libtextedittexttospeech}
Summary: KDE library for Text-To-Speech processing
Group: System/Libraries
# Qt 5.x is no longer supported, got to get rid of the
# old package somewhere
Obsoletes: %{lib5textedittexttospeech} < %{EVRD}

%description -n %{libtextedittexttospeech}
KDE library for Text-To-Speech processing

%package -n %{devtextedittexttospeech}
Summary: Development files for the KDE Text-To-Speech library
Group: Development/C++
Requires: %{libtextedittexttospeech} = %{EVRD}
# Qt 5.x is no longer supported, got to get rid of the
# old package somewhere
Obsoletes: %{dev5textedittexttospeech} < %{EVRD}

%description -n %{devtextedittexttospeech}
Development files for the KDE Text-To-Speech library

%package -n %{libtextgrammarcheck}
Summary: KDE library for grammar checking
Group: System/Libraries
# Qt 5.x is no longer supported, got to get rid of the
# old package somewhere
Obsoletes: %{lib5textgrammarcheck} < %{EVRD}

%description -n %{libtextgrammarcheck}
KDE library for grammar checking

%package -n %{devtextgrammarcheck}
Summary: Development files for the KDE Grammar Check library
Group: Development/C++
Requires: %{libtextgrammarcheck} = %{EVRD}
# Qt 5.x is no longer supported, got to get rid of the
# old package somewhere
Obsoletes: %{dev5textgrammarcheck} < %{EVRD}

%description -n %{devtextgrammarcheck}
Development files for the KDE Grammar Check library

%package -n %{libtexttranslator}
Summary: KDE library for translating text online
Group: System/Libraries
# Qt 5.x is no longer supported, got to get rid of the
# old package somewhere
Obsoletes: %{lib5texttranslator} < %{EVRD}

%description -n %{libtexttranslator}
KDE library for translating text online

%package -n %{libtexttranslatord}
Summary: Qt Designer plugin for the KDE library for translating text online
Group: System/Libraries
# Qt 5.x is no longer supported, got to get rid of the
# old package somewhere
Obsoletes: %{lib5texttranslatord} < %{EVRD}

%description -n %{libtexttranslatord}
Qt Designer plugin for the KDE library for translating text online

%package -n %{devtexttranslator}
Summary: Development files for the KDE Text Translation library
Group: Development/C++
Requires: %{libtexttranslator} = %{EVRD}
# Qt 5.x is no longer supported, got to get rid of the
# old package somewhere
Obsoletes: %{dev5texttranslator} < %{EVRD}

%description -n %{devtexttranslator}
Development files for the KDE Text Translation library

%package -n %{libtextemoticons}
Summary: KDE library for emoticon handling
Group: System/Libraries
# Qt 5.x is no longer supported, got to get rid of the
# old package somewhere
Obsoletes: %{lib5textemoticons} < %{EVRD}

%description -n %{libtextemoticons}
KDE library for emoticon handling

%package -n %{devtextemoticons}
Summary: Development files for the KDE Emoticons library
Group: Development/C++
Requires: %{libtextemoticons} = %{EVRD}
# Qt 5.x is no longer supported, got to get rid of the
# old package somewhere
Obsoletes: %{dev5textemoticons} < %{EVRD}

%description -n %{devtextemoticons}
Development files for the KDE Emoticons library

%package -n %{libtextemoticonswidgets}
Summary: KDE library for emoticon widgets
Group: System/Libraries
# Qt 5.x is no longer supported, got to get rid of the
# old package somewhere
Obsoletes: %{lib5textemoticonswidgets} < %{EVRD}

%description -n %{libtextemoticonswidgets}
KDE library for emoticon widgets

%package -n %{devtextemoticonswidgets}
Summary: Development files for KDE Emoticons widgets
Group: Development/C++
Requires: %{libtextemoticonswidgets} = %{EVRD}
# Qt 5.x is no longer supported, got to get rid of the
# old package somewhere
Obsoletes: %{dev5textemoticonswidgets} < %{EVRD}

%description -n %{devtextemoticonswidgets}
Development files for KDE Emoticons widgets

%package -n %{libtextaddonswidgets}
Summary: KDE library for text addon widgets
Group: System/Libraries
# Qt 5.x is no longer supported, got to get rid of the
# old package somewhere
Obsoletes: %{lib5textaddonswidgets} < %{EVRD}

%description -n %{libtextaddonswidgets}
KDE library for text addon widgets

%package -n %{devtextaddonswidgets}
Summary: Development files for KDE Text Addon Widgets
Group: Development/C++
Requires: %{libtextaddonswidgets} = %{EVRD}
# Qt 5.x is no longer supported, got to get rid of the
# old package somewhere
Obsoletes: %{dev5textaddonswidgets} < %{EVRD}

%description -n %{devtextaddonswidgets}
Development files for the KDE Text Addon Widgets

%package -n %{libtextcustomeditor}
Summary: KDE custom text editor widget
Group: System/Libraries
# Qt 5.x is no longer supported, got to get rid of the
# old package somewhere
Obsoletes: %{lib5textcustomeditor} < %{EVRD}

%description -n %{libtextcustomeditor}
KDE custom text editor widget

%package -n %{libtextcustomeditord}
Summary: Qt Designer plugin for the KDE custom text editor widget
Group: Development/Tools
Requires: %{libtextcustomeditor} = %{EVRD}
# Qt 5.x is no longer supported, got to get rid of the
# old package somewhere
Obsoletes: %{lib5textcustomeditord} < %{EVRD}

%description -n %{libtextcustomeditord}
Qt Designer plugin for the KDE custom text editor widget

%package -n %{devtextcustomeditor}
Summary: Development files for KDE custom text editor
Group: Development/C++
Requires: %{libtextcustomeditor} = %{EVRD}
# Qt 5.x is no longer supported, got to get rid of the
# old package somewhere
Obsoletes: %{dev5textcustomeditor} < %{EVRD}

%description -n %{devtextcustomeditor}
Development files for the KDE custom text editor

%package -n %{libtextutils}
Summary: KDE text utility library
Group: System/Libraries
# Qt 5.x is no longer supported, got to get rid of the
# old package somewhere
Obsoletes: %{lib5textutils} < %{EVRD}

%description -n %{libtextutils}
KDE text utility library

%package -n %{devtextutils}
Summary: Development files for the KDE text utility library
Group: Development/C++
Requires: %{libtextutils} = %{EVRD}
# Qt 5.x is no longer supported, got to get rid of the
# old package somewhere
Obsoletes: %{dev5textutils} < %{EVRD}

%description -n %{devtextutils}
Development files for the KDE text utility library

# AutoGenerateText and SpeechToText were never implemented for Qt5,
# no deprecations needed there
%package -n %{libtextautogeneratetext}
Summary: KDE text auto-generation library
Group: System/Libraries

%description -n %{libtextautogeneratetext}
KDE text auto-generation library

%package -n %{devtextautogeneratetext}
Summary: Development files for the KDE text auto-generation library
Group: Development/C++
Requires: %{libtextautogeneratetext} = %{EVRD}

%description -n %{devtextautogeneratetext}
Development files for the KDE text auto-generation library

%package -n %{libtextspeechtotext}
Summary: KDE speech-to-text library
Group: System/Libraries

%description -n %{libtextspeechtotext}
KDE speech-to-text library

%package -n %{devtextspeechtotext}
Summary: Development files for the KDE speech-to-text library
Group: Development/C++
Requires: %{libtextspeechtotext} = %{EVRD}

%description -n %{devtextspeechtotext}
Development files for the KDE speech-to-text library

%install -a
%find_lang libtextautocorrection
%find_lang libtextedittexttospeech
%find_lang libtextemoticons
%find_lang libtextgrammarcheck
%find_lang libtexttranslator
%find_lang libtextgrammarcheck
%find_lang libtextcustomeditor
%find_lang libtextaddonswidgets
%find_lang libtextautogeneratetext
%find_lang libtextspeechtotext

%files -n %{libtextautocorrectioncore}
%{_libdir}/libKF6TextAutoCorrectionCore.so.%{major}*

%files -n %{devtextautocorrectioncore}
%{_libdir}/libKF6TextAutoCorrectionCore.so
%{_libdir}/cmake/KF6TextAutoCorrectionCore
%{_includedir}/KF6/TextAutoCorrectionCore

%files -n %{libtextautocorrectionwidgets} -f libtextautocorrection.lang
%{_libdir}/libKF6TextAutoCorrectionWidgets.so.%{major}*

%files -n %{devtextautocorrectionwidgets}
%{_libdir}/libKF6TextAutoCorrectionWidgets.so
%{_libdir}/cmake/KF6TextAutoCorrectionWidgets
%{_includedir}/KF6/TextAutoCorrectionWidgets

%files -n %{libtextedittexttospeech} -f libtextedittexttospeech.lang
%{_libdir}/libKF6TextEditTextToSpeech.so.%{major}*

%files -n %{devtextedittexttospeech}
%{_libdir}/libKF6TextEditTextToSpeech.so
%{_libdir}/cmake/KF6TextEditTextToSpeech
%{_includedir}/KF6/TextEditTextToSpeech

%files -n %{libtextgrammarcheck} -f libtextgrammarcheck.lang
%{_libdir}/libKF6TextGrammarCheck.so.%{major}*

%files -n %{devtextgrammarcheck}
%{_libdir}/libKF6TextGrammarCheck.so
%{_libdir}/cmake/KF6TextGrammarCheck
%{_includedir}/KF6/TextGrammarCheck

%files -n %{libtexttranslator} -f libtexttranslator.lang
%{_libdir}/libKF6TextTranslator.so.%{major}*
%dir %{_libdir}/qt6/plugins/kf6/translator
%{_libdir}/qt6/plugins/kf6/translator/translator_*.so

%files -n %{libtexttranslatord}
%{_libdir}/qt6/plugins/designer/texttranslatorwidgets6.so

%files -n %{devtexttranslator}
%{_libdir}/libKF6TextTranslator.so
%{_libdir}/cmake/KF6TextTranslator
%{_includedir}/KF6/TextTranslator

%files -n %{libtextaddonswidgets} -f libtextaddonswidgets.lang
%{_libdir}/libKF6TextAddonsWidgets.so*
%{_datadir}/qlogging-categories6/ktextaddons.categories
%{_datadir}/qlogging-categories6/ktextaddons.renamecategories

%files -n %{devtextaddonswidgets}
%{_includedir}/KF6/TextAddonsWidgets
%{_libdir}/cmake/KF6TextAddonsWidgets

%files -n %{libtextemoticons} -f libtextemoticons.lang
%{_libdir}/libKF6TextEmoticonsCore.so*

%files -n %{devtextemoticons}
%{_includedir}/KF6/TextEmoticonsCore
%{_libdir}/cmake/KF6TextEmoticonsCore

%files -n %{libtextemoticonswidgets}
%{_libdir}/libKF6TextEmoticonsWidgets.so*

%files -n %{devtextemoticonswidgets}
%{_includedir}/KF6/TextEmoticonsWidgets
%{_libdir}/cmake/KF6TextEmoticonsWidgets

%files -n %{libtextcustomeditor} -f libtextcustomeditor.lang
%{_libdir}/libKF6TextCustomEditor.so*

%files -n %{libtextcustomeditord}
%{_qtdir}/plugins/designer/textcustomeditor.so

%files -n %{devtextcustomeditor}
%{_includedir}/KF6/TextCustomEditor
%{_libdir}/cmake/KF6TextCustomEditor

%files -n %{libtextutils}
%{_libdir}/libKF6TextUtils.so*

%files -n %{devtextutils}
%{_includedir}/KF6/TextUtils
%{_libdir}/cmake/KF6TextUtils

%files -n %{libtextautogeneratetext} -f libtextautogeneratetext.lang
%{_libdir}/libKF6TextAutoGenerateText.so.%{major}*
%{_libdir}/libtextautogenerate-cmark-rc-copy.so*
%{_libdir}/libtextautogenerategenericnetwork.so*
%{_libdir}/libtextautogenerateollama.so*
%dir %{_qtdir}/plugins/kf6/textautogeneratetext
%{_qtdir}/plugins/kf6/textautogeneratetext/autogeneratetext_genericnetwork.so
%{_qtdir}/plugins/kf6/textautogeneratetext/autogeneratetext_ollama.so

%files -n %{devtextautogeneratetext}
%{_libdir}/libKF6TextAutoGenerateText.so
%{_libdir}/cmake/KF6TextAutoGenerateText
%{_includedir}/KF6/TextAutoGenerateText
%{_libdir}/cmake/textautogenerate-cmark-rc-copy

%files -n %{libtextspeechtotext} -f libtextspeechtotext.lang
%{_libdir}/libKF6TextSpeechToText.so.%{major}*
%dir %{_qtdir}/plugins/kf6/speechtotext
%{_qtdir}/plugins/kf6/speechtotext/speechtotext_google.so
%{_qtdir}/plugins/kf6/speechtotext/speechtotext_whisper.so

%files -n %{devtextspeechtotext}
%{_libdir}/libKF6TextSpeechToText.so
%{_libdir}/cmake/KF6TextSpeechToText
%{_includedir}/KF6/TextSpeechToText
