#!usr/bin/python

import wx
import threading
from middle import middle 
from right import Right
from ServerRTC import ServerRTC
from ChannelRTC import ChannelRTC

MAIN_SCREEN_WIDTH = 700
MAIN_SCREEN_HEIGHT = 500

ID_MAIN_SCREEN = 50
ID_LEFT = 100
ID_MIDDLE = 200
ID_RIGHT = 300
ID_SPLITTER1 = 400
ID_SPLITTER2 = 500

class MainScreen(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(MainScreen, self).__init__(*args, **kwargs)

        self.server_list = []    

        self.InitUI()
        
    def InitUI(self):

        self.SetSize((MAIN_SCREEN_WIDTH,MAIN_SCREEN_HEIGHT))        
        self.SetTitle('STirc - connecting chatters')                

        self.CreateMenuBar()

        self.splitter1 = wx.SplitterWindow(self,ID_SPLITTER1)
        self.splitter1.SetMinimumPaneSize(110)

        self.splitter2 = wx.SplitterWindow(self.splitter1,ID_SPLITTER2)     
        self.splitter2.SetMinimumPaneSize(110)
        self.splitter2.SetSashGravity(1.0)

        self.channel_list = wx.TreeCtrl(self.splitter1,ID_LEFT,style=wx.TR_HIDE_ROOT|wx.SUNKEN_BORDER|wx.TR_HAS_BUTTONS)

        self.channel_list.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnChannelChanged, id=-1)
        
        self.root = self.channel_list.AddRoot("ChannelList")    

        self.middle = middle(self.splitter2,ID_MIDDLE,(594,450))        
        self.server_list.append(self.AddServerRoot(self.root,ServerRTC(self.middle.chat_panel,'irc.DejaToons.net',6667,'Dejatoons')))
        self.AddChannelNode(self.server_list[0],ChannelRTC(self.middle.chat_panel,'vjtians','.less','gaurav'))
        self.AddChannelNode(self.server_list[0],ChannelRTC(self.middle.chat_panel,'scraggy','Pokemon','gaurav'))        
        self.server_list.append(self.AddServerRoot(self.root,ServerRTC(self.middle.chat_panel,'irc.FreeNode.net',6667,'FreeNode')))
        self.AddChannelNode(self.server_list[1],ChannelRTC(self.middle.chat_panel,'boost','Maths','gaurav'))
        self.AddChannelNode(self.server_list[1],ChannelRTC(self.middle.chat_panel,'gsoc','Coding','gaurav'))        
        
        self.channel_list.ExpandAll()        
        
        self.right = Right(self.splitter2,ID_RIGHT)          
        
        self.splitter1.SplitVertically(self.channel_list,self.splitter2,20)
        self.splitter2.SplitVertically(self.middle ,self.right,600)                       

        self.Centre()
        self.Show(True)
        
        dejatoons=self.channel_list.GetPyData(self.server_list[0])
        try:
            t=threading.Thread(target=dejatoons.makeConnection)
            t.daemon=True
            t.start()
        except:
            print "Error"

    def CreateMenuBar(self):

    	menubar = wx.MenuBar()

    	filemenu = wx.Menu()

    	quit = filemenu.Append(wx.ID_EXIT, '&Quit\tCtrl+Q')
    	self.Bind(wx.EVT_MENU, self.OnQuit, id=wx.ID_EXIT)

    	helpmenu = wx.Menu()

    	about = helpmenu.Append(wx.ID_ABOUT, 'A&bout\tCtrl+B')
    	self.Bind(wx.EVT_MENU, self.OnAboutBox, id=wx.ID_ABOUT)

    	menubar.Append(filemenu,'&File')
    	menubar.Append(helpmenu,'&Help')

    	self.SetMenuBar(menubar)    

    def AddChannelNode(self,parent_item,item):
        idx = self.channel_list.AppendItem(parent_item,item.name)    #item.name                
        self.channel_list.SetPyData(idx,item)

    def AddServerRoot(self,parent_item,item):        
        idx = self.channel_list.AppendItem(parent_item,item.name)    #item.name                
        self.channel_list.SetPyData(idx,item)        
        return idx

    def OnQuit(self,e):
    	self.Destroy()

    def OnChannelChanged(self,e):
        item = e.GetItem()        
        self.middle.SetChatWindow(self.channel_list.GetPyData(item))        

    def OnAboutBox(self, e):
        
        description = """
STirc is an IRC client by Suttit Tech Ltd. 
It is advanced client featured with the custom commands.
If user finds any bug, please report it to following email. 
Also email us suggessions.
Enjoy It!
"""

        licence = """
STirc is free software; you can redistribute 
it and/or modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation; either version 2 of the License, 
or (at your option) any later version.

STirc is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
See the GNU General Public License for more details. You should have 
received a copy of the GNU General Public License along with STirc. 
"""


        info = wx.AboutDialogInfo()

        #info.SetIcon(wx.Icon('hunter.png', wx.BITMAP_TYPE_PNG))
        info.SetName('STirc')
        info.SetVersion('1.0')
        info.SetDescription(description)
        info.SetCopyright('(C) 2013 - 2023 Suttit Tech Ltd.')
        info.SetWebSite('suttittech@gmail.com')
        info.SetLicence(licence)
        info.AddDeveloper('Gaurav Deshmukh (gauravdeshmukh42@gmail.com)')
        info.AddDeveloper('Jignesh Jain (jigneshjain@gmail.com)')
        info.AddDeveloper('Tanmay Inamdar (taninamdar@gmail.com)')
        info.AddDocWriter('Gaurav Deshmukh')
        info.AddArtist('Jignesh Jain')
        info.AddTranslator('Tanmay Inamdar')

        wx.AboutBox(info)


def main():
    
    ex = wx.App()
    MainScreen(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()
