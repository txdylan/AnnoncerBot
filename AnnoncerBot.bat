@echo off
title Discord Annoncer
color 03
:1
echo Discord Annoncer
echo.
echo   [0] Install Required Files
echo   [1] Start Announcing!!
echo.
choice /c 01 /n /m ":~$"
if %errorlevel%==1 goto install
if %errorlevel%==2 goto run
:install
winget install 9NCVDN91XZQP
pip install discord.py
pip install python-dotenv
goto run
:run
color 03
cd %USERPROFILE%\Downloads\Discord Annoncer
python AnnoncerBot.py
goto 1