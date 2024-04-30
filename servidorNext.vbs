Set WshShell = WScript.CreateObject("WScript.Shell")
obj = WshShell.Run(chr(34) & "%ProgramFiles%\Oracle\VirtualBox\VBoxHeadless.exe" & chr(34) & " -s SRV_NEXTCLOUD", 0,false)
set WshShell = Nothing