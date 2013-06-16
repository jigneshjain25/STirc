import wx

class AddServer(wx.Frame):
    'The Add Server List Box in STirc menu'
    def __init__(self,p):
        super(AddServer,self).__init__(p,style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
        self.InitUI()
		
        
    def InitUI(self):    


        self.SetSize((450,210))
        self.SetTitle('Add Server')
        self.Move((25,25))

        panel = wx.Panel(self)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(12)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2= wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)

        st1 = wx.StaticText(panel, label='Name')
        st1.SetFont(font)
        self.tc1 = wx.TextCtrl(panel)
        
        st2 = wx.StaticText(panel, label='Domain name')
        st2.SetFont(font)
        self.tc2 = wx.TextCtrl(panel)

        st3 = wx.StaticText(panel, label='Port No')
        st3.SetFont(font)
        self.tc3 = wx.TextCtrl(panel)
        
        
        st4 = wx.StaticText(panel, label='Fav Channels')
        st4.SetFont(font)
        self.tc4 = wx.TextCtrl(panel)
        self.tc4.SetToolTipString("Enter channel names separated by a \",\"  Also make sure that channel name begins with a \"#\"")

        okbtn = wx.Button(panel,label="OK")
        okbtn.Bind(wx.EVT_BUTTON,self.onOK)
        cancelbtn=wx.Button(panel,label="Cancel")
        cancelbtn.Bind(wx.EVT_BUTTON,self.onCANCEL)


        hbox1.Add(st1)
        hbox1.Add(self.tc1, proportion=1,flag = wx.LEFT, border =70)
        hbox2.Add(st2)
        hbox2.Add(self.tc2, proportion=1,flag = wx.LEFT,border=15)
        hbox3.Add(st3)
        hbox3.Add(self.tc3, proportion=1,flag = wx.LEFT,border=57)
        hbox4.Add(st4)
        hbox4.Add(self.tc4, proportion=1,flag = wx.LEFT,border = 20)
        hbox5.Add(cancelbtn)
        hbox5.Add(okbtn,flag=wx.LEFT|wx.RIGHT,border=10)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add(hbox4, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add(hbox5, flag=wx.ALIGN_RIGHT|wx.TOP, border=20)
        panel.SetSizer(vbox)
        self.Show(True)
    
    def onOK(self,e):
        
        name=self.tc1.GetValue().strip()
        domainname=self.tc2.GetValue().strip()
        port=self.tc3.GetValue().strip()
        favch= self.tc4.GetValue().strip()
    

        if name=="":
            wx.MessageBox("Please specify a name for your Server")
            return
        
        if port=="":
            wx.MessageBox("Please specify a Port no for your Server")
            return

        if domainname=="":
            wx.MessageBox("Please specify the domain address of your Server")
            return

        f=open(name,"w")
        f.write(name+"\n")
        f.write(domainname+"\n")
        f.write(port+"\n")
        f.write(favch+"\n")
        f.close()
        self.Destroy()
       
    def onCANCEL(self,e):
        self.Destroy()

	
if __name__ == '__main__':
    app=wx.App()
    AddServer(None)
    app.MainLoop()
    

