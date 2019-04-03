#### 一、linux简介：

* Unix对Linux的最大贡献就是非常不好用
* Unix诞生于60年代末期的贝尔实验室
* Linus Torvalds 来纳斯  ，1991/10/5，大学学Unix极其不爽，写了个几十K的内核，放在GNU
* GNU ，创始人richard stallman 第一黑客，组织的中心思想是开源，技术发展慢，开源拿着去，开源放回来
* 发展出好多衍生版本
* 微软，最后的8M。
* red hat ：最大的开源公司
* Fedora  ：飞到热，新的软件，测试没问题放会redhat，redhat桌面版
* ubuntu : 号称界面最精美
* debian :的版，纯开源
* suse: 
* 中标麒麟：一个军用，一个民用
* 深度deepin: 基于debian
* centos   :
* 差不多，99%相似
* redhat 稳定性最好，使用最广，美国北卡罗来纳州，全球22个分部
* 课程设计的非常好
* rhce 中级，rhca 最高级，几百个，中国大头，
* 按照培训课程体系走
* RHEL 红帽企业版

二、系统安装

* https://opsx.alibaba.com/mirror
* http://mirrors.163.com/
* everythin   什么都有，包含源码包
* kdump   崩溃转存，内存中花一块地
* /boot     启动相关，内核  200M
* /  根分区  
* swap <8g 两倍内存，内存不够用的当内存用。

#### 三、基础操作

* 普通用户$，root用户#
* 图形化对服务器没有好处，占资源，耗带宽
* etc/shells
* cd -  回到上一次
* cd ~  回到家目录
* alias 查看别名

四、文件管理

* touch
* 文件最长256个字符
* 文件名前加点 .  隐藏文件
* b 块设备   c  字符设备
* id root
* su - qin
* chown  root:root  /home/qin/test
* u(user)   g(group)    o(onthers) 
* useradd bing
* rwx    
* groupadd  caiwubu
* useradd kuaiji -g caiwubu
* chown kuaiji:caiwubu /caiwubu/    对文件夹生效， -R  递归
* chmod o-r  -R /caiwubu/
* r -4   w -2    x-1    chmod 400 /caiwubu/zhangben
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

#### 八、用户和组

* cat /etc/passwd
* `root​:x:​0:0:root:/root:/bin/bash`    3列： uid   普通用户1000以后 ，/bin/bahs 该用户可以登陆   
* 第4列 组用户，第5列 描述，第6列  家目录  
* cat /et/shadow   密码
* uid  为 0 权利最大，为管理员
* useradd  bing
* useradd  -u  8888  boss
* userdel -r  bing     -r   删除相关资源
* passwd  zhangsan    
* bc
* 1970.1.1
* shadow  mima:密码创建时间： 几天只能不能该密码：密码有效期：过期多少天前提醒：过期后几天禁用
* chage -d 0 zhangsan   -d有效期   -E  失效日期
* /etc/group      /etc/gshadow
* groupadd xiaoshoubu
* id xiaoshou
* useradd -g   xiaoshoubu xiaoshou2    -g  分配组
* useradd -G xiaoshoubu xiaoshao3  -G   建同名组并且加入xiaoshoubu
* usermod -g shichangbu xiaoshou2    修改用户
* groupdel    组里不能有成员

#### 九、软件包的安装

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
  
  ```

  






