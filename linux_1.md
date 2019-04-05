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
> tail -n 5 /etc/passwd  # 现实最后5行
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
chmod go-w+x <dir> # 拒绝组成员和其他人创建或删除目录 dir（go-w）中文件的权限，允许组成员和其他人搜索 dir，或在路径名(go+x)中使用它.

# 用数字修改文件访问权限，-R 迭代目录
chmod 700 ex0   #  user拥有最大权限（rwx 4+2+1=7)，组和其他人无权限



# 两个文件属性查看命令：
file ex01    # file 辨识文件类型
stat ex01    # 文件/文件系统的详细信息显示,诸如访问时间，修改时间等
```

#### 5.3 文件隐藏属性的设置

* 对每一个文件设置更精确的权限设置，设置文件访问列表ACL
* 

```shell


```



* umask  掩码  0022     ：    umask   0000
* useradd boss
* setfacl  -m u:boss:rwx  -R  /caiwubu/         set   f    acl
* ll 后有个加
* getfacl  /caiwubu/zhangben 
* lsattr   /caiwubu/zhangben    隐藏属性
* chattr   +i /caiwubu/zhangben    i 不让改不让删    a 能追加   root也不行
* chattr  -i /caiwubu/zhangben
* ln -s /etc/passwd  ./passwd2   软链接
* ln    /etc/passwd   ./passwd3   硬链接     -rw-r--r--   2    有一个硬链接这个数字加1，与源文件保持一致

#### 五、目录管理：

* /root
* /boot    内核，启动资源
* /home   用户家目录
* /dev    设备，sda   cpu
* /etc    配置文件
* /mnt   挂载点
* /opt    第三方工具
* /proc    虚目录，对应内存映射，开机才有
* /run     运行的东西，进程号
* /srv
* /sys   虚目录，对应内存映射，开机才有
*  /usr   自己编译的文件
* /var  放一些数据文件，日志文件  /var/log/messages
* /lib   /lib64    动态链接库
* /bin   /sbin    可执行文件
* /tmp   临时文件，定期自动清理

* which  rm

* u+s  g+s  o +t

* u+s   加给命令的，passwd  bing  , which passwd  , ll /usr/bin/passwd

* 有 s 时，表示暂时拥有属主的权限

* chmod u+s /usr/bin/vim     相当于给命令提权

* vim /etc/passwd   保存成功

*  g+s  mkdir /caiwubu  /  groupadd caiwubu /  useradd -g caiwubu chuna

* 

* ll  -d /caiwubu/

* chown kuaiji:caiwubu -R /caiwubu/

* 谁创建的目录权限归谁

* 文件夹的执行权限表示能不能进来看

*  chmod g+s /caiwu/   不管谁建文件，属主归文件夹属主

* o+t  只有文件本人能管理

* u+s 4   g+s 2  o+t  1

* chmod 4740  qingbing    加在前面

#### 六、系统交互工具与编辑器

* linux下一切都是文件
* yy  复制当前行   p   粘贴
* 4yy   复制4行
* dd   剪切
* u   撤销
* gg   去第一行   G   最后一行
* o  下插一行  O 上插一行
* w  q   !
* 命令行模式下： r   /etc/fstab     把其他文件的内容读入
* ： r!  df -Th    把命令结果输入到文件内
* ：X  文件加密码    
* /mail   搜索   n  下一个
* : set number      :30       set nonumber
* s/nologin/qin/g   替换一行的    1,10s/nologin/qin/g 换10行的   %s/nologin/qin/g全部换掉
* vim  /etc/vimrc    配置文件

#### 七、输入、是输出和重定向

* `>`
* `>>`
* `2>`错误输出重定向
* find / -user qin > yes 2> no   正确和错误的分别输出
* find / -user qin &> all 疏导一个文件
* cat  >  qintest  <<  EOF
* |  管道     cat  /etc/passwd  |  grep  root
* wc  -l  /etc/passwd    多少行
* cat /boot/grub2/grub.cfg |  grep -v ^#  ^$    $空行
* head -n 2   头两行    tail -n 2  尾2行    
* tail -f /var/log/messages   持续不断后10行
* sort  qintest  排序文件内内容   sort  - n   按数字大小排序  -r 反序
* sort  -t :  -k3  -n /etc/passwd    按冒号分割按第3列,以数字排序
* uniq  qingtest     去重    uniq  -c  qintest   统计合并  挨着的合并
* df -Th  | tee file |  grep boot  |  tr -s " " | cut -d "  " -f 6    ;   tr  把多个空格转换成一个
* tee file     转存文件
* paste 1 2 3  按列合并  按行对应

#### 八、用户和组九、软件包的安装

* rpm    yum    编译安装

* rpm   redhat 打包格式

* mkdir /mnt/cdrom/

* mount /dev/cdrom  /mnt/cdrom/

* rpm -ivh  /mnt/cdrom/Packages/zziplib-i331xxxxxxxxx.rpm --force 

* rpm -e   rpm包名   卸载

* rpm -qa    查询所有安装过的包

* rpm -qpi  xxx.rpm   查询包信息

* rpm  -qf  /usr/bin/touch     查询从那个包装的

* which touch

* 红帽内核升级必须用rpm，千万不要终止升级过程

* rpm  不能解决依赖包

* yum  yellow dog  解决依赖包

* vim /etc/yum.repos.d/1222.repo     仓库源

* rm /etc/yum.repos.d/*

* vim /etc/yum.repos.d/qin.repo

* ```
  [qin]
  name=qin
  baseurl=file:///mnt/cdrom
  enabled=1
  gpgcheck=0
  ```

* yum list

* yum install   httpd

* yum remove  httpd

* yum search htt

* yum clean all    清缓存

* yum makecache   建立缓存

* .bin   的安装   ，直接运行它

* 源码包，编译安装

* PREFIX   安装在那里

* make   假装编译一下

* make install   开始安装

* service nginx start

#### 十、系统监控及进程管理

* uname -r   

* uname -a

* lscpu

*  cat  /proc/cpuinfo

* cat  /proc/meminfo

* hostname

* hostnamectl  set-hostname qin   改主机名

* last  

* top  

* ```
  zombie  僵尸进程，
  id  空闲情况
  
  ```

* pstree  

* `dd if=/dev/zero of=/dev/null bs=1M count=10000000000000`

* ps  aux   | grep  

* kill  -l  给进程发信号

* kill -19 2978

* pidof   httpd

* killall -9 httpd  

* firfox &   放到后台

* ctrl + z 回到后台   fg 回去    

* jobs

* fg 1

#### 十一、服务与计划任务

* linux 6

* system-v 架构

* 第一个进程是init

* service httpd start  stop  restart  status

* vim /etc/httpd/conf/httpd.conf

* vim /etc/inittab,id:5:initdefault:  

* init 6  重启去了

* chkconfig --list

* chkconfig httpd on    开机启动

* chkconfig iptables off   

* linux 7

* pstree    /   systemd

* systemctl  start httpd

* !yum 表示执行上一次的yum命令

* ![](\pic\1554028346756.png)

  这个disabled 表示不随机启动

* systemctl enable httpd.service   随机启动

* systemctl  mask httpd.service   不允许启动这个服务

* systemctl unmask httpd.service

* systemctl set-default runlevel3.target

* systemctl  get-default

* systemctl list-unit-files

* systemctl mask firewalld.service

* vim  /etc/selinux/config   selinux=disabled

* systemctl  status atd.service    一次性计划任务

* at  1 am  monday

  ```
  > /usr/bin/touch  /root/Desktop/qin
  > /usr/bin/systemctl restart httpd
  ```

* atq   查询定任务

* atrm 删除定时任务

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

#### 十二、启动流程和故障恢复

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

  #### 十三、系统文件查找与文件管理

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

  #### 十四、网络管理

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

  #### 十五、磁盘管理

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

  


