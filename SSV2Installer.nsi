OutFile "SeagullScaringV2Setup.exe"
Name "Seagull Scaring V2"
InstallDir $ProgramFiles\SeagullScaringV2

Section

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
RMDir /r media

RMDir $INSTDIR

SectionEnd