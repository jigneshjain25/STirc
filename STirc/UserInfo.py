import wx

class UserInfo(wx.Frame):
    'The Network List Box in STirc menu'
    def __init__(self,*args,**kw):
        super(UserInfo,self).__init__(*args,**kw)
        self.InitUI()
		
        
    def InitUI(self):    


        self.SetSize((400,170))
        self.SetTitle('User info')
        self.Move((25,25))

        panel = wx.Panel(self)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(12)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2= wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)

        st1 = wx.StaticText(panel, label='Username ')
        st1.SetFont(font)
        
        self.tc1 = wx.TextCtrl(panel)
        
        st2 = wx.StaticText(panel, label='Nick Name')
        st2.SetFont(font)
        
        self.tc2 = wx.TextCtrl(panel)
        st3 = wx.StaticText(panel, label='Real Name')
        st3.SetFont(font)
        
        self.tc3 = wx.TextCtrl(panel)


        okbtn = wx.Button(panel,label="OK")
        okbtn.Bind(wx.EVT_BUTTON,self.onOK)
        cancelbtn=wx.Button(panel,label="Cancel")
        cancelbtn.Bind(wx.EVT_BUTTON,self.onCANCEL)


        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        hbox1.Add(self.tc1, proportion=1)
        hbox2.Add(st2, flag=wx.RIGHT, border=8)
        hbox2.Add(self.tc2, proportion=1)
        hbox3.Add(st3, flag=wx.RIGHT, border=8)
        hbox3.Add(self.tc3, proportion=1)
        hbox4.Add(cancelbtn)
        hbox4.Add(okbtn,flag=wx.LEFT|wx.RIGHT,border=10)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add(hbox4, flag=wx.ALIGN_RIGHT|wx.TOP, border=20)
        panel.SetSizer(vbox)
        self.Show(True)
    
    def onOK(self,e):
        
        self.username=self.tc1.GetValue().strip()
        self.nickname=self.tc2.GetValue().strip()
        self.realname=self.tc3.GetValue().strip()

        if self.username=="":
            wx.MessageBox("Please enter a Username")
            return
        
        if self.nickname=="":
            wx.MessageBox("Please enter a Nickname")
            return

        if self.realname=="":
            wx.MessageBox("You must be having a real name, don't you?")
            return

        f=open("UserInfo.txt","w")
        f.write(self.username+"\n")
        f.write(self.nickname+"\n")
        f.write(self.realname+"\n")

        f.close()

    def onCANCEL(self,e):
        self.Destroy()

	
if __name__ == '__main__':
    app=wx.App()
    UserInfo(None,style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
    app.MainLoop()
    

