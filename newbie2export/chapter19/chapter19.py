# LOOK 界面开发
"""Python 用户界面开发包
    TKinter     官方提供，跨平台，标准包，文档不健全
    PyQt        需要额外安装
    wxPython    需要额外安装。
"""

"""wxPython 安装
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

# 创建应用程序
app = wx.App()
# 创建窗口
frm = wx.Frame(None, title="test app", size=(400,300), pos=(100,100))
# 显示窗口
frm.Show()
# 进入主事件循环
app.MainLoop()