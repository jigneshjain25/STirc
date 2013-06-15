#!usr/bin/python

import wx
from ServerRTC import ServerRTC

class middle(wx.Panel):
    def __init__(self,parent,id,size):
        wx.Panel.__init__(self,parent,id,size)        
        self.parent = parent        
        
        self.SetSize(size)        

        self.vbox = wx.BoxSizer(wx.VERTICAL)

        self.topic_name = wx.TextCtrl(self)
        self.vbox.Add(self.topic_name,flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=0)		
        self.vbox.Add((-1,5))

        self.chat_panel = wx.Panel(self,size=(-1,-1),id=-1)
        self.box = wx.BoxSizer(wx.HORIZONTAL)        
        self.chat_window = ServerRTC(self.chat_panel,'irc.tp.net',6667)        
        self.box.Add(self.chat_window,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)     
        self.chat_panel.SetSizerAndFit(self.box)  
        self.vbox.Add(self.chat_panel,1,flag=wx.LEFT|wx.RIGHT|wx.EXPAND,border=0)		
        self.vbox.Add((-1,5))        

        self.type_window = wx.TextCtrl(self)	
        self.vbox.Add(self.type_window, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM, border=0)

        self.vbox.Add((-1,5))
        
        self.SetSizerAndFit(self.vbox)        
        

    def SetChatWindow(self,chat_win):                                    
        self.chat_window.Hide()               
        self.chat_window=chat_win
        self.chat_window.Show()
        self.topic_name.SetValue(chat_win.topic_name)                   