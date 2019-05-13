# LOOK 界面开发
"""Python 用户界面开发包
    TKinter     官方提供，跨平台，标准包，文档不健全
    PyQt        需要额外安装
    wxPython    需要额外安装。
"""

"""wxPython 安装 for ubuntu 18
sudo apt install make gcc libgtk-3-dev libwebkitgtk-dev 
     libwebkitgtk-3.0-dev libgstreamer-gl1.0-0 freeglut3 
     freeglut3-dev python-gst-1.0 python3-gst-1.0 libglib2.0-dev 
     ubuntu-restricted-extras libgstreamer-plugins-base1.0-dev

sudo pip3 install wxPython
安装的时间超级长
"""
""" wxPython 类层次结构
    wx.Object   根类
    wx.Window   窗口类
        wx.Control 
        wx.NonOwnedWindow
            wx.TopLevelWindow       所有其他窗口的容器
                wx.Frame            构建用户界面的主要窗口类
                wx.Dialog           
        wx.Panel                    容器窗口
        wx.MenuBar
    wx.Control  控件类
        wx.StaticText
        wx.AnyButton
            wx.Button
                wx.BitmapButton
            wx.ToggleButton
        wx.RadioButton
        wx.CheckBox
        wx.TextCtrl
        wx.ListBox
        wx.ComboBox
        wx.Choice
        wx.Gauge
        wx.ScrollBar
        wx.ToolBar
        wx.TreeCtrl
        wx.StaticBox
        wx.StaticBitmap
"""

""" 一个简单示例
    wxPython 中主要使用wx.Frame
    wx.App 为了关闭窗口，代表当前应用程序
"""
import wx

def simple_frame():
    # 创建应用程序
    app = wx.App()
    # 创建窗口
    frm = wx.Frame(None, title="test app", size=(400,300), pos=(100,100))
    # 显示窗口
    frm.Show()
    # 进入主事件循环
    app.MainLoop()

"""一个稍微功能多点的窗口
    窗口的Parent属性表示的是包含关系
"""
"""定义一个窗口类"""
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="First Frame", size=(400,300))
        # 窗口居中
        self.Center()  
        # 创建一个panel
        panel = wx.Panel(parent=self) 
        # 在panel上放一个静态文本
        statictext = wx.StaticText(parent=panel, label='Hello world', pos=(10,10))

class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print("exit")
        return 0

""" 事件处理的示例程序
    事件、事件类型、事件源、时间处理者
    wx.Event 事件及其子类
    wx.CommandEvent     按钮事件
    wx.MoveEvent        鼠标事件

    绑定事件源和事件处理者：
    Bind(self, event, handler, source=None, id=wx.ID_ANY, id2=wx.ID_ANY)

"""            
class MyFrame1(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="event", size=(400,300))
        # 窗口居中
        self.Center()  
        # 创建一个panel
        panel = wx.Panel(parent=self) 
        # 在panel上放一个静态文本
        self.statictext = wx.StaticText(parent=panel, pos=(10,10))
        # 创建按钮
        b1 = wx.Button(parent=panel, id=10, label='Button1', pos=(100,50))
        b2 = wx.Button(parent=panel, id=11, label='Button2', pos=(100,100))
        # wx.EVT_BUTTON 是事件类型
        # on_click是事件处理者
        # b 是事件源
        self.Bind(wx.EVT_BUTTON,self.on_click, b1)
        self.Bind(wx.EVT_BUTTON,self.on_click, id=11)
        # self.Bind(wx.EVT_BUTTON,self.on_click, id=11, id=10)
        # 鼠标事件的处理
        # 因为窗口上放了一个panel，所以鼠标只能操作在这一层上
        # self 也就是Frame捕获不到鼠标事件，不能用self.Bind()
        panel.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)
        panel.Bind(wx.EVT_LEFT_UP, self.on_left_up)
        panel.Bind(wx.EVT_MOTION, self.on_mouse_move)
    
    def on_left_down(self, evt):
        print('mouse push down')

    def on_left_up(self, evt):
        print('mouse push up')
    
    def on_mouse_move(self, event):
        if event.Dragging() and event.LeftIsDown() :
            pos = event.GetPosition()
            print(pos)

    def on_click(self, event):
        print(type(event))
        event_id = event.GetId()
        if event_id == 10:
            self.statictext.SetLabelText('Button1 被单击')
        else:
            self.statictext.SetLabelText('Button2 被单击')
            

class App1(wx.App):
    def OnInit(self):
        frame = MyFrame1()
        frame.Show()
        return True

    def OnExit(self):
        print("exit")
        return 0


""" wxPython的布局管理
    绝对布局：位置固定
    相对布局：
        wxPython 提供了8个布局管理器：
            wx.Sizer
                wx.BoxSizer
                    wx.StaticBoxSizer
                    wx.WrapSizer
                    wx.StdDialogButtonSizer
                wx.GridSizer
                    wx.FlexGridSizer
                        wx.GridBagSizer
"""

"""Box 布局器
    让子窗口沿着水平或垂直方向布局
    hbox = wx.BoxSizer(wx.HORIZONTAL)   水平布局
    hbox = wx.BoxSizer()                默认水平
    vbox = wx.BoxSizer(wx.VERTICAL)     垂直布局
    Add(window, proportion=0, flag=0, border=0, userData=None)
        window: 父窗口。也可以是另外一个容器
        proportion: 仅BoxSizer使用，在父窗口所占比例
        flag: 控制对齐、边框、尺寸
        border:边框宽度
        userData:传递额外数据
"""
class MyFrameBox(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Box', size=(300,120))
        self.Center()
        panel = wx.Panel(parent=self)
        
        # 创建垂直方向的布局管理器
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        self.statictext = wx.StaticText(parent=panel, Label='Button1')
        
        # 将上述静态文本空间添加到布局管理器中，上部居中且最小化大小，边框10像素
        vbox.Add(self.statictext, proportion=2,
            flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTER,border =10)
        
        b1 = wx.Button(parent=panel, id=10,label='Button1')
        b2 = wx.Button(parent=panel, id=11,label='Button2')
        self.Bind(wx.EVT_BUTTON, self.on_click, id=10, id2=11)
        
        # 创建水平方向的布局管理器
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        # 将2个按钮添加进去，底部填满
        hbox.Add(b1, 0, wx.EXPAND | wx.BOTTOM, 20)
        hbox.add(b2, 0, wx.EXPAND | wx.BOTTOM, 5)

        # 把水平管理器加到垂直管理器中
        vbox.Add(hbox,proportion=1, flag=wx.CENTER)
        panel.SetSizer(vbox)

    def on_click(self, event):
        event_id =event.GetId()
        print(event_id)
        if event_id == 10:
            self.statictext.SetLabelText('Button1 click')
        else:
            self.statictext.SetLabelText('Button2 click')
class App1Box(wx.App):
    def OnInit(self):
        frame = MyFrame1()
        frame.Show()
        return True

    def OnExit(self):
        print("exit")
        return 0

""" StaticBox 布局
    和Box基本一样，多了一个容器的静态文本
"""

""" Grid布局
    网格形式布局
    wx.GridSizer(rows, cols, vgap, hgap) 间隙
    wx.GridSizer(row,cols,gap)
        gap是wx.Size类型，wx.Size(2,3) 水平2像素，垂直3
    wx.GridSizer(cols,vgap,hgap)
        不限定行数
    wx.GridSizer(cols, gap=wx.Size(0,0))
"""
class Grid_Frame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Grid', size=(300,300))
        self.Center()
        panel = wx.Panel(self)
        btn1 = wx.Button(panel, label='1')
        btn2 = wx.Button(panel, label='2')
        btn3 = wx.Button(panel, label='3')
        btn4 = wx.Button(panel, label='4')
        btn5 = wx.Button(panel, label='5')
        btn6 = wx.Button(panel, label='6')
        btn7 = wx.Button(panel, label='7')
        btn8 = wx.Button(panel, label='8')
        btn9 = wx.Button(panel, label='9')

        grid =  wx.GridSizer(cols=3, rows=3, vgap=0, hgap=0)

        grid.Add(btn1, 0, wx.EXPAND)
        grid.Add(btn2, 0, wx.EXPAND)
        grid.Add(btn3, 0, wx.EXPAND)
        grid.Add(btn4, 0, wx.EXPAND)
        grid.Add(btn5, 0, wx.EXPAND)
        grid.Add(btn6, 0, wx.EXPAND)
        grid.Add(btn7, 0, wx.EXPAND)
        grid.Add(btn8, 0, wx.EXPAND)
        grid.Add(btn9, 0, wx.EXPAND)
        
        panel.SetSizer(grid)
        
class App1Grid(wx.App):
    def OnInit(self):
        frame = Grid_Frame()
        frame.Show()
        return True

    def OnExit(self):
        print("exit")
        return 0

""" FlexGrid 布局
    如果想网格大小不同可以使用FlexGrid布局，他是wx.GridSizer的子类
    AddGrowableRow(idx, proportion=0) 指定行可扩展，proportion是该行所占比例
    AddGrowableCol(idx, proportion=0)

"""
class FlexGrid_Frame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='FlexGrid', size=(300,300))
        self.Center()
        panel = wx.Panel(self)

        fgs = wx.FlexGridSizer(3,2,10,10)

        title = wx.StaticText(panel, label="title")
        author = wx.StaticText(panel, label="author")
        review = wx.StaticText(panel, label="review")

        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel)
        tc3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

        fgs.AddMany([title,(tc1,1,wx.EXPAND),
                     author,(tc2,1,wx.EXPAND),
                     review,(tc3,1,wx.EXPAND)])
        fgs.AddGrowableRow(0,1)
        fgs.AddGrowableRow(1,1)
        fgs.AddGrowableRow(2,3)
        fgs.AddGrowableCol(0,1)
        fgs.AddGrowableCol(1,2)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)

        panel.SetSizer(hbox)

class App1FlexGrid(wx.App):
    def OnInit(self):
        frame = FlexGrid_Frame()
        frame.Show()
        return True

    def OnExit(self):
        print("exit")
        return 0


""" wxPython 控件
    wx.StaticText
    wx.Button
    wx.BitmapButton
    wx.ToggleButton
    wx.TextCtrl   wx.TE_MULTILINE 多行，wx.TE_PASSWORD 密码框
"""
class ControlExample(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='控件', size=(300, 1000))
        self.Center()
        panel = wx.Panel(self)
        # 复选框 水平布局器--------------------------------------------------
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        
        checkbox_text = wx.StaticText(panel, label='选择你喜欢的：')
        cb1 = wx.CheckBox(panel, 1, 'Python')
        cb2 = wx.CheckBox(panel, 2, 'Java')
        cb2.SetValue(True)
        cb3 = wx.CheckBox(panel, 3, 'C++')
        self.Bind(wx.EVT_CHECKBOX, self.on_checkbox_click, id=1, id2=3)
        
        hbox1.Add(checkbox_text, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)
        hbox1.Add(cb1, 1, flag=wx.ALL | wx.FIXED_MINSIZE)
        hbox1.Add(cb2, 1, flag=wx.ALL | wx.FIXED_MINSIZE)
        hbox1.Add(cb3, 1, flag=wx.ALL | wx.FIXED_MINSIZE)

        # 单选框 水平布局器---------------------------------------------------
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        statictext = wx.StaticText(panel, label='选择性别')
        radio1 = wx.RadioButton(panel, 4, '男', style=wx.RB_GROUP)
        radio2 = wx.RadioButton(panel, 5, '女')
        self.Bind(wx.EVT_RADIOBUTTON, self.on_radio1_click, id=4, id2=5)

        hbox2.Add(statictext, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)
        hbox2.Add(radio1, 1, flag=wx.ALL | wx.FIXED_MINSIZE)
        hbox2.Add(radio2, 1, flag=wx.ALL | wx.FIXED_MINSIZE)

        # 按钮、文本输入、下来列表 垂直布局器------------------------------------
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        # 普通按钮
        statictext = wx.StaticText(panel, label='普通按钮')
        b1 = wx.Button(parent=panel, label='wx.Button')
        self.Bind(wx.EVT_BUTTON, self.on_click, b1)
        # ToggleButton
        b2 = wx.ToggleButton(panel, -1, 'wx.ToggleButton')
        self.Bind(wx.EVT_BUTTON, self.on_click, b2)
        # 图像按钮
        bmp = wx.Bitmap('newbie2export/chapter19/183.png',wx.BITMAP_TYPE_PNG)
        b3 = wx.BitmapButton(panel, -1, bmp, name='wx.BitmapButton' )
        self.Bind(wx.EVT_BUTTON, self.on_click, b3)

        vbox1.Add(statictext, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)
        vbox1.Add(b1, proportion=1, flag=wx.CENTER | wx.EXPAND)
        vbox1.Add(b2, proportion=1, flag=wx.CENTER | wx.EXPAND)
        vbox1.Add(b3, proportion=1, flag=wx.CENTER | wx.EXPAND)
        # 文本输入框
        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        tc3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        tc1.SetValue('单行输入')
        tc3.SetValue('多行输入')
        #print('User ID:{0}'.format(tc1.GetValue()))

        vbox1.Add(tc1, proportion=1, flag=wx.CENTER | wx.EXPAND)
        vbox1.Add(tc2, proportion=1, flag=wx.CENTER | wx.EXPAND)
        vbox1.Add(tc3, proportion=1, flag=wx.CENTER | wx.EXPAND)
        # 复选框（可修改）
        statictext = wx.StaticText(panel, label='please choice:')
        list1 = ['Python', 'C++', 'Java']
        ch1 = wx.ComboBox(panel, -1, value='C', choices=list1, style=wx.CB_SORT)
        self.Bind(wx.EVT_COMBOBOX, self.on_combobox, ch1)

        vbox1.Add(statictext, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)
        vbox1.Add(ch1, proportion=1, flag=wx.CENTER | wx.EXPAND)
        # 复选框（不可修改）
        statictext = wx.StaticText(panel, label='选择性别：')
        list2 = ['男','女']
        ch2 = wx.Choice(panel, -1, choices=list2)
        self.Bind(wx.EVT_CHOICE, self.on_choice, ch2)

        vbox1.Add(statictext, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)
        vbox1.Add(ch2, proportion=1, flag=wx.CENTER | wx.EXPAND)
        # 列表（可单选多选）
        statictext = wx.StaticText(panel, label='请选择语言：')
        list1 = ['Python', 'C++', 'Java']
        #lb1 = wx.ListBox(panel, -1, choices=list1, style=wx.LB_SINGLE) #单选
        lb1 = wx.ListBox(panel, -1, choices=list1, style=wx.LB_EXTENDED)  #多选
        self.Bind(wx.EVT_LISTBOX, self.on_listbox1, lb1)

        vbox1.Add(statictext, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)
        vbox1.Add(lb1, proportion=1, flag=wx.CENTER | wx.EXPAND)
        # 静态图片控件
        bmp = wx.Bitmap('newbie2export\\chapter19\\2.jpg', type=wx.BITMAP_TYPE_JPEG)
        image = wx.StaticBitmap(panel, -1, bmp)
        vbox1.Add(image,proportion=1, flag=wx.CENTER)

        # 按顺序加入上面几个布局器到一个父布局器中-----------------------------------------
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox1, 1, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(hbox2, 1, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(vbox1, 1, flag=wx.ALL | wx.EXPAND, border=5)
        panel.SetSizer(vbox)
        
    def on_click(self, event):
        self.statictext.SetLabelText('Hello,world')
    
    def on_checkbox_click(self, event):
        cb = event.GetEventObject()
        print('选择{0},状态{1}'.format(cb.GetLabel(), event.IsChecked()))
    
    def on_radio1_click(self, event):
        rb = event.GetEventObject()
        print('第一组{0} 被选中'.format(rb.GetLabel()))
    
    def on_combobox(self, event):
        print('选择 {0}'.format(event.GetString()))
    
    def on_choice(self, event):
        print('选择 {0}'.format(event.GetString()))

    def on_listbox1(self, event):
        listbox = event.GetEventObject()
        print('选择 {0}'.format(listbox.GetSelections()))


class ControlExampleAPP(wx.App):
    def OnInit(self):
        frame = ControlExample()
        frame.Show()
        return True

    def OnExit(self):
        print("exit")
        return 0


""" 分隔窗口
    wx.SplitterWindow常用方法
    SplitVertically(window1, window2,cashPosition=0),左右布局，cashPosition是窗框位置
    SplitHorizontally(win1, win2, cashPosition=0) 上下
    SetMinimumPaneSize(paneSize) 最小窗口尺寸，左右布局指的是左，上下指的是上，默认0
"""

class split_win(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='分隔窗口', size=(350, 180))
        self.Center()
        splitter = wx.SplitterWindow(self, -1)
        leftpanel = wx.Panel(splitter)
        rightpanel = wx.Panel(splitter)
        splitter.SplitVertically(leftpanel, rightpanel, 100)
        splitter.SetMinimumPaneSize(80)

        list1 = ['苹果', '橘子', '香蕉']
        lb2 = wx.ListBox(leftpanel, -1, choices=list1, style=wx.LB_SINGLE)
        
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox1.Add(lb2, 1, flag=wx.ALL | wx.EXPAND, border=5)
        leftpanel.SetSizer(vbox1)

        vbox2 = wx.BoxSizer(wx.VERTICAL)
        self.content = wx.StaticText(rightpanel, label='右侧面板')
        vbox2.Add(self.content, 1, flag=wx.ALL | wx.EXPAND, border=5)
        rightpanel.SetSizer(vbox2)
    
class split_winApp(wx.App):
    def OnInit(self):
        frame = split_win()
        frame.Show()
        return True

    def OnExit(self):
        print("exit")
        return 0

"""
 此外还有菜单、工具栏、网格（Excel）、树等等
 太多了，用的时候再整理吧，写界面是最烦人的工作。
"""
if __name__ == '__main__':
    app = split_winApp()
    app.MainLoop()