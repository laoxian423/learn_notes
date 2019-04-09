       1991年10月5日，还在上大学的Linus在一次UNIX实验后，对UNIX极度不满，决定自己写一个最好用操作系统，随后将第一个Linux 内核版本放到GNU。
       （GNU  自由软件基金会，由当时被成为第一黑客的richard stallman创建）
### 1、linux 常见版本：

* RedHat ：RHEL ，使用最广，全球最大。培训课程设计的最好。
* centos：redhat的克隆版本，几乎就是RHEL，与RHEL唯一的技术差异就是品牌。
* Fedora  ：Redhat将其新的修改，首先放到Fedora供用户使用，被称之为Redhat的小白鼠。
* Ubuntu : 号称界面最精美，最受欢迎的桌面Linux发行版
* Debian :有史以来最大的协作软件项目，它由1000多名志愿者开发。
* SUSE: Novell公司旗下产品，由于其与微软在Linux知识产权纠纷事件被大量客户放弃
* 中标麒麟：国产Linux，一个民用，一个军用，合并而成。

### 2、系统安装:

> 以下实验都在Centos上操作，可通过下列镜像网站下载：
>
> * 阿里： https://opsx.alibaba.com/mirror
>
> * 网易：http://mirrors.163.com/
>
> 注：everythin 版本，包含所有的RPM和源码包。
>
> ```shell
> # 部署虚拟机实验环境，最好虚拟两台，一台安装centos 6 ,一台安装centos 7,6 和 7有一部分系统管理不同，目前6和7是企业中使用最广的版本。其中6.8被称为6里面的终极稳定版。
> # 安装过程比较简单，只需注意一下几点：
> 1、无关硬件都去掉，比如声卡、打印机等
> 2、在安装配置中不要启用SELinux,后期学习过以后再考虑启动
> 3、KDUMP 为系统崩溃转存功能，可关闭。
> 4、硬盘最好分区，不要一股脑分到一个区上，不利于后期实验，下面是建议：
>    /boot    启动相关的文件，还有内核，分配200M即可
>    swap     如果内存<8G ,就分配两倍内存的空间。如果内存很大比如256G，这个分区
>             不用过大，没有必要。
>    /        剩下的都可以给根。
> # 安装完毕后，对两台虚拟机建立快照，防止后期实验系统崩溃。
> ```
>
> 

### 3、基础操作

> * 命令：
>
> ```shell
> # 提示符 $ 表示普通用户， # 表示root用户
> # ~ 表示home目录，对于root来说，它的家目录在 /root
> 
> # 列出目录列表：
> ls -l /boot      # -l 使用长列表方式
> ls -l -a /boot   # -a 显示所有文件，包括隐藏属性
> ls -la -h /boot  # -h 以人类方式显示，就是文件大小显示为 K,M,G
> 
> # 创建目录：
> mkdir /home/zhangsan/test 
> 
> # 改变当前目录
> cd /home/zhangsan/test
> cd -  # 回到上一次的目录
> cd ~  # 改变目录到家目录home
> 
> # 查看当前目录
> pwd
> 
> # 创建一个文本文件：
> touch ex01     # 创建一个0字节大小的文件，文件名为ex01
> echo "this is a test" > ex02 # 利用重定向生成一个文件ex02
> echo "second line" >> ex02  # 在文件ex02末尾追加一行内容
> vi /home/zhangsan/ex03  # 用编辑程序 vi 创建文件ex03
> vim /home/zhangsan/ex04  # 用编辑程序 vim 创建文件ex04
> 
> # 查看文件内容
> cat ex02    # 列出ex02文件内容
> tail ex02   # 从文件末尾显示
> tail -n 5 /etc/passwd  # 显示最后5行
> tail -f /var/log/messages  # 不停的现实最后内容，适合监控日志
> head ex02   # 从文件头开始显示，支持指定行数，-n 5
> vi  vim   more   
> 
> # 拷贝文件：
> cp /etc/passwd /home/zhangsan/test/  # 把/etc下的文件passed拷贝到test下
> cp -r /etc  /home/zhangsan/test/  # 把/etc下的所有文件包含子目录全拷贝过来
> 
> # 删除文件：
> rm ex03     # 删除文件ex03
> rm -f ex03  # 强制删除ex03
> rm -rf /home/zhangsan/test  # 强制删除目录test及其下所有目录文件
> 
> # 移动文件（可当作改名命令）
> mv /home/zhangsan/test/ex02  /home/zhangsan/test/ex30
> 
> # 查看当前系统支持的shell  
> cat /etc/shells
> 
> # 查看Linux内核版本
> uname -a 
> ls -l /boot/
> 
> # 查看命令别名
> alias
> 
> # 重复上一次的某个命令
> !cp
> 
> # 查看当前登陆用户
> who
> 
> # 查看当前身份
> whoami
> 
> # 查看历史命令
> history
> 
> # 查看防火墙SELinux 状态
> getenforce  # 可能返回结果有三种：Enforcing、Permissive 和 Disabled。Disabled 代表 SELinux 被禁用，Permissive 代表仅记录安全警告但不阻止可疑行为，Enforcing 代表记录警告且阻止可疑行为。
> setenforce 0 # 暂时关闭
> 
> ```

### 4、用户和组管理

#### 4.1 passwd 和 shadow

* /etc/passwd 文件：

> ```shell
> root: x : 0 : 0: root:/root:/bin/bash
> 1 : 2 : 3 : 4:  5  : 6   :  7
> ```
>
> > 1  用户名
> >
> > 2  口令
> >
> > 3  uid  用户ID，root 的UID 是0,**应该说uid等于0的root用户**，普通用户在1000以后
> >
> > 4  gid  组ID
> >
> > 5  描述
> >
> > 6  家目录
> >
> > 7  login后的动作，/bin/bash 表示登陆后进入shell，如果是nologin 则禁止登陆

* 口令文件：/etc/shadow

>
> ```shell
> root:k1KrZUNStssQ1.....: 17810 : 0 : 99999 : 7 :   :  :
> 1 :       2            :   3   : 4 :  5    : 6 : 7 : 8
> ```
>
> > 1  用户名  2   口令
> >
> > 3  密码创建日期，自1970.1.1起计算，每过一天加1
> >
> > 4   和3相比两次密码的修改间隔时间，也就是多少天改一次密码
> >
> > 5   和3相比，密码有效期
> >
> > 6   密码过期多少天开始提醒
> >
> > 7   过期多少天后禁用
> >
> > 8   账号失效时间

#### 4.2 用户管理常用命令：

```shell
# 增加新用户 zhangsan 
useradd xiaomin

# 新增用户并指定uid
useradd -u 888 boss

# 为用户设置密码
passwd xiaomin

# 管理用户密码时效，密码60天失效
chage -E 60 xiaomin 
# 查看用户密码策略
chage -l xiaomin

# 修改用户账号信息
usermod -d /home/xm xiaomin   # 修改家目录
usermod -g class2 xiaomin     # 修改组信息  

# 切换账户,exit 退出
su - xiaomin

# 删除用户,-r 删除小明的相关资源，如家目录
userdel -r xiaomin  
```
#### 4.3 组管理命令

>   * 组配置文件： /etc/group    /etc/gshadow
>
>   ```shell
>   # 增加新组，可以 -g  指定组ID
>   groupadd class1
>   # 分配组成员,把xiaomin加到class1组里
>   gpasswd -a xiaomin class1
>   # 从组中删除一个成员
>   gpasswd -d xiaomin class1
>   # 删除组（里面不能有成员）
>   groupdel class1
>   ```

### 5、文件管理

* Linux 中一切都是文件,包括硬件设备

* linux 文件名长度限制在256个字节。

* 文件名前加点表示隐藏文件，如`.git`

#### 5.1 文件类型说明：
```shell
$ ls -l /etc 
...
drwxr-xr-x  2  root  root   244,  0  4月   4  18:26 pts
...
```
```shell
# 第1位，文件类型说明：
- 普通文件
d 目录
b 块设备，接口设备，比如硬盘、光驱
c 字符设备，串行端口的接口设备，比如键盘、鼠标
l 链接文件，类似windows的快捷方式。
# 第2,3,4为代表user(u)的权限，第5,6,7位代表group(g)的权限，第8,9,10位代表other（o）的权限。
r  表示读,对应的10进制数值为4
w  表示写，对应的10进制数值为2
X  对于文件来说表示执行，对目录来说就是搜索，对应的10进制数值为1
- 表示无权限
```

#### 5.2  文件管理常用命令

```shell
# 将指定文件的拥有者改为指定的用户或组 chown
chown root:root /home/test/ex0  # 把文件ex0的拥有者修改为root，组修改为root
chown root /home/test/ex0  # 文件给root
chown :root /home/test/ex0  # 文件给root组
chown -R root /home/test/   # 包含子目录

# 修改文件访问权限，-R 迭代目录
chmod o+w ex0    # 给其他人授予写这个文件的权限
chmod go-rw ex0  # 删除群组和其他人对这个文件的读和写的权限
chmod go-w+x <dir> # 拒绝组成员和其他人创建或删除目录 dir（go-w）中文件的权限，允许组成员# 和其他人搜索 dir，或在路径名(go+x)中使用它.
# 只有拥有者能够操作
chmod u+t ex0 
# 让用户能够执行他无权执行的程序
chmod u+s /usr/bin/vim

# 用数字修改文件访问权限，-R 迭代目录
chmod 700 ex0   #  user拥有最大权限（rwx 4+2+1=7)，组和其他人无权限

# 两个文件属性查看命令：
file ex01    # file 辨识文件类型
stat ex01    # 文件/文件系统的详细信息显示,诸如访问时间，修改时间等

# 查看默认文件权限掩码
umask 

```

#### 5.3 文件隐藏属性的设置

* 对每一个文件设置更精确的权限设置，设置文件访问列表ACL
* 文件访问控制列表：

```shell
# 设置一个非拥有者和组的用户，访问文件的权限
setfacl -m u:boss:rwx -R /home/test/

# 查看文件的访问控制列表
getfacl /home/test/a

# 移除用户的访问控制列表
setfacl -x u:boss /home/test/a

# 移除文件的所有访问控制列表
setfacl -b /home/test/a
```

* chmod只是改变文件的读写、执行权限，更底层的属性控制由chattr来改变的。 

* 文件隐藏属性的设置

  ```shell
  # 显示文件隐藏属性：
  lsattr <filename>
  
  # 任何人不得修改
  chattr +i /home/test/ex01
  # 只允许文件追加内容
  chattr +a /home/test/ex01
  ```

* 创建文件链接

  ```shell
  # 创建软链接（类似windows下的快捷方式）
  ln -s /etc/passwd  ./passwd2
  
  # 创建硬链接
  ln /etc/passwd ./passwd3  # ls -l观察一下，属性后面的数字会加1,有多硬链接就加多少  
  ```

#### 5.4、文件查找、压缩的命令

```shell
# 文件查找命令
which rm
whereis  touch
locate passwd  # 第一次使用时需要执行 updatedb，后期不用做
# find 命令
find  /  -name  passwd  # 按名字查找，前面指定从哪里查找
find / -name *passwd*   # 通配符查找
find /etc/ -type d    # 按文件类型查找，d 找文件夹
find / -user stud01  # 按用户找
find / -size +1M  # 按大小找
find / -perm 777  # 按权限找
find /etc/ -type f -and -size +1M  # 支持 .and  .or  等逻辑指令
find / -usstud01 -exec cp -rf {}  /root/Desktop/stud01/  \;  # 支持命令嵌套
   
# 文件里找内容
grep   root  /etc/passwd
grep -i ROOT /etc/passwd  #忽略大小写
 
# 压缩解压  gzip  bzip2 
# 通过打包程序 tar 实现压缩和解压缩
tar czvf log.tar.gz /var/log/  #c建立tar包，z gzip v 要看到过程 f 保存的文件名
tar czvf /root/Desktop/`date +%F`-log.tar.gz /var/log/

# 如果不清楚文件的压缩类型，可以用file查看
file <filename> #看文件类型

# 解压
tar xzvf /root/Desktop/sssss.tar.gz -C  /tmp/  #指定解压路径  
```



### 6、目录管理：

#### 6.1  linux 常见目录说明

```shell
/root 		# root用户的家目录
/boot    	# 内核，启动资源
/home   	# 用户家目录
/dev    	# 设备，sda   cpu
/etc    	# 配置文件
/mnt   		# 挂载点
/bin   /sbin    	# 可执行文件
/opt    	# 第三方工具
/proc    	# 虚目录，对应内存映射，开机才有
/usr   		# 自己编译的文件
/var  		# 放一些数据文件，日志文件  /var/log/messages

/lib   /lib64 	  	# 动态链接库
/run     			# 运行的东西，进程号
/sys   				# 虚目录，对应内存映射，开机才有
/tmp   				# 临时文件，定期自动清理
```

#### 6.2 目录相关命令

```shell
# linux 下一切都是文件，所以针对文件的命令都适用于目录
```

### 7、 vi 和vim  编辑器

#### 7.1 vim 常用键盘操作

* 其配置文件一般在/etc/vimrc

```shell
yy  # 复制当前行
4yy  # 复制当前行到其下共4行
p    # 粘贴
dd   # 剪切
u    # 撤销操作
gg   # 光标到第一行
G    # 光标到最后一行
o    # 下插一行
：w  # 保存
:q   # 没有修改文件情况下退出
:q!  # 不保存强制退出
:wq  # 保存退出
:r /etc/fstab  # 把fstab文件内容读到当前位置
:r! df -Th  # 把df -Th的命令结果插入到当前位置
:set number # 设置行号
:s/nologin/bash/g  # 搜索替换当前行
:1,10s/nogoin/bash/g # 替换第一行到第10行的
:%s/nologin/bash/g  # 全部替换
/main  #搜索”mail“  n  下一个
```

* ctrl + z  可以暂时回到shell，fg 返回，jobs 查看有几个任务

### 8、输入输出及管道重定向

#### 8.1 输出重定向

* `>`    覆盖输出重定向

```shell
# 将输出到屏幕的内容输出到文件，覆盖原有内容
ls -l > list.txt
find / -user boss  > ofboss.txt

```

* `>>`  追加输出重定向

```shell
# 新的内容追加到文件
ls -l /etc >> list.txt
```

* `2>`   错误输出重定向

```shell
#  shell中:
#      0    表示标准输入
#      1    表示标准输出
#      2    表示标准错误输出
find / -user boss > right 2> error
# 把标准输出和标准错误输出一起输出
find / -user boss &> all
```

#### 8.2 输入重定向

* `<`

```shell
# 出入重定向到test1
cat > test2 < test1
```

#### 8.3 管道

* `|`

```shell
# 将cat的内容通过管道输出给grep
cat /etc/passwd | grep root

# 取磁盘使用百分比的一个列子：将磁盘信息中boot目录的信息先grep出来，然后用tr把各列的多个空格压缩成一个，然后在用cut进行分割，分割后的字段取第6个。
df -Th  | tee temp01 |  grep boot  |  tr -s " " | cut -d " " -f 6 
# tee     把临时内容转存到一个文件中
# tr      压缩空格
# cut     分割

```



### 9、软件包的安装

* 三种安装软件包的方式：rpm 、 yum  、  编译安装
* rpm 是Redhat的打包格式。
* 升级内核必须使用rpm，升级过程中不可被终止。
* rpm 不能解决包依赖问题。

#### 9.1 rpm 的使用

```shell
# 安装一个软件包， -i 安装  v 过程信息可见   h  进度条
rpm -ivh httpd-2.2.15-39.el6.centos.x86_64.rpm
rpm -ivh httpd-2.2.15-39.el6.centos.x86_64.rpm --force   #force 强制安装

# 查询包详细信息
rpm -qpi  httpd-2.2.15-39.el6.centos.x86_64.rpm   
# 查询软件包安装的文件列表
rpm -ql httpd-2.2.15-39.el6.centos.x86_64.rpm
# 查询软件包的依赖
rpm -q --requires httpd

# 升级一个软件包
rpm -Uvh httpd-2.2.15-39.el6.centos.x86_64.rpm

# 降级一个软件包
rpm -Uvh --oldpackage httpd-2.2.15-30.el6.centos.x86_64.rpm

# 卸载一个软件包
 rpm -e httpd
 
# 查询已经安装的所有包，可结合grep
rpm -qa
rpm -qa | wc -l    # 统计安装了多少个包
rpm -qa | grep python  # 是否安装了python

# 查询某个命令来自于那个包
rpm  -qf  /usr/bin/touch 
```

#### 9.2 yum的使用

* yellow dog update

* 解决了包依赖的问题

* 重新指定yum源的一些方法（有时候因为下载速度，或者保持版本环境）：

  ```shell
  # 将yum源指向cdrom，或者某个目录：
  # 备份/etc/yum.repos.d/的所有文件，然后清空这个目录。
  vim /etc/yum.repos.d/test.repo
  # -----------------------------------
  [stud01]
  nastud01
  baseurl=file:///mnt/cdrom
  enabled=1
  gpgcheck=0
  
  # 将YUM源指向163(网易）
  # 首先备份/etc/yum.repos.d/CentOS-Base.repo，下载版本对应的文件
  # CentOS5 ：http://mirrors.163.com/.help/CentOS5-Base-163.repo
  # CentOS6 ：http://mirrors.163.com/.help/CentOS6-Base-163.repo
  # CentOS7 ：http://mirrors.163.com/.help/CentOS7-Base-163.repo
  wget http://mirrors.163.com/.help/CentOS6-Base-163.repo
  mv CentOS6-Base-163.repo CentOS-Base.repo
  
  # 生成缓存
  yum clean all
  yum makecache
  ```

* yum 的一些常用命令

  ```shell
  # 列出所有可安裝的软件清单:
  yum list 
  # 列出可供更新的软件：
  yum check-update
  # 查找软件包 :
  yum search <keyword> 
  # 安装指定软件
  yum install <package_name>
  # 升级所有软件包
  yum update
  # 升级指定软件
  yum update <package_name>
  # 删除指定软件
  yum remove <package_name> 
  # 查询软件信息
  yum info python
  ```

### 10、系统监控及进程管理

#### 10.1 常用命令：

```shell
# 查看系统信息
uname -a  # 查看内核
lscpu    # 查看CPU信息
cat /proc/cpuinfo  # 查看CPU信息
cat /proc/meminfo  # 查看内存信息
hostname   # 获取主机名
hostnamectl set-hostname  class_3  # 设置主机名

# last，显示近期用户或终端的登录情况。通过last命令管理员可以获知谁曾经或者企图连接系统
last -n 10   # 显示10条
last -10 -f /var/log/btmp   # btmp 记录错误登陆的日志
# 查看恶意ip试图登录次数，lastb 直接显示 btmp 文件内容：
lastb | awk ‘{ print $3}’ | sort | uniq -c | sort -n 
```

```shell
# top 的使用，常用快捷键
s  改变画面更新频率
N  以 PID 的大小的顺序排列表示进程列表
P  以 CPU 占用率大小的顺序排列进程列表
M  以内存占用率大小的顺序排列进程列表
m  显示内存情况，用条状图
t  显示CPU使用情况
h  显示帮助
n  设置在进程列表所显示进程的数量
q  退出 top
# 需要关注的一个空闲情况ID，另外是僵尸进程bombie

```

```shell
# 进程树查看
pstree

# 进程查看 
ps aux | grep xxxxx

# 查看进程信号，给进程发信号
kill -l   # 9   15
kill -19 2978

```

```shell
# 其他系统信息查看命令
# 查看CPU信息
cat /proc/cpuinfo
# 查看板卡信息或者敲入命令 lspci：
cat /proc/pci
lspci |grep Ethernet # 查看网卡型号
# 查看内存信息
cat /proc/meminfo
#查看USB设备： 
cat /proc/bus/usb/devices
# 查看各设备的中断请求(IRQ):
cat /proc/interrupts
```

* `dd if=/dev/zero of=/dev/null bs=1M count=10000000000000`  给CPU施加压力

### 11、服务与计划任务

#### 11.1  systemv 和 sytemd

>**system V (Centos 6):**
>
>* 大多数基于 linux 的操作系统，使用的是System-V风格的init守护进程，换句话说，它们的启动处理由**init**进程管理，其管理功能在一定程度上继承了基于System V 的Unix操作系统。该守护进程根据运行级别(run level)的原则，系统的运行级别表示当前计算机的状态。
>* runlevel0:  系统停机状态，系统默认运行级别不能设置为0，否则不能正常启动，机器关闭。 
>  runlevel1:  单用户工作状态，root权限，用于系统维护，禁止远程登陆，就像Windows下的安全模式登录。 
>  runlevel2:  多用户状态，没有NFS支持。 
>  runlevel3:  完整的多用户模式，有NFS，登陆后进入控制台命令行模式。 
>  runlevel4:  系统保留。 
>  runlevel5:  登陆后进入图形GUI模式。 
>  runlevel6:  系统正常关闭并重启，默认运行级别不能设为6，否则不能正常启动。运行init 6机器就会重启。标准的Linux运行级别为3或5
>* system V主要用 chkconfig, sevice,  update-rc.d 命令管理服务
>* /etc/inittab
>
>**systemd(Centos 7)**
>
>* 守护进程是systemd。
>* 在systemd的管理体系里面，以前的运行级别（runlevel）的概念被新的运行目标（target）所取代。target（相当于以前的默认运行级别）是通过软链来实现。如： 
>  `ln -s /lib/systemd/system/runlevel3.target /etc/systemd/system/default.target `
>* /etc/inittab 文件被废弃。
>* systemd使用systemctl命令管理。

#### 11.2  Centos 6 操作：

* 使用 pstree 查看进程。`yum -y install psmisc`

```shell
# 修改默认启动模式：
vim /etc/inittab  
id:5:initdefault

# 检查开机自启动项目
chkconfig --list
# 设置某个进程开机自启动或者关闭
chkconfig httpd on
chkconfig iptables off

# 重启机器或者从字符模式启动到图形模式
init 6   # 重启
init 5   # 从字符模式启动到图形模式
```

#### 11.3 Centos 7 操作

* 使用pstree 查看进程。`yum -y install psmisc`

```shell
systemctl enable httpd.service   # 随机自启动
systemctl  mask httpd.service    # 屏蔽这个服务
systemctl mask firewalld.service  # 屏蔽防火墙，或者 vim /etc/selinux/config 然后 selinux=disabled
systemctl unmask httpd.service   # 解除屏蔽

systemctl disable firewalld.service  # 禁止这个服务

systemctl status xxx.service   # 检查某个服务状态
systemctl set-default runlevel3.target  # 设置缺省模式为命令行模式
systemctl  get-default  # 获取当前启动模式
systemctl list-units   # 列出所有正在运行的单元

systemctl start xxx.service  # 启动某服务
systemctl stop xxx.service  # 停止某服务
systemctl restart xxx.service # 重启某服务
systemctl kill  crond   # 杀死服务
```

#### 11.4 计划任务管理

* 一次性任务 at

  ```shell
  # atd服务管理，Centos 6
  service atd start    # 启动服务
  service atd  stop    # 关闭服务
  service atd restart  # 重启服务
  service atd reload   # 重新载入配置
  service atd status   # 查看服务状态 
  # atd服务管理Centosx 7
  systemctl  start atd.service  
  # 例子：
  at 2:05 tomorrow   # 在命令行下敲入命令后，回车进入at编辑模式
  at> /home/kyle/do_job   # 输入要执行的脚本或命令
  at> ctrl+d
  # 关于时间的说明：
  at now + 5 minutes     任务在5分钟后运行
  at now + 1 hour        任务在1小时后运行
  at now + 3 days        任务在3天后运行
  at now + 2 weeks       任务在两周后运行
  at midnight            任务在午夜运行
  at 10:30pm             任务在晚上10点30分
  at 23:59 12/31/2018　  任务在2018年12月31号23点59分运行
  
  # 查询at任务：atq
  # 删除at任务：atrm
  ```

  

* 周期任务 crontab

  1. Centos  6 下 

  ```shell
  # 安装 crontab 
  yum install crontabs
  
  # 管理服务:
  service crond start   # 启动服务
  service crond stop    # 关闭服务
  service crond restart # 重启服务
  service crond reload  # 重新载入配置
  service crond status  # 查看crontab服务状态
  
  # 开机自启动管理，或者使用 ntsysv 管理随机启动项
  chkconfig crond on  
  chkconfig crond off
  
  # 设置周期任务：
  #   第一种方法 crontab -e ,也可指定某用户 -u root 然后手动编辑，第二种 vi /etc/crontab 手动编辑
  # 任务格式：Minute Hour Day Month DayofWeek CommandPath
  # Minute：每个小时的第几分钟执行该任务；取值范围0-59
  # Hour：每天几点执行该任务；取值范围0-23
  # Day：每月的第几天执行该任务；取值范围1-31
  # Month：每年的第几个月执行该任务；取值范围1-12
  # DayOfWeek：每周的第几天执行该任务；取值范围0-6，0表示周末
  # CommandPath：指定要执行的程序路径
  
  # 几个例子
  Minute Hour Day Month DayofWeek CommandPath
  30 21 * * * /etc/init.d/nginx restart             # 每晚的21:30重启 nginx。
  45 4 1,10,22 * * /etc/init.d/nginx restart        # 每月1、10、22日的4:45重启nginx。
  10 1 * * 6,0 /etc/init.d/nginx restart            # 每周六、周日的1:10重启nginx。
  0,30 18-23 * * * /etc/init.d/nginx restart        # 每天18:00至23:00之间每隔30分钟重启nginx。
  0 23 * * 6 /etc/init.d/nginx restart              # 每星期六的11:00 pm重启nginx。
  * */1 * * * /etc/init.d/nginx restart             # 每一小时重启nginx
  * 23-7/1 * * * /etc/init.d/nginx restart          # 晚上11点到早上7点之间，每隔一小时重启nginx
  0 11 4 * mon-wed /etc/init.d/nginx restart        # 每月的4号与每周一到周三的11点重启nginx
  0 4 1 jan * /etc/init.d/nginx restart             # 一月一号的4点重启nginx
  */30 * * * * /usr/sbin/ntpdate 210.72.145.20      # 每半小时同步一下时间
  
  # * ：表示任意的时刻；如小时位 * 则表示每个小时
  # n ：表示特定的时刻；如小时位 5 就表示5点
  # n,m ：表示特定的几个时刻；如小时位 1,10 就表示1时和10时
  # n－m ：表示一个时间段；如小时位 1-5 就表示1到5点
  # */n : 表示每隔多少个时间单位执行一次；如小时位 */1 就表示每隔1个小时执行一次命令，也可以写成 1-23/1
  
  ```

  2. Centos  7 下：

  ```shell
  # 安装 crontab
  yum -y install vixie-cron
  yum -y install crontabs
  
  # 管理服务：
  systemctl start crond.service
  systemctl stop crond.service
  systemctl restart crond.service
  systemctl status crond.service
  # 开机自启动
  systemctl enable crond.service
  
  # 其他和 centos 6 下的操作相同
  ```

  * Centos默认所有用户都可以使用crond，如果要禁止某个用户使用，可以编辑 /etc/cron.deny,将禁止的用户写进去。

  ### 12、网络管理

#### 12.1 网卡管理

  ```shell
# Centos 6
# 为了规范 systemV 和 systemd ，一般企业将 Centos 6 中的 systemd 关闭，只保留systemV：
service NetworkManager stop
chkconfig NetworkManager off
service network start
chkconfig network on

# 查询网卡地址信息
ifconfig
ip addr show

# 编辑网卡配置文件，Centos 6 和 Centos 7 网卡命名规则不同，eth? 是 Centos 6 的格式，也可以自己起名。
# 新加网卡，系统不会自动创建这些文件，需要手动创建编辑。
vim /etc/sysconfig/network-scripts/ifcfg-eth0
# 网卡配置文件参数说明：
DEVICE=eth0    # 网卡逻辑设备名
HWADDr=00:0C:29:CC:60:B2    # 以太网卡硬件地址
TYPE=Ethernet    # 上网类型，目前基本上都是以太网
UUID=176582f6-d198-4e4f-aab0-34ab10d1724    #通用唯一识别码
ONBOOT=NO    # 启动时是否激活
NM_CONTROLLED=yes # 是否通过NetWorkManager管理网卡设备
BOOTPROTO=none    # IP启动协议，获取配置方式，有:none|static|dhcp三种方式
IPADDR=10.0.0.8    # IP地址
NETMASK=255.255.255.0    # 子网掩码
GATEWAY=10.0.0.254    # 网关地址;
DNS1=202.206.0.20    # 主DNS，这里优先于/etc/resolv.conf的配置生效
DNS2=8.8.8.8        # 备DNS
IPV6INIT=no    #是否支持IPV6;

# 重新启动网络服务，一般调整完网络参数需要执行：
service network restart 
  ```

  ```shell
# Centos 7
# Centos 7 下使用systemctl进行管理
systemctl mask network
systemctl stop network

systemctl start NetworkManager
systemctl restart NetworkManager
systemctl stop NetworkManager

systemctl enable NetrokManager

# Centos 下网卡命名规范
# 网卡名变成了类似ens33 类型的名字，这个名字是系统计算出来的。
#  其中 en 以太网 ， wl无线 ， o 集成网卡， s 标识PCI网卡 ， p 表示usb外置网卡等等。
# 取消新的网卡名计算方法。


# centos 7 下的网络管理工具 nmcli （网络管理命令行工具），网卡的配置全部由这个工具完成。
# 查看连接的设备
nmcli connection show
# 查看特定设备的信息
nmcli connection show ens33
# 查看网络设备状态
nmcli device status
# 给网卡配置DHCP连接
nmcli connection add con-name "dhcp" type ethernet ifname ens33
# 给网卡配置固定IP
nmcli connection add con-name "static" ifname ens33 autoconnect no type ethernet ip4 192.168.1.45 gw4 192.168.1.1
# 启动或者关闭网卡
nmcli connection up ens33
nmcli connection down ens33
# 单独配置地址,还有：ipv4.dns，ipv4.gateway
nmcli connection modify ens33 ipv4.addresses '192.168.1.44'
# 设置网卡开机自动连接
nmcli connection modify ens33 connection.autoconnect yes
# 重新加载配置
nmcli connection reload
# 重新启动网络
systemctl restart network.service
  ```



#### 12.2 常用命令：

* ethtool   

```shell
# 查询网卡信息
ethtool eth0

# 设置网卡速率为100M
# 需要永久生效的话，在网卡配置文件中：ETHTOOL_OPTS="speed 100 duplex full autoneg off"
ethtool -s eth0 speed 100 duplex full autoneg off

# 查看网卡收发包情况
ethtool -S eth0
ifconfig -s
```

* netstat (`yum install net-tools`)

```shell
# 列出所有端口
netstat -a
# 列出所有监听端口
netstat -l
# 按照协议列出所有端口的统计信息
netstat -s 
# 显示tcp链接及其进程
netstat -pt
# 显示路由信息
netstat -r
# 找出程序运行的端口
netstat -ap | grep ssh
netstat -an | grep ':80' # 运行在80端口上的程序
# 链接某服务端口最多的IP地址
netstat -ntu | grep :80 | awk '{print $5}' | cut -d: -f1 | awk '{++ip[$1]} END {for(i in ip) print ip[i],"\t",i}' | sort -nr
```

* route  路由管理

```shell
# 添加一条去往192.56.76.X网络的路由，从设备eth0发送
route add -net 192.56.76.0 netmask 255.255.255.0 dev eth0

# 添加一条去往192.1.3的主机路由，网关地址是172.16.0.1,从设备eth0发出
route add -host 192.168.1.3 gw 172.16.0.1 dev eth0

# 查看路由表
route -n

```

* IP 

```shell
# 显示网卡收发信息
ip -s link

# 显示网卡状态,是up 还是 down
ip addr 
ip link 
```



  ### 13、磁盘管理

#### 13.1 磁盘管理常用命令

  ```shell
  # 磁盘分区信息查看
  fdisk -l  
  
  # 磁盘使用情况查看
  df -Th   
  
  # 磁盘分区
  fdisk /dev/sda 
  partprobe  # 分区表有效
  
  # 格式化分区
  mkfs.ext4 /dev/sda5
  
  # 挂载新的分区
  mkdir /mnt/sda5
  mount /dev/sda5 /mnt/sda5
  # 卸载
  unmount /mnt/sda5
  
  # 编辑  /etc/fstab 使其开机有效，  blkid 命令可以设备UUID，建议使用UUID
  /dev/sda5  /mnt/sda5  ext4  defaults  0  0
  UUID=332ad3d3311......  /mnt/sda5  ext4  defaults  0  0                          
  
  # 创建SWAP ,首先用fdisk -l 分一个swap分区，或者在fdisk 中修改磁盘类型 t                         
  mkswap /dev/sda6
  # 配置文件/etc/fstab
  UUID=，，，，，，    swap  swap defaults 0 0 
  # 查看swap分区
  swapon -s  
  # 卸载
  swapoff /dev/sda6 
  # 挂载通过fstab
  swapon -a 
  # 挂载fstab中所有的配置
  mount -a 
  
  
  # fdisk 只能管理小于2T的硬盘，大于2T的硬盘用gdisk
  gdisk /dev/sdb
  ```

####  13.2 LVM 磁盘卷的管理

  ```shell
 Linux的LVM非常强大，可以在生产运行系统上面直接在线扩展硬盘分区，可以把分区umount以后收缩分区大小，还可以在系统运行过程中把一个分区从一块硬盘搬到另一块硬盘上面去等等，简直就像变魔术，而且这一切都可以在一个繁忙运行的系统上面直接操作，不会对你的系统运行产生任何影响，很安全。
# 磁盘卷
# 逻辑卷，redhat，lvm，
# sda1 sda2 >>>>>>  pv >>>>>> vg  >>>>>>> lv
# fdisk /dev/sdb
#  5  6  7 >>>>> 8e  转换成lvm
partprobe
# 第一步：创建pv ,pvcreate
pvcreate /dev/sda5{5..7}
pvs
pvdisplay
# 第二步：创建vg ,vgcreate,合成一个vg
vgcreate  stud01vg /dev/sda5 /dev/sda6
vgs
# 第三步：创建lv ,lvcreate
lvcreate -L 500M  stud01vg -n stud01lv
lvs
lvdisplay
# 删除
lvremove /dev/stud01vg/stud01lv
vgremove stud01vg
pvremove /dev/sda5 
  ```

  ```shell
  # 在线扩容
  pvcreate /dev/sda{5..7}
  vgcreate -s 32M stud01vg  /dev/sda5 /dev/sda6
  lvcreate -L 1G stud01vg -n stud01lv
  # 格式化
  mkfs.ext4 /dev/stud01vg/stud01lv
  mkdir /mnt/stud01lv
  mount /dev/stud01vg/stud01lv  /mnt/stud01lv/
  # 写入fstab
  blkid
  # vim /etc/fstab
  UUID="22222"  /mnt/stud01lv  ext4 defaults  0 0 
  # mount
  mount -a
  df -Th
  # 扩充
  lvresize -L +5G /dev/stud01vg/stud01lv  
  # 新建一个分区 sda7 加入
  vgextend stud01vg /dev/sda7  # 把sda7加入到stud01vg中
  pvs
  vgs
  lvresize -L 2G /dev/stud01vg/stud01lv 
  df -Th
  resize2fs /dev/stud01vg/stud01lv  # ext4
  df -Th
  
  ```

#### 13.3 XFS

  ```shell
  # centos 7 全面转向 xfs
  # xfs的扩容，准备分区，如sda4
  1、可扩展性ext4不如XFS
  2.Ext4的单个目录文件超过200W个后，性能下降的就比较厉害。由于Ext4 的inode 个数限制(32位数)最多只能有大概40多亿文件。而且Ext4的单个文件大小最大只能支持到16T(4K block size) 的话，这些至少对于目前来说已经是瓶颈。
  3.XFS使用64位管理空间，文件系统规模可以达到EB级别。
  4.如果存储的小文件多就选择xfs,其他情况下两者性能差不多。
  
  vgcreate stud01vg /dev/sda4
  lvcreate -L stud01vg -n stud01lv
  mkfs.xfs /dev/std01vg/stud01lv
  blkid
  mkdir /mnt/stud01lv
  vim fstab
  UUID =.........
  mount -a
  touch /mnt/stud01lv/stud01test
  df -Th
  lvresize -L 2G /dev/stud01vg/stud01lv
  df -Th
  # 在线扩容
  xfs_growfs /mont/stud01lv/
   
  ```

#### 13.4  磁盘配额

  ```shell
  # 准备分区，sda4 ,sda5
  mkfs.ext4 /dev/sda5
  mkdir /mnt/sda5
  setenforce 0 # 关闭SElinux，vim /etc/selinux/config ，不然扩容可能会失败
  blkid
  vim /etc/fstab
  UUID=333  /mnt/sda5  ext4   defaults,usrquota，grpquota 0 0
  mount -a
  quotacheck -cugv /mnt/sda5  # 检查磁盘的使用空间与限制
  # 在sda5中多两个文件，aquota.group   aquot.user
  setquota -u boss 10240 20480 5 6  /mnt/sda5/   # 10M报警，20M不让用了 ,5个文件警告，6不让用
  # 激活规则
  quotaon -ugv /mnt/sda5/
  
  history  # 历史命令
  
  # 测试：
  dd if=/dev/zero/ of=/mnt/sda5/1 bs=1M count=21
  ```

####  13.5 文件系统性能分析

https://www.cnblogs.com/sbaicl/p/4075679.html

> 文件系统EXT3，EXT4和XFS的区别： 
> 1. EXT3 
>   （1）最多只能支持32TB的文件系统和2TB的文件，实际只能容纳2TB的文件系统和16GB的文件 
>   （2）Ext3目前只支持32000个子目录 
>   （3）Ext3文件系统使用32位空间记录块数量和i-节点数量 
>   （4）当数据写入到Ext3文件系统中时，Ext3的数据块分配器每次只能分配一个4KB的块 
> 2. EXT4 
>   EXT4是Linux系统下的日志文件系统，是EXT3文件系统的后继版本。 
>   （1）Ext4的文件系统容量达到1EB，而文件容量则达到16TB 
>   （2）理论上支持无限数量的子目录 
>   （3）Ext4文件系统使用64位空间记录块数量和i-节点数量 
>   （4）Ext4的多块分配器支持一次调用分配多个数据块 
> 3. XFS 
>   （1）根据所记录的日志在很短的时间内迅速恢复磁盘文件内容 
>   （2）采用优化算法，日志记录对整体文件操作影响非常小 
>   （3） 是一个全64-bit的文件系统，它可以支持上百万T字节的存储空间 
>   （4）能以接近裸设备I/O的性能存储数据

###  14、启动流程和故障恢复

#### 14.1 Linux 启动流程

![](pic\1554785210197.png)

![](pic\1554785324229.png)

![](pic\1554785399392.png)

#### 14.2 Centos  6 故障恢复

##### 14.1.1 /boot/grub/grub.conf  详解

```shell
default=0   # 从第一个title 启动
timeout=5   # 等待5秒，-1 为一直等待
splashimage=(hd0,0)/gnjb/splash.xpm.gz  # 用来指定 GRUB 启动时的背景图像的保存位置。
hiddenmenu  # 隐藏菜单，要看到菜单就注释掉
title CentOS 6 (2.6.32-754.el6.x86_64)   #  菜单名称
kernel /vmlinuz-2.6.32-279.el6.i686 ro root=UUID=b9a7a1a8-767f-4a87-8a2b-a535edb362c9 rd_NO_LUKS KEYBOARDTYPE=pc KEYTABLE=us rd_NO_MD crashkernel=auto LANG=zh_CN.UTF-8 rd_NO_LVM rd_NO_DM rhgb quiet
initrd /initramfs-2.6.32-754.el6.x86_64.img
# /vmlinuz-2.6.32-279.el6.i686 内核位置，/ 指的是 boot 分区
# ro 只读打开内核
# root=UUID=b9a7a1a8-767f-4a87 根文件系统的所在位置
# rd_NO_LUKS  禁用LUKS（磁盘加密） ，这四个禁用是为了加速系统启动
# rd_NO_MD    禁用软RAID
# rd_NO_DM    禁用硬RAID
# rd_NO_LVM   禁用LVM
# KEYBOARDTYPE=pc KEYTABLE=us：键盘类型。
# crashkernel=auto：自动为crashkernel预留内存。
# LANG=zh_CN.UTF-8：语言环境。
# rhgb：(redhatgraphics boot)用图片来代替启动过程中的文字信息。启动完成之后可以使用dmesg命令来查看这些文字信息。
# quiet：隐藏启动信息，只显示重要信息。
# initrd /initramfs-2.6.32-754.el6.x86_64.img：指定了initramfs虚拟文件系统镜像文件的所在位置。
```

<font size="4" color="yellow">注：在手动恢复这个文件时，最重要的三个字段是init (h0,0),kernel  , initrd 其他都可以省略</font> 

##### 14.1.2 单用户模式下修改root密码

* 必须在主机的控制台上，不能远程操作

```shell
# 1、重启电脑，进入菜单
# 2、在菜单中按 a 键
# 3、在行末输入 1 ，回车
# 4、passwd root
# 5、输入新密码OK
```

##### 14.1.3 系统恢复实验：

- 先用 getenforce  查看 selinux 状态 , 如果是Enforcing，则用`setenforce 0`暂时关闭，否则实验容易失败。
- <font color="red" >grub文件损害后的手动恢复</font>(记得备份好grun.conf或者做好虚拟机快照)

```shell
# 1、删除/boot/grub/grub.conf
# 2、重新启动虚拟机
# 3、重启后系统会停留在 grub> 提示符下，手动输入：
root (hd0,0)  # 回车
kernel /vmlinuz-2.6.32-754.el6.x86_64 ro  # tab 补齐，回车
initrd /initramfs-2.6.32-754.el6.x86_64.img # 回车
boot #回车

```

- vim  /etc/fstab

- 系统恢复实验

  ```shell
  rm -rm /boot/*
  rm -f /etc/fstab
  rm -f /etc/inittab
  rm -f /etc/rc.d/rc.sysinit
  rm -f /etc/rc.d/rc.local
  dd  if=/dev/zero of=/dev/sda  bs=446 count=1
  # 进入光盘救援模式
  fdisk -l
  mkdir /stud01   # 在光盘上建立个目录
  mount /dev/sda2 /stud01  #把根目录挂载到stud01上
  ls -l /stud01
  cp /stud01/backup/fstab /stud01/etc/fstab
  exit
  reboot
  
  mkdir /stud01
  mount /dev/cdrom /stud1/
  rpm -ivh /stud1/Packages/kernel-2.xxxxxxxx  --root=/mnt/sysimage --force
  ls -l /mnt/sysimage/boot/
  chroot /mnt/sysimage/   #挂载到根上
  grub-install /dev/sda   #恢复grub
  ls -l /boot/grub/
  vim /boot/grup/grub.conf
  --------------------------
  default=0
  timeout=3
  title  stud01
  kernel /vmlinuz=2.6.32-642.e16.x86.64 ro root=/dev/sda2
  initrd /initramfs-2.6.32-642.e16.x86.64.img
  --------------------------------------
  rpm -qf /etc/inittab
  rpm -qf /etc/rc.d/rc.sysinit
  rpm -qf /etc/rc.d/rc.local
  mount /dev/cdrom /mnt/cdrom
  rpm -ivh /mnt/cdrom/Packages/initscripts-9.03xxxxxxx.rpm --force
  
  ```