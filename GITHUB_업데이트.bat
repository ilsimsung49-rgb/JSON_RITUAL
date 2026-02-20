@echo off
echo ==========================================
echo   JSON RITUAL - GitHub Force Sync Bot v2
echo ==========================================
echo.
cd /d "%~dp0"

:: 1. Git Identity Setup (Required for new repo)
echo [0/4] Setting up identity...
git config user.email "ilsimsung49@gmail.com"
git config user.name "ilsimsung49-rgb"

:: 2. Initialize or repair Git
if not exist ".git" (
    echo [1/4] Initializing Git repository...
    git init
    git remote add origin https://github.com/ilsimsung49-rgb/JSON_RITUAL.git
) else (
    echo [1/4] Git already initialized. Checking remote...
    git remote remove origin >nul 2>&1
    git remote add origin https://github.com/ilsimsung49-rgb/JSON_RITUAL.git
)

:: 3. Add and Commit
echo [2/4] Adding changes...
git add .
echo.
echo [3/4] Committing changes...
git commit -m "Final Sync: Master Fusion v6.4 Deployment"

echo.
echo [4/4] Pushing to GitHub...
echo (If this stops here, please check for a GitHub login window)
:: Ensure we are on 'main' branch name
git branch -M main
git push -u origin main --force

echo.
echo ==========================================
echo   Task Complete! Your Web App is updating.
echo ==========================================
echo Please wait 2 minutes for the site to refresh.
pause
