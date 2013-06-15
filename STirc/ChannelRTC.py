#!usr/bin/python

import wx
import wx.richtext
import re
from time import strftime, localtime


class ChannelRTC (wx.richtext.RichTextCtrl):
    
    def __init__ (self,parent ,cname, tname, nick, *args, **kwargs):
        super(ChannelRTC,self).__init__(parent,*args,**kwargs)
        self.SetSize((1050,954))
        self.parent = parent
        self.name = cname
        self.topic_name=tname
        self.logging = True
        self.nick = nick
        self.smileys = [":\)", ":\(", ":o", ":D", ":P"]   
        
    def ParseString (self, string):
        positions = []
        strlen = len(string)
        smlen = len(self.smileys)
        
        for i in range(0, smlen):
            start = 0
            while True:
                a = string.find(self.smileys[i],start, strlen)
                if a != -1:
                    positions.append([i, a])
                    start = a + len(self.smileys[i])
                else:
                    break
        positions.sort(key=lambda x: x[1])
        return positions

    def ContainsNick(self, string, source):
        return source != self.nick and self.nick in string
    
    def AttachTime(self, string):
        curtime = localtime()
        if self.logging:
            with open(self.name+".txt", "a") as myfile:
                myfile.write(strftime("%Y-%m-%d %H:%M:%S", curtime)+string)
        return "["+strftime("%H:%M:%S", curtime)+"] "+string
    
    def AddLine (self, string, nick):
        #nick specifies whether msg came from server or textbox
        boolean = self.ContainsNick(string, nick)
        if boolean:
            RedColor = wx.Color("red")
            self.BeginTextColour(RedColor)
        string = "<"+nick+"> "+string
        string = self.AttachTime(string)
        positions = self.ParseStrings(string)