#!usr/bin/python

import wx

class MainScreen(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(MainScreen, self).__init__(*args, **kwargs) 
            
        self.InitUI()
        
    def InitUI(self):    

        self.CreateMenuBar()

        self.SetSize((700, 500))
        self.SetTitle('About dialog box')
        self.Centre()
        self.Show(True)

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

    def OnQuit(self,e):
    	self.Destroy()


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