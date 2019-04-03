第二章：

* 获得完整的容器ID，`-- no-trunc`

* docker有三个特定的功能，帮助建立与环境无关的系统：

  * 只读文件系统
  * 环境变量注入
  * 存储卷

* 只读文件系统

  ```shell
  # 使用--read-only 标志
  docker run -d --name wp --read-only wordpress:4
  ```

* 环境变量的注入

  ```shell
  # 给容器注入环境变量，--env 缩写是 -e
  docer run --env MY_ENVIRONMENT_VAR="this is a test" busybox:latest env
  ```

* 当容器中的所有进程都退出后，该容器将进入退出状态。

* --restart，docker基于重新启动策略提供的功能

  * 从不重新启动（默认）
  * 检测到故障时尝试重新启动
  * 当检测到故障时，在一段预定的时间后重新开始尝试重启
  * 不管任何条件，始终重新启动容器

  ```shell
  # 测试--restart 参数
  docker run -d --name backoff-detector --restart always busybox date
  # 几秒钟后：
  docker logs -f backoff-detector
  ```

  

