@echo off
powershell.exe -ExecutionPolicy ByPass -Command "& 'C:\ProgramData\anaconda3\shell\condabin\conda-hook.ps1' ; cd %1 ; conda activate nlp_tools ; python %2.py '%3'"
