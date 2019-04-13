### 一、常用操作

#### 1.1 常用操作

```shell
:vimtutor   # 官方新手教程
ctrl + g   # 显示当前行以及文件信息
:!shell    # 执行外部命令
:r /etc/fstab  # 把fstab文件内容读到当前位置
:r! df -Th  # 把df -Th的命令结果插入到当前位置
# ctrl + z  可以暂时回到shell，fg 返回，jobs 查看有几个任务
```


#### 1.2 光标的移动

```shell
上: k   下: j   左：h   右:l
2w  # 向前移动两个单词
0   # 移动到行首
$   # 移动到行尾
gg  # 文件第一行
G   # 文件最后一行
行号+G # 指定行
<ctrl>+o # 跳转回之前的位置 
<ctrl>+i # 返回跳转之前的位置
```

#### 1.3 删除操作

```shell
x    # 删除当前字符
dw   # 删除至当前单词末尾
de   # 删除当前单词
d$   # 删除至当前行尾
dd   # 删除整行,其实这个操作是剪切
2dd  # 删除两行，其实这个操作是剪切
```

#### 1.4 修改操作

```shell
i   # 插入文本
A   # 当前行末尾添加
o   # 打开新的一行并进入插入模式
u   # 撤销操作
```

#### 1.5 复制粘贴

```shell
v # 进入可视模式
y # 复制
p # 粘贴
yy # 复制当前行
dd # 剪切当前行
```

#### 1.6  查找

```shell
/   # 正向查找（n：继续查找，N：相反方向继续查找）
？  # 逆向查找
%   # 查找配对的 {，[，(
:set ic  # 忽略大小写
:set noic # 取消忽略大小写
:set hls # 匹配项高亮显示
:set is # 显示部分匹配
```

#### 1.7 替换

```shell
:s/old/new  # 替换该行第一个匹配串
:s/old/new/g # 替换全行的匹配串
:%s/old/new/g #替换整个文件的匹配串
```

#### 1.8 折叠

```shell
# 相应配置
set foldmethod=indent
set foldlevel=99

zc  # 折叠
zC  # 折叠所有嵌套
zo  # 展开折叠
zO  # 展开所有折叠嵌套
nnoremap <space> za  # 用空格键代替za
```

#### 1.9 窗口管理

```shell
:vs  或者 :vsplit  将当前窗口竖直分割，并在上面新窗口中显示当前文件
:vs filename 将当前窗口竖直分割，新文件在新窗口中显示
:sp 或者:sv或者:split  将当前窗口水平分割，并在左边新窗口中显示当前文件
:sp filename 将当前窗口竖直分割，新文件在左边新窗口中显示
:new 新建文件并竖直分割
:vnew 新建文件并水平分割
如果想让新窗口在右边或者下方打开，添加配置：
set splitbelow
set splitright
在窗口之间切换可以用鼠标，如果不想用鼠标，切换按键如下：
Ctrl-w-j 切换到下方的分割窗口
Ctrl-w-k 切换到上方的分割窗口
Ctrl-w-l 切换到右侧的分割窗口
Ctrl-w-h 切换到左侧的分割窗口
觉得三个按键多的话可以设置快捷键：
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>
这样就不用按w键了。
```

#### 1.10 自定义快捷键

* 一键F5执行python

```shell
# 在配置文件中：
map <F5> :call RunPython()<CR>
func! RunPython()
    exec "W"
    if &filetype == 'python'
        exec "!time python3 %"
    endif
endfunc
```


### 二、 插件的安装和管理

#### 2.1  手动安装插件

* 插件网站：http://vimawesome.com/ , http://www.vim.org
* 如果下载不了，去github官网手动安装

```shell
# 以安装solarized背景插件为例
git clone git://github.com/altercation/vim-colors-solarized.git 
cd vim-colors-solarized/colors 
mv solarized.vim ~/.vim/colors/ 
#  modify .vimrc 
syntax enable 
set background=dark    # set background=light 选择浅色模式 
colorscheme solarized 
```



#### 2.2 自动插件管理

* Vundle 插件管理

```shell
# 下载vundle
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
#如果不存在~/.vim/bundle目录，则：
cd ~
mkdir .vim
cd .vim
mkdir bundle
# 将下列配置放在.vimrc的开头-----------------------------------------
set nocompatible              " be iMproved, required
filetype off                  " required
 
" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
 
" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
 
" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
# ------------------------------------------------------------------

# 如果想下载某个插件，比如自动缩进indentpython.vim插件，需要将
Plugin 'vim-scripts/indentpython.vim'
# 置于call vundle#begin()和call vundle#end()之间，保存配置后在vim中执行
:PluginInstall
# 即可以自动下载indentpython.vim插件了。

# bundle可以管理下载几种不同的插件,方式如下：
github上的插件
Plugin 'tpope/vim-fugitive'
来自于http://vim-scripts.org/vim/scripts.html的插件
Plugin 'L9'
非github上的git插件
Plugin 'git://git.wincent.com/command-t.git'
本地插件
Plugin 'file:///home/gmarik/path/to/plugin'
" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
" Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
有旧插件的情况下，下载新的插件并重命名以避免冲突
Plugin 'ascenator/L9', {'name': 'newL9'}

# 下载方式除了在vim中运行:PluginInstall外，还可以在命令行中运行：
vim +PluginInstall +qall
```

#### 2.3 常用插件

* YouCompleteMe  自动补全，替代产品（jedi-vim)

```shell
# 非常好用的自动补全插件，就是比较重。
# 官网地址：http://valloric.github.io/YouCompleteMe/
# github地址：https://github.com/Valloric/YouCompleteMe
# YouCompleteMe安装后还需要手动编译，然后再在.vimrc中配置。
# 在ubuntu中使用，首先准备一些工具：
sudo apt-get install build-essential cmake
sudo apt-get install python-dev python3-dev
# 使用vundle安装：
Plugin 'Valloric/YouCompleteMe'
# 编译：
cd ~/.vim/bundle/YouCompleteMe
./install.py --clang-completer
# 参数 --clang-completer是为了加上C系列语言的自动补全，也可以不加：
cd ~/.vim/bundle/YouCompleteMe
./install.py
# 耐心等待吧，要花很长时间...
# 复制一下默认配置文件到用户主目录：
cp third_party/ycmd/examples/.ycm_extra_conf.py ~/
# YCM常用的一些选项，可根据个人喜好调整：
let g:ycm_min_num_of_chars_for_completion = 2  "开始补全的字符数"
let g:ycm_python_binary_path = 'python'  "jedi模块所在python解释器路径"
let g:ycm_seed_identifiers_with_syntax = 1  "开启使用语言的一些关键字查询"
let g:ycm_autoclose_preview_window_after_completion=1 "补全后自动关闭预览窗口"
# 代码跳转：
nnoremap <leader>jd :YcmCompleter GoToDefinitionElseDeclaration<CR>
# 开关YCM：
let g:ycm_auto_trigger = 0   "turn off
let g:ycm_auto_trigger = 1   "turn on
# 支持vim8的补全插件
YouCompleteMe实际上是使用jedi-vim来补全python代码的，如果觉得YCM实在太重，可以使用支持vim8的maralla/completor.vim来补全代码：
下载：
Plugin 'maralla/completor.vim'
下载jedi：
pip install jedi
配置：
let g:completor_python_binary = '/path/to/python/with/jedi/installed'
设置起来比YCM简单很多了。
```

* 自动缩进插件

```shell
# 写python代码，自动缩进是必须的，可以使用indentpython.vim插件：
Plugin 'vim-scripts/indentpython.vim'
```

* 美化状态栏插件

```shell
# vim-powerline
# 美化状态栏，可以显示当前的虚拟环境、Git分支、正在编辑的文件等信息。
Plugin 'Lokaltog/vim-powerline'
```

* 缩进指示线插件

```shell
# indentLine 缩进指示线，地址https://github.com/Yggdroot/indentLine。
# 安装：
Plugin 'Yggdroot/indentLine'
# 开关：
:IndentLinesToggle
```

* 自动格式化插件

```shell
# vim-autopep8
# 自动格式化工具，安装后运行:Autopep8就可以自动依照pep8的标准自动格式化代码。
# 地址https://github.com/Yggdroot/indentLine。
# 首先安装autopep8：
pip install autopep8
# 配置
Plugin 'tell-k/vim-autopep8'
# 可以设置快捷键F8代替:Autopep8：
autocmd FileType python noremap <buffer> <F8> :call Autopep8()<CR>
```

* 自动补全括号和引号插件

```shell
# auto-pairs
# 自动补全括号和引号等，地址https://github.com/jiangmiao/auto-pairs。
Plugin 'jiangmiao/auto-pairs'
```

* 语法检查插件

```shell
# w0rp/ale
```

### 三、自定义VIM

​        vim配置文件是 ~/.vimrc ，这个文件需要手动自己创建。

#### 3.1 常用文件配置：

```shell
set encoding=utf-8  # 设置文件编码
set number   # 显示行号
set nowrap   # 取消换行
set ruler    # 显示光标当前位置
set cindent  
set tabstop=4  # 设置tab为4个空格 
set sheiftwidth=4  # 设置行之间交错时使用4个空格
set ai  # 设置自动缩进
set noai
set history=1000 # 记录历史的行数
syntax on  # 语法高亮显示
set background=dark # 背景使用黑色
set showmatch  # 设置匹配模式，输入右括号时匹配左括号，没有就报警
set noshowmatch
set vb t_vb=   # 去掉命令错误时的报警声
set ruler      # 右下角显示光标位置的状态行
set cursorline # 突出显示当前行
set showmode  # 右下角显示当前vim模式
```
#### 3.2 VIM 示例文件一

```shell
":echo "Hello, world!"    注释:"开头表示注释 
"=========================一般设置======================================= 
set nocompatible          "vim比vi支持更多的功能，如showcmd，避免冲突和副作用，最好关闭兼容 
set encoding=utf-8	  "使用utf-8编码 
set number                "显示行号 
set showcmd               "显示输入命令 
set clipboard=unnamed,unnamedplus    "可以从vim复制到剪贴版中 
set mouse=a               "可以在buffer的任何地方使用鼠标 
set cursorline            "显示当前行 
set hlsearch              "显示高亮搜索 
"set incsearch 
set history=100           "默认指令记录是20 
set ruler                 "显示行号和列号（默认打开) 
set pastetoggle=<F3>      "F3快捷键于paste模式与否之间转化，防止自动缩进 
"set helplang=cn           "设置为中文帮助文档,需下载并配置之后才生效 
 
 
"===========================文本格式排版================================o 
set tabstop=4              "设置tab长度为4 
set shiftwidth=4           "设置自动对齐的缩进级别 
"set cindent                "自动缩进,以c语言风格，例如从if进入下一行，会自动缩进shiftwidth大小 
"set smartindent            "改进版的cindent,自动识别以#开头的注释，不进行换行 
set autoindent              "autoindent配合下面一条命令根据不同语言类型进行不同的缩进操作，更加智能 
filetype plugin indent on 
"set nowrap 
 
"===========================选择solarized的模式========================== 
syntax enable  
syntax on 
"solarzed的深色模式  
"set background=dark 
"solarized的浅色模式 
"set background=light 
"colorscheme solarized        "开启背景颜色模式 
 
"===========================选择molokai的模式============================ 
"let g:rehash256 = 1 
let g:molokai_original = 1    "相较于上一个模式，个人比较喜欢此种模式 
highlight NonText guibg=#060606 
highlight Folded  guibg=#0A0A0A guifg=#9090D0 
"set t_Co=256 
"set background=dark 
colorscheme  molokai   
```
#### 3.3 VIM 配置文件示例二

​        高亮+自动缩进+行号+折叠+优化。(~/.vimrc)

```shell
"=========================================================================
" DesCRiption: 适合自己使用的vimrc文件，for Linux/Windows, GUI/Console
"
" Last Change: 2010年08月02日 15时13分 
"
" Version: 1.80
"
"=========================================================================

set nocompatible " 关闭 vi 兼容模式
syntax on " 自动语法高亮
colorscheme molokai " 设定配色方案
set number " 显示行号
set cursorline " 突出显示当前行
set ruler " 打开状态栏标尺
set shiftwidth=4 " 设定 << 和 >> 命令移动时的宽度为 4
set softtabstop=4 " 使得按退格键时可以一次删掉 4 个空格
set tabstop=4 " 设定 tab 长度为 4
set nobackup " 覆盖文件时不备份
set autochdir " 自动切换当前目录为当前文件所在的目录
filetype plugin indent on " 开启插件
set backupcopy=yes " 设置备份时的行为为覆盖
set ignorecase smartcase " 搜索时忽略大小写，但在有一个或以上大写字母时仍保持对大小写敏感
set nowrapscan " 禁止在搜索到文件两端时重新搜索
set incsearch " 输入搜索内容时就显示搜索结果
set hlsearch " 搜索时高亮显示被找到的文本
set noerrorbells " 关闭错误信息响铃
set novisualbell " 关闭使用可视响铃代替呼叫
set t_vb= " 置空错误铃声的终端代码
" set showmatch " 插入括号时，短暂地跳转到匹配的对应括号
" set matchtime=2 " 短暂跳转到匹配括号的时间
set magic " 设置魔术
set hidden " 允许在有未保存的修改时切换缓冲区，此时的修改由 vim 负责保存
set guioptions-=T " 隐藏工具栏
set guioptions-=m " 隐藏菜单栏
set smartindent " 开启新行时使用智能自动缩进
set backspace=indent,eol,start
" 不设定在插入状态无法用退格键和 Delete 键删除回车符
set cmdheight=1 " 设定命令行的行数为 1
set laststatus=2 " 显示状态栏 (默认值为 1, 无法显示状态栏)
set statusline=\ %<%F[%1*%M%*%n%R%H]%=\ %y\ %0(%{&fileformat}\ %{&encoding}\ %c:%l/%L%)\ 
" 设置在状态行显示的信息
set foldenable " 开始折叠
set foldmethod=syntax " 设置语法折叠
set foldcolumn=0 " 设置折叠区域的宽度
setlocal foldlevel=1 " 设置折叠层数为
" set foldclose=all " 设置为自动关闭折叠 
" nnoremap <space> @=((foldclosed(line('.')) < 0) ? 'zc' : 'zo')<CR>
" 用空格键来开关折叠


" return OS type, eg: windows, or linux, mac, et.st..
function! MySys()
if has("win16") || has("win32") || has("win64") || has("win95")
return "windows"
elseif has("unix")
return "linux"
endif
endfunction

" 用户目录变量$VIMFILES
if MySys() == "windows"
let $VIMFILES = $VIM.'/vimfiles'
elseif MySys() == "linux"
let $VIMFILES = $HOME.'/.vim'
endif

" 设定doc文档目录
let helptags=$VIMFILES.'/doc'

" 设置字体 以及中文支持
if has("win32")
set guifont=Inconsolata:h12:cANSI
endif

" 配置多语言环境
if has("multi_byte")
" UTF-8 编码
set encoding=utf-8
set termencoding=utf-8
set formatoptions+=mM
set fencs=utf-8,gbk

if v:lang =~? '^\(zh\)\|\(ja\)\|\(ko\)'
set ambiwidth=double
endif

if has("win32")
source $VIMRUNTIME/delmenu.vim
source $VIMRUNTIME/menu.vim
language messages zh_CN.utf-8
endif
else
echoerr "Sorry, this version of (g)vim was not compiled with +multi_byte"
endif

" Buffers操作快捷方式!
nnoremap <C-RETURN> :bnext<CR>
nnoremap <C-S-RETURN> :bprevious<CR>

" Tab操作快捷方式!
nnoremap <C-TAB> :tabnext<CR>
nnoremap <C-S-TAB> :tabprev<CR>

"关于tab的快捷键
" map tn :tabnext<cr>
" map tp :tabprevious<cr>
" map td :tabnew .<cr>
" map te :tabedit
" map tc :tabclose<cr>

"窗口分割时,进行切换的按键热键需要连接两次,比如从下方窗口移动
"光标到上方窗口,需要<c-w><c-w>k,非常麻烦,现在重映射为<c-k>,切换的
"时候会变得非常方便.
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l

"一些不错的映射转换语法（如果在一个文件中混合了不同语言时有用）
nnoremap <leader>1 :set filetype=xhtml<CR>
nnoremap <leader>2 :set filetype=css<CR>
nnoremap <leader>3 :set filetype=javascript<CR>
nnoremap <leader>4 :set filetype=php<CR>

" set fileformats=unix,dos,mac
" nmap <leader>fd :se fileformat=dos<CR>
" nmap <leader>fu :se fileformat=unix<CR>

" use Ctrl+[l|n|p|cc] to list|next|previous|jump to count the result
" map <C-x>l <ESC>:cl<CR>
" map <C-x>n <ESC>:cn<CR>
" map <C-x>p <ESC>:cp<CR>
" map <C-x>c <ESC>:cc<CR>


" 让 Tohtml 产生有 CSS 语法的 html
" syntax/2html.vim，可以用:runtime! syntax/2html.vim
let html_use_css=1

" Python 文件的一般设置，比如不要 tab 等
autocmd FileType python set tabstop=4 shiftwidth=4 expandtab
autocmd FileType python map <F12> :!python %<CR>

" 选中状态下 Ctrl+c 复制
vmap <C-c> "+y

" 打开javascript折叠
let b:javascript_fold=1
" 打开javascript对dom、html和css的支持
let javascript_enable_domhtmlcss=1
" 设置字典 ~/.vim/dict/文件的路径
autocmd filetype javascript set dictionary=$VIMFILES/dict/javascript.dict
autocmd filetype css set dictionary=$VIMFILES/dict/css.dict
autocmd filetype php set dictionary=$VIMFILES/dict/php.dict

"-----------------------------------------------------------------
" plugin - bufexplorer.vim Buffers切换
" \be 全屏方式查看全部打开的文件列表
" \bv 左右方式查看 \bs 上下方式查看
"-----------------------------------------------------------------


"-----------------------------------------------------------------
" plugin - taglist.vim 查看函数列表，需要ctags程序
" F4 打开隐藏taglist窗口
"-----------------------------------------------------------------
if MySys() == "windows" " 设定windows系统中ctags程序的位置
let Tlist_Ctags_Cmd = '"'.$VIMRUNTIME.'/ctags.exe"'
elseif MySys() == "linux" " 设定windows系统中ctags程序的位置
let Tlist_Ctags_Cmd = '/usr/bin/ctags'
endif
nnoremap <silent><F4> :TlistToggle<CR>
let Tlist_Show_One_File = 1 " 不同时显示多个文件的tag，只显示当前文件的
let Tlist_Exit_OnlyWindow = 1 " 如果taglist窗口是最后一个窗口，则退出vim
let Tlist_Use_Right_Window = 1 " 在右侧窗口中显示taglist窗口
let Tlist_File_Fold_Auto_Close=1 " 自动折叠当前非编辑文件的方法列表
let Tlist_Auto_Open = 0
let Tlist_Auto_Update = 1
let Tlist_Hightlight_Tag_On_BufEnter = 1
let Tlist_Enable_Fold_Column = 0
let Tlist_Process_File_Always = 1
let Tlist_Display_Prototype = 0
let Tlist_Compact_Format = 1


"-----------------------------------------------------------------
" plugin - mark.vim 给各种tags标记不同的颜色，便于观看调式的插件。
" \m mark or unmark the word under (or before) the cursor
" \r manually input a regular expression. 用于搜索.
" \n clear this mark (i.e. the mark under the cursor), or clear all highlighted marks .
" \* 当前MarkWord的下一个 \# 当前MarkWord的上一个
" \/ 所有MarkWords的下一个 \? 所有MarkWords的上一个
"-----------------------------------------------------------------


"-----------------------------------------------------------------
" plugin - NERD_tree.vim 以树状方式浏览系统中的文件和目录
" :ERDtree 打开NERD_tree :NERDtreeClose 关闭NERD_tree
" o 打开关闭文件或者目录 t 在标签页中打开
" T 在后台标签页中打开 ! 执行此文件
" p 到上层目录 P 到根目录
" K 到第一个节点 J 到最后一个节点
" u 打开上层目录 m 显示文件系统菜单（添加、删除、移动操作）
" r 递归刷新当前目录 R 递归刷新当前根目录
"-----------------------------------------------------------------
" F3 NERDTree 切换
map <F3> :NERDTreeToggle<CR>
imap <F3> <ESC>:NERDTreeToggle<CR>


"-----------------------------------------------------------------
" plugin - NERD_commenter.vim 注释代码用的，
" [count],cc 光标以下count行逐行添加注释(7,cc)
" [count],cu 光标以下count行逐行取消注释(7,cu)
" [count],cm 光标以下count行尝试添加块注释(7,cm)
" ,cA 在行尾插入 /* */,并且进入插入模式。 这个命令方便写注释。
" 注：count参数可选，无则默认为选中行或当前行
"-----------------------------------------------------------------
let NERDSpaceDelims=1 " 让注释符与语句之间留一个空格
let NERDCompactSexyComs=1 " 多行注释时样子更好看


"-----------------------------------------------------------------
" plugin - DoxygenToolkit.vim 由注释生成文档，并且能够快速生成函数标准注释
"-----------------------------------------------------------------
let g:DoxygenToolkit_authorName="Asins - asinsimple AT gmail DOT com"
let g:DoxygenToolkit_briefTag_funcName="yes"
map <leader>da :DoxAuthor<CR>
map <leader>df :Dox<CR>
map <leader>db :DoxBlock<CR>
map <leader>dc a /* */<LEFT><LEFT><LEFT>


"-----------------------------------------------------------------
" plugin – ZenCoding.vim 很酷的插件，HTML代码生成
" 插件最新版：http://github.com/mattn/zencoding-vim
" 常用命令可看：http://nootn.com/blog/Tool/23/
"-----------------------------------------------------------------


"-----------------------------------------------------------------
" plugin – checksyntax.vim JavaScript常见语法错误检查
" 默认快捷方式为 F5
"-----------------------------------------------------------------
let g:checksyntax_auto = 0 " 不自动检查


"-----------------------------------------------------------------
" plugin - NeoComplCache.vim 自动补全插件
"-----------------------------------------------------------------
let g:AutoComplPop_NotEnableAtStartup = 1
let g:NeoComplCache_EnableAtStartup = 1
let g:NeoComplCache_SmartCase = 1
let g:NeoComplCache_TagsAutoUpdate = 1
let g:NeoComplCache_EnableInfo = 1
let g:NeoComplCache_EnableCamelCaseCompletion = 1
let g:NeoComplCache_MinSyntaxLength = 3
let g:NeoComplCache_EnableSkipCompletion = 1
let g:NeoComplCache_SkipInputTime = '0.5'
let g:NeoComplCache_SnippetsDir = $VIMFILES.'/snippets'
" <TAB> completion.
inoremap <expr><TAB> pumvisible() ? "\<C-n>" : "\<TAB>"
" snippets expand key
imap <silent> <C-e> <Plug>(neocomplcache_snippets_expand)
smap <silent> <C-e> <Plug>(neocomplcache_snippets_expand)


"-----------------------------------------------------------------
" plugin - matchit.vim 对%命令进行扩展使得能在嵌套标签和语句之间跳转
" % 正向匹配 g% 反向匹配
" [% 定位块首 ]% 定位块尾
"-----------------------------------------------------------------


"-----------------------------------------------------------------
" plugin - vcscommand.vim 对%命令进行扩展使得能在嵌套标签和语句之间跳转
" SVN/git管理工具
"-----------------------------------------------------------------
 

　

"-----------------------------------------------------------------
" plugin – a.vim
"-----------------------------------------------------------------
```




