!include "MUI.nsh"

OutFile "SeagullScaringV2Setup.exe"
Name "Seagull Scaring V2"
InstallDir $ProgramFiles\SeagullScaringV2
BrandingText "Gabriel Alonso-Holt"

!define MUI_HEADERIMAGE_BITMAP "header.bmp"
!define MUI_WELCOMEFINISHPAGE_BITMAP "wizard.bmp"
!define MUI_ICON "setup.ico"

!define MUI_WELCOMEPAGE_TEXT "Setup will guide you through the installation process of Seagull Scaring V2.\n\nYou should close all other application before continuing.\n\nClick Next to continue and Cancel to exit the Setup Wizard."

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE "license.rtf"
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_LANGUAGE "English"

Section ""

    SetOutPath $INSTDIR

    File SeagullScaringV2.exe
    File ssv2cfg.ini
    File seagull.png
    File /r media

    CreateShortcut "$SMPROGRAMS\SeagullScaringV2.lnk" "$INSTDIR\SeagullScaringV2.exe"

    WriteUninstaller $INSTDIR\uninstall.exe

    MessageBox MB_OK "Seagull Scaring V2 has successfully been installed"

SectionEnd

Section "Uninstall"

    Delete $INSTDIR\SeagullScaringV2.exe
    Delete $INSTDIR\ssv2cfg.ini
    Delete $INSTDIR\seagull.png
    Delete $INSTDIR\uninstall.exe
    Delete media\seagull.wav
    Delete media\alarm_seagull.wav
    Delete media\confused_seagull.wav
    Delete media\sad_seagull.wav
    Delete media\disgust_seagull.wav
    Delete media\Seagull_2.wav
    RMDir /r media

    RMDir $INSTDIR

SectionEnd