@echo off

:: 检测并设置正确的包管理器 (pip或pip3)
where pip >nul 2>nul
if %errorlevel% neq 0 (
    where pip3 >nul 2>nul
    if %errorlevel% neq 0 (
        echo Neither pip nor pip3 found. Please ensure Python is properly installed with pip.
        pause
        exit /b
    ) else (
        set PIP=pip3
    )
) else (
    set PIP=pip
)

:: 检测并安装所需的Python库
%PIP% list | findstr /i "requests" >nul 2>nul
if %errorlevel% neq 0 (
    echo Required Python libraries not found. Installing them...
    %PIP% install -r requirements.txt
)

:: 运行主文件
python main.py
if %errorlevel% neq 0 (
    echo First attempt failed, trying with python3...
    python3 main.py
)

pause