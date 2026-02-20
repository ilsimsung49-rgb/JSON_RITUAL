@echo off
echo ==========================================
echo   JSON RITUAL - GitHub Force Sync Bot v3
echo ==========================================
echo.
cd /d "%~dp0"

:: Set Identity
git config user.email "ilsimsung49@gmail.com"
git config user.name "ilsimsung49-rgb"

:: Re-initialize and Force Point to correct GitHub URL
echo [1/3] Repairing Git connection...
git init
git remote remove origin >nul 2>&1
git remote add origin https://github.com/ilsimsung49-rgb/JSON_RITUAL.git

:: Force Update
echo [2/3] Adding all files...
git add .
git commit -m "Deployment Fix: Force update to v6.5.1 Stable"

echo.
echo [3/3] Power Pushing to GitHub...
git branch -M main
git push -u origin main --force

echo.
echo ==========================================
echo   DONE! Please wait 2 minutes and refresh.
echo ==========================================
pause
