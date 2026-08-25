@echo off
setlocal enabledelayedexpansion
title SANGLIM - Local Web Server
color 0B

set "PORT=8000"
cd /d "%~dp0"

REM ================================================
REM  1. locate index.html
REM ================================================
set "ROOT="
if exist "index.html" set "ROOT=%CD%"
if not defined ROOT if exist "web\index.html" set "ROOT=%CD%\web"
if not defined ROOT if exist "sanglim_web\web\index.html" set "ROOT=%CD%\sanglim_web\web"
if not defined ROOT goto NOINDEX
cd /d "%ROOT%"

REM ================================================
REM  2. find LAN IPv4 address
REM ================================================
set "IP="
for /f "usebackq delims=" %%i in (`powershell -NoProfile -Command "(Get-NetIPAddress -AddressFamily IPv4 ^| Where-Object { $_.IPAddress -ne '127.0.0.1' -and $_.IPAddress -notlike '169.254.*' -and $_.PrefixOrigin -ne 'WellKnown' } ^| Sort-Object InterfaceMetric ^| Select-Object -First 1).IPAddress" 2^>nul`) do set "IP=%%i"
if not defined IP set "IP=[check-ipconfig]"

REM ================================================
REM  3. pick an available server
REM ================================================
python --version >nul 2>&1
if not errorlevel 1 goto USE_PYTHON

py -3 --version >nul 2>&1
if not errorlevel 1 goto USE_PY3

where npx >nul 2>&1
if not errorlevel 1 goto USE_NPX

goto NOSERVER


:USE_PYTHON
set "RUN=python -m http.server %PORT% --bind 0.0.0.0"
set "ENGINE=Python"
goto START

:USE_PY3
set "RUN=py -3 -m http.server %PORT% --bind 0.0.0.0"
set "ENGINE=Python (py launcher)"
goto START

:USE_NPX
set "RUN=npx --yes http-server -p %PORT% -a 0.0.0.0 -c-1"
set "ENGINE=Node (http-server)"
goto START


:START
cls
echo.
echo  ============================================================
echo    SANGLIM TECHNOLOGIES - Local Web Server
echo  ============================================================
echo.
echo    Serving : %ROOT%
echo    Engine  : %ENGINE%
echo.
echo  ------------------------------------------------------------
echo    THIS PC        http://localhost:%PORT%
echo.
echo    SHARE THIS     http://%IP%:%PORT%
echo  ------------------------------------------------------------
echo.
echo    Give the second address to people on the same network.
echo.
echo    NOTE  If Windows Firewall asks for permission,
echo          click ALLOW for Private networks.
echo.
echo    To stop the server: press Ctrl+C, or just close this window.
echo  ============================================================
echo.

start "" "http://localhost:%PORT%"
%RUN%

echo.
echo  Server stopped.
pause
exit /b 0


:NOINDEX
cls
echo.
echo  [ERROR] index.html not found.
echo.
echo  Place this file in the same folder as index.html
echo  (or in the folder that contains the "web" folder) and run again.
echo.
pause
exit /b 1


:NOSERVER
cls
echo.
echo  [ERROR] No web server engine found.
echo.
echo  Install Python (recommended) and run this file again:
echo.
echo      winget install -e --id Python.Python.3.12
echo.
echo  After installing, CLOSE this window, open a new one,
echo  and double-click this file again.
echo.
echo  Alternative: install Node.js and this script will use it.
echo.
pause
exit /b 1
