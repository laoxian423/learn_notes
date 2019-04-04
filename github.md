### 一、简单体验

#### 1、我们用git的来做什么？

* 最初是用来管理代码的
* 现在啥人都来用：写小说、写日志、写日记、免费的存储空间、书籍翻译等等
* 大牛们云集的地方，与其仰望大牛，不如github

#### 2、github网站：

##### 2.1    浏览网站结构

* 找个大牛的网站，了解git的主要概念。仓库、提交、工作态度等，比如Linus，看看一个50岁的人是如何工作的。大牛之所以成为大牛是有原因的。
* git   Linux Kernel  perl  eclipse  gnome  kde  docker   react  ruby on rails  android  postgresql   debain 

##### 2.2、 创建自己的账户

##### 2.3、安装windows客户端gitbash

* 所有命令在linux下是一样的。

##### 2.4、一个简单的实验

* 构建仓库
* 本地下载仓库
* 编写点内容
* push，最大100M限制，可配置

#### 3、git、github、gitlab

* git：是一个开源的分布式版本控制系统，作者linus,bitkeeper,samba,two weeks。
* github：是一个网站，来管理git项目（仓库）,最著名的开源网站
* gitlab：是一个基于git的开源项目

### 二、git   bash的使用

#### 1、重要概念：

> ![](/pic/1554078515520.png)
>
> - Workspace：工作区，工作目录，我们在本地的仓库（项目）目录。我们修改、创建文件等操作都是先在工作区中操作。
> - Index / Stage：暂存区，工作区修改确认的文件添加到暂存区里，可以多次加入，分批或者一次提交到本地仓库，为了项目颗粒度的管理。
> - Repository：仓库区（或本地仓库），把暂存区或工作区提交状态保存起来。
>
> ![](/pic/1554078562914.png)
>
> * Remote：远程仓库，与本地仓库进行交换，分工协作的目的，分布式代码管理。

#### 2、创建仓库：

> * 创建仓库的命令：
>
>   ```shell
>   # 从本地创建
>   mkdir <Reposistory name>    # 创建一个仓库目录
>   git init   # 在创建好的目录中，初始化仓库
>   # 直接克隆远程仓库
>   git clone <url>
>   ```
>
> * 例子
>
>   ```shell
>   # 我们计划在 D 盘 （都是在Windows上实验，如果你是linux，请忽略某某盘的语句），创建一个myRepository 的目录，作为后面所有实验用的总目录，以后所有的仓库都放在这个目录里。
>   $ mkdir /d/myRepository
>   # 创建第一个式样仓库，testgit
>   $ mkdir /d/myRepository/testgit
>   # 初始化这个仓库
>   $ cd /d/myRepository/testgit
>   $ git init
>   # 查看testgit的目录结构，观察里面多了些什么
>   $ ls -l -a
>   # 看看目录中.git子目录中的文件,.git目录实际就是本地仓库
>   $ ls -l -a ./.git
>   ```
>
>   





#### 2、命令示例：

```shell
# git 安装，直接去官网，有详细步骤。 
https://git-scm.com/

git config --list
git config --global user.name "laoxian423"
git config --global user.email "362293069@qq.com"
git version
```

```shell
# 在当前目录新建一个Git代码库
git init
# 下载一个项目和他的整个代码历史
git clone [url]

#添加文件到暂存区
git add [file1] [file2]
# 删除工作区文件，并且将这次删除放入暂存区
git rm [file1] [file2]
# 改名文件，并且将这个改名放入暂存区
git mv [file-origin] [file-renamed]

#提交暂存区到仓库
git commit -m [message]
#直接从工作区提交到仓库（前提该文件已经有仓库中的历史版本）
git commit -a -m [message]
#现实变更信息
git status
# 显示当前分支的历史版本
git log
git log --oneline

# 查看是否和远程仓库建立了链接
git remote -v
# 增加远程仓库并命名
git remote add [shortname] [url]
# 将本地的提交推送到远程仓库
git push [remote] [branch]
# 将远程仓库的提交拉下到本地
git pull [remote] [branch]

# 闯关游戏
1 https://try.github.io/
2 安装nodeJS,npm install git-it-g 

```

#### 三、git  简介

* 发明人  linux  Trovalds 
* ![](/pic/1554080537699.png)
* git   Linux Kernel  perl  eclipse  gnome  kde  docker   react  ruby on rails  android  postgresql   debain 
* 三个区域四个状态

#### 4、git 图形界面工具

* git gui
* SourceTree  https://www.sourcetreeapp.com/        https://bitbucket.org/
* EGIT
* git log --oneline

#### 5、git  配置

* .gitignore    每一行代表一个或一类要忽略的文件，支持通配符
* git  check-ignore  -v .project
* git commit -am  "this is test"
* warning: ..LF  ..  CRLF   （windows  换行问题）
* Linux  :换行\n    windows  换行\r\n   MAC  :  换行  \r
* git config --global core.autocrlf true    默认设置，提交时LF ,检出时CRLF
* git config --global core.safecrlf  false    允许提交混合换行符的文件。
* 别名
* git log --pretty=format:'%h %ad | %s%d [%an]'  --graph --date=short
* git config --global alias.ci commit 
* cd ~
* vim .gitconfig
* 存储凭证
* git  config  --global  credential.helper  wincred

#### 6、git 协议

* 本地：  git  clone  /c/wd/test.git

* git协议： git clone git://server_ip/test.git    没有权限管理，访问速度最快

* http协议：git clone https://github.com/zhangsan/test.git

* ssh协议：

  ```shell
  git clone ssh://git@github.com/laoxian/test.git
  git clone git@github.com:laoxian/test.git
  git remote add origin git@github.com:laoxian/test.git
  
  # 生成RSA密钥对
  ssh-Keygen -t rsa -C "your email"
  # 把生成的公钥配置到github网站上:cat ~/.ssh/id_rsa.pub
  "SSH and GPG keys"
  "new"
  git clone git@github.com:laoxian/test.git   
  ```

#### 7、几个git命令

```shell
# 查看所有子命令
git help -a
# 逐行查看文件历史
git blame  <filename>
git blame -L 5,10 <filename>  # 从第5行开始查看到第10行
# 清除修改
git clean -n    # 列出未add的文件
git clean -f    # 清除掉
git clean -x  -f  # 连.gitignore中的文件也清除掉
# 输出信息简短提示
git status -sb  

# 删除,红色是工作去，绿色是缓冲区
git rm  <filename>
git commit - m "delete"
git log -5

rm a
git add .
git commit -m "delete a"

# git add 可以提交的状态，git 可跟踪的,add 是把文件放到暂存区中，只有放到暂存区中，git 才能跟踪。
添加新文件
删除文件
编辑文件（增加能容，删除内容，修改内容）
文件改名
文件移动
文件夹的操作（添加、删除、改名、移动）

# 改名和移动
git mv a b

# 一个文件多个提交，一个文件中的不同修改做不同提交
git diff # 查看变更  ，git diff --cached  查看暂存区变更。
git add -p a  # 多次提交 ，
git show HEAD # 显示最后一次提交

# ------------------  git commit -------------------------------------------
#  提交的一些注意事项（经验）：1、以一个小功能、小改进或一个bug fix为单位  2、对应的unit test 程序在同一个commit   3、无相关的修改不在同一个提交   4、语法错误的半成品程序不能 commit
# message 书写规范（安哥拉）：
<type>(<scope>):<subject>
//空一行
<body>
//空一行
<footer>
feat: 新功能
fix： 修补bug
docs：文档
style：格式（不影响代码运行的变动）
refactor:重构（既不是新增功能，也不是修改bug的代码变动）
test:增加测试
chore:构建过程或辅助工具的变动

# 关闭BUG,在message中：
close #6

```

```shell
# 信息查看
git status -sb
# 查看某个提交信息
git show 8938a3d   
git show HEAD    # 第一个
git show HEAD^   # 前一个
git show HEAD^^  # 前2个
git show HEAD~5  # 从HEAD数到第5个
# 查看提交历史
git log <filename>
git log --grep <msg>
git log -n  # n 是个数字
```

* git  diff  的使用

  ![](/pic/1554181539995.png)

```shell
# 按照上图，制作一个测试环境
echo 1111 >> a
git commit -am '1'
echo 2222 >> a
git commit -am '2'
echo 3333 >> a
git commit -am '3'
echo 4444 >> a
git commit -am '4'
echo 5555 >> a
git commit -am '5'
echo 6666 >> a    # 放在暂存区中
git add .
echo 7777 >> a    # 放在工作区中

git  diff --cached  # 比较暂存区和master
git diff HEAD  # 比较工作去和master
git diff    # 比较工作区和暂存区
git diff da988  cd112  # 比较这两个版本
```

* 回撤操作

* ![](pic/1554257471341.png)



```shell
# 回撤暂存区内容到工作区
git reset HEAD

# 回撤提交到暂存区
git reset HEAD --soft

# 回撤提交，放弃变更,HEAD可以是任意一个提交
git reset HEAD  --hard

# 回撤远程操作，团队协作时不能这样做
git push -f

# 回撤上一次提交
git add .
git commit --amend -m "messages"

# 变基操作，改写历史提交
git rebase -i HEAD~3
```

####  8、标签操作

```shell
# 大版本，里程碑，重大变动上
# 在当前提交上，打标签,在HEAD上
git tag foo
git show foo

# 在当前提交上，打标签，并给message信息注释
git tag foo -m "message"

# 在当前提交之前的第4个版本上，打标签
git tag foo HEAD~4

# 列出所有标签
git tag

# 删除标签
git tag -d foo

# 把标签推送到remote
git push origin --tags  # 推送多个标签
git push origin v0.1   # 推送1个标签

# 删除远程仓库标签
git push origin :refs/tags/v0.0

```

#### 9、分支操作

![](pic\1554269674384.png)

![](pic\1554270320533.png)

```shell
# 为解决并行开发
(master) git branch iss53
(master) git branch hotfix
(master) git merge hotfix
# 切换分支
(master) git checkout iss53
# 显示所有分支
git branch
git branch -v  # 显示分支并显示每个分支的当前提交
# 合并操作，注意：要把 A 合并 到 B 上，必须在B上操作，比如把hotfix合并到master，必须到master上操作
git checkout master
git merge hotfix
# 删除分支
git branch -d hotfix

# 解决冲突
# 模拟在两个分支中编辑同一个文件的同一个地方
```

```shell
# 常用分支命令
# 创建分支foo
git branch foo
# 切换到分支
git checkout foo
# 创建分支并同时切换到foo
git checkout -b foo
# 修改分支名字
git branch -m old_name new_name
git branch -M old_name new_name  # 强制执行
# 删除分支
git branch -d foo  # 未合并不允许删除
git branch -D foo  # 强制删除
# 列出远程分支
git branch -r
git branch -v # 本地带分支版本
# 查看已经合并的分支
git branch --merged
git branch --no-merged
# 列出远程合并的分支
git branch -r --merged
# 取出远程foo 分支
git checkout -t origin/foo
# 删除远程分支
git push origin <space>:<remote branch>  # 
git fetch -p
# 合并分支
git merge <branch name>
# 合并分支，拒绝fast forward ,产生合并commit
git merge --no-ff
# 推送到远程,分支要一个个推，在分支内
(master) git push
(iss53) git push -u origin iss53
```

```shell
# git stash
# 在分支中的工作去中有未提交暂存区或暂存区未提交时，切换不到别的分支。
# 保存进度
git stash
# 弹出进度
git stash pop
# 查看stash列表
git stash lish
# 删除stash列表
git stash clear
```



