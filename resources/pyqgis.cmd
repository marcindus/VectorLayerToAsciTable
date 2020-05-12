@echo off
SET OSGEO4W_ROOT=C:\OSGeo4W3
call "%OSGEO4W_ROOT%"\bin\o4w_env.bat
call "%OSGEO4W_ROOT%"\apps\grass\grass-7.4.0\etc\env.bat
@echo off
path %PATH%;%OSGEO4W_ROOT%\apps\qgis\bin
path %PATH%;%OSGEO4W_ROOT%\apps\grass\grass-7.4.0\lib
path %PATH%;C:\OSGeo4W3\apps\Qt5\bin
path %PATH%;C:\OSGeo4W3\apps\Python36\Scripts

set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\qgis\python
set PYTHONHOME=%OSGEO4W_ROOT%\apps\Python36

set PATH=C:\Program Files\Git\bin;%PATH%

cmd.exe