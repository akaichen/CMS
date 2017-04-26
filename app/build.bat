rmdir /S /Q dist\
rmdir /S /Q build\
rmdir /S /Q cms\


copy CMS.py CMS.pyw

rem mkdir dbdir\

python setup.py py2exe

del CMS.pyw

copy MSVCP90.DLL dist\

mkdir dist\dbdir\
copy dbdir\customerinfo-default.mdb dist\dbdir\customerinfo.mdb

mkdir dist\imgdir\
copy imgdir\custpicture.png dist\imgdir\
copy imgdir\mainpage.png    dist\imgdir\
copy imgdir\prodpicture.png dist\imgdir\
xcopy /E /Y /I imgdir\prod-pro dist\imgdir\prod

rem xcopy /E /Y dbdir dist\dbdir\
rem xcopy /E /Y imgdir dist\imgdir\

mkdir cms\

rmdir /S /Q build\
move dist cms\

cd cms\dist\

call CMS.exe
call CMS.exe.log

cd ..\..\
