@echo off
echo Setting up Video Downloader Bot...

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

:: Create virtual environment
echo Creating virtual environment...
python -m venv venv

:: Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

:: Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

:: Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

:: Check if .env file exists
if not exist .env (
    echo Creating .env file from template...
    copy .env.example .env
    echo.
    echo Please edit .env file with your configuration values:
    echo - API_ID and API_HASH from my.telegram.org
    echo - BOT_TOKEN from @BotFather
    echo - STORAGE_CHANNEL_ID for file storage
    echo - ADMIN_IDS for admin access
    echo.
    pause
)

:: Create directories
echo Creating directories...
if not exist logs mkdir logs
if not exist db mkdir db

echo.
echo Setup completed!
echo.
echo To start the bot:
echo 1. Activate the virtual environment: venv\Scripts\activate
echo 2. Run the bot: python main.py
echo.
pause
