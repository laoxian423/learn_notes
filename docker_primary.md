**docker初级操作培训   **

#### 一、了解docker（[docker 官网 ](http://www.docker.com/) )

##### 1、docker的历史

> ​      要了解docker，首先要知道什么是容器，docker实际上就是管理Linux容器的一个工具。
>
> ​      容器已经存在了几十年，早起UNIX操作系统使用jail来形容一个修改过的运行时环境，**以防止程序访问受保护的资源**，通俗的说就是程序在运行的时候的软件环境、系统环境。在2005年，Sun的容器发布后，这一运行环境就被称之为容器。在docker推出来之前，需要手动配置容器，这一工作极富挑战且容易出错。这个问题直到2013年3月推出Docker后，终于得到解决。
>
> ​      Docker是由dotCloud公司在github上发布的一个开源项目，使用go语言开发，属于操作系统层面的虚拟化技术，可以将其视为一种新兴的虚拟化方式。

##### 2、docker是什么

> ​        docker不是一门编程语言，也不是构建软件的框架。docker是一个工具，是一个容器管理工具，可以帮助你解决如安装、拆卸、升级、分发、信任和管理软件等问题。
>
> ​        你可以把Docker当作软件分发供应商，用来节省你的时间，让你专注于高价值的事情。可以用docker构建网络应用、构建应用程序。

##### 3、docker解决了什么问题

> * 软件安装复杂性问题：要考虑操作系统的版本、内核的版本，所需的资源，与软件包冲突问题，与软件包的依赖问题，最后，你还需要知道如何安装。你还需要考虑多个程序在运行时的冲突和影响（多个程序运行在一个环境下会带来各种问题，比如升级、删除一个会不会影响到另外一个）。而docker可以有序的把这一切管理起来，docker通过容器和镜像隔离所有的一切。
> * 高移植性问题：只要能运行docker的系统（目前都可以），都可以运行相同的程序。
> * 安全性问题：容器将应用程序带来的影响，全部限制在容器内部，比如病毒、黑客，就像运行在一个沙箱内部，就算出了问题，删掉容器后重新创建容器即可。
> * 持续交付和部署：通过Dockerfile进行镜像创建，并结合持续集成系统。
> * 维护和扩展问题：高质量的官方镜像可以直接生产使用，应用的复用更为容易。应用打包部署，项目打包部署。
> * 资源利用率问题：单服务器能支持上千个容器
> * **干干净净的机器**
> * 没有Docker，一台机器看起来就像一个装满垃圾的抽屉。

##### 4、docker 与虚拟机

>* 虚拟机：模拟一套硬件，然后安装系统和软件，资源耗费多，部署环节多，开发和运维分离。
>* docker：不虚拟硬件，容器内的进程直接运行于宿主的内核，容器间进程隔离。资源耗费很小，部署快捷，开发既运维。 



##### 5、需要熟知的概念 

> docker 宿主机： 安装docker的物理、虚拟服务器
>
> docker镜像(Image)：特殊文件系统，包含容器运行所需的程序、库、资源、配置，除非重建镜像否则内容不会改变。
>
> dcoker容器(Container)：镜像和容器的关系就像类和实例，根据镜像生成的实例，容器可以启动、停止、删除。容器与容器之间是隔离的，每一个容器就像是一个沙箱。容器和宿主机之间的数据交换是权限可控的。容器有自己独立的命名空间，拥有自己的root，自己的网络配置，自己的进程空间等等，因此更加安全。
>
> docker仓库(Repository)：存放镜像的地方，有本地仓库和云端仓库（阿里、[docker hub](https://hub.docker.com)）.，用户可搭建私有仓库（官方的docker registry，VMWare Harbor 和 Sonatype Nexus)。

#### 二、准备一个实验环境

##### 1.准备宿主机系统

> * 准备宿主机：虚拟机并安装操作系统,内核不低于3.1（[centos](https://www.centos.org/download/) centos7）
>
> * 连接虚拟机（[putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)  [secureCRT]() )
>
> * linux常用命令：
>
> ```shell
> cat /etc/issue  # 查看发行版本（所有Linux适用）
> cat /etc/redhat-release #查看发行版本（redhat centos适用)
> cat /etc/os-release
> uname -r #查看linux内核版本
> cat /proc/version #查看内核，稍微详细
> cat /proc/cpuinfo   #查看CPU信息文件
> cat /proc/meminfo   #查看内存信息文件
> reboot   #重启
> halt     #关闭系统
> yum install #安装软件包
> yum remove #移出软件包
> ```
>
> * putty的拷贝工具pscp,可以从Windows和Linux之间拷贝文件：
>
> `pscp -C root@192.168.159.139:/home/compose-haproxy-web/web/index.py e:\`



##### 2、安装docker

[docker有两个版本](https://www.docker-cn.com)：社区版CE版和企业版EE。我们安装CE版,需要安装在64位平台上，内核不低于3.10，内核越新越好。

[多查看安装帮助](https://docs.docker-cn.com/)，官方网站有详细安装步骤。（最好的资料就是官方文档）

```shell
#设置yum源，安装依赖包
yum install -y yum-utils device-mapper-persistent-data lvm2
yum-config-manager \
     --add-repo \
     https://download.docker.com/linux/centos/docker-ce.repo
yum makecache fast
yum install docker-ce
```

##### 3、启动和停止

```shell
docker version	#查看版本
systemctl start docker	#启动
systemctl stop docker̴	#停止
systemctl status docker	#状态
systemctl restart docker̴̴	#重新启动
systemctl enable docker	#设置开机自动启动
docker run hello-world	#验证，下载运行hello-world
```

##### 4、配置Docker镜像加速

​	[使用阿里云作为镜像加速](https://www.aliyun.com/)

​	使用淘宝账号登陆，点击控制台，点击“产品与服务”，点击容器镜像服务。

![1551684850407](http://pnxlhjoss.bkt.clouddn.com/1551684850407.png)

​	点击“镜像加速器” ，按照提示操作。

#### 三、第一次体验用docker部署应用：

>    通过安装Tomcat服务，体验一下使用docker部署应用的快捷。

##### 1、从镜像仓库拉取Tomcat官方镜像

```shell
docker search tomcat       # 查看tomcat信息
```

![1553491997975](http://pnxlhjoss.bkt.clouddn.com/1553491997975.png)

```shell
dcoker pull tomcat  # 拉取镜像
```

![1553492313605](http://pnxlhjoss.bkt.clouddn.com/1553492313605.png)

##### 2、运行tomcat

```shell
docker run -it -d -p 80:8080 tomcat 
```

从浏览器输入IP地址，如：http://192.168.159.139 ,tomcat 已经正常运行。

![1553492589185](http://pnxlhjoss.bkt.clouddn.com/1553492589185.png)

#### 四、docker 命令行操作：

```shell
# 获取docker 帮助
docker help 
# 获取docker某个命令的帮助,如获取cp命令的帮助
docker help cp
```



#### 五、docker镜像操作

​        **输入docker可以查看命令用法，docker COMMAND --help查看详细用法。**

##### 1、镜像文件常用操作命令

| 操作             | 命令                             | 说明                                                         |
| ---------------- | -------------------------------- | ------------------------------------------------------------ |
| 查找             | docker search 关键字             | 可以在Docker Hub 网站查看镜像的详细信息，如镜像的tag标签<br> `docker search centos` |
| 拉取             | docker pull 镜像名:tag           | 从官方镜像仓库拉取镜像，`:tag`标识软件的版本，如果不指定默认是latest<br> `dcoker pull centos` |
| 查看本地镜像     | docker images                    | 这里看到的镜像大小和Docker Hub中显示的大小不同，Hub上显示的压缩后的大小。镜像大小的总合没有看起来那样大，由于UFS分层存储的原因，实际耗费空间要小的多。【虚悬镜像，已被发布者覆盖掉的镜像，显示为none】【中间层镜像】<br> `docker images `  #简单列出本地镜像 |
| 查看镜像详细信息 | docker inspect 镜像id            | 查看镜像文件详细信息                                         |
| 删除本地镜像     | docker rmi -f 镜像id或镜像名:tag | 删除本地镜像文件，-f 强制删除，不管它有没有容器存在          |
| 保存             | docker save                      | b保存镜像文件为归档文件`docker save centos |gzip > alpine-latest.tar.gz`,该命令官方不推荐使用 |
| 加载             | docker load                      | j加载镜像，`docker load -i alpine-latest.tar.gz` <br> `docker save <镜像名> |bzip2 |pv|ssh <用户名>@<主机名> 'cat | docker load'` 实现一个命令从一个机器迁移到另一个机器上。该命令官方不推荐。 |

##### 2、镜像操作的一些用法

```shell
#列出某个特定镜像
docker images ubuntu:18.04
#过滤参数filter的用法
docker images -f since=mongo:3.2
docker images -f before=mongo:3.2
#以特定格式显示
docker images -q    #只显示ID
docker images --format "{{.ID}}:{{.Repository}}"  #格式输出，只显示ID和工厂，无标题行
docker images --format "table {{.ID}}\t{{.Repository}}\t{{.Tag}}"  #包含标题
# 批量清理临时镜像文件
docker rmi $(docker images -q -f dangling=true)
# 本地镜像文件放在哪里？
/var/lib/docker/

```



#### 六 、docker容器操作

##### 1、常用容器操作命令列表：

| 操作       | 命令                                                         | 说明                                                         |
| ---------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 运行       | docker run --name 容器名 -i -t -p 主机端口:容器端口 -d -v 主机目录:容器目录:ro 镜像id或镜像名称:tag<br> `docker run --name mytomcat -it -p 80:8080 -v /web:/web:ro tomcat` | --name  自定义容器名；可以通过docker rename old new改名字<br> -i  以交互方式运行;<br>-t 分配一个伪终端；<br>-p 端口映射，宿主机端口与容器内端口映射；<br>-d 后台运行；守护方式<br>-v 挂载宿主机目录到容器目录，默认读写rw,ro表示只读。 |
| 创建       | docker create nginx                                          | 创建但是不运行容器，可以用start启动，这种方式主要是为了在it方式下使shell获得容器的ID：<br> CID=$(docker create nginx)<br> echo $CID |
| 查看       | docker ps -a -q                                              | 查看正在运行的容器。-a 显示所有  ，-q只显示id                |
| 启动       | docker start 容器id或名称                                    | 启动容器                                                     |
| 停止       | docker stop 容器id或名称                                     | 停止正在运行的容器                                           |
| 删除       | docker rm -f 容器id或名称                                    | 删除容器，-f 强制删除                                        |
| 日志       | docker logs 容器id或名称                                     | 获取容器日志                                                 |
| 进入容器   | docker exec -it 容器id或名称 /bin/bash                       | 进入容器并开启一个交互式终端。                               |
| 拷贝       | docker cp 主机文件 容器id或名称:容器路径；docker cp 容器id或名称:容器路径 主机文件 | 在宿主机和容器之间拷贝数据                                   |
| 获取元信息 | docker inspect 容器id或名称                                  | 获取容器的元信息                                             |

##### 2、命令举例：

```shell
# 如何停止所有容器：
docker kill $(docker ps -q)
# 清理批量后台停止的容器：
docker rm -f $(docker ps -aq)
# 获得某个容器的PID，c751f56e496d是某个容器的ID
docker inspect --format '{{ .State.Pid }}' c751f56e496d
# 获取某个容器的IP
 docker inspect --format '{{ .NetworkSettings.IPaddress}}' c751f56e496d
# 出一个正在交互的容器的终端， 而不终止
ctrl-p  ctrl-q

```

##### 3、补充说明

> * 如果容器内的程序运行，容器运行；程序停止，容器停止；

#### 七、 自定义docker镜像文件

##### 1、更新已有镜像文件

当已有的镜像文件不满足我们的要求，可以使用 docker commit 进行修改。

> tip:把自己的镜像上传到阿里仓库:
>
> 首先登陆阿里用（可以使用淘宝账户），在镜像容器服务中创建命名空间和镜像仓库，设定Registry登陆密码。
>
> 在镜像仓库中点击“管理”，里面有说明如何上传和下载镜像文件(有提供详细命令)

 

 **注：实际工作中并不会使用commit：容易造成镜像臃肿；黑箱镜像，别人无从得知你做了什么；目前的主要用途就是被入侵后保存现场 **

* 先根据要修改的镜像，创建容器，如：

```shell
docker run -it -d centos
```

* 然后修改你的容器，比如我们安装一个vim:

```shell
docker exec -it d33da313a /bin/bash  # 进入到这个容器中
vim # 提示没有这个命令
yum install vim 
exit
```

* 提交为新镜像，语法：` dcoker commit -m="描述信息"-a="作者" 容器id或容器名:tag `  

```shell
docker commit -m="增加vim编辑器" -a="laoxian" 6c5b52d06d97 laoxian/centos:1.0
```

* 运行新镜像

```shell
docker run -it -d laoxian/centos:1.0
docker exec -it 6c5b52d06d97 /bin/bash
vim # 可以用了
```

##### 2、根据dockerfile文件构建镜像文件

使用**docker build** 根据编写的Dockerfile文件生产新的镜像。

* 第一步，编写一个Dcokerfile，一般默认文件名为dockerfile，也可以是其他名称，使用其他名称需要用 -f 指定:


```shell
#基础镜像,必须是第一句
FORM tomcat
#作者
MAINTAINER laoxian
#执行命令
RUN rm -f /usr/local/tomcat/webapps/ROOT/index.jsp
RUN echo "welcome to tomcat!" > /usr/local/tomcat/webapps/ROOT/index.jsp
```
 > 在Docker Hub 上有很多官方镜像，可以直接做基础镜像：nginx  , redis , mongo , mysql , httpd , php , tomcat , node , openjdk , python , ruby ,操作系统类：ubuntu , debian , centos , fedora ,alpine等
 >
 > 特殊的scratch镜像：FROM  scratch，这个镜像是个虚拟镜像，表示一个空白镜像。对于linux下静态编译的程序来说，并不需要系统提供运行时的支持。所需要的一切库都在可执行文件里了。scratch会让镜像更小巧。

* 第二步，构建镜像。` docker build -f Dockerfile文件 -t 镜像名:tag`

```shell
docker build -f Dcokerfile -t laoxian/tomcat:1.1 # 指定镜像名的用法
docker build -t laoxian/tomcat:1.1 .  # 另一种用法，注意 “.” ,这是构建上下文路径，不是dockerfile路径
```

> **镜像文件构建上下文**：dockers在运行时分为docker引擎（就是守护进程）和客户端工具。引擎提供了一组REST API （docker Remote API），而如docker命令这样的客户端工具，则是通过API与Docker引擎相互交互，完成各种功能。Docker builde 命令构建镜像，并非在本地构建，而是在服务端，也就是引擎中完成的。这就引入了上下文的概念，当构建时，用户会指定镜像文件的上下文路径，docker build 得知这个命令后，会将路径下所有内容打包上传给引擎。
>
> 一般来说，会将dockerfile置于一个空目录下，或者项目根目录下，应该把项目所需文件拷贝到这个目录。也可以用 .gitignore 语法写一个dockerignore文件，改文件可以剔除不需要传给引擎的文件。
>
> 其他几种docker build 用法：
>
> * 直接用Git repo进行构建：`docker build https://github.com/twang2218/gitlab-ce-zh.git:8.14`
> * 用tar压缩包建立：`docker build http://servber/context.tar.gz`
> * 从标准输入中dockerfile构建：`docker build - < Dockerfile` 或者 `cat Dockerfile | docker build -` 甚至 压缩包`docker build - < context.tar.gz`

* 第三步，运行容器

```shell
docker run -p 8888:8080 -d laoxian/tomcat:1.1
```

##### 2.1 常用Dockerfile命令

| 命令       | 解释                                                         |
| ---------- | ------------------------------------------------------------ |
| FORM       | 指定基础镜像，既当前新建镜像是基于那个镜像                   |
| MAINTAINER | 指定作者                                                     |
| RUN        | 构建过程中要运行的命令                                       |
| ENV        | 设置环境变量                                                 |
| WORKDIR    | 指定默认工作目录，既进入容器后默认进入的目录，该目录必须事先存在。 |
| VOLUME     | 定义匿名卷，创建挂载点，也称容器数据卷，用于数据持久化和共享 |
| CMD        | 容器启动时要执行的命令，与RUN不同。CMD只有最后一条起作用，多写无用。有两种格式：`shell 格式：CMD <命令>`还有`exec 格式：CMD ["可执行文件","参数1","参数2"...]，在指定了ENTRYPOINT指令后，CMD指定具体的参数`。一般推荐使用exec格式。<br> **注意** ：容器内没有后台服务的概念，比如 `CMD service nginx start` 这样的命令是执行不了的，包括在容器内执行systemctl命令。正确的做法是直接执行nginx 可执行文件，并且以前台形式运行`CMD ["nginx","-g","daemon off;"]` |
| ENTRYPOINT | 指定容器启动时要运行的命令，docker run 后的参数会被作为ENTRYPOINT的参数，组合成新的命令。 |
| COPY       | 在构建中拷贝文件或目录到镜像中 `COPY hom* /mydir/` ,目标路径可以是绝对路径，也可以是相对路径（用WORKDIR指定），目标路径不需要事先创建，自动创建 |
| ADD        | 拷贝文件到镜像中，如果源文件是压缩文件且会自动在目标路径解压。（源路径可以是一个URL，下载后的文件权限默认为600，这个命令不推荐使用。）官方建议尽可能的使用COPY，因为它的命令功能单一，思路清晰。 |
| EXPOSE     | 指定对外暴漏的端口                                           |
| ONBUILD    | 当前镜像不执行，只有被作为基础镜像时才会执行                 |

**编写dockerfile需要注意的问题:** 

```shell
# 每一个RUN都会创建一层镜像。UFS最大层数限制是127层，比如
FROM debian:jessie
RUN apt-get update
RUN apt-get install -y gcc libc6-dev make
RUN wget -0 redis.tar.gz "http://download.redis.io/release....."
RUN mkdir -p /usr/src/redis
RUN tar -zxf redis.tar.gs -C /usr/src/redis --strip-components=1
RUN make -C /usr/src/redis
RUN make -C /usr/src/redis install
# 上面的这种写法不正确，会产生不必要的层数，导致镜像文件过大，正确的写法如下：
FROM debian:jessie
RUN buildDeps='gcc libc6-dev make' \
	&& apt-get update \
	&& apt-get install -y $buildDeps \
	&& wget -0 redis.tar.gs "http://downlad.redis.io/....." \
	&& mkdir -p /usr/src/redis
	&& RUN tar -zxf redis.tar.gs -C /usr/src/redis --strip-components=1
	&& RUN make -C /usr/src/redis
	&& RUN make -C /usr/src/redis install \
	&& rm -rf /var/lib/apt/lists/* \
	&& rm redis.tar.gz \
	&& rm -r /usr/src/redis \
	&& apt-get purge -y --auto-remove $buildDeps
```



##### 2.2 几个例子

```shell
## 给官方镜像centos添加 vim , wget 。
# 第一步，编写Dockerfile文件，文件名任意起，比如 Dockerfile2
vi Dockerfile2
## 下面是dockerfile文件内容
#------------------------------------------------------------------------------------------
# 基础镜像
 FROM centos
# 作者
 MAINTAINER laoxian@21cn.com
# 设置环境变量
 ENV MYPATH /usr/local/centos
# 运行命令：新建一个目录，由环境变量$MYPATH指定
RUN mkdir -p $MYPATH
# 指定默认工作目录，进入容器后进入的目录
WORKDIR $MYPATH
# 运行命令
RUN yum -y install vim
RUN yum -y install wget
# 创建挂载点，无法对应宿主机目录，自动生成的
VOLUME ["/data1","/data2"]
CMD ["/bin/bash"]
#-------------------------------------------------------------------------------------------

#使用docker build构建镜像
docker build -f Dockerfile2 -t laoxian/centos:v1 .
#运行容器࢏
docker run -it laoxian/centos:v1
#查看镜像的变更历史
docker history b25b1dad795c
# 验证挂载点
/var/lib/docker/volumes/0b001b4cc8db1ebbbb4c537c17a5c44adb700fb0e1b941bc82cc717c4ae1
96f6/_data
/var/lib/docker/volumes/f020f5a5664bf68312be9f49a640f27ecfb49990b231aaf3d0eb7cb723fa0dd
d/_data
```

```shell
##  自定义一个TOMCAT 和指定版本的 JDK
# 编写dockerfile
vi Dockerfile
#----------------------------------------------------------------------------------------------
FROM centos
MAINTAINER laoxian@21cn.com
#拷贝文件，事先下载好，文件必须和Dockerfile在同一目录中
COPY test.txt /usr/local      # test.txt是一个用来体验COPY命令的文件，随便什么文件都行 
ADD jdk-8u171-linux-x64.tar.gz /usr/local   #jdk 从官网下载
ADD apache-tomcat-8.5.30.tar.gz /usr/local  #tomcat 从官网下载
#配置JAVA运行所需的环境变量
ENV JAVA_HOME /usr/local/jdk1.8.0_171
ENV CLASSPATH .:$JAVA_HOME/lib
ENV CATALINA_HOME /usr/local/apache-tomcat-8.5.30
ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/bin
WORKDIR $CATALINA_HOME
RUN yum -y install vim
EXPOSE 8080    # 对外暴漏的端口
CMD ["catalina.sh", "run"]  # 运行tomcat
#----------------------------------------------------------------------------------------------
# 构建镜像
docker build -t laoxian/tomcat:1.0 .
# 运行镜像
docker run \
--name mytomcat \
-p 8080:8080 \
-v /my/tomcat/webapps/spring-web.war:/usr/local/apache-tomcat-8.5.30/webapps/spring-web.war \
-d laoxian/tomcat:1.0
```

#### 八、多做些练习：

##### 1、 制作python镜像文件

```shell
# 这是用docker commit 建立的镜像，体验一下，创建后会生成一个巨大的镜像文件。然后用dockerfile的方式再创建一个，比较一下。
# 1、把基础镜像拉到本地
docker pull centos
docker run -it -d centos
docker exec -it 容器id /bin/bash    #进入容器
# 2、安装wget
apt-get install wget
# 3、安装编译器
yum -y install gcc automake autoconf libtool make
yum -y install gcc-c++
yum -y install zlib*
yum install libffi-devel -y  #python3.7需要的新的包
# 4、安装 python,大约10分钟
wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz
tar -xzvf Python-3.7.2.tgz
cd PyPython-3.7.2
# 添加配置,设置编译后安装到哪里
./configure --prefix=/usr/python
# 编译源码
make
# 执行安装
make install
# 退出镜像
exit

# 提交创建镜像
docker commit -m="增加vim编辑器" -a="laoxian" 容器id laoxian/python37:1.0
```

##### 2、用docker部署mysql

```shell
#1、拉取镜像
docker pull mysql:5.7
#2、运行容器
docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7
docker exec -it mysql /bin/bash
find / -name "*mysql*"
exit
#3、创建挂载目录
mkdir -p /my/mysql/conf  #配置目录
mkdir -p /my/mysql/data  #数据目录 
mkdir -p /my/mysql/logs  #日志目录
#4、拷贝配置文件并修改
docker cp mysql:/etc/mysql/mysql.conf.d/mysqld.cnf /my/mysql/conf/
vi /my/mysql/conf/mysqld.conf
character-set-server=utf8
#5、重新运行容器
docker rm -f mysql  #删除原来的容器
docker run \
 --name mysql \
 -p 3306:3306 \
 -v /my/mysql/conf:/etc/mysql/mysql.conf.d/ \
 -v /my/mysql/data:/var/lib/mysql \
 -v /my/mysql/logs:/logs \
 -e MYSQL_ROOT_PASSWORD=root \
 -d \
 mysql:5.7
#6、访问
#本地访问
docker exec -it mysql /bin/bash
mysql -u root -p
#远程访问
mysql -u root -p -h  <宿主机地址>
```

##### 3、用docker部署Redis

```shell
#1、拉取镜像
docker pull redis
#2、创建用于挂载的镜像
mkdir -p /my/redis/conf
mkdir -p /my/redis/data
#3、拷贝配置文件并修改
wget http://download.redis.io/releases/redis-4.0.10.tar.gz
tar zxf redis-4.0.10.tar.gz
cp redis.conf /my/redis/conf/
vi redis.conf
requirepass laoxian
appendonly yes
#4、运行容器
docker run \
--name myredis \
-p 6379:6379 \
-v /my/redis/conf/redis.conf:/usr/local/etc/redis/redis.conf \
-v /my/redis/data:/data \
-d redis redis-server /usr/local/etc/redis/redis.conf
#5、访问
#本地访问
docker exec -it myredis /bin/bash
redis-cli
#远程访问
ֵ#使用RedisDesktopManager工具访问

```

##### 4、用docker部署Nginx

```shell
# 1、拉取镜像
docker pull nginx
# 2、运行容器
docker run --name mynginx -p 80:80 -d nginx
# 3、创建用于挂载的目录
mkdir -p /my/nginx # 挂载nginx所有数据
mkdir -p /my/nginx/html # 挂载nginx虚拟主机
# 4、拷贝配置文件
docker cp mynginx:/etc/nginx/nginx.conf /my/nginx #拷贝主配置文件
docker cp mynginx:/etc/nginx/conf.d /my/nginx #拷贝虚拟主机配置文件
echo welcome to nginx > /my/nginx/html/index.html #自定义索引页
# 5、重启容器
docker rm -f mynginx
docker run \
 --name mynginx \
 -p 80:80 -p 443:443 \
 -v /my/nginx/nginx.conf:/etc/nginx/nginx.conf \
 -v /my/nginx/html:/usr/share/nginx/html:ro \
 -v /etc/nginx/conf.d:/usr/nginx/conf.d \
 -d nginx
# 6、测试
http://宿主机地址

```

##### 5、使用Supervisor来管理进程

容器启动时只能执行一个进程，我们可以将多个进程写到一个shell中，也可以用一些工具来管理这些进程，比如使用supervisor来管理，下面我们用supervisor管理ssh和apache服务的启动。

单独创建一个目录来制作镜像，目录内只存在和这个镜像相关的文件

```shell
# 同时使用ssh和apache服务
# 创建一个dockerfile
vi Dockerfile #下面是dockerfile文件内容
FROM ubuntu:13.04
MAINTAINER examples@docker.com
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y --force-yes perl-base=5.14.2-6ubuntu2
RUN apt-get install -y apache2.2-common
RUN apt-get install -y openssh-server apache2 supervisor
RUN mkdir -p /var/run/sshd
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
EXPOSE 22 80
CMD ["/usr/bin/supervisord"]
```

```shell
#supervisord.conf的内容
[supervisord]
nodaemon=true
[program:sshd]
command=/usr/sbin/sshd -D
[program:apache2]
command=/bin/bash -c "source /etc/apache2/envvars && exec /usr/sbin/apache2 -DFOREGROUND"
```

```shell
#创建supervisord镜像：
sudo docker build -t test/supervisord . #注意这个.，它指镜像文件相关文件，不是指的dockerfile的位置
```

```shell
#运行并检测：
sudo docker run -p 22 -p 80 -t -i test/supervisord
```

##### 6、建立一个网站的监控器：

* 本例是《docker实战》中的例子。

* 本例使用三个容器：第一个运行NGINX，第二个运行一个邮件程序，这两个容器以守护方式运行 `-d`。第三个以交互方式运行。

```shell
# 运行nginx,--detach 以守护方式运行。
docker run --detach  --name web nginx:latest
# 或者
docker run -d  --name web nginx:latest
# 以守护方式启动邮件服务器，dockerinaction/ch2_mailer这个镜像是《docker实战》作者提供的。
docker run -d --name mailer  dockerinaction/ch2_mailer
# 使用交互式容器,--link 链接web容器，冒号左面是要链接的容器，右边是别名
# BusyBox 是一个集成了三百多个最常用Linux命令和工具的软件镜像包。
docker run -it --name web_test --link web:web busybox:latest /bin/sh
# 在容器内执行命令，验证web容器是否运行正常，正常会返回一个页面
wget -O - http://web:80 /
# 启动监控器，镜像由作者提供.执行后会每秒输出"system up"字样，按 ctrl+p+q 会返回宿主机
docker run -it --name agent --link web:insideweb \
         --link mailer:insidemailer dockerinaction/ch2_agent
# 查看日志,logs 有一个参数 -f 查看全部日志并持续监控，要终止按ctrl+c
docker logs mail 
# 暂停web服务器，检查监控器日志是否提示
docker stop web
docker logs mailer
```



#### 九、容器的监控

##### 1、最简单的监控docker stats，后期用k8s ,jeekins

```bash
# 直接输入命令,docker stats 只显示时点信息，不动态变化
docker stats
```



#### 十、常见问答：

```shell
# docker的配置文件放在哪里？
不同的操作系统放置的位置不同，一般在：
/etc/default/docker   或者   /etc/systemd/system/docker.service.d/docker.conf 
# docker创建的容器中PID是否可以加入到宿主机的PID中
docker run --pid host busybox:latest ps   #会列出宿主机的所有进程
```

#### 十一、资源链接：

* Docker 官方主页: https://www.docker.com
  Docker 官方博客: https://blog.docker.com/
  Docker 官方文档: https://docs.docker.com/
  Docker Hub: https://hub.docker.com
  Docker 的源代码仓库: https://github.com/docker/docker
  Docker 发布版本历史： https://docs.docker.com/release-notes/
  Docker 常见问题： https://docs.docker.com/engine/faq/
  Docker 远端应用 API:https://docs.docker.com/reference/api/docker_remote_api/ 



​                                                                                                                                    编写者：laoxian 