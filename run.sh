# 检测是否安装了Python
if ! command -v python3 &> /dev/null; then
    echo "Python not found. Installing Python..."
    
    # 自动下载并安装Python
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip
    
    # 再次检查Python是否安装成功
    if ! command -v python3 &> /dev/null; then
        echo "Python installation failed. Please install Python manually and run this script again."
        exit 1
    else
        echo "Python installed successfully."
    fi
else
    echo "Python is already installed."
fi

# 设置正确的包管理器 (pip)
PIP=pip3

# 检测并安装所需的Python库
if ! pip3 list | grep -q requests; then
    echo "Required Python libraries not found. Installing them..."
    pip3 install -r requirements.txt
fi

# 运行主文件
python3 main.py
if [ $? -ne 0 ]; then
    echo "First attempt failed, trying with python3..."
    python3 main.py
fi

# 暂停以便查看输出
read -p "Press [Enter] key to continue..."