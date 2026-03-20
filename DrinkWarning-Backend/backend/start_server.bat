@echo off
echo 正在启动FastAPI服务...
echo.

cd /d "c:\Users\31059\Desktop\酒后检测\DrinkWarning-Backend\backend"

echo 激活虚拟环境...
call venv\Scripts\activate.bat

echo 启动服务...
python main.py

pause
