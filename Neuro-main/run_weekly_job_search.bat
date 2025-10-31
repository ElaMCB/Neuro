@echo off
REM Weekly Job Search Runner for Windows
REM Run this with Windows Task Scheduler for weekly automation

cd /d "%~dp0"
python run_neuro.py my_job_search.neuro

REM Optional: Open results viewer
REM python display_results.py

pause

