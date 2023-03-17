import wx

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)        
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        my_sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer1.Add(self.text_ctrl, 12, wx.TOP, 1.5)        
        my_btn = wx.Button(panel, label='Press Me')
        my_sizer1.Add(my_btn, 2, 0, 0)
        my_sizer.Add(my_sizer1,4,wx.ALL|wx.EXPAND,2)
        my_sizer.SetSizeHints(panel)
        panel.SetSizer(my_sizer)        
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
