@echo off
setlocal enableextensions disabledelayedexpansion

if [%~1] == [] (
  goto error
) else (
  goto begin
)

:error
echo No arguments supplied.
pause
goto exit

:begin
rem set "output_file=%~dp0file_list.txt"
set "template_path=C:\Users\thomas.olson\Documents\Git\mailtemplates\src\templates\freemarker\test\"
set "output_file=%template_path%file_list.ftl"

rem echo ^<#assign file_list = ^"> "%output_file%"
dir /s/b/a-d %*> "%output_file%"
rem echo ^"^>>> "%output_file%"

set "search=\"
set "replace=/"

for /f "delims=" %%i in ('type "%output_file%" ^& break ^> "%output_file%"') do (
  set "line=%%i"
  setlocal enabledelayedexpansion
  set "line=!line:%search%=%replace%!"
  >>"%output_file%" echo(!line!
    endlocal
  )
)

:exit
