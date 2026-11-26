@echo off
echo ========================================================
echo  Starting AI Multi-Platform Content Generator - Frontend
echo ========================================================
set "PATH=%LOCALAPPDATA%\Programs\nodejs;%PATH%"
cd /d "%~dp0frontend"
npm run dev
pause

