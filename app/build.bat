rmdir /S /Q dist\
rmdir /S /Q build\
rmdir /S /Q cms\


copy CMS.py CMS.pyw

rem mkdir dbdir\

python setup.py py2exe

del CMS.pyw

copy MSVCP90.DLL dist\
xcopy /E /Y dbdir dist\dbdir\
xcopy /E /Y imgdir dist\imgdir\

mkdir cms\

rmdir /S /Q build\
move dist cms\

call cms\dist\CMS.exe

call cms\dist\CMS.exe.log
