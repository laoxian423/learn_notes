#### 一、Docker的底层实现：

> Docker底层的核心技术包括Linux的命名空间（Namespaces）、控制组（Control groups）、Union文件系统（Union file systems）和容器格式（Container format）
>
> Namespaces 、cgroups早在2007年就是Linux的一部分。docker使用了这些技术，让容器更容易使用。

#####  1、基本结构

> Docker采用C/S架构，包括客户端和服务端（daemon)，可以本地，也可以通过scoket 或者RESTful来通信。

##### 2、命名空间：

> ​        什么是命名空间呢？举个例子，当你在命令行执行命令时，实际上是在被成为用户空间的内存中运行，理想情况下，用户空间运行的程序不能修改内核空间的内存。
>
> Linux内核一个强大特性。每个容器都有自己单独的命名空间，保证彼此不受影响。
>
> * pid 命名空间：进程标识符和能力,为每个容器创建一个PID命名空间是Dcoker的关键特征。
> * net命名空间：网络隔离是通过net命名空间实现的，docker默认采用veth的方式，将容器中的虚拟网卡同host上的一个dcoker网桥docker0链接在一起
> * ipc命名空间：进程间交互，通过共享内存的进程间通信
> * mnt命名空间：文件系统访问和结构
> * uts命名空间：允许容器拥有独立的hostname和domain name。
> * usr命名空间：用户名和标识
> * chroot():控制文件系统根目录的位置
> * cgroups：资源保护

##### 3、控制组：

> Linux内核的一个特性，主要来对共享资源进行隔离、限制、审计等。

##### 4、联合文件系统：

> 是一种分层、轻量级并且高性能的文件系统，支持对文件系统一层层的叠加，同时可以将不同目录挂载到同一个虚拟文件系统下。
>
> docker目前支持：AUFS，btrfs，vfs和DeviceMapper

##### 5、容器格式：

> 采用了LXC容器格式，从1.20开始支持libcontainer并默认。

##### 6、Docker网络实现：

> Docker的网络实现其实就是利用了Linux上的网络命名空间和虚拟网络设备（特别是veth pair)。
>
> **docker创建一个容器的时候，执行如下操作**：
>
> * 创建一对虚拟接口，分别放到本地主机和新容器中。
> * 本地主机一端桥接到默认的docker0或指定网桥上，并具有一个唯一的名字，如veth65f9
> * 容器一端放到虚拟容器中，并修改名字作为eth0,这个接口只在容器的命名空间可见。
> * 从网桥可用地址段中获取一个空闲地址分配给容器的eth0,并配置默认路由到桥接网卡veth65f9
>
> **使用docker run 的时候通过--net 指定容器的网络配置，有4个可选项**：
>
> * --net=bridge 默认值，连脚到默认的网桥
> * --net=host 不要容器化容器内的网络。使用本地主机的网络，拥有完全的本地主机接口访问权限。如果进一步使用--privileged=true ，容器会被允许直接配置主机的网络堆栈。
> * `--net=noe`让docker将新容器放到隔离的网络栈中，不进行网络配置，之后，可以自行配置。
> * `--net=container:NAME_or_ID`让docker将新容器的进程放到一个已存在的网络栈中，新容器进程有自己的文件系统、进程列表和资源限制，但会和已存在的容器共享IP地址和端口等网络资源，两者进程可以直接通过lo环回接口通信。
>
> **网络配置细节**：
>
> 使用`--net=none` 后，自行配置网络，通过这个过程，了解docker配置网络的细节：
>
> `sudo docker run -it --rm --net=none base /bin/bash`
>
> 在本地查找容器的进程ID，并为它创建网络命名空间
>
> ```shell
> sudo docker inspect -f '{{.State.Pid}}' 63f36fc01b5f
> pid=2778
> sudo mkdir -p /var/run/netns
> sudo ln -s /proc/$pid/ns/net /var/run/netns/$pid
> ```

> 检查桥接网卡的IP 和子网掩码信息
>
> ```shell
> ip addr show docker0
> # inet 172.17.42.1/16 scope global docker0
> ```
>
> 创建一对veth pair接口 A 和 B，绑定A 到网桥docker0，并启用它
>
> ```shell
> sudo ip link add A type veth peer name B
> sudo brctl addif docker0 A
> sudo ip link set A up
> ```
>
> 将B 放到容器的网络命名空间，命名为eth0,启动它并配置一个可用IP（桥接网段）和默认网关
>
> ```shell
> sudo ip link set B netns $pid
> sudo ip netns exec $pid ip link set dev B name eth0
> sudo ip netns exec $pid ip link set eth0 up 
> sudo ip netns exec $pid ip addr add 172.17.42.99/16 dev eth0
> sudo ip netns exec $pid ip route add default via 172.17.42.1
> ```
>

#### 二、Dcoker Compose项目：

> ​	官方编排（Orchestration）项目之一，负责快速在集群中部署分布式应用，负责实现对Docker容器集群的快速编排，从功能上看，跟OpenStack中的Heat十分相似。
>
> 其代码在https://github.com/docker/compose上开源。
>
> Compose允许用户通过一个单独的docker-compose.yml模板文件（YAML格式）来定义一组相关联的应用容器为一个项目（project）
>
> Compose中的两个重要概念：
>
> * 服务（Service）：一个应用的容器，实际上可以包括若干运行相同镜像的容器实例。
> * 项目（Project）：由一组关联的应用容器组成的一个完整业务单元，在docker-compose.yml文件中定义。
>
> Compose的默认管理对象是项目，Compose项目由python编写，调用了docker提供的API来对容器进行管理。

##### 1、安装与卸载：

* 需要docker Engine 1.7.1 +
* 可以通过python的pip安装，可以直接下载编译好的二进制文件，可以直接运行在容器中。

```shell
# 通过PIP安装
sudo pip install -U docker-compose
# centos 如果没有安装pip，按下列步骤安装pip：
yum -y install epel-release    #是由 Fedora 社区打造，为 RHEL 及衍生发行版如 CentOS、Scientific Linux 等提供高质量软件包的项目。
yum -y install python-pip
#卸载
pip uninstall docker-compose

#通过二进制文件下载：
https://github.com/docker/compose/releases
chomd a+x /usr/local/bin/docker-compose

#通过容器执行：
dcoker/compose
```

##### 2、创建一个经典的Web项目：

* 一个Haproxy ，挂载三个Web容器。

```shell
#创建一个compose-haproxy-web目录，作为项目目录
mkdir compose-haproxy-web
#创建两个子目录：
mkdir haproxy web
```

```python
#在WEB目录里创建一个python简单的HTTP服务，打印出访问者的IP和实际本地IP
#index.py

#!/usr/bin/python
#authors: yeasy.github.com
#date: 2013-07-05
import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import socket
import fcntl
import struct
import pickle
from datetime import datetime
from collections import OrderedDict

class HandlerClass(SimpleHTTPRequestHandler):
	def get_ip_address(self,ifname):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		return socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915, \
                                            struct.pack('256s', ifname[:15]))[20:24])

	def log_message(self, format, *args):
		if len(args) < 3 or "200" not in args[1]:
			return
		try:
			request = pickle.load(open("pickle_data.txt","r"))
		except:
			request=OrderedDict()
		time_now = datetime.now()
		ts = time_now.strftime('%Y-%m-%d %H:%M:%S')
		server = self.get_ip_address('eth0')
		host=self.address_string()
		addr_pair = (host,server)
		if addr_pair not in request:
			request[addr_pair]=[1,ts]
		else:
			num = request[addr_pair][0]+1
			del request[addr_pair]
			request[addr_pair]=[num,ts]
		file=open("index.html", "w")
		file.write("<!DOCTYPE html> <html> <body><center><h1><font color=\"blue\" face=\"Georgia, Arial\" size=8><em>HA</em></font> Webpage Visit Results</h1></center>")
		for pair in request:
			if pair[0] == host:
				guest = "LOCAL: "+pair[0]
			else:
				guest = pair[0]
			if (time_now-datetime.strptime(request[pair][1],'%Y-%m-%d %H:%M:%S')).seconds < 3:
				file.write("<p style=\"font-size:150%\" >#"+ str(request[pair][1]) +": <font color=\"red\">"+str(request[pair][0])+ "</font> requests " + "from &lt<font color=\"blue\">"+guest+"</font>&gt to WebServer &lt<font color=\"blue\">"+pair[1]+"</font>&gt</p>")
			else:
				file.write("<p style=\"font-size:150%\" >#"+ str(request[pair][1]) +": <font color=\"maroon\">"+str(request[pair][0])+ "</font> requests " + "from &lt<font color=\"navy\">"+guest+"</font>&gt to WebServer &lt<font color=\"navy\">"+pair[1]+"</font>&gt</p>")
		file.write("</body> </html>");
		file.close()
		pickle.dump(request,open("pickle_data.txt","w"))


if __name__ == '__main__':
	try:
		ServerClass = BaseHTTPServer.HTTPServer
		Protocol = "HTTP/1.0"
		addr = len(sys.argv) < 2 and "0.0.0.0" or sys.argv[1]
		port = len(sys.argv) < 3 and 80 or int(sys.argv[2])
		HandlerClass.protocol_version = Protocol
		httpd = ServerClass((addr, port), HandlerClass)
		sa = httpd.socket.getsockname()
		print "Serving HTTP on", sa[0], "port", sa[1], "..."
		httpd.serve_forever()
	except:
		exit()
```

```shell
# 在web目录下生成一个临时的index.html文件，用于被index.py 更新
touch index.html
```

```shell
# 在web目录下生产一个dockerfile文件
FROM python:2.7
WORKDIR /code
ADD . /code
EXPOSE 80
CMD python index.py
```

```shell
# 在haproxy目录下创建一个haproxy.cfg文件：
global
	log 127.0.0.1 local0
	log 127.0.0.1 local1 notice
defaults
	log global
	mode http
	option httplog
	option dontlognull
	timeout connect 5000ms
	timeout client 50000ms
	timeout server 50000ms
listen stats
	bind 0.0.0.0:70
	stats enable
	stats uri /
frontend balancer
	bind 0.0.0.0:80
	mode http
	default_backend web_backends
backend web_backends
	mode http
	option forwardfor
	balance roundrobin
	server weba weba:80 check
	server webb webb:80 check
	server webc webc:80 check
	option httpchk GET /
	http-check expect status 200
```

```shell
# 在compose-haproxy-web目录下创建docker-compose.yml文件：
weba:
   build: ./web
   expose:
        - 80
webb:
   build: ./web
   expose:
        - 80
webc:
   build: ./web
   expose:
        - 80
haproxy:
   image: haproxy:latest
   volumes:
        - ./haproxy:/haproxy-override
        - ./haproxy/haproxy.cfg:/usr/local/etc/haproxy/haproxy.cfg:ro
   links:
        - weba
        - webb
        - webc
   ports:
        - "80:80"
        - "70:70"
   expose:
        - "80"
        - "70"
```

```shell
#在compose-haproxy-web目录下，运行compose项目,目录结构如下：
└── compose-haproxy-web
    ├── docker-compose.yml
    ├── haproxy
    │   └── haproxy.cfg
    └── web
        ├── dockerfile
        ├── index.html
        └── index.py
docker-compose up
```



##### 3、compose模板文件：

* 默认的模板文件名称为docker-compose.yml，格式为YAML。

```shell
version: "2"
services:
  webapp:
    image:examples/web
    ports:
      - "80:80"
    volumes:
      - "/data"   
```

> 注意每个服务都必须通过image指定镜像或build指令（需要dockerfile）生成镜像。dockerfile中的设置的选项如CMD、EXPOSE等会自动被获取，无需在dcoker-compose.yml中再次设定。
>
> 

| 指令             | 说明                                                         |
| ---------------- | ------------------------------------------------------------ |
| build            | 指定dcokerfile所在文件夹路径（可绝对路径，或相对dcoker-compose.yml路径)。 |
| cap_add,cap_drop | 指定容器的内核能力分配。如cap_add:  - ALL   容器拥有所有能力。cap_drop : - NET_ADMIN  去掉net_admin能力。 |
| command          | 覆盖容器启动后默认执行的命令。                               |
| cgroup_parent    | 指定父cgroup组，将继承该组的资源限制。                       |
| container_name   | 指定容器名称，默认会使用`项目名词_服务名称_序号`这样的格式。<br> container_name: dcoker-web-container |
| devices          | 指定设备映射关系<br> devices: <br>      - "/dev/ttyUSB1:/dev/ttyUSB0" |
| dns              | 自定义DNS服务器。可以是一个值，也可以是一个列表：<br> dns:8.8.8.8<br> dns:<br>   - 8.8.8.8 <br>   - 9.9.9.9 |
| dns_search       | 配置dns搜索域：dns_search: example.com <br> dns_search:<br>    - domain1.example.com<br>    - domain2.example.com |
| dockerfile       | 该指令不能和image同时使用                                    |
| env_file         | 从文件中获取环境变量：env_file: .env  <br> PROG_ENV=development |
| enviroment       | 设置环境变量，只给定名称的变量会自动获取运行Compose主机上的对应的值。<br> environment:<br>     RACK_ENV:development <br>     SESSION_SECRET |
| expose           | 暴露的端口。expose:  -  "3000"                               |
| extends          | 基于其他模板文件进行扩展                                     |
| image            | 指定镜像名称，如果本地不在，compose会去拉                    |
| links            | 链接到其他服务中的容器                                       |
| ports            | 暴露端口信息。(宿主机：容器) <br> ports:<br>     - "3000"    #宿主机端口随机选择<br>    -  "8000:8000"<br>    -  "127.0.0.1:8001:8001" #指定网卡 |
| volumes          | 挂载数据卷。<br> volumes:<br>     -   /var/lib/mysql         |
#### 三、Docker Machine项目：

* 官方编排项目之一，负责在多种平台上快速安装Docker环境。
* 可在多平台安装，Linux、Mac OS、windows

```shell
#安装，直接下载，修改属性为执行（百度到网站上有详细说明和指令）
base=https://github.com/docker/machine/releases/download/v0.16.0 &&
  curl -L $base/docker-machine-$(uname -s)-$(uname -m) >/tmp/docker-machine &&
   install /tmp/docker-machine /usr/local/bin/docker-machine
```



#### 四、Docker Swarm 项目：

* 官方编排项目之一，负责对Docker集群进行管理。
* 它将一群Docker宿主机变成一个单一的虚拟的主机。
* swarm调度策略：spread,binpack,random,可通过--strategy参数来指定，默认是spread。spread下swarm会选择一个正在运行的容器数量最小的那个节点来运行容器，考虑CPU内存。binpack相反，它会经可能的放到一台机器上。

![1553572296865](F:\myRepositraies\dockerTrain\pic\1553572296865.png)

>* swarm 本身不运行容器，所以即使它挂掉了也不影响已经运行的容器。
>* 集群中的每台节点上面的Docker版本不能低于1.4
>* 为了让swarm manager能够与每台swarm node进行通信，集群中的每台节点的Dcoker daemon都必须监听同一个网络接口。

* 安装的最简单方式是使用swarm镜像：`sudo docker pull swarm`

  检查是否安装成功：`sudo docker run --rm swarm -v`

* 修改docker配置文件，将docker监听方式改为一致：

  ```shell
  # 修改docker配置文件，各个Linux版本位置不同，在文件末尾添加：
  DOCKER_OPTS="-H 0.0.0.0:2375 -H unix:///var/run/docker.sock"
  # 修改之后重启docker
  systemctl restart docker   # centos
  service docker restart   # ubuntu
  
  ```

* Docker 集群管理需要使用服务发现功能(Discovery service bachend)，swarm支持多种方式：

  DockerHub 提供的服务发现功能，本地的文件，etcd,consul,zookeeper和IP列表

##### 4.1   使用DockerHub提供的服务发现功能：

* 实验环境：

  包括三台机器，IP分别为192.168.1.84    192.168.1.83    192.168.1.124  。83同时充当swarm manager节点。

* 创建集群token

  在任意一台机器上执行`docker run --rm swarm create`,会获取到一个全球唯一的token,如：

  ![1553573938727](F:\myRepositraies\dockerTrain\pic\1553573938727.png)

  **看下面提示的意思，这个功能好像在未来会被抛弃**

* 加入集群：

  在所有要加入集群的节点上面执行 swarm join 命令。

  `docker run -d swarm join --addr=ip_address:2345 token://token_id`

  ip_address 是当前执行命令的机器IP     token_id  是上一行的那个token

  **这个容器如果停止或删除，改节点会从集群中消失**

* 启动swarm manager:

  在83上执行：

  `docker run -d -p 2376:2375 swarm manage token://08ae3b9dfc695c6ec132ccc1b5224831`

  此时集群整个已经启动起来了。

* 查看：

  ```shell
  # 列出集群节点,可在任意节点执行：
  docker run --rm swarm list token://08ae3b9dfc695c6ec132ccc1b5224831
  # 查看节点信息，要指明manager节点地址
  docker -H 192.168.1.83:2376 info
  ```

#### 4.2 使用文件方式创建集群：

* 第一步 在管理节点上新建一个文件，比如在83上：

  ```shell
  echo 192.168.1.83:2375 >> cluster
  echo 192.168.1.84:2375 >> cluster
  echo 192.168.1.124:2375 >> cluster
  ```

* 第二步 在83上执行swarm manage

  ```shell
  docker run -d -p 2376:2375 -v $(pwd)/cluster:/tmp/cluster swarm manage file:///tmp/cluster
  ```

#### 五、etcd

> CoreOS团队发起的一个管理配置信息和服务发现的项目。它的目标是构建一个高可用的分布式键值数据库，基于go语言实现。
>
> 可以使用制作好的Docker镜像文件来体验。

#### 六、CoreOS

> CoreOS的设计是为你提供能够像谷歌一样的大型互联网公司一样的基础设施管理能力来动态扩展和管理的计算能力。
>
> CoreOS的安装文件和运行依赖非常小,它提供了精简的Linux系统。 它使用Linux容器在更高的抽象层来管理你的服务， 而不是通过常规的YUM和APT来安装包。
>
> 同时， CoreOS几乎可以运行在任何平台： Vagrant, Amazon EC2, QEMU/KVM,VMware 和 OpenStack 等等， 甚至你所使用的硬件环境。 
>
> CoreOS是一种支持大规模服务部署的Linux系统 
>
> CoreOS使得在基于最小化的现代操作系统上构建规模化的计算仓库成为了可能。 
>
> CoreOS被设计成一个来构建你平台的最小化的现代操作系统。
> 它比现有的Linux安装平均节省40%的RAM（ 大约114M） 并允许从 PXE/iPXE 非常快速的启动 。
>
> CoreOS提供了三大工具， 它们分别是： 服务发现， 容器管理和进程管理。 
>
> CoreOS的第一个重要组件就是使用etcd来实现的服务发现。 
>
> 第二个组件就是docker， 它用来运行你的代码和应用。 
>
> 第三个CoreOS组件是fleet。fleet管理docker容器的生命周期。  

#### 七、Kubernetes

>Kubernetes 是 Google 团队发起并维护的基于Docker的开源容器集群管理系统， 它不仅支持常见的云平台， 而且支持内部数据中心。它的目标是管理跨多个主机的容器，提供基本的部署， 维护以及运用伸缩， 主要实现语言为Go语言。  
>
>建于 Docker 之上的 Kubernetes 可以构建一个容器的调度服务， 其目的是让用户透过Kubernetes集群来进行云端容器集群的管理， 而无需用户进行复杂的设置工作。 
>
>其核心概念是Container Pod（ 容器仓） 。 

