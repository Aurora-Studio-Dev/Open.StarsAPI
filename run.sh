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

# 可选：暂停以便查看输出，仅在前台执行时有效
if [ -t 1 ]; then
    read -p "Press [Enter] key to continue..."
fi