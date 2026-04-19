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
!insertmacro MUI_PAGE_COMPONENTS
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_WELCOME
!insertmacro MUI_UNPAGE_DIRECTORY
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH

!insertmacro MUI_LANGUAGE "English"

Section "Main program"

    SetOutPath $INSTDIR

    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\SeagullScaringV2" "DisplayName" "SeagullScaringV2"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\SeagullScaringV2" "DisplayVersion" "2.1.1"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\SeagullScaringV2" "Publisher" "Gabriel Alonso-Holt"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\SeagullScaringV2" "DisplayIcon" "$INSTDIR\seagull.ico"
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\SeagullScaringV2" "NoModify" 1
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\SeagullScaringV2" "NoRepair" 1
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\SeagullScaringV2" "UninstallString" "$INSTDIR\uninstall.exe"

    File SeagullScaringV2.exe
    File ssv2cfg.ini
    File seagull.png
    File seagull.ico
    File ssv2_log.txt

    CreateShortcut "$SMPROGRAMS\SeagullScaringV2.lnk" "$INSTDIR\SeagullScaringV2.exe"

    WriteUninstaller $INSTDIR\uninstall.exe

SectionEnd

Section "Gabriel's Seagull Sound Pack"

    File /r media

SectionEnd

Section "Desktop shortcut"

    CreateShortcut "$DESKTOP\SeagullScaringV2.lnk" "$INSTDIR\SeagullScaringV2.exe"

SectionEnd

Section "Uninstall"

    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\SeagullScaringV2"

    Delete $INSTDIR\SeagullScaringV2.exe
    Delete $INSTDIR\ssv2cfg.ini
    Delete $INSTDIR\seagull.png
    Delete $INSTDIR\uninstall.exe
    Delete $INSTDIR\seagull.ico
    Delete $INSTDIR\ssv2_log.txt
    Delete media\seagull.wav
    Delete media\alarm_seagull.wav
    Delete media\confused_seagull.wav
    Delete media\sad_seagull.wav
    Delete media\disgust_seagull.wav
    Delete media\Seagull_2.wav
    Delete media\sea_gull.wav
    Delete media\robot_seagull.wav
    RMDir /r media

    RMDir $INSTDIR

SectionEnd