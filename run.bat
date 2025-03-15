@echo off

:: 检测是否安装了Python
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python not found. Installing Python...
    :: 自动下载并安装Python
    powershell -Command "Invoke-WebRequest -Uri 'https://mirrors.aliyun.com/python-release/windows/python-3.10.10.exe' -OutFile 'python-installer.exe'; Start-Process -FilePath 'python-installer.exe' -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1' -Wait"
    
    :: 等待Python安装完成
    timeout /t 30
    
    :: 再次检查Python是否安装成功
    where python >nul 2>nul
    if %errorlevel% neq 0 (
        echo Python installation failed. Please install Python manually and run this script again.
        pause
        exit /b
    )
)

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