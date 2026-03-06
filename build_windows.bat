@echo off
REM Build script for Windows
REM Run from the project root directory.

setlocal EnableDelayedExpansion

echo === QR Code Generator — Windows build ===

set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

set "VENV_DIR=.venv"

REM 1. Create / reuse virtual environment
if not exist "%VENV_DIR%\Scripts\activate.bat" (
    echo Creating virtual environment...
    python -m venv "%VENV_DIR%"
)

call "%VENV_DIR%\Scripts\activate.bat"

REM 2. Install / upgrade dependencies
echo Installing dependencies...
pip install --upgrade pip -q
pip install -r requirements.txt -q

REM 3. Build with PyInstaller
echo Running PyInstaller...
pyinstaller qrcode_gen.spec --clean --noconfirm

echo.
echo Build complete. Output is in dist\QRCodeGen\
echo Run with: dist\QRCodeGen\QRCodeGen.exe
