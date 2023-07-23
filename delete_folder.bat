@echo off

set "folder_path=C:\Users\USER\Desktop\another one"

if exist "%folder_path%" (
    rmdir /s /q "%folder_path%"
    echo The Folder was deleted successfully
) else (
    echo Folder not found
)

pause