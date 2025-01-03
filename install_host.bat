@echo off
reg add "HKCU\Software\Google\Chrome\NativeMessagingHosts\com.your_extension.native" /ve /t REG_SZ /d "%~dp0native_host.json" /f