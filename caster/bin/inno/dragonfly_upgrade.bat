@echo off

cd C:\
mkdir temp_dragonfly
cd temp_dragonfly




git clone --recursive https://github.com/Danesprite/dragonfly.git
cd dragonfly
git submodule foreach python setup.py install



cd dragonfly/dragonfly
xcopy /Y/E/Q * C:\Python27\Lib\site-packages\dragonfly 

cd C:\
rmdir /S/Q temp_dragonfly

echo ------------------------------------------
echo         Dragonfly Upgrade Complete
echo ------------------------------------------

pause