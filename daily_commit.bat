@echo off
python  daily_commit.python
git add .
git commit -m "Daily commit - %date%"
git push
pause