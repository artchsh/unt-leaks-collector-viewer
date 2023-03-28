@echo off
:menu
cls
echo Select an option:
echo [1] - Collect
echo [2] - View
echo [3] - Collect and view
set /p option=Enter option number:

if %option%==1 goto collect
if %option%==2 goto viewer
if %option%==3 goto collect_viewer
goto menu

:collect
echo You have selected Collect option.
python __collect__.py
pause
goto menu

:viewer
echo You have selected View option.
python __main__.py
goto menu

:collect_viewer
echo You have selected Collect and view option.
echo Collecting data...
python __collect__.py
echo Viewing data...
python __main__.py
pause
goto menu
