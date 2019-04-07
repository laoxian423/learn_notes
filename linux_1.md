       1991年10月5日，还在上大学的Linus在一次UNIX实验后，对UNIX极度不满，决定自己写一个最好用操作系统，随后将第一个Linux 内核版本放到GNU。
       GNU  自由软件基金会，由当时被成为第一黑客的richard stallman创建
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
>   注：everythin 版本，包含所有的RPM和源码包。
>
> ```shell
> # 部署虚拟机实验环境，最好虚拟两台，一台安装centos 6 ,一台安装centos 7,6 和 7有一部分系统管理不同，目前6和7是企业中使用最广的版本。其中6.8被称为6里面的终极稳定版。
> # 安装过程比较简单，只需注意一下几点：
>   1、无关硬件都去掉，比如声卡、打印机等
>   2、在安装配置中不要启用SELinux,后期学习过以后再考虑启动
>   3、KDUMP 为系统崩溃转存功能，可关闭。
>   4、硬盘最好分区，不要一股脑分到一个区上，不利于后期实验，下面是建议：
>       /boot    启动相关的文件，还有内核，分配200M即可
>       swap     如果内存<8G ,就分配两倍内存的空间。如果内存很大比如256G，这个分区
>                不用过大，没有必要。
>       /        剩下的都可以给根。
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
> # 查找文件位置：
> which rm   
> find 
> whereis 
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

### 7、系统交互工具与编辑器 vim

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
  [qin]
  name=qin
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

* `dd if=/dev/zero of=/dev/null bs=1M count=10000000000000`  给CPU施加压力

### 11、服务与计划任务

#### 11.1  systemv 和 sytemd

>**system V (Linux 6):**
>
>* 大多数基于Linux的操作系统，使用的是System-V风格的init守护进程，换句话说，它们的启动处理由**init**进程管理，其管理功能在一定程度上继承了基于System V 的Unix操作系统。该守护进程根据运行级别(run level)的原则，系统的运行级别表示当前计算机的状态。
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
>**systemd(Linux 7)**
>
>* 守护进程是systemd。
>* 在systemd的管理体系里面，以前的运行级别（runlevel）的概念被新的运行目标（target）所取代。target（相当于以前的默认运行级别）是通过软链来实现。如： 
>  `ln -s /lib/systemd/system/runlevel3.target /etc/systemd/system/default.target `
>* /etc/inittab 文件被废弃。
>* systemd使用systemctl命令管理。

#### 11.2  Linux 6 操作：

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

#### 11.3 Linux 7 操作

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
  # atd服务管理，Linux 6
  service atd start    # 启动服务
  service atd  stop    # 关闭服务
  service atd restart  # 重启服务
  service atd reload   # 重新载入配置
  service atd status   # 查看服务状态 
  # atd服务管理，Linux 7
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

  

* 

* crond  周期任务

* crontab   -e -u root

  ```
  # 分时日月周
  30  2 * * 1,3,5  /usr/bin/touch /root/Desktop/bing 
  30 2 * * 1 /qin.sh
  - 几号到几号
  1,3,5  每周1,3,5
  */2  每隔两天
  ```

* vim  /etc/cron.deny     把用户名写进去

### 12、启动流程和故障恢复

* linux  6

![](\pic\1554035939501.png)

* du  -sh    /boot/grub/

* /boot/grub/grub.conf

  ```
  default=0   从第一个title 启动
  
  ```

* blkid    查询uuid

* 单用户模式破解密码

* getenforce

* setenforce 0  暂时关闭

* passwd root

* vim  /etc/rc.d/rc.sysinit

* vim /etc/rc.d/rc脚本   k   s    用来决定开机是否启动

* 删除grub文件后的恢复

  ![](\pic\1554039459655.png)

  * vim  /etc/fstab

  * 系统恢复实验

    ```shell
    rm -rm /boot/*
    rm -f /etc/fstab
    rm -f /etc/inittab
    rm -f /etc/rc.d/rc.sysinit
    rm -f /etc/rc.d/rc.local
    dd  if=/dev/zero of=/dev/sda  bs=446 count=1
    # 进入光盘救援模式
    fdisk -l
    mkdir /qin   # 在光盘上建立个目录
    mount /dev/sda2 /qin  #把根目录挂载到qin上
    ls -l /qin
    cp /qin/backup/fstab /qin/etc/fstab
    exit
    reboot
    
    mkdir /qin
    mount /dev/cdrom /qin/
    rpm -ivh /qin/Packages/kernel-2.xxxxxxxx  --root=/mnt/sysimage --force
    ls -l /mnt/sysimage/boot/
    chroot /mnt/sysimage/   #挂载到根上
    grub-install /dev/sda   #恢复grub
    ls -l /boot/grub/
    vim /boot/grup/grub.conf
    --------------------------
    default=0
    timeout=3
    title  qin
    kernel /vmlinuz=2.6.32-642.e16.x86.64 ro root=/dev/sda2
    initrd /initramfs-2.6.32-642.e16.x86.64.img
    --------------------------------------
    rpm -qf /etc/inittab
    rpm -qf /etc/rc.d/rc.sysinit
    rpm -qf /etc/rc.d/rc.local
    mount /dev/cdrom /mnt/cdrom
    rpm -ivh /mnt/cdrom/Packages/initscripts-9.03xxxxxxx.rpm --force
    
    ```

  * linux 7

  * ll /boot/

  * vmlinuz-0-rescue......

  * cd /boot/grub2/

  * /etc/grub.d/*



### 13、系统文件查找与文件管理

  ```shell
which rm
whereis  touch
locate passwd  不能直接用，updatedb，后期不用做
find  /  -name  passwd
find / -name *passwd*
find /etc/ -type d    #找文件夹
find / -type b  #按文件类型找
find / -user qin #按用户找
find / -size +1M 
find / -perm 777
find /etc/ -type f -and -size +1M 
find / -user qin -exec cp -rf {}  /root/Desktop/qin/  \;
   
# 文件里找内容
grep   root  /etc/passwd
grep -i ROOT /etc/passwd  #忽略大小写
 
# 压缩解压  gzip  bzip2 
# tar 打包
/var/log
tar czvf log.tar.gz /var/log/  #c建立tar包，z gzip v 要看到过程 f 保存的文件名
date +"%Y-%m-%d"
tar czvf /root/Desktop/`date +%F`-log.tar.gz /var/log/
file <filename> #看文件类型
# 解压
tar xzvf /root/Desktop/sssss.tar.gz -C  /tmp/  #指定解压路径  
  ```

  ### 14、网络管理

  ```shell
# linux 6
network   
service NetworkManager stop
chkconfig NetworkManager off
service network start
chkconfig network on
# 查询网卡地址信息
ifconfig
ip addr show
vim /etc/sysconfig/network-scripts/ifcfg-eth0
service network restart
!ser
# 一个网卡可以有多个网卡
cp /etc/sysconfig/network-scripts/ifcfg-eth0  /etc/sysconfig/network-scripts/ifcfg-eth0：0
vim /etc/sysconfig/network-scripts/ifcfg-eth0:0
#  DEVICE=eth0:0
#  IPADDR=new ip
service network restart 
  
  ```

  ```shell
  # linux 7
  NetworkManager
  nmcli
  systemctl
  systemctl mask network
  systemctl stop network
  systemctl start NetworkManager
  systemctl enable NetrokManager
  
  en以太网  wl无线  ww  o 集成  s PCI  p usb外置网卡
  # 取消新的网卡名计算方法。
  vim /etc/sysconfig/grub 
  GRUB-CMDLINE_LINUX="rhgb quiet net.isnames=0 biosdevname=0"
  grub2-mkconfig -o /boot/grub2/grub.cfg
  
  要去想办法适应技术
  
  
  ```

  ### 15、磁盘管理

  ```shell
  # 磁盘查看和分区
  fdisk -l  # 分区信息
  /dev/sda
  df -Th   #磁盘使用情况
  fdisk /dev/sda 
  # 格式化分区
  mkfs.ext4 /dev/sda5
  # 挂载
  mkdir /mnt/sda5
  mount /dev/sda5 /mnt/sda5
  # 卸载
  unmount /mnt/sda5
  vim /etc/fstab
  blkid  # 查看UUID
  /dev/sda5  /mnt/sda5  ext4  defaults  0  0
  /建议UUID                            /访问方式  /是否检测
  # 可以在fdisk 中修改磁盘类型 t                            
  # 创建SWAP                            
  mkswap /dev/sda6                            
  UUID=，，，，，，    swap  swap defaults 0 0 
  swapon -s  # 查看swap分区
  swapoff /dev/sda6 # 卸载
  swapon -a # 挂载通过fstab
  mount -a # 挂载fstab中所有的配置
  # 大于2T的硬盘
  gdisk /dev/sdb
  ```

  ```shell
  # 磁盘卷
  # 逻辑卷，redhat，lvm，
  # sda1 sda2 >>>>>>  pv >>>>>> vg  >>>>>>> lv
  准备7个分区
  5  6  7 >>>>> 8e  转换成lvm
  partprobe
  pvcreate /dev/sda5{5..7}
  pvs
  pvdisplay
  # 合成一个vg
  vgcreate  qinvg /dev/sda5 /dev/sda6
  vgs
  lvcreate -L 500M  qingvg -n qinlv
  lvs
  lvdisplay
  # 删除
  lvremove /dev/qingvg/qinlv
  vgremove qingvg
  pvremove /dev/sda5 
  ```

  ```shell
  # 在线扩容
  pvcreate /dev/sda{5..7}
  vgcreate -s 32M qinvg  /dev/sda5 /dev/sda6
  lvcreate -L 1G qinvg -n qinlv
  # 格式化
  mkfs.ext4 /dev/qinvg/qinlv
  mkdir /mnt/qinlv
  mount /dev/qinvg/qinlv  /mnt/qinlv/
  # 写入fstab
  blkid
  <fstab>
  UUID="22222"  /mnt/qinlv  ext4 defaults  0 0 
  mount -a
  
  df -Th
  # 扩充
  lvresize  
  vgextend qinvg /dev/sda7  # 把sda7加入到qinvg中
  pvs
  vgs
  lvresize -L 2G /dev/qinvg/qinlv 
  df -Th
  resize2fs /dev/qinvg/qinlv  # ext4
  df -Th
  
  ```

  ```shell
  # xfs的扩容，准备分区，如sda4
  vgcreate qinvg /dev/sda4
  lvcreate -L 1G qinvg -n qinlv
  mkfs.xfs /dev/qinvg/qinlv
  blkid
  mkdir /mnt/qinlv
  vim fstab
  UUID =.........
  mount -a
  touch /mnt/qinlv/qintest
  df -Th
  lvresize -L 2G /dev/qinvg/qinlv
  df -Th
  xfs_growfs /mont/qinlv/
  ```

  * 磁盘配额：不能随便用，要给用户限制使用

  ```shell
  # 准备分区，sda4 ,sda5
  mkfs.ext4 /dev/sda5
  mkdir /mnt/sda5
  setenforce 0 # 关闭SElinux，vim /etc/selinux/config
  blkid
  vim /etc/fstab
  UUID=333  /mnt/sda5  ext4   defaults,usrquota，grpquota 0 0
  mount -a
  quotacheck -cugv /mnt/sda5
  # 在sda5中多两个文件，aquota.group   aquot.user
  setquota -u qin 10240 20480 5 6  /mnt/sda5/   # 10M报警，20M不让用了 ,5个文件警告，6不让用
  # 激活规则
  quotaon -ugv /mnt/sda5/
  
  history  # 历史命令
  
  # 测试：
  dd if=/dev/zero/ of=/mnt/sda5/1 bs=1M count=9
  ```

  


