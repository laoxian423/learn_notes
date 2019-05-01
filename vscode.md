##### 001. 简单开始：

```bash
# 新建一个目录作为你的workspace
mkdir pyprojects
cd pyprojects
code .      # code 将使用当前目录作为工作区
```

##### 002. 如何设置解释器：

```bash
# 1. 进入code界面
# 2. "crtl+shift+p"
# 3. 输入"python:select interpreter"
# 4. 选择你要使用python版本
```

##### 003. code常用快捷键：

```bash
ctrl + shift + `    # 打开一个新的终端。
ctrl + shift + P    # 打开命令面板
```

##### 004. 安装软件包在虚拟环境：

* `pip3 install virtualenv -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com`
* `sudo apt-get install python3-venv`

```bash
# 1. create and activate thi virtual environment
# For windows
py -3 -m venv env
env\scripts\activate
# For Linux/macOS
python3 -m venv env
source env/bin/activate

# 2. Install the packages
# windows
python -m pip install matplotlib
# linx(Debian)
apt-get install python3-tk
python3 -m pip install matplotlib   

# 3. Select your new environment by using the "Python:Select interpreter"


```

