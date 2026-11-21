@echo off
setlocal enabledelayedexpansion

title QUANTUM GRAVITY - Scientific Interactive Presentation

echo =========================================================================
echo  QUANTUM GRAVITY: Unifying the Universe and the Future of Technology
echo  Automated Launch System
echo =========================================================================
echo.

:: Navigate to project directory
cd /d "%~dp0"
echo [INFO] Current Directory: %CD%

:: Check Python availability
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not found in PATH!
    echo Please install Python 3.10+ and ensure it is added to system PATH.
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do set PYTHON_VER=%%i
echo [INFO] Detected: %PYTHON_VER%

:: Install missing dependencies if required
echo [INFO] Checking Python dependencies...
python -m pip install -r requirements.txt --quiet >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARN] Dependency check encountered issues. Attempting to proceed...
)

:: Run MATLAB runner / Python calculation pipeline if results missing
if not exist "results\quantum_gravity_data.json" (
    echo [INFO] Pre-generating numerical calculation data and plots...
    python matlab_runner.py
)

:: Generate audio assets if missing
if not exist "static\audio\cinematic_music.wav" (
    echo [INFO] Pre-generating audio assets...
    python generate_assets.py
)

:: Generate SVG vector assets if missing
if not exist "static\images\lab_background.svg" (
    echo [INFO] Pre-generating vector SVG assets...
    python generate_svgs.py
)

:: Launch browser in background after short delay
echo [INFO] Opening presentation at http://127.0.0.1:5000/ ...
start "" http://127.0.0.1:5000/

:: Start Flask server
echo [INFO] Starting Flask server...
echo Press CTRL+C to terminate server.
echo.
python app.py

pause
